import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MiVentana(Gtk.Window):
	def __init__(self, *args, **kwargs):
		super(MiVentana, self).__init__(*args, **kwargs)
		self.set_default_size(500,300)
		self.connect('delete-event', Gtk.main_quit)
		self.agregar_contenedor()
		

	def agregar_contenedor(self):
		contenedor = Gtk.Grid()
		contenedor.set_column_homogeneous(True)
		contenedor.set_row_homogeneous(False)
		contenedor.attach(self.boton(), #elemento
		0, #columna
		0, #fila
		3, #numero de columna a usar
		1, #numero de filas a usar


		)
		contenedor = Gtk.VBox()
		contenedor.pack_start(boton, False, False, 0)

	

	def boton(self):
		self.boton = Gtk.Button('inicio')



	def text(self):
		entrada = Gtk.Entry()
		entrada.get_text()


	def label(self):
		etiqueta = Gtk.Label()
		etiqueta.set_markup('texto a ingresar')

if __name__ == '__main__':
	ventana = MiVentana()
	ventana.show_all()

	Gtk.main()
