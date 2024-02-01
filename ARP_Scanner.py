#!/usr/bin/env python3

import scapy.all as scapy
import argparse

def get_arguments():
    parser = argparse.ArgumentParser(description="ARP Scanner")
    parser.add_argument("-t", "--target", required=True, dest="target", help="Host / IP Range To Scan")


    args = parser.parse_args()

    return args.target

def scan(ip):
    #scapy.arping(ip) # asi se envian los paquetes # parte facil!
    arp_packet = scapy.ARP(pdst=ip) #pdst = protocol destination ARP
    broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff") #Trama de ethernet
    
    arp_packet = broadcast_packet/arp_packet # no es una division es un perador de composicion uni capas o protocolos de paquetes
    answered, unanswered = scapy.srp(arp_packet, timeout=1,verbose=False) #srp = send recive paquet    

    response = answered.summary()
    
    if response:
        print(response)

def main():
    target = get_arguments()
    #print(target)
    scan(target)

if __name__ == '__main__':

    main()
