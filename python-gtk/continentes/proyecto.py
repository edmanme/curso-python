
import random
import gi
import logging


# importar modulo que contiene clase base de actividad.
from sugar3.activity import activity

from sugar3.graphics.toolbarbox import ToolbarBox

# boton para toolbar
from sugar3.activity.widgets import (

    ActivityToolbarButton,
    StopButton
)

        


#from ppt_utils import OPCIONES

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GdkPixbuf
#gi.require_version('Gtk', '3.0')
#from gi.repository import Gtk
logger = logging.getLogger(__name__)

#ventanas

class continentes(activity.Activity):


	def __init__(self, handle):
		activity.Activity.__init__(self, handle)
		self.primer = 1
		self.mensaje = 'Continentes'
		self.agregar_toolbar()
		self.agregar_canvas()
  		self.agregar_boton()
  		#self.boton_europa()
  		self.agregar_lista()

  	def agregar_toolbar(self):
  		toolbar_box = ToolbarBox()
  		aplicacion_toolbar_boton = ActivityToolbarButton(self)
  		activity_stop_button = StopButton(self)

        # Insertar boton al toolbar en la posicion 0
        toolbar_box.toolbar.insert(aplicacion_toolbar_boton, 0)
        # Mostrar boton
        aplicacion_toolbar_boton.show()

        # Insertar boton cerrar al toolbar en la posicion -1
        toolbar_box.toolbar.insert(aplicacion_stop_boton, -1)
        # Mostrar boton
        aplicacion_stop_boton.show()

        # Asignar/establecer el toolbar box para esta actividad
        self.set_toolbar_box(toolbar_box)
toolbar_box.show()

	def agregar_canvas(self):
		self.canvas = Gtk.Grid()
		
		scrolled_window = Gtk.ScrolledWindow()
		scrolled_window.add(self.contenedor)
  		self.add(scrolled_window)

		#self.set_canvas(self.contenedor)
		#self.agregar_boton
	def agregar_boton(self):
		self.boton = Gtk.Button('America')
  		self.canvas.attach(self.boton,0,0,2,1)
		self.boton.connect('clicked',self.lista_paises_america)
		self.boton.set_name('botones')

		self.boton2 = Gtk.Button('Europa')
  		self.canvas.attach_next_to(self.boton2,
		self.boton,
		Gtk.PositionType.RIGHT,
		2,
		1,)
		self.boton2.connect('clicked',self.lista_paises_europa)
		self.boton2.set_name('botones')

		self.boton3 = Gtk.Button('Africa')
  		self.canvas.attach_next_to(self.boton3,
		self.boton2,
		Gtk.PositionType.RIGHT,
		2,
		1,)
		self.boton3.connect('clicked',self.lista_paises_africa)
		self.boton3.set_name('botones')

		self.boton4 = Gtk.Button('Asia')
  		self.canvas.attach(self.boton4,0,1,3,1)
		self.boton4.connect('clicked',self.lista_paises_asia)
		self.boton4.set_name('botones')

		self.boton5 = Gtk.Button('Oceania')
  		self.canvas.attach(self.boton5,3,1,3,1)
		self.boton5.connect('clicked',self.lista_paises_oceania)
		self.boton5.set_name('botones')
  	
  	def agregar_lista(self):
		self.modelo = Gtk.ListStore(str)
		self.lista_pais = Gtk.TreeView(self.modelo)

  		pais_cellrenderer = Gtk.CellRendererText()
		columna_paises =  Gtk.TreeViewColumn(
		'paises',
		pais_cellrenderer,
		text=0)


		self.lista_pais.append_column(columna_paises)
		self.canvas.attach_next_to(self.lista_pais, self.boton4, Gtk.PositionType.BOTTOM, 6,6)
	def lista_paises_america(self,btn):
		
		self.modelo.clear()	
		
		self.modelo.append(['Antigua y barbuda'])
		self.modelo.append(['Argentina'])
		self.modelo.append(['Bahamas'])
		self.modelo.append(['Barbados'])
		self.modelo.append(['Belice'])
		self.modelo.append(['Bolivia'])
		self.modelo.append(['Brasil'])
		self.modelo.append(['Canada'])
		self.modelo.append(['Chile'])
		self.modelo.append(['Colombia'])
		self.modelo.append(['Costa Rica'])
		self.modelo.append(['Cuba'])
		self.modelo.append(['Dominica'])
		self.modelo.append(['Ecuador'])
		self.modelo.append(['El Salvador'])
		self.modelo.append(['Estados Unidos'])
		self.modelo.append(['Granada'])
		self.modelo.append(['Guatemala'])
		self.modelo.append(['Guyana'])
	def lista_paises_africa(self,btn3):
		self.modelo.clear()	
	def lista_paises_asia(self,btn4):
		self.modelo.clear()	

	def lista_paises_oceania(self,btn5):
		self.modelo.clear()	


	def lista_paises_europa(self,btn2):
		
		self.modelo.clear()	
		self.modelo.append(['Albania'])
		self.modelo.append(['Alemania'])
		self.modelo.append(['Andorra'])
		self.modelo.append(['Armenia'])
		self.modelo.append(['Austria'])
		self.modelo.append(['Azerbaiyan'])
		self.modelo.append(['Belgica'])
		self.modelo.append(['Bielorrusia'])
		self.modelo.append(['Bosnia y Herzegovina'])
		self.modelo.append(['Bulgaria'])
		self.modelo.append(['Chipre'])
		self.modelo.append(['Ciudad del Vaticano'])
		self.modelo.append(['Croacia'])
		self.modelo.append(['Dinamarca'])
		self.modelo.append(['Eslovaquia'])
			

	def agregar_estilo(self):
        return
        css_provider = Gtk.CssProvider()
        css_provider.load_from_path('estilo.css')

        # TODO: Investigar GDK.Screen
        Gtk.StyleContext.add_provider_for_screen(
            Gdk.Screen.get_default(),
            css_provider,
			Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION


