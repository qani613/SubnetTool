import ipaddress

def get_user_input():
    choice = input("What do you want to do?\n1. Subnetting\n2. Decimal to Binary\n3. Binary to Decimal\n4. Calculate Subnets and Hosts\n")
    return choice

def handle_subnetting():
    network_ip = input("Enter the network IP: ")
    subnet_mask = input("Enter the subnet mask: ")
    num_subnets = int(input("Enter the number of subnets: "))
    
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
    calculate_subnets_hosts(subnet_mask)

def subnet_division(network_ip, subnet_mask, num_subnets):
    network = ipaddress.ip_network(network_ip + '/' + subnet_mask, strict=False)
    
    subnet_prefix = network.prefixlen + num_subnets.bit_length() - 1
    subnets = list(network.subnets(new_prefix=subnet_prefix))
    
    return subnets

def decimal_to_binary(decimal):
    binary = bin(decimal)[2:]
    return binary

def binary_to_decimal(binary):
    decimal = int(binary, 2)
    return decimal

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
            file.write(f"# of usable host IDs: {subnet.num_addresses - 2}\n")
            file.write(f"Broadcast ID: {subnet.broadcast_address}\n\n")
    
    print(f"Subnet details have been saved to {file_name}")

def calculate_subnets_hosts(subnet_mask):
    network = ipaddress.ip_network(f"0.0.0.0/{subnet_mask}", strict=False)
    num_subnets = network.num_networks
    num_hosts = network.num_addresses - 2  # Exclude network and broadcast addresses

    print(f"Number of Subnets: {num_subnets}")
    print(f"Number of Hosts per Subnet: {num_hosts}")

# Main script
choice = get_user_input()

if choice == "1":
    handle_subnetting()
elif choice == "2":
    handle_decimal_to_binary()
elif choice == "3":
    handle_binary_to_decimal()
elif choice == "4":
    handle_calculate_subnets_hosts()
else:
    print("Invalid choice. Please select 1, 2, 3, or 4.")
