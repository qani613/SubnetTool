# Network Tool

This Python script is a versatile network tool that provides various functionalities for network administrators. It includes subnetting, decimal-to-binary and binary-to-decimal conversion, subnet and host calculations, reverse DNS lookup, IP address geolocation, and network port scanning.

## Functionalities

1. **Subnetting**: Perform subnetting calculations to divide an IP network into multiple subnets with custom subnet masks.

2. **Decimal to Binary**: Convert decimal numbers to binary representation.

3. **Binary to Decimal**: Convert binary numbers to decimal representation.

4. **Calculate Subnets and Hosts**: Calculate the number of subnets and hosts per subnet based on a given subnet mask.

5. **Reverse DNS Lookup**: Retrieve the domain name associated with a given IP address.

6. **IP Address Geolocation**: Fetch geolocation data for an IP address, including country, city, organization, ISP, and time zone information. **Note**: To use this functionality, you need to obtain an API key from [IPGeolocation](https://ipgeolocation.io/).

7. **Network Port Scanning**: Scan open ports on a specified IP address or range of IP addresses.

## Usage

1. Clone or download the repository.
2. Run the script `network_tool.py`.
3. Choose one of the available options by entering the corresponding number.
4. Follow the prompts and provide the required inputs as requested.
5. View the output and proceed to the next task or select a new option.

## Requirements

- Python 3.x
- Required Python libraries: `ipaddress`, `socket`, `requests`

## IP Address Geolocation API Key

To use the IP address geolocation functionality (#6), you need to obtain an API key from [IPGeolocation](https://ipgeolocation.io/). Follow these steps to get an API key:

1. Visit [IPGeolocation website](https://ipgeolocation.io/) and sign up for an account.
2. After signing up, navigate to your account dashboard.
3. Locate the API key section and generate an API key for the IP Geolocation service.
4. Copy the API key and replace the placeholder `API-KEY HERE` in the `network_tool.py` script with your actual API key.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

Feel free to explore the different functionalities of this network tool and adapt it to suit your specific needs!
