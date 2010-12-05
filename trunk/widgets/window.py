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
		self.set_box = None

		self.set_title("Noname MIB 'Browser'")
		self.set_size_request(640, 480)
		self.connect('delete_event', self.delete_event)

		label = gtk.Label('Address: ')
		self.inputbox = gtk.Entry()
		self.hbox = gtk.HBox()
		self.hbox.pack_start(label, expand = False)
		self.hbox.pack_start(self.inputbox)

		self.login_box = gtk.HBox()
		label = gtk.Label('Username: ')
		self.login_box.pack_start(label, expand = False)
		self.uname_box = gtk.Entry()
		self.login_box.pack_start(self.uname_box)
		label = gtk.Label('Password: ')
		self.login_box.pack_start(label, expand = False)
		self.passwd_box = gtk.Entry()
		self.passwd_box.set_visibility(False)
		self.login_box.pack_start(self.passwd_box)
		button = gtk.Button('Login')
		button.connect('clicked', self.login)
		self.login_box.pack_start(button)

		self.vbox = gtk.VBox()
		self.vbox.pack_start(self.hbox, expand=False)
		self.vbox.pack_start(self.login_box, expand = False)

		self.add(self.vbox)

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

		if self.set_box is None:
			self.set_box = gtk.HBox()
			label = gtk.Label('OID: ')
			self.set_box.pack_start(label, expand = False)
			self.set_entry_oid = gtk.Entry()
			self.set_box.pack_start(self.set_entry_oid)
			label = gtk.Label('Value: ')
			self.set_box.pack_start(label, expand = False)
			self.set_entry_value = gtk.Entry()
			self.set_box.pack_start(self.set_entry_value)
			button = gtk.Button('Set')
			button.connect('clicked', self.set_value)
			self.set_box.pack_start(button, expand = False)
			
			self.vbox.pack_start(self.set_box, expand = False)


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
	
	def set_value(self, widget, data = None):
		"""
		Set the value at the OID in self.set_entry_oid
		"""
		self.nms_accessor.set_value(self.combobox.get_active_text(),
				self.set_entry_oid.get_text(),
				self.set_entry_value.get_text())

	def run(self):
		"""
		Run the application.
		"""
		gtk.main()
		return
