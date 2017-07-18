
#def agregar_boton(self):
#	self.boton = Gtk.Button('agregar')

import gi
gi.require_version('Gtk','3.0')

from gi.repository import Gtk, Gio, GLib

from activos import Mi_Ventana

class CursoPythonApp(Gtk.Application):
	def __init__(self, *args, **kwargs):
		super(CursoPythonApp, self).__init__(
			*args,
			application_id='of.cursopython.cursopythonapp',
			**kwargs

			)
		self.window = None

	def do_activate(self):
		if not self.window:
			self.window = Mi_Ventana(application=self, title='ventana principal')
		self.window.show_all()
		self.window.present()

if __name__ == '__main__':
	app = CursoPythonApp()
	app.run()