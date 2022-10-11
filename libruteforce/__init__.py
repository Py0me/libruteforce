import socket
import ssl
import random
import os
import urllib.parse
from .ddos import *

package = os.path.realpath(__package__)
STD_AGENTS = os.path.join(package, "user-agents.txt")

class RandomArray:
	def __init__(self, data=[]):
		self.data = list(data)
		self.max_iterations = None

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
		if self.data:
			return random.choice(self.data)
		else:
			raise IndexError("No data in array")

	def append(self, data):
		self.data.append(data)

	def extend(self, data):
		self.data.extend(data)

	def clear(self):
		self.data.clear()

	def __bool__(self):
		return bool(self.data)

	def __iter__(self):
		self.iteration = 0
		return self

	def __next__(self):
		if self.max_iterations:
			self.iteration += 1
			if self.iteration > self.max_iterations:
				raise StopIteration
		return self.get()

class BruteForce:
	__doc__ = "\nAttack Types (case insensitive):\n\tReFresh -\n\t\tPerforms as many requests on the target as possible. Response\n\t\tdata will not be saved and only stored temporarily to allow\n\t\taccurate updating of counters, following redirects, etc.\n\t\tIf redirects are enabled, the redirected resources are saved\n\t\tin folders corresponding to their returned status code and\n\t\tprefixed (abcd.) with their hash representation as to prevent\n\t\tfiles from being overriden or duplicated.\n\n\tDoS -\n\t\tSimmilar to the ReFresh attack, but tries to direct as much traffic\n\t\tto the target as possible. Everything in this method is optimized\n\t\tfor speed and quantity of the request. No response data will be\n\t\treceived, and, if supported, UDP mode will be enabled. DoS is\n\t\tthe shorter term for Denial of Service, a type of attack which\n\t\thas been around for a long time and has been well documented by\n\t\tother sources, so there is not as much detail provided here.\n\n\tDDoS -\n\t\tA modified variant of the DoS attack. Uses a decentralized network\n\t\tof zombie computers, which may be created using the methods of the\n\t\tZombieDDoS class in the ddos module. All zombies are controlled\n\t\tby the 'master', a server which functions like a router for all\n\t\tthe instructions that are comming from the master computer. The\n\t\tmaster computer may also be the router, though this is not recommended\n\t\tdue to potential identity leaks or security concerns. Having the\n\t\tmaster computer seperated from the router also has the benefit of\n\t\tbeing able to query multiple servers at the same time which may\n\t\tbe used to activate the zombie network.\n\n\tURL -\n\t\tRuns through a word list or randomly generated text strings.\n\t\tAll responses other than 404 errors will be saved in folders\n\t\tcorresponding to the returned status code. Headers may be saved\n\t\tas well if so requested by the user.\n\n\tLogIn -\n\t\tSends continuous requests to a login page until a non-error status\n\t\tis returned. Supports word lists and randomly generated text strings.\n\n\tPasswrd -\n\t\tRuns through a list of password hashes and tries to crack them one by\n\t\tone using either word lists or randomly generated text strings.\n\n\tSearchHTML -\n\t\tRuns through a list of HTML resources and saves all pages containing the\n\t\tspecified search string to disk. Two types of mode are available for this\n\t\tattack, the first one being the scanning of multiple targets and the second\n\t\tone parsing all encountered documents and subsequently following all links\n\t\tfound on the page ('scraping' and 'indexing' the website). The latter may\n\t\ttake very long depending on the size of the website, which is why this\n\t\tspecific mode has a variety of flags available to operate more efficiently.\n\t\tThose flags include, but are not limited to: maximum nesting depth, follow\n\t\texternal hosts, exclude URLs, ignore status XXX, etc.\n"

	def __init__(self, target, attack="ReFresh"):
		self.target = target
		self.attack = attack.lower()
		self.http_header = bytearray()
		self.client = socket.socket()
		self.user_agents = RandomArray()
		self.sslcontext = ssl.create_default_context()

	# HTTP Requests & Client functions
	def load_user_agents(self, *agents, file=""):
		"""
		Loads a new list of User Agents that may be picked by the request handler. The User Agent strings
		must be of a bytes-like type in order to be properly handled by the _insert_uagent() method.
		"""
		if file:
			with open(file, "rb") as f:
				self.user_agents.extend(f.read().splitlines())
		if agents:
			self.user_agents.extend(agents)

	def clear_user_agents(self):
		"""
		Remove all stored User Agents from the list of possible choices. This might be useful in such cases
		where you want to load a new list of User Agents but only have limited memory resources.
		"""
		self.user_agents.clear()

	def reuse_user_agents(self, reuse=0):
		"""
		Specifies how often the request handler should reuse a certain User Agent string. Values lower
		than 1 will automatically set the reuse count to 0, meaning User Agents will not be reused.
		This doesn't mean that the string will be removed from the list of possibe choices, but rather
		that a new string from the list is randomly selected. Therefore it might be possible that despite
		the reuse count being 0, the same string gets randomly picked again.
		"""
		if isinstance(reuse, int):
			self.reuse_agents = reuse if reuse > 0 else 0
		else:
			raise ValueError("Expected variable of type 'int' but received '%s' instead" %type(reuse))

	def _parse_header(self):
		self.http_header.clear()
		self.http_header.extend(b"%s %s HTTP/1.1\r\nHost: %s\r\nUser-Agent: %{UAagent}\r\nConnection: keep-alive\r\n\r\n" %(self.method, self.uri, self.target.netloc))

	def _insert_uagent(self, agent):
		self.http_header.replace(b"%{UAgent}", agent)

	def force(self, target, method="GET", iterations=None, timeout_frequency=None, timeout_duration=None):
		"""
		The basic method to start a brute force attack. Timeouts may be specified to pause after a certain
		amount of requests as to not overload the target server and risking an IP block from said server.
		Iterations may be specified to set the amount of requests that should be performed.
		"""
		self.target = urllib.parse.urlsplit(target.encode())
		self.realhost = socket.gethostbyname(self.target.netloc)
		self.method = method.encode()
		for uagent in USER_AGENTS(iterations):
			pass

	def _proto_http(self):
		raise NotImplementedError

	def _proto_https(self):
		raise NotImplementedError