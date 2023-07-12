import ipaddress
import socket
import requests

API_KEY = 'API KEY HERE'  # Replace with your actual API key

def get_location(ip_address):
    api_url = f'https://api.ipgeolocation.io/ipgeo?apiKey={API_KEY}&ip={ip_address}'
    response = requests.get(api_url)
    if response.status_code == 200:
        location_data = response.json()
        country = location_data['country_name']
        city = location_data['city']
        continent = location_data['continent_name']
        postal = location_data['zipcode']
        latitude = location_data['latitude']
        longitude = location_data['longitude']
        organization = location_data['organization']
        connection_type = location_data['connection_type']
        isp = location_data['isp']
        country_flag = location_data['country_flag']
        time_zone = location_data['time_zone']['name']
        current_time = location_data['time_zone']['current_time']

        asn = location_data.get('asn', 'N/A')  # Handle the case when 'asn' key is not present

        return f"The IP address {ip_address} is located in {city}, {country} ({continent}). Postal Code: {postal}. Coordinates: {latitude}, {longitude}\nOrganization: {organization}\nConnection Type: {connection_type}\nISP: {isp}\nCountry Flag: {country_flag}\nASN: {asn}\nTime Zone: {time_zone}\nCurrent Time: {current_time}"
    else:
        return "Unable to retrieve geolocation data."

def subnet_division(network_ip, subnet_mask, num_subnets):
    network = ipaddress.ip_network(network_ip + '/' + subnet_mask, strict=False)
    subnet_prefix = network.prefixlen + num_subnets.bit_length() - 1
    subnets = list(network.subnets(new_prefix=subnet_prefix))
    return subnets

def get_user_input():
    choice = input("What do you want to do?\n1. Subnetting\n2. Decimal to Binary\n3. Binary to Decimal\n4. Calculate Subnets and Hosts\n5. Reverse DNS Lookup\n6. IP Address Geolocation\n7. Network Port Scanning\n")
    return choice

def handle_subnetting():
    network_ip = input("Enter the network IP: ")
    subnet_mask = input("Enter the subnet mask: ")
    num_subnets = int(input("Enter the number of subnets: "))

    if not is_valid_ip_address(network_ip) or not is_valid_ip_address(subnet_mask):
        print("Invalid IP address format. Please enter valid IP addresses.")
        return

    subnets = subnet_division(network_ip, subnet_mask, num_subnets)

    # Save subnet details to a text file
    file_name = input("Enter the file name to save subnet details: ")
    save_subnet_details(subnets, network_ip, subnet_mask, num_subnets, file_name)

def handle_decimal_to_binary():
    decimal = int(input("Enter a decimal number: "))
    binary = decimal_to_binary(decimal)
    print("Binary representation:", binary)

def handle_binary_to_decimal():
    binary = input("Enter a binary number: ")
    decimal = binary_to_decimal(binary)
    print("Decimal representation:", decimal)

def handle_calculate_subnets_hosts():
    subnet_mask = input("Enter the subnet mask: ")
    if not is_valid_ip_address(subnet_mask):
        print("Invalid IP address format. Please enter a valid subnet mask.")
        return

    calculate_subnets_hosts(subnet_mask)

def handle_reverse_dns_lookup():
    ip_address = input("Enter an IP address: ")
    if not is_valid_ip_address(ip_address):
        print("Invalid IP address format. Please enter a valid IP address.")
        return

    domain_name = reverse_dns_lookup(ip_address)
    print("Domain name:", domain_name)

def handle_ip_address_geolocation():
    ip_address = input("Enter an IP address: ")
    if not is_valid_ip_address(ip_address):
        print("Invalid IP address format. Please enter a valid IP address.")
        return

    location = get_location(ip_address)
    print(location)

def handle_network_port_scanning():
    ip_address = input("Enter an IP address: ")
    if not is_valid_ip_address(ip_address):
        print("Invalid IP address format. Please enter a valid IP address.")
        return

    scan_ports(ip_address)

def is_valid_ip_address(ip_address):
    try:
        ipaddress.ip_address(ip_address)
        return True
    except ValueError:
        return False

def save_subnet_details(subnets, network_ip, subnet_mask, num_subnets, file_name):
    with open(file_name, 'w') as file:
        file.write(f"Network IP: {network_ip}\n")
        file.write(f"Subnet Mask: {subnet_mask}\n")
        file.write(f"Number of Subnets: {num_subnets}\n\n")

        for i, subnet in enumerate(subnets, start=1):
            file.write(f"Subnet {i}:\n")
            file.write(f"Network ID: {subnet.network_address}\n")
            file.write(f"Subnet Mask: {subnet.netmask}\n")
            file.write(f"Host ID Range: {subnet.network_address + 1} - {subnet.broadcast_address - 1}\n")
            file.write(f"# of Usable Host IDs: {subnet.num_addresses - 2}\n")
            file.write(f"Broadcast ID: {subnet.broadcast_address}\n\n")

def decimal_to_binary(decimal):
    binary = bin(decimal)[2:]
    return binary

def binary_to_decimal(binary):
    decimal = int(binary, 2)
    return decimal

def calculate_subnets_hosts(subnet_mask):
    network = ipaddress.ip_network(f'0.0.0.0/{subnet_mask}', strict=False)
    subnet_bits = subnet_mask.count('1')
    subnets = 2 ** subnet_bits
    hosts = network.num_addresses - 2
    print(f"Number of subnets: {subnets}")
    print(f"Number of hosts per subnet: {hosts}")

def reverse_dns_lookup(ip_address):
    try:
        domain_name = socket.gethostbyaddr(ip_address)[0]
        return domain_name
    except socket.herror:
        return "N/A"

def scan_ports(ip_address):
    open_ports = []
    for port in range(1, 65536):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip_address, port))
        if result == 0:
            open_ports.append(port)
        sock.close()

    if len(open_ports) > 0:
        print(f"Open ports on {ip_address}:")
        for port in open_ports:
            print(f"Port {port} is open")
    else:
        print(f"No open ports found on {ip_address}")

# Main script
while True:
    choice = get_user_input()

    if choice == "1":
        handle_subnetting()
    elif choice == "2":
        handle_decimal_to_binary()
    elif choice == "3":
        handle_binary_to_decimal()
    elif choice == "4":
        handle_calculate_subnets_hosts()
    elif choice == "5":
        handle_reverse_dns_lookup()
    elif choice == "6":
        handle_ip_address_geolocation()
    elif choice == "7":
        handle_network_port_scanning()
    else:
        print("Invalid choice. Please select a valid option (1, 2, 3, 4, 5, 6, or 7).")
