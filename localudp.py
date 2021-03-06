import socket
import select


class Server(object):

    """docstring for Server"""

    def __init__(self, host='0.0.0.0', port=5000):
        self.host = host
        self.port = port

        self.ss = self.init_socket()
        self.clientaddr = None

    def init_socket(self):
        ss = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        ss.bind((self.host, self.port))
        return ss

    def recv_data(self):
        data, self.clientaddr = self.ss.recvfrom(2048)
        print data
        return data

    def send_data(self, serveraddr, data):
        self.ss.sendto(data, serveraddr)

    def close(self):
        self.ss.close()

        epoll.unregister(ss.fileno())
        epoll.close()
        ss.close()

if __name__ == '__main__':
    serveraddr = ('104.224.132.120', 5000)
    port = 5001
    ss = Server(port=port)
    ss.send_data(serveraddr, 'client connect')
    ss.recv_data()
    ss.close()
