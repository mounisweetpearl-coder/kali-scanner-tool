#!/usr/bin/env python3
import socket
import argparse
import sys

def scan_port(target, port):
    try:
        # Create a socket object (AF_INET = IPv4, SOCK_STREAM = TCP)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1) # Wait 1 second for a response
        result = s.connect_ex((target, port)) # 0 means port is open
        if result == 0:
            print(f"[+] Port {port} is OPEN")
        s.close()
    except Exception as e:
        pass

def main():
    parser = argparse.ArgumentParser(description="Simple Kali Port Scanner")
    parser.add_argument("-t", "--target", help="Target IP or Domain", required=True)
    parser.add_argument("-p", "--ports", help="Range of ports (e.g., 1-100)", default="1-1024")
    args = parser.parse_args()

    target = args.target
    start_port, end_port = map(int, args.ports.split('-'))

    print(f"[*] Scanning {target} from port {start_port} to {end_port}...")
    for port in range(start_port, end_port + 1):
        scan_port(target, port)
    print("[*] Scan complete.")

if __name__ == "__main__":
    main()
