from ncclient import manager

from demo import iosxeao

iosxe_manager = manager.connect(
    host = iosxeao["address"],
    port = iosxeao['netconf_port'],
    username = iosxeao["username"],
    password = iosxeao["password"],
    hostkey_verify = False
)

print(type(iosxe_manager))

print(iosxe_manager.connected)

srv_capablities = iosxe_manager.server_capabilities

for capblity in srv_capablities:
    print(capblity)

filter_GigabitEthernet3 = """
<filter>
 <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
  <interface>
   <name>GigabitEtherneet3</name>
  </interface>
 </interfaces>
</filter>
"""

iosxe_GigabitEthernet3 = iosxe_manager.get_config("running", filter_GigabitEthernet3)

print(type(iosxe_GigabitEthernet3))

from xml.dom import minidom

iosxe_config_xml = minidom.parseString(iosxe_GigabitEthernet3.xml)

print(iosxe_config_xml.toprettyxml(indent = "  "))
