#!/usr/bin/env python3

import argparse
import re
import subprocess
import signal
import sys
import time

def def_handler(sig, frame):
    print(f"Exit...\n")
    sys.exit(1)

signal.signal(signal.SIGINT, def_handler)

def get_arguments(): # Va a retornar todos los argumentos que le pasaremos a la herramienta
    parser = argparse.ArgumentParser(description="Tool to change the mac direction from a network interface") # parses una istancoa de la clase ArgumentParses 
    parser.add_argument("-i", "--interface", required=True, dest="interface", help="Name of the network interface")
    parser.add_argument("-m", "--mac", required=True, dest="mac_address",help="New MAC direction fot the network interface")

    return parser.parse_args() # con args tiene que estar recibiendo algo.
    
def is_valid_input(interface, mac_address):
    
    is_valid_interface = re.match(r'^[e][n|t][s|h]\d{1,2}$', interface) #regex empieza por e tiene una e o t un s o h y entre 1 y 2 digitos # empieza ^ finaliza $
    is_valid_mac_address = re.match(r'^([A-Fa-f0-9]{2}[:]){5}[A-Fa-f0-9]{2}$', mac_address) # entre parentesis es un grupo {2} esto es dos veces esa es la esctricura AV ac pero 2 veces para el primer byte luego son 2 :
    #print(is_valid_interface)
    #print(is_valid_mac_address)
    
    return is_valid_interface and is_valid_mac_address # entonces esto retorna a if is_valid_input de la def change_mac_address

def change_mac_address(interface, mac_address):

    if is_valid_input(interface, mac_address):
        print("Los datos introducidos son correctos")
        subprocess.run(["ifconfig", interface, "down"]) # inconfig interface down
        subprocess.run(["ifconfig", interface, "hw", "ether", mac_address])
        subprocess.run(["ifconfig", interface, "up"])

        print("The MAC has changed successfully")
    else:
        print("Los datos introducidos son incorectos")

def main():
    args = get_arguments()
    #time.sleep(10)
    change_mac_address(args.interface, args.mac_address) 
    

    #print(args.interface) # aora en args dentro del main llamamos el nombre de la interfac
    #print(args.mac_address)


if __name__ == '__main__':

    main()
