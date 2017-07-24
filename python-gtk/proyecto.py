
import random
import gi
#import logging


# importar modulo que contiene clase base de actividad.
#from sugar3.activity import activity

#from sugar3.graphics.toolbarbox import ToolbarBox

# boton para toolbar
#from sugar3.activity.widgets import (

    #ActivityToolbarButton,
    #StopButton
#)

#from ppt_utils import OPCIONES

#gi.require_version('Gtk', '3.0')
#from gi.repository import Gtk, Gdk, GdkPixbuf
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
#logger = logging.getLogger(__name__)

#ventanas

class continentes(Gtk.Window):


	def __init__(self, *args, **kwargs):
		super(continentes, self).__init__(*args, **kwargs)
		self.set_default_size(500,300)
  		self.agregar_contenedor()
    		self.agregar_boton()
      		self.agregar_lista()



	def agregar_contenedor(self):
		self.contenedor = Gtk.Grid()
		self.contenedor.set_column_homogeneous(True)
  		self.add(self.contenedor)
		#self.set_canvas(self.contenedor)
		#self.agregar_boton
	def agregar_boton(self):
		self.boton = Gtk.Button('America')
  		self.contenedor.attach(self.boton,3,3,1,1)
		self.boton.connect('clicked',self.lista_paises)
  		#self.boton2 = Gtk.Button('Europa')
  		#self.boton3 = Gtk.Button('Asia')
  	def agregar_lista(self):
		self.modelo = Gtk.ListStore(str)
		self.lista_pais = Gtk.TreeView(self.modelo)

  		pais_cellrenderer = Gtk.CellRendererText()
		columna_paises =  Gtk.TreeViewColumn(
		'paises',
		pais_cellrenderer,
		text=0)


		self.lista_pais.append_column(columna_paises)
  		self.contenedor.attach_next_to(self.lista_pais, self.boton, Gtk.PositionType.BOTTOM, 1,1)


  	def lista_paises(self,btn=None):
       		if len(self.modelo) == 0:
       			self.modelo.append(['nicaragua'])
         		self.modelo.append(['costa rica'])
if __name__ == '__main__':
	ventana = continentes()
	ventana.show_all()

	Gtk.main()
