import ipaddress
import re
import json
import csv
import math

def validate_ip_address(ip_address):
    ipv4_pattern = r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$'
    ipv6_pattern = r'^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$'

    if re.match(ipv4_pattern, ip_address) or re.match(ipv6_pattern, ip_address):
        return True
    else:
        return False

def validate_subnet_mask(subnet_mask):
    ipv4_pattern = r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$'
    cidr_pattern = r'^\/\d{1,2}$'

    if re.match(ipv4_pattern, subnet_mask) or re.match(cidr_pattern, subnet_mask):
        return True
    else:
        return False

def subnetting(ip_address, subnet_mask):
    if not validate_ip_address(ip_address):
        print("Invalid IP address.")
        return None
    if not validate_subnet_mask(subnet_mask):
        print("Invalid subnet mask.")
        return None

    network = ipaddress.ip_network(ip_address + '/' + subnet_mask, strict=False)
    network_address = str(network.network_address)
    broadcast_address = str(network.broadcast_address)
    netmask = str(network.netmask)
    wildcard = str(network.hostmask)
    cidr = str(network)
    num_addresses = network.num_addresses
    address_type = 'Unicast, Private' if network.network_address.is_private else 'Unicast, Public'
    first_host = str(network.network_address + 1)
    last_host = str(network.broadcast_address - 1)
    binary_address = '.'.join(format(int(x), '08b') for x in network.network_address.packed)
    binary_subnet = '.'.join(format(int(x), '08b') for x in network.netmask.packed)
    binary_network = '.'.join(format(int(x), '08b') for x in network.network_address.packed)

    subnet_info = f"IP Version: IPv{network.version}\n"
    subnet_info += f"IP Address: {ip_address}\n"
    subnet_info += f"Network: {network_address}\n"
    subnet_info += f"Broadcast: {broadcast_address}\n"
    subnet_info += f"NetMask: {netmask}\n"
    subnet_info += f"Wildcard: {wildcard}\n"
    subnet_info += f"CIDR: {cidr}\n"
    subnet_info += f"# of Addresses: {num_addresses}\n"
    subnet_info += f"Address Type: {address_type}\n"
    subnet_info += f"First Host: {first_host}\n"
    subnet_info += f"Last Host: {last_host}\n"
    subnet_info += f"Binary Address: {binary_address}\n"
    subnet_info += f"Binary Subnet: {binary_subnet}\n"
    subnet_info += f"Binary Network: {binary_network}\n"

    return subnet_info

def save_subnet_details(subnet_info, file_name):
    with open(file_name, 'a') as file:
        file.write(subnet_info + "\n\n")

def handle_subnetting_single():
    ip_address = input("Enter an IP address: ")
    subnet_mask = input("Enter the subnet mask: ")
    subnet_info = subnetting(ip_address, subnet_mask)
    print(subnet_info)

    save_option = input("Do you want to save the subnet details? (y/n): ")
    if save_option.lower() == 'y':
        file_name = input("Enter the file name to save the details: ")
        save_subnet_details(subnet_info, file_name)
        print("Subnet details saved successfully.")

def handle_subnetting_multiple():
    ip_address = input("Enter an IP address: ")
    subnet_mask = input("Enter the subnet mask: ")
    num_subnets = int(input("Enter the number of subnets: "))

    network = ipaddress.ip_network(ip_address + '/' + subnet_mask, strict=False)
    prefix_length = int(math.log2(num_subnets))
    subnets = list(network.subnets(new_prefix=network.prefixlen + prefix_length))

    subnet_info = ""
    for i, subnet in enumerate(subnets, start=1):
        subnet_info += f"Subnet {i}\n"
        subnet_info += subnetting(str(subnet.network_address), str(subnet.netmask))
        subnet_info += "\n"

    print(subnet_info)

    save_option = input("Do you want to save the subnet details? (y/n): ")
    if save_option.lower() == 'y':
        file_name = input("Enter the file name to save the details: ")
        save_subnet_details(subnet_info, file_name)
        print("Subnet details saved successfully.")

while True:
    print("What do you want to do?")
    print("1. Subnetting for a single IP")
    print("2. Subnetting for multiple IPs with desired subnets")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        handle_subnetting_single()
    elif choice == '2':
        handle_subnetting_multiple()
    elif choice == '3':
        print("Exiting the program...")
        break
    else:
        print("Invalid choice. Please select 1, 2, or 3.")
