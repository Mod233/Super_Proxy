import socks
from socket import *
from logging import *
from struct import *


def main():
    s = socks.socksocket()
    s.set_proxy(socks.SOCKS5, "localhost", 9050)
    s.connect(("95.163.200.165", 1523))
    # s.sendall(('GET /ic.asp HTTP/1.1'))
    print(s.recv(4096))
    try:
        while True:
            msg = raw_input()
            s.sendall(msg)
            echo = s.recv(4096)
            print("msg from sever is ", echo)
    except error as e:
        s.close()
        error(e)
    except (KeyboardInterrupt, SystemExit):
        s.close()


if __name__ == '__main__':
    main()

