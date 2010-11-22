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

from widgets.treestore import TreeStore

ADDR = 'localhost'

class TreeView(gtk.TreeView):
	"""
	View of the MIB tree structure.
	"""
	def __init__(self, mibs, textview, inputbox):
		"""
		Create ourself, passing the TreeStore as our Model.
		"""
		self.store = TreeStore(mibs)
		gtk.TreeView.__init__(self, self.store)
		self.renderer = gtk.CellRendererText()

		self.column0 = gtk.TreeViewColumn('Name', self.renderer, text=0)
		self.column1 = gtk.TreeViewColumn('OID Part', self.renderer, text=1)
		self.column2 = gtk.TreeViewColumn('Full OID', self.renderer, text=2)

		self.append_column(self.column0)
		self.append_column(self.column1)
		self.append_column(self.column2)

		# set the TextView so we can edit text.
		self.textview = textview
		self.inputbox = inputbox

		self.connect('row-activated', self.callback)

		self.func = 'get'

	def callback(self, treeview, path, params=None):
		"""
		Callback to process the data from expanding a row.
		"""
		addr = self.inputbox.get_text()
		self.store.get_data(self.set_text, self.func, addr, path)

	def set_text(self, sendRequestHandle,
			errorIndication,
			errorStatus,
			errorIndex,
			varBinds,
			callbackContext):
		"""
		Set the text in the textview.
		"""
		text = ''
		if self.func == 'get-next':
			# get each row of data
			for row in varBinds:
				# for the name and value of the row, add the value to running text
				for name, val in row:
					text = text + '\n' + str(val)

		elif self.func == 'get':
			# Extract the value out of the singleton
			for name, val in varBinds:
				text = text + '\n' + str(val)
		
		elif self.func == 'get-bulk':
			for row in varBinds:
				# for the name and value of the row, add value
				# bulk can return zero-length rows
				if len(row) > 0:
					for name, val in row:
						text = text + '\n' + str(val)

		# output can have arbitrary unicode, including embedded null,
		# which gtk, being C, doesn't deal well with.  Replace
		# embedded nulls with empty string
		text = text.replace('\x00', '').decode('utf-8', 'replace').encode('utf-8')
		self.textview.set_text(text)

	def change_func(self, func):
		"""
		Change which function we execute.
		"""
		self.func = func
