from concurrent.futures import ThreadPoolExecutor
from multiprocessing import cpu_count
from socket import socket

pool = ThreadPoolExecutor(max_workers=(cpu_count() or 1) * 32)

def handle(sock: socket) -> None:
    try:
        sock.settimeout(1)

        sock.recv(4096)
        sock.sendall(b"HTTP/1.1 200 OK\r\nConnection: close\r\nContent-Length: 11\r\n\r\nHello world")
    except:
        pass
    finally:
        sock.close()
