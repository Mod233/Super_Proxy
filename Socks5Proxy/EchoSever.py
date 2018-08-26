from socket import *
from threading import *
from logging import *
from struct import *


def handle_con(socketclient, addr):
    socketclient.send("client addr is %s" % (str(addr)))
    try:
        while True:
            msg = socketclient.recv(1024)
            print("msg from client is: %s" % msg)
            socketclient.send("Roger!")
    except error as e:
        socketclient.close()
        error(e)
    except (KeyboardInterrupt, SystemExit):
        socketclient.close()


def main():
    socketsever = socket(AF_INET, SOCK_STREAM)
    socketsever.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    socketsever.bind(('', 1523))
    socketsever.listen(10)
    print("socketsever is listening...")
    try:
        while True:
            sock, addr = socketsever.accept()
            print "connecting from ", addr
            t = Thread(target=handle_con, args=(sock, addr))
            t.start()
    except error as e:
        socketsever.close()
        error(e)
    except (KeyboardInterrupt, SystemExit):
        socketsever.close()


if __name__ == '__main__':
    main()
