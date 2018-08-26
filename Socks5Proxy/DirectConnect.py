from socket import *


def main():
    socketclient = socket(AF_INET, SOCK_STREAM)
#    socketclient.connect(('47.104.21.159', 1523))
    socketclient.connect(('127.0.0.1', 1523))
    print(socketclient.recv(4096))
    try:
        while True:
            msg = raw_input()
            socketclient.send(msg)
            msg = socketclient.recv(4096)
            print("server echo is: %s" % msg)
    except error as e:
        socketclient.close()
        error(e)
    except (KeyboardInterrupt, SystemExit):
        socketclient.close()


if __name__ == '__main__':
    main()
