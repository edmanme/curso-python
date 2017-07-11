import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MiVentana(Gtk.Window):
	def __init__(self, *args, **kwargs):
		super(MiVentana, self).__init__(*args, **kwargs)
		self.set_default_size(500,300)
		self.connect('delete-event', Gtk.main_quit)
		self.agregar_contenedor()
  		self.agregar_entrada()
    		self.agregar_boton()



	def agregar_contenedor(self):
		self.contenedor = Gtk.Grid()
		self.contenedor.set_column_homogeneous(True)
		self.add(self.contenedor)



	def agregar_boton(self):
		self.boton = Gtk.Button('inicio')
  		self.contenedor.attach_next_to(
  		self.boton,
    		self.entrada,
      		Gtk.PositionType.BOTTOM,
        	1,
         	1

  		)



	def agregar_entrada(self):
		self.entrada = Gtk.Entry()
		self.contenedor.attach(self.entrada,0,0,1,1)


	def label(self):
		etiqueta = Gtk.Label()
		etiqueta.set_markup('texto a ingresar')


if __name__ == '__main__':
	ventana = MiVentana()
	ventana.show_all()

	Gtk.main()
