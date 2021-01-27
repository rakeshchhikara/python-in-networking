__copyright__ = "Copyright (c) 2018 Cisco Systems. All rights reserved."

from borg3.result import IssueResult, OkResult, NotApplicableResult, MissingInfoResult, ResultList, \
    NotApplicableResultCodes, LineValue, Severity
from datetime import datetime, timezone
import re
import logging
import pymongo

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# days to say there is a crash of interest
MAX_CRASH_DAYS = 30
timezone_str = None

# possible list of commands to find a crashinfo file
list__possible_commands = ['show flash0: all', 'show sup-bootdisk: all', 'show slavesup-bootdisk: all',
                           'show slavebootflash: all', 'show disk: all', 'show disk0: all',
                           'show slavedisk0: all', 'show sup-bootdisk0: all', 'show slavesup-bootdisk0: all',
                           'show sup-bootflash: all', 'show slavesup-bootflash: all', 'show sup-bootflash0: all',
                           'show sup-bootflash0: all', "show bootflash: all", "show harddisk: all", "dir crashinfo:",
                           "show crashinfo: all", "show crashinfo-2: all", "show crashinfo-3: all",
                           "show crashinfo-4: all", "show crashinfo-5: all", "show crashinfo-6: all",
                           "show crashinfo-7: all", "show crashinfo-8: all", "show flash: all", "show flash-2: all",
                           "show flash-3: all", "show flash-4: all", "show flash-5: all", "show flash-6: all",
                           "show flash-7: all", "show flash-8: all", "show dfc#1-bootdisk: all",
                           "show dfc#2-bootdisk: all",
                           "show dfc#3-bootdisk: all", "show dfc#4-bootdisk: all", "show dfc#5-bootdisk: all",
                           "show dfc#6-bootdisk: all", "show dfc#7-bootdisk: all", "show dfc#8-bootdisk: all",
                           "show dfc#9-bootdisk: all", "show dfc#10-bootdisk: all", "show dfc#11-bootdisk: all",
                           "show dfc#12-bootdisk: all", "show dfc#13-bootdisk: all", "show cfc#1-bootflash: all",
                           "show cfc#2-bootflash: all", "show cfc#3-bootflash: all", "show cfc#4-bootflash: all",
                           "show cfc#5-bootflash: all", "show cfc#6-bootflash: all", "show cfc#6-bootflash: all",
                           'more slavecrashinfo:data', 'show platform kinfo', 'show platform slavekinfo',
                           'dir slavecrashinfo:', "show slavebootdisk: all", "dir /recur all-filesystems"]

# To fill the information of the crashfiles
issue = IssueResult(title=('Crash file found '))


def task(env):
    return 'something useful here'


def symptoms_check(symptom, keywords):
    for word in keywords:
        if word.lower() in symptom:
            return True


def sn_checker(sn, parsed_file):
    flag = False
    sup_or_rp_pid = None
    sup_or_rp_name = None
    if parsed_file.has_command('show inventory'):
        previous_line = None
        for line in parsed_file.get_command_lines('show inventory'):
            if sn in line:
                flag = True
            if ("PID:" in line and any(pid in line for pid in ["-SUP", "-RP", "-RSP"])) or (
                    previous_line and "Supervisor" in previous_line):
                sup_or_rp_pid = line.split(',')[0].split(":")[1].replace('"', '').strip()
                sup_or_rp_name = previous_line
                sup_or_rp_name.split(',')[1].split(':')[1].replace('"', '')
            if sup_or_rp_pid and flag:
                break

            previous_line = line

    if parsed_file.has_command('show version'):
        for line in parsed_file.get_command_lines('show version'):
            if "Cisco IOS Software" in line:
                if "c7600s32" in line or "c7600s720" in line:
                    sup_or_rp_pid = sup_or_rp_pid + "-7600"

    return flag, sup_or_rp_pid, sup_or_rp_name


def borg_module(env, borg_env, device_meta_data, parsed_file, cisco_service_request):
    result_list = ResultList()

    subtech = cisco_service_request.sub_technology
    keyword = ['unexpected reboot', 'unexpected reload']

    if (not any(kwword in subtech.lower() for kwword in keyword)) and env.user_name not in ['lreyescr', 'pedgarci',
                                                                                            'cadiazar']:
        result_list.add_result(MissingInfoResult(required_info=['Not open with unexpected reboot keywords']))
        return result_list

    # If there werent a command to check we end the script and say there werent a useful command
    isCommand, listCommands = is_a_command_to_check(parsed_file)

    if not isCommand:
        result_list.add_result(MissingInfoResult(required_info=['Missing show file system or dir commands']))

        return result_list
        # If the problem is not present then return back an OkResult
    #  if we detect a crashfile we return the list of crashes
    issueFound, listOfCrashes = check_for_crashfiles(parsed_file, listCommands)
    if issueFound:
        result_list.append(issue)
        crashes_string = ' \n'.join(listOfCrashes)
    else:
        result_list.add_result(OkResult(title='There are not crash files on the device on the last 30 days'))

    last_crashes = []
    if listOfCrashes:
        all_crashes = []
        for filesystem in listOfCrashes.keys():
            all_crashes.append(listOfCrashes[filesystem])

        all_crashes[0].sort(key=lambda x: x[1], reverse=True)
        day_of_last_crash = None
        for line, date in all_crashes[0]:
            if day_of_last_crash == None:
                day_of_last_crash = date
            temp_day = day_of_last_crash - date
            if (temp_day.total_seconds() / 60) <= 5:
                last_crashes.append(line)

    sn_match, sup_or_rp_pid, sup_or_rp_name = sn_checker(cisco_service_request.customer_serialnumber, parsed_file)
    db_inputs = {
        'sr_number': cisco_service_request.sr,
        'filename': borg_env.filename,
        'model': device_meta_data.get_model(),
        'platform': device_meta_data.get_platform(),
        'username': env.user_name,
        'serial_number': device_meta_data.get_serial_number(),
        'ios-type': device_meta_data.get_ios_type(),
        'version': device_meta_data.get_version_string(),
        'reload_reason': device_meta_data.get_reload_reason(),
        'crashinfo_files': listOfCrashes,
        'sn_match': sn_match,
        'last_crashes': last_crashes,
        'processor_match': sup_or_rp_pid,
        'processor_name_match': sup_or_rp_name
    }

    logger.info(db_inputs)
    mongo_url = "mongodb://crash_detector_architecture:83f3a1e810d55825cfaa6784e830ff3263bd75c2@bdb-dbaas-alln-1:27000,bdb-dbaas-alln-2.cisco.com:27001,bdb-user-alln-2.cisco.com:27000/task_crash_detector_architecture?replicaSet=bdb-dbaas"
    db = pymongo.MongoClient(mongo_url)
    my_db = db["task_crash_detector_architecture"]
    my_collection = my_db["crash_detector"]
    my_collection.insert_one(db_inputs)

    return result_list


# This part is to check if there is at least one command where we can check for a crashinfo file and to select which command are we gonna look into
def is_a_command_to_check(parsed_file):
    # Of the list of possible commands, which of them we found on the show tech. We add them to this list
    list_commands_found = []
    is_a_command = False
    for command in list__possible_commands:
        if parsed_file.has_command(command):
            list_commands_found.append(command)

    # If there were a command we continue wiht the script
    if list_commands_found:
        is_a_command = True

    return is_a_command, list_commands_found


# return true if detects a crashfile or false if not
def check_for_crashfiles(parsed_file, list_commands_found):
    problem_found = False
    # checking each output for a crash file
    regex = r".*(crashinfo_|core.gz|fullcore_|system-report|kernel.rp).*\b"
    listOfCrashes = {}
    for command in list_commands_found:
        crash_files = []
        # Record the starting location of the command we are analyzing
        offset = parsed_file.get_command_offset(command)
        for linenum, line in enumerate(parsed_file.get_command_lines(command)):
            matches_iter = re.finditer(regex, line, re.MULTILINE)
            temp_result = []
            for matchNum, match in enumerate(matches_iter, start=1):
                temp_result.append(match.group())

            if temp_result:
                today = datetime.now(timezone.utc)
                day_of_crash = get_date(line)
                days_from_crash = today - day_of_crash
                if days_from_crash.days < MAX_CRASH_DAYS:
                    crash_files.append((line, day_of_crash))
                    problem_found = True
                    issue.line_values.append(LineValue(offset + linenum))
            if crash_files != []:
                listOfCrashes[command] = crash_files

                # If there is a crash, we fill the test of the issue with the crashfiles
    # sevrity, Error, Warning, Notice
    OutputCrash = [line for line, date in crash_files]
    if problem_found:
        issue.text = '\n'.join(OutputCrash)
        issue.external_title = 'Crash file found '
        issue.external_text = 'Crash file found '
        issue.severity = Severity.CRITICAL

    return problem_found, listOfCrashes


# To get the day of the crash
def get_date(line):
    global timezone_str
    # regex = r"(([a-zA-Z]){3}( )([0-9]){1,2}( )([0-9]){4}( )([0-9]){2}(:)([0-9]){2}(:)([0-9]){2})((\.)(([0-9]){0,10}))?( )((\+|-)([0-9]){2}(:)([0-9]){2})"
    regex = r"(([a-zA-Z]{3})( )([0-9]{1,2})( )([0-9]{4})( )([0-9]{2}:[0-9]{2}:[0-9]{2}))(\.[0-9]{0,10})?( )((\+|-)[0-9]{2}:[0-9]{2})?"
    matches = re.finditer(regex, line, re.MULTILINE)
    temp_result = []
    for matchNum, match in enumerate(matches, start=1):
        temp_result.append(match.group(0))
        temp_result.append(match.group(1))
        temp_result.append(match.group(11))
        # We should have only one result

    if temp_result[2]:
        timezone_str = temp_result[2].replace(':', '')

    if timezone_str:
        day_string = temp_result[1] + " " + timezone_str
    else:
        day_string = temp_result[1] + " +0000"  # If UCT is not in the timestamp, we add 0000

    datetime_crash = datetime.strptime(day_string, "%b %d %Y %H:%M:%S %z")

    return datetime_crash
