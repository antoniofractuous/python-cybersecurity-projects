import argparse
import subprocess
import re

def change_mac(interface, new_mac):
    print(f"[+] Changing MAC address: {interface} to {new_mac}")
    subprocess.call(['sudo', 'ifconfig', interface, 'down'])
    subprocess.call(['sudo', 'ifconfig', interface, 'hw', 'ether', new_mac])
    subprocess.call(['sudo', 'ifconfig', interface, 'up'])

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", dest="interface", help="Interface to change MAC address")
    parser.add_argument("-m", dest="new_mac", help="MAC address value to change")
    options = parser.parse_args()
    if not options.interface:
        print("[-] Please specify an interface, type --help, for more info")
    elif not options.new_mac:
        print("[-] Please specify a MAC address, type --help for more info")
    return options

def get_mac(mac):
    ifconfig_output = subprocess.check_output(['ifconfig', mac])
    check_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_output))
    if check_mac:
        return check_mac.group(0)
    else:
        print("[-] Could not retrieve MAC address, type --help for more info")
    
options = get_arguments()
mac_regex = get_mac(options.interface)
print("Current MAC address = ", str(mac_regex))

change_mac(options.interface, options.new_mac)
new_mac_regex = get_mac(options.interface)

if new_mac_regex == options.new_mac:
    print(f"[+] MAC address successfully changed to {mac_regex}")
else:
    print("[-] Could not change MAC address, type --help for more info")
