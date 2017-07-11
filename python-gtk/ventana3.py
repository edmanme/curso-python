import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MiVentana(Gtk.Window):
	def __init__(self, *args, **kwargs):
		super(MiVentana, self).__init__(*args, **kwargs)
		self.set_default_size(500,300)
		self.connect('delete-event', Gtk.main_quit)



  	def agregar_boton(self):
       		self.boton = Gtk.Button('Enviar')
if __name__ == '__main__':
	ventana = MiVentana()
	ventana.show_all()
	Gtk.main()
