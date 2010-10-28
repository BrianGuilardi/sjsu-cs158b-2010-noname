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

class TreeView(gtk.TreeView):
	"""
	View of the MIB tree structure.
	"""
	def __init__(self, mibs):
		"""
		Create ourself, passing the TreeStore as our Model.
		"""
		gtk.TreeView.__init__(self, TreeStore(mibs))
		self.renderer = gtk.CellRendererText()

		self.column0 = gtk.TreeViewColumn('Name', self.renderer, text=0)
		self.column1 = gtk.TreeViewColumn('OID Part', self.renderer, text=1)
		self.column2 = gtk.TreeViewColumn('Full OID', self.renderer, text=2)

		self.append_column(self.column0)
		self.append_column(self.column1)
		self.append_column(self.column2)

