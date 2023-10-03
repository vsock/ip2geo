import requests
import socket
import argparse
import sys

api_key = "4d1009d1ce926ee6e8248851bfa12251"


def get_location_data(ip_address):
    base_url = "http://api.ipstack.com/"
    response = requests.get(f"{base_url}{ip_address}?access_key={api_key}")
    data = response.json()
    return data


def get_args():
    parser = argparse.ArgumentParser(
        prog='IP to GEO LOCATION',
        description='script prints GEO location coordinates in latittude,longitude format for a given TCP/IP address')
    parser.add_argument('ip_address', help='Enter a valid ip address or url i.e 142.251.46.228 or www.google.com')
    parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")
    return parser.parse_args()


if __name__ == "__main__":

    args = get_args()

    try:
        ipv4 = socket.gethostbyname(args.ip_address)
        location_data = get_location_data(ipv4)
        latitude, longitude = (location_data['latitude'], location_data['longitude'])
        if args.verbose:
            print(location_data)
        else:
            print(f"{latitude}, {longitude}")
        if "error" in location_data:
            error_message = location_data["error"]["info"]
            print(error_message)
    except Exception as Error:
        print(f"IP address {args.ip_address} not found")
        sys.exit(1)
    sys.exit()

