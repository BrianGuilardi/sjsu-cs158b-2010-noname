#!/usr/bin/env python

import socket

BUFFER_SIZE = 1024

class NMSAccessor(object):
	"""
	Accessor to the NMS server.
	"""
	def __init__(self, ip = '127.0.0.1', port = '12345'):
		"""
		Create the accessor.
		"""
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.connect((ip, int(port)))
	
	def login(self, uname, passwd):
		"""
		Login to the server.
		"""
		message = 'login %s %s \n' % (uname, passwd)
		self.sock.send(message)
		data = self.sock.recv(BUFFER_SIZE)

	def get_devices(self):
		"""
		Returns the list of devices the server knows about.
		"""
		message = 'devices \n'
		self.sock.send(message)
		data = self.sock.recv(BUFFER_SIZE)

		data = data.split(' ')
		return data[1:-1]

	def get_oids(self, device):
		"""
		Get the OID's the given device supports
		"""
		message = 'list %s \n' % (device)
		self.sock.send(message)
		data = self.sock.recv(BUFFER_SIZE)

		data = data.split(' ')
		return data[1:-1]

	def get_label(self, device, oid):
		"""
		Get the label the device has for a given oid
		"""
		message = 'name %s %s \n' % (device, oid)
		self.sock.send(message)
		data = self.sock.recv(BUFFER_SIZE)

		data = data.split(' ')
		return data[1]

	def get_value(self, device, oid):
		"""
		Get the data associated with this OID on this device.
		"""
		message = 'get %s %s \n' % (device, oid)
		self.sock.send(message)
		data = self.sock.recv(BUFFER_SIZE)

		data = data.split(' ')
		return data[1]

	def set_value(self, device, oid, value):
		""""
		Set the value associated with the OID.
		"""
		message = 'set %s %s %s \n' % (device, oid, value)
		self.sock.send(message)
		data = self.sock.recv(BUFFER_SIZE)

		data = data.split(' ')
		return data[1:]
