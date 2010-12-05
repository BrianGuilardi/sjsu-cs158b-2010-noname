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

class Builder(object):
	"""
	Build the strings from which the tree and data and gathered.
	"""
	def __init__(self, nms_accessor):
		"""
		Create the builder with the given mib module.
		"""
		self.nms_accessor = nms_accessor

	def get_parts(self, device):
		"""
		Get the lists of bits of the mib.
		"""
		parts = []
		oids = self.nms_accessor.get_oids(device)

		first = True
		label_prefix = ''
		label_prefix2 = ''
		for oid in oids:
			# on our first go-round, add the initial bits to the label
			bits = oid.split('.')
			old_bits = ''
			label_prefix2 = ''
			for bit in bits:
				old_bits = old_bits + '.' + bit
				old_bits = old_bits.lstrip('.')
				label_prefix2 = \
						label_prefix2 + \
						'.' + \
						self.nms_accessor.get_label(device, old_bits).strip()
			label_prefix = label_prefix.lstrip('.')
			if label_prefix2 != label_prefix:
				label_prefix = label_prefix2

			label = label_prefix + self.nms_accessor.get_label(device, oid).strip()

			oid = oid.split('.')
			label = label.split('.')[1:]

			parts.append((label, oid))

		return parts
