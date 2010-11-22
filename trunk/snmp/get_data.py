# Copyright (c) 2010 Arthur Mesh
#               2010 Christopher Nelson
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

from pysnmp.entity.rfc3413.oneliner import cmdgen

def next_data(function, addr, oid):
	# Get a command generator
	commandgen = cmdgen.CommandGenerator()
	# Build the command
	ls = [int(bit) for bit in oid.split('.')]
	tup = tuple(ls)
	try:
		errorIndication, errorStatus, errorIndex, varBinds = commandgen.nextCmd(
			cmdgen.CommunityData('noname', 'public'),
			cmdgen.UdpTransportTarget((addr, 161)),
			tup)

		function(0, errorIndication, errorStatus, errorIndex, varBinds, None)
	except:
		pass

def bulk_data(function, addr, oid):
	# Get a command generator
	commandgen = cmdgen.CommandGenerator()
	# Build the command
	ls = [int(bit) for bit in oid.split('.')]
	tup = tuple(ls)

	try:
		errorIndication, errorStatus, errorIndex, varBinds = commandgen.bulkCmd(
			cmdgen.CommunityData('noname', 'public'),
			cmdgen.UdpTransportTarget((addr, 161)),
			0, 25, # non-repeaters, repeaters
			tup)

		function(0, errorIndication, errorStatus, errorIndex, varBinds, None)
	except:
		pass

def get_data(function, addr, oid):
	# Get a command generator
	commandgen = cmdgen.CommandGenerator()
	# Build the command
	ls = [int(bit) for bit in oid.split('.')]
	ls.append(0)
	tup = tuple(ls)

	try:
		errorIndication, errorStatus, errorIndex, varBinds = commandgen.getCmd(
			cmdgen.CommunityData('noname', 'public'),
			cmdgen.UdpTransportTarget((addr, 161)),
			tup)

		function(0, errorIndication, errorStatus, errorIndex, varBinds, None)
	except:
		pass
