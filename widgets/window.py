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

from snmp.nms_accessor import NMSAccessor

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

		self.scrolled = None
		self.scrolled_text = None
		self.treeview = None
		self.textview = None

		self.set_title("Noname MIB 'Browser'")
		self.set_size_request(640, 480)
		self.connect('delete_event', self.delete_event)

		label = gtk.Label('Address: ')
		self.inputbox = gtk.Entry()
		self.hbox = gtk.HBox()
		self.hbox.pack_start(label, expand = False)
		self.hbox.pack_start(self.inputbox)

		#self.textview = TextView()

		#self.treeview = TreeView(
		#		('TCP-MIB', 'UDP-MIB', 'IF-MIB', 'HOST-RESOURCES-MIB',),
		#		self.textview,
		#		inputbox)

		self.login_box = gtk.HBox()
		label = gtk.Label('Username: ')
		self.login_box.pack_start(label, expand = False)
		self.uname_box = gtk.Entry()
		self.login_box.pack_start(self.uname_box)
		label = gtk.Label('Password: ')
		self.login_box.pack_start(label, expand = False)
		self.passwd_box = gtk.Entry()
		self.login_box.pack_start(self.passwd_box)
		button = gtk.Button('Login')
		button.connect('clicked', self.login)
		self.login_box.pack_start(button)

		"""
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
		"""

		self.vbox = gtk.VBox()
		#self.scrolled.add_with_viewport(self.treeview)
		#self.scrolled_text.add_with_viewport(self.textview)
		self.vbox.pack_start(self.hbox, expand=False)
		self.vbox.pack_start(self.login_box, expand = False)
		#self.vbox.pack_start(self.radio_box, expand=False)
		#self.vbox.pack_start(self.scrolled)
		#self.vbox.pack_start(self.scrolled_text)

		self.add(self.vbox)

		#self.change_func(None, 'get')

		self.show_all()

	def login(self, widget, data = None):
		"""
		Login to the application.
		"""
		# first, create the nms_accessor
		self.nms_accessor = NMSAccessor(self.inputbox.get_text())
		# then, login
		self.nms_accessor.login(self.uname_box.get_text(),
				self.passwd_box.get_text())
		# then, set up the choice of devices to activate
		self.combobox = gtk.combo_box_new_text()
		combo_data = self.nms_accessor.get_devices()
		for data in combo_data:
			self.combobox.append_text(data)
		self.combobox.set_active(1)
		self.combobox.connect('changed', self.change_device)

		self.vbox.remove(self.login_box)
		self.vbox.pack_start(self.combobox, expand = False)

		self.change_device(None)

		self.show_all()

	def change_device(self, widget, data = None):
		"""
		Change which device we're looking at.
		"""

		if self.scrolled is not None:
			self.vbox.remove(self.scrolled)
		if self.scrolled_text is not None:
			self.vbox.remove(self.scrolled_text)

		self.scrolled = gtk.ScrolledWindow()
		self.scrolled_text = gtk.ScrolledWindow()

		self.textview = TextView()

		self.treeview = TreeView(self.textview,
				self.nms_accessor, 
				self.combobox.get_active_text())

		if self.treeview is not None:
			self.scrolled.remove(self.treeview)
		self.scrolled.add_with_viewport(self.treeview)
		if self.textview is not None:
			self.scrolled_text.remove(self.textview)
		self.scrolled_text.add_with_viewport(self.textview)

		self.vbox.pack_start(self.scrolled)
		self.vbox.pack_start(self.scrolled_text)

		self.show_all()
	
	'''
	def change_func(self, widget, data=None):
		"""
		Change which function we execute.
		"""
		self.func = data
		self.treeview.change_func(self.func)
	'''

	def run(self):
		"""
		Run the application.
		"""
		gtk.main()
		return
