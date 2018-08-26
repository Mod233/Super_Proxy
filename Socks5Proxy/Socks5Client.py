import socks


def main():
    s = socks.socksocket()
    s.set_proxy(socks.SOCKS5, "localhost", 1077)
    s.connect(("www.ip132.com", 80))
    s.sendall(('GET /ic.asp HTTP/1.1'))
    print(s.recv(4096))


if __name__ == '__main__':
    main()
