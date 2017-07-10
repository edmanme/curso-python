import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

def imprimir_algo(boton):
	print boton

	print 'hola mundo'

def imprimir_alg(boton2):
	print boton2

	print 'adios mundo'

if __name__ == '__main__':
	ventana = Gtk.Window(title='Ventana 1')
	ventana.connect('delete-event', Gtk.main_quit)
	boton = Gtk.Button('boton 1')
	boton.connect('clicked', imprimir_algo)
	boton2 = Gtk.Button('boton 2')
	boton3 = Gtk.Button('boton 3')

	boton4 = Gtk.Button('boton 4')

	boton2.connect('clicked', imprimir_alg)
	contenedor = Gtk.Grid()
	contenedor.set_column_homogeneous(True)
	contenedor.set_row_homogeneous(False)

	contenedor.attach(
		boton, #elemento
		0, #columna
		0, #fila
		3, #numero de columna a usar
		1, #numero de filas a usar


		)

	contenedor.attach(boton2,1,1,1,1)
	contenedor.attach(boton3,2,1,1,1)
	contenedor.attach(boton4,0,2,1,1)
	ventana.add(contenedor)

	contenedor = Gtk.VBox()

	contenedor.pack_start(boton, False, False, 0)
	contenedor.pack_end(boton2, False, False, 0)

	


	ventana.show_all()

	Gtk.main()