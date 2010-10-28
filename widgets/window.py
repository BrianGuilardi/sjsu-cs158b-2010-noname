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

from widgets.treeview import TreeView

class Window(gtk.Window):
	"""
	Top-level window of the application.
	"""
	
	def delete_event(self, widget, event, data=None):
		"""
		Close the window and exit.
		"""
		gtk.main_quit()
		return False

	def __init__(self):
		"""
		Create the top-level window and add children to it.
		"""
		gtk.Window.__init__(self, gtk.WINDOW_TOPLEVEL)
		
		self.scrolled = gtk.ScrolledWindow()

		self.set_title("Noname MIB 'Browser'")
		self.set_size_request(640, 480)
		self.connect('delete_event', self.delete_event)

		self.treeview = TreeView(
				('TCP-MIB', 'UDP-MIB', 'IF-MIB', 'HOST-RESOURCES-MIB',))

		self.scrolled.add_with_viewport(self.treeview)
		self.add(self.scrolled)

		self.show_all()

	def run(self):
		"""
		Run the application.
		"""
		gtk.main()
		return
