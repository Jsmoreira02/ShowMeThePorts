import socket
import argparse
from os import system

parser = argparse.ArgumentParser(description="Simple Port Scanner")
parser.add_argument(
    '-t', '--target', metavar="", type=str, help="The Target Address")
parser.add_argument(
    '-lp', '--limitPort', metavar="", type=int, help="Search from port 1 to a\
specific port number")
parser.add_argument(
    '-b', '--banner', metavar="", type=str, nargs='?', const="", help="What\
service is running?")
parser.add_argument(
    '-p', '--ports', metavar="", type=int, help="Search for a especific port")

args = parser.parse_args()
host = args.target
port = args.limitPort
banner = args.banner
sp = args.ports

running = True
open_ports = []


def sender(target):
    with open('logo.txt', 'rt') as showmetheports:
        print(showmetheports.read())

    target_ip = socket.gethostbyname(target)
    print("============================================")
    print(f"[+] Scanning the target: [{target_ip}] ...")
    print("============================================")
    print()

    if port is not None and sp is None:
        for ports_list in range(1, (port + 1)):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.12)
            response = sock.connect_ex((f"{target_ip}", ports_list))
            if response == 0:

                open_ports.append(ports_list)
                print()
                print("[+] Found!: ", ports_list, "STATUS: OPEN!")
                print()
    elif port is not None and sp is not None:
        print("Improper use of arguments. It makes no sense to use -lp with port specific fetching enabled")
        
    elif port is None and sp is None:
        print("""
----------------------------------------------------------------------------------------
WARNING: port scan threshold not selected. This means that the process may take a while.
----------------------------------------------------------------------------------------
""")
        for ports_list in range(1, 65536):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.1)
            response = sock.connect_ex((f"{target_ip}", ports_list))
            if response == 0:

                open_ports.append(ports_list)
                print()
                print("[+] Found!: ", ports_list, "STATUS: OPEN!")
                print()

    if sp is not None:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.12)
        response = sock.connect_ex((f"{target_ip}", sp))
        if response == 0:

            open_ports.append(sp)
            print()
            print("[+] Found!: ", sp, "STATUS: OPEN!")
            print()


def banner_grabber(target):
    target_ip = socket.gethostbyname(target)
    print()
    print()
    print("===================")
    print("[+] Getting Banner")
    print("===================")
    print()
    
    if sp is None:
        for list in open_ports:
            print(f"Running Now on port {list}:")
            system(f'nc -v -W 1 -w 1 {target_ip} {list}')
            if list == 80 or list == 8080:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(0.12)
                sock.connect((f"{target_ip}", list))
                sock.send('GET\n'.encode())
                response = sock.recv(1024)
                print(response)
            print()
            print()    
    else:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((f"{target_ip}", sp))
        print(f"Running Now on port {sp}:")
        system(f'nc -v -W 2 -w 2 {target_ip} {sp}')
        if sp == 80 or sp == 8080:
            sock.send('GET\n'.encode())
            response = sock.recv(1024)
            print(response)
    print()
    print()


if host is not None and banner is not None:
    sender(host)
    banner_grabber(host)
    print("---- FINISHED ----")
    print()
elif host is not None and banner is None:
    sender(host)
    print("---- FINISHED ----")
    print()

if host is None:
    parser.print_usage()
    print("Info: ShowMeThePorts.py -t/--target <target address or DNS> -lp/\
--limitPort <maximum port to search> -b/--banner <get active service> -p/--p\
 <especifc port number")
    print()
    print("Example: python3 ShowMeThePorts.py --target site.com -lp 1000")
    print("Example: python3 ShowMeThePorts.py -t www.hackme.com --banner")
    print()
    print("some banners may not appear with the -lp option but may appear if you only scan the desired port with the -p option")
