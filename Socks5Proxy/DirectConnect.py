from socket import *


def main():
    socketclient = socket(AF_INET, SOCK_STREAM)
    socketclient.connect(('127.0.0.1', 1523))
    print(socketclient.recv(4096))


if __name__ == '__main__':
    main()
