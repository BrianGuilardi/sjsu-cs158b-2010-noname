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
from widgets.textview import TextView

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
		self.scrolled_text = gtk.ScrolledWindow()

		self.set_title("Noname MIB 'Browser'")
		self.set_size_request(640, 480)
		self.connect('delete_event', self.delete_event)

		label = gtk.Label('Address: ')
		inputbox = gtk.Entry()
		self.hbox = gtk.HBox()
		self.hbox.pack_start(label, expand = False)
		self.hbox.pack_start(inputbox)

		self.textview = TextView()

		self.treeview = TreeView(
				('TCP-MIB', 'UDP-MIB', 'IF-MIB', 'HOST-RESOURCES-MIB',),
				self.textview,
				inputbox)

		self.radio_box = gtk.HBox()
		button = gtk.RadioButton(None, "Get")
		button.connect("toggled", self.change_func, "get")
		self.radio_box.pack_start(button)
		button = gtk.RadioButton(button, "Get-Next")
		button.connect("toggled", self.change_func, "get-next")
		self.radio_box.pack_start(button)
		button = gtk.RadioButton(button, "Get-Bulk")
		button.connect("toggled", self.change_func, "get-bulk")
		self.radio_box.pack_start(button)

		self.vbox = gtk.VBox()
		self.scrolled.add_with_viewport(self.treeview)
		self.scrolled_text.add_with_viewport(self.textview)
		self.vbox.pack_start(self.hbox, expand=False)
		self.vbox.pack_start(self.radio_box, expand=False)
		self.vbox.pack_start(self.scrolled)
		self.vbox.pack_start(self.scrolled_text)

		self.add(self.vbox)

		self.change_func(None, 'get')

		self.show_all()

	def change_func(self, widget, data=None):
		"""
		Change which function we execute.
		"""
		self.func = data
		self.treeview.change_func(self.func)

	def run(self):
		"""
		Run the application.
		"""
		gtk.main()
		return
