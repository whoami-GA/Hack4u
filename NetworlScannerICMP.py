#!/usr/bin/env python3

import argparse
from termcolor import colored
import subprocess
import signal
import sys
from concurrent.futures import ThreadPoolExecutor

def def_handler(sig, frame):
    print(colored(f"[!] Exit...", 'red'))
    sys.exit(1)

signal.signal(signal.SIGINT, def_handler)

def get_arguments():
    parser = argparse.ArgumentParser(description="Tool to discover active hosts on a network (ICMP)")
    parser.add_argument("-t", "--target", required=True, dest="target", help="Host or network range to which we apply discovery")

    args = parser.parse_args()

    return args.target 

def parse_target(target_str):

    # 192.168.1.1-100
    target_str_splitted = target_str.split('.') # ["192", "168", "1", "1-100"] # una lista donde el punto es el delimitador 
    first_three_octets = '.'.join(target_str_splitted[:3]) # en estos rangos el 0 no tiene solo por el punto # juntarlo otra vez pero con puntos

    if len(target_str_splitted) == 4: # taget splited tiene que ser = a 4 para que no entren mas parametros
        if "-" in target_str_splitted[3]:
            start, end = target_str_splitted[3].split('-')  # separar target target_str_splitted tomando el guion colo delimitador pero solo el tercer elemento
            return[f"{first_three_octets}.{i}" for i in range(int(start),int(end)+1)]
        else:
            return[target_str]
    else:
        print(colored(f"[!] The range is not Valid!"), 'red')

def host_dicovery(target):
    
    #for target in targets: # se puede asi pero ThreadPoolExecutor itera solo 
        try:
            ping = subprocess.run(["ping", "-c", "1", target], timeout=1, stdout=subprocess.DEVNULL) # timeout 1 segundo maximo que tarde
            
            if ping.returncode == 0:
                print(colored(f"\t[i] The Ip {target} It Is Active", 'green'))
        except subprocess.TimeoutExpired:
            pass

def main():
    target_str = get_arguments() 
    targets = parse_target(target_str) 
    
    print(f"[+]Active Hosts On The Network")

    max_threads = 100
    with ThreadPoolExecutor(max_workers=max_threads) as executor:
        executor.map(host_dicovery, targets) # le va pasando lo que coge de targets a host_dicovery esta en sigular porque recoge target de host_dicovery
    #print(targets)

    

if __name__ == '__main__':
    main()
