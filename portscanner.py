import argparse
import socket
import ipaddress
import threading
from concurrent.futures import ThreadPoolExecutor

# Function to check if the port is open
def check_port(ip, port, timeout):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((ip, port))  # Connect to the port
        sock.close()

        # If result is 0, the port is open
        if result == 0:
            print(f"Port {port} is open on {ip}")
    except socket.error as err:
        # Skip error
        pass

# Function to scan a single IP
def scan_ip(ip, port_range, timeout):
    for port in port_range:
        check_port(ip, port, timeout)

# Function to parse the port range (e.g., 1-1024 or just 80)
def parse_port_range(port_range_str):
    ports = []
    if '-' in port_range_str:
        start_port, end_port = map(int, port_range_str.split('-'))
        ports = range(start_port, end_port + 1)
    else:
        ports = [int(port_range_str)]
    return ports

# Function to scan a range of IPs using multiple threads
def scan_ip_range(ip_range, port_range, timeout, threads):
    with ThreadPoolExecutor(max_workers=threads) as executor:
        for ip in ip_range:
            executor.submit(scan_ip, str(ip), port_range, timeout)

# Main function to handle argument parsing and scanning
def main():
    parser = argparse.ArgumentParser(description="Port scanner")
    parser.add_argument("ip_range", help="IP range in CIDR format (e.g., 192.168.1.0/24)")
    parser.add_argument("ports", help="Port range (e.g., 1-1024 or a single port like 80)")
    parser.add_argument("-t", "--timeout", type=float, default=1.0, help="Timeout for each connection attempt (in seconds)")
    parser.add_argument("-T", "--threads", type=int, default=10, help="Number of threads to use for scanning")

    args = parser.parse_args()

    # Parse IP range using ipaddress module
    ip_range = list(ipaddress.IPv4Network(args.ip_range).hosts())

    # Parse port range
    port_range = parse_port_range(args.ports)

    print(f"Scanning IP range {args.ip_range} for ports {args.ports} with a timeout of {args.timeout} seconds and {args.threads} threads...")

    scan_ip_range(ip_range, port_range, args.timeout, args.threads)

if __name__ == "__main__":
    main()
