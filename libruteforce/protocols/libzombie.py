import socket
import time
from ..shared import * # Shared Brute Force Library
from  .shared import * # Shared Protocol Library


def parse(data: bytes):
	if not data:
		return None
	
	data_parsed = data.split(b"\r", 1)
	if len(data_parsed) == 0:
		return packet(None)
	if len(data_parsed) == 1:
		return packet(data_parsed[0])
	if len(data_parsed) == 2:
		return packet(data_parsed[0], bytearray(data_parsed[1]))

def status(status_line: bytes):
	status_line_parsed = status_line.split(b" ")
	if len(status_line_parsed) == 0:
		raise ProtocolError("Invalid status line response")
	if len(status_line_parsed) == 1:
		if status_line_parsed[0] == b"INTERNAL_ERROR":
			raise ClientError
		raise ProtocolError("Invalid status line response")
	if len(status_line_parsed) == 2:
		if status_line_parsed[0] == b"STATUS":
			pass


class zombie:
	def __init__(self, socket_obj: socket.socket):
		self.socket = socket_obj

	def ping(self):
		self.socket.send(b"PING\r")
		starttime = time.time_ns()
		if self.socket.recv(1):
			return time.time_ns() - starttime
		else:
			raise ConnectionResetError

	def activate(self):
		self.socket.sendall(b"ACTIVATE\r")
		response = parse(self.socket.recv(40))
		if response is None:
			raise ConnectionResetError
		return status(response.head)

class client:
	def __init__(self, router=("127.0.0.1", 9797)):
		self.client = socket.socket()
		self.router = router
		self.connect_reset()

	def connect_reset(self):
		self.client.close()
		self.client = socket.socket()
		self.client.connect(self.router)

	def connect_zombie(self):
		self.client.sendall(b"CONNECT Zombie\r")
		response = parse(self.socket.recv(40))

	def connect_master(self, auth_token=None):
		self.client.sendall(b"CONNECT Master\r")


class server:
	def __init__(self, address=("127.0.0.1", 9797)):
		self.server = socket.socket()
		self.server.bind(address)
		self.server.listen()
		self.zombies = []
		self.master = None

	def await_master(self, auth_ip=None, auth_token=None):
		if not any((accept_master, accept_token)):
			raise AuthenticationError("At least one authentication method is required to start the server, received 0")

	def ask_ready(self):
		pass