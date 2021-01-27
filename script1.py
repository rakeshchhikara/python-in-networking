import getpass
import telnetlib

HOST = input ("Enter your Device IP: ")
user = input("Enter your remote account: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"term len 0\n")
tn.write(b"config t\n")
tn.write(b"router bgp 100\n")
tn.write(b"network 1.1.1.1 mask 255.255.255.255\n")
tn.write(b"end\n")
tn.write(b"show ver\n")
tn.write(b"show ip int br\n")
tn.write(b"show platform\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))