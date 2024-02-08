import argparse
import subprocess
import re

def change_mac(interface, new_mac):
    print("[+] Changing MAC address to " + interface + " to " + new_mac)
    subprocess.call(["sudo", "ifconfig", interface, "down"])
    subprocess.call(["sudo", "ifconfig", interface, "ether", new_mac])
    subprocess.call(["sudo", "ifconfig", interface, "up"])

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--interface", dest="interface", help="Interface to change MAC address")
    parser.add_argument("-m", "--mac", dest="new_mac", help="New MAC address for interface")
    options = parser.parse_args()
    if not options.interface:
        print("[-] Please specify an interface, type --help for more info")
    elif not options.new_mac:
        print("[-] Please specify a MAC address, type --help for more info")
    return options

def get_mac(mac):
    ifconfig_result = subprocess.check_output(["ifconfig", mac])
    mac_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_result))
    if mac_result:
        return mac_result.group(0)
    else:
        print("[-] Could not read MAC address, type --help for more info")

options = get_arguments()
mac_retrieve = get_mac(options.interface)
print("Current MAC = " + str(mac_retrieve))

change_mac(options.interface, options.new_mac)

if mac_retrieve == options.new_mac:
    print("[+] MAC address was successfully changed to " + mac_retrieve)
else:
    print("[-] MAC address could not be changed, use --help for more info. ")
