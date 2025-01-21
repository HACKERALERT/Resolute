from multiprocessing import Queue, Process
from socket import socket, AF_INET, SOCK_STREAM
from resolute.http._handler import pool, handle

def accept(host: str, port: int, queue: Queue):
	with socket(family=AF_INET, type=SOCK_STREAM) as sock:
		sock.bind((host, port))
		sock.listen(4096)
		while True:
			queue.put(sock.accept()[0], block=True, timeout=None)

def listen(host: str = "127.0.0.1", port: int = 8000):
	connQueue: Queue[socket] = Queue()
	Process(target=accept, args=(host, port, connQueue), daemon=True).start()
	while True:
		conn = connQueue.get(block=True, timeout=None)
		pool.submit(handle, conn)
