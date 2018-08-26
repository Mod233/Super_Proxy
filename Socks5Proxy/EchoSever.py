from socket import *
from threading import *
from logging import *
from struct import *


def handle_con(socketclient, addr):
    socketclient.send(addr)


def main():
    socketsever = socket(AF_INET, SOCK_STREAM)
    socketsever.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    socketsever.bind(('', 1523))
    socketsever.listen(10)
    print("socketsever is listening")
    try:
        while True:
            sock, addr = socketsever.accept()
            print("addr type is %s" % type(addr))
            print("connecting from %s" % addr)
            t = Thread(target=handle_con, args=(sock, addr))
            t.start()
    except error as e:
        error(e)
    except (KeyboardInterrupt, SystemExit):
        socketsever.close()


if __name__ == '__main__':
    main()