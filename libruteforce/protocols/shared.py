class AuthenticationError(Exception):
	pass

class ProtocolInfo(Exception):
	def __init__(self, *args, identifier="BasicProtocolInfo", **data):
		self.args = args
		self.identifier = identifier
		self.__dict__.update(data)

class ProtocolError(Exception):
	pass

class ProtocolWarning(Exception):
	pass

class SeverError(Exception):
	def __init__(self, *args, identifier="BasicServerError", **data):
		self.args = args
		self.identifier = identifier
		self.__dict__.update(data)

class ClientError(Exception):
	def __init__(self, *args, identifier="BasicClientError", **data):
		self.args = args
		self.identifier = identifier
		self.__dict__.update(data)

class packet:
	def __init__(self, head: bytes, body=bytearray()):
		self.head = head
		self.body = body