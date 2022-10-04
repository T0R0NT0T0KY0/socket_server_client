import socket
import ipaddress

from timeserver import print_hi

def create_socket_client(ip_address, port):
    skt = socket.socket()
    skt.connect((ip_address, port))
    return skt


def validate_ip_address(ip_address):
    try:
        ipaddress.ip_address(ip_address)
        return ip_address != '0.0.0.0'
    except ValueError:
        # Not legal
        return False


def ask_ip_address():
    while True:
        ip_address = input('Enter IP Address: ')
        if validate_ip_address(ip_address):
            return ip_address
        else:
            print(f'Invalid IP Address: {ip_address}')


def accept_socket_client(skt):
    data = skt.recv(1024).decode()
    print(f'Server Date: {data}')


if __name__ == '__main__':
    print_hi('PyCharm')
    try:
        ip_address = ask_ip_address()
        skt = create_socket_client(ip_address, 1303)
        accept_socket_client(skt)
    except KeyboardInterrupt:
        print("\nProgram Exit")
        pass
