import socket

def request(url):
    assert url.startswith("http://")
    url = url[len("http://"):]

    if ("/" in url):
        host, path = url.split('/', 1)
        path = "/" + path
    else:
        host = url
        path = "/"

    s = socket.socket(
        family=socket.AF_INET,
        type=socket.SOCK_STREAM,
        proto=socket.IPPROTO_TCP,
    )

    print(host)

    s.connect((host, 80))

    # s.send(b"GET /index.html HTTP/1.0\r\n" + b"Host: example.org\r\n\r\n")


def load(url):
    request(url)


if __name__ == "__main__":
    import sys
    load(sys.argv[1])