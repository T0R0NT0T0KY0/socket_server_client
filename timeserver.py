import socket
import datetime


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


#  в формате 22.09.2022 17:30
def send_date_in_socket(conn):
    now = datetime.datetime.now()
    conn.send(now.strftime('%Y.%m.%d %H:%M').encode())


class SocketListener:

    def __init__(self, host, port, backlog):
        self.host = host
        self.port = port
        self.skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.skt.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.skt.bind((host, port))
        self.skt.listen(backlog)
        print(f"Date: {datetime.datetime.now()} Listener Host: {self.host} And Port: {self.port} ")

    def accept(self):
        while True:
            conn, addr = self.skt.accept()
            print(f'connected: {addr}, Time: {datetime.datetime.now()}')
            send_date_in_socket(conn)
            conn.close()

    def close(self):
        self.skt.close()


if __name__ == '__main__':
    print_hi('PyCharm')
    sock = None
    try:
        sock = SocketListener('0.0.0.0', 1303, 1)
        sock.accept()
    except KeyboardInterrupt:
        print("\nProgram Exit")
        sock.close()
        pass
