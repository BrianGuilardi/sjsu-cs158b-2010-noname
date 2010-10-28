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

import pygtk
pygtk.require('2.0')
import gtk

from snmp.builder import Builder

class TreeStore(gtk.TreeStore):
	"""
	Store the data for building the tree.
	"""
	def __init__(self, mibs):
		"""
		Create the store.
		"""
		gtk.TreeStore.__init__(self, str, int, str)

		self.builders = []
		for mib in mibs:
			self.builders.append(Builder(mib))

		for builder in self.builders:
			self.create_rows(builder)

	def create_rows(self, builder):
		"""
		Create a row of the tree.
		"""
		parts = builder.get_parts()

		for part in parts:
			old_part = None
			labels = part[0]
			oids = part[1]
			for label, oid in zip(labels, oids):
				# Update the full OID and
				# Create an iterator, so we can check for duplicates
				if old_part is None:
					iterator = self.get_iter_first()
					full_oid = str(oid)
				else:
					iterator = self.iter_children(old_part)
					full_oid = full_oid + '.' + str(oid)
	
				match = False
				if iterator is None:
					old_part = self.append(old_part, [label, oid, full_oid ])
					continue
				else:
					while iterator:
						if self.get_value(iterator, 0) == label:
							match = True
							break
						else:
							iterator = self.iter_next(iterator)
				if not match:
					old_part = self.append(old_part, [label, oid, full_oid])
				else:
					old_part = iterator
					# old_part = self.append(old_part, None)
