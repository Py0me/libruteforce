import socket
import ssl
import random
import urllib.parse

sslcontext = ssl.create_default_context()

class RandomArray:
	def __init__(self, data):
		self.data = tuple(data)

	def __call__(self, max_iterations=None):
		if max_iterations is None:
			self.max_iterations = None
		elif max_iterations < 1:
			raise ValueError("The iteration limit must be set to a value greater than zero")
		elif not isinstance(max_iterations, int):
			raise ValueError("The iteration limit must be of type 'int'")
		else:
			self.max_iterations = max_iterations

	def get(self):
		return random.choice(self.data)

	def __iter__(self):
		self.iteration = 0
		return self

	def __next__(self):
		if max_iterations:
			self.iteration += 1
			if self.iteration > max_iterations:
				raise StopIteration
		return self.get()

with open("user-agents.txt", "rb") as file:
	USER_AGENTS = RandomArray(file.read().splitlines())

class BruteForce:
	def __init__(self, target):
		self.target = target
		self.http_header = bytearray()
		self.client = socket.socket()

	def _parse_header(self):
		self.http_header.clear()
		self.http_header.extend(b"%s %s HTTP/1.1\r\nHost: %s\r\nUser-Agent: %{UAagent}\r\nConnection: keep-alive\r\n\r\n" %(self.method, self.uri, self.target.netloc))

	def _insert_uagent(self, agent):
		self.http_header.replace(b"%{UAgent}", agent)

	def force(self, target, method="GET", iterations=None, timeout_frequency=None, timeout_duration=None):
		self.target = urllib.parse.urlsplit(target.encode())
		self.realhost = socket.gethostbyname(self.target.netloc)
		self.method = method.encode()
		for uagent in USER_AGENTS(iterations):
			pass

	def _proto_http(self):
		raise NotImplementedError

	def _proto_https(self):
		raise NotImplementedError