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

from pysnmp.smi import builder, view

class Builder(object):
	"""
	Build the strings from which the tree and data and gathered.
	"""
	def __init__(self, mib):
		"""
		Create the builder with the given mib module.
		"""
		self.mib = mib
		self.mibbuilder = builder.MibBuilder().loadModules(mib)
		self.viewcontroller = view.MibViewController(self.mibbuilder)

	def get_parts(self):
		"""
		Get the lists of bits of the mib.
		"""
		parts = []

		oid, label, suffix = self.viewcontroller.getFirstNodeName(self.mib)
		parts.append( (label, oid) )

		done = False
		while not done:
			try:
				oid, label, suffix = self.viewcontroller.getNextNodeName(
						label, self.mib)
				parts.append( (label, oid) )
			except:
				done = True

		return parts
