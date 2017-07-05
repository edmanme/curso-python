# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

#las vistas manejan la logica del sitio web,
 #importar clase base para vistas
from django.views.generic import View
from documentos.models import Documento

#crear vista de Documentos
#definir metodo get
class Documentos(View):
	def get(self, request, *args, **kwargs):

		docs = Documento.objects.all()
		#select * from documentos?_documento;

		context = {

		'docs':docs,
		'encabezado':'Mis Documentos'
		}


		return render(request,'documentos.html',context)
