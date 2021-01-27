import csv           # Import csv module to handle csv file
from netmiko import ConnectHandler        # Import ConnectHandler Class of netmiko library
import time
import threading
from datetime import datetime

def backup(device):
    for device in device_list:
        connection = ConnectHandler(**device)
        print('Entering the enable mode...')
        connection.enable()

        output = connection.send_command('show run')
        # print(output)

        # creating the backup filename (hostname_date_backup.txt)
        prompt = connection.find_prompt()
        hostname = prompt[0:-1]
        # print(hostname)

        # getting the current date (year-month-day)
        now = datetime.now()
        year = now.year
        month = now.month
        day = now.day
        hour = now.hour
        min = now.minute
        second = now.second

        # creating the backup filename (hostname_date_backup.txt)
        filename = f'{hostname}_{day}-{month}-{year}-{hour}-{min}-{second}_backup.txt'
        full_path = f"/Users/rakeshk6/PycharmProjects/First-python-project/Netmiko-scripts/config-backups/'{filename}"

        # writing the backup to the file
        with open(full_path, 'w') as backup:
            backup.write(output)
            print(f'Backup of {hostname} completed successfully')
            print('#' * 30)


        print('Closing connection')
        connection.disconnect()


start = time.time()

# Create an Empty List
threads = list()

# open csv file and read it as dictionary.
with open('devices_detail.csv') as f:
    reader = csv.DictReader(f, delimiter=',')
    th = threading.Thread(target=backup, args=(device,))
    threads.append(th)

    for row in reader:             # Use for loop to append dictionary rows to the earlier created empty list.
        device_list.append(row)

#print(list)
#print(type(list))




end = time.time()
print(f'Total time taken by Script {end-start} seconds')