import argparse
import subprocess
import re

def change_mac(interface, mac_new):
    print(f"Changing MAC address: {interface} to "{mac_new}")
    subprocess.call(['sudo', 'ifconfig', interface, 'down'])
    subprocess.call(['sudo', 'ifconfig', interface, 'ether', mac_new])
    subprocess.call(['sudo', 'ifconfig', interface, 'up'])

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', dest='interface', help='Interface to change MAC address')
    parser.add_argument('-m', dest='mac_new', help='New MAC address')
    options = parser.parse_args()
    if not options.interface:
        print('Please specify an interface, type --help for more info')
    elif not options.mac_new:
        print('Please specify a MAC address, type --help for more info')
    return options

def get_mac(mac):
    mac_result = subprocess.check_output(['ifconfig', mac])
    regex_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(mac_result))
    if regex_result:
        return regex_result.group(0)
    else:
        print('Could not retrieve MAC address, please type --help for more info')

options = get_arguments()
retrieve_mac = get_mac(options.interface)
print(f"Current MAC address = {retrieve_mac}")

change_mac(options.interface, options.mac_new)
retrieve_mac_two = get_mac(options.interface)

if retrieve_mac_two == options.mac_new:
    print(f"MAC address successfully changed to {retrieve_mac_two}")
else:
    print('MAC address could not be changed, please type --help for more info')
