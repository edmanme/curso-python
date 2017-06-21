# -*- encoding: utf-8

"""
1. Crear un script para
 - Recibir args ‘nombre’, ‘edad’, ‘clase’ y
   crear un diccionario de la forma:
       estudiante = {
           'nombre': <nombre>,
           'edad': <edad>,
           'curso': <curso>
       } 

 Imprimir diccionario ( print estudiante )
 Imprimir las llaves del diccionario y los valores

2. Crear un script para:
   Recibir un nombre y verificar si existe en el diccionario dado.
   'La llave <nombre> existe en el diccionario generado.' o
   'La llave <nombre> no existe en el diccionario'
"""
import argparse
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('nombre')
    parser.add_argument('edad')
    parser.add_argument('curso')

    args = parser.parse_args()
    datos={
        'nombre':args.nombre,
        'edad':args.edad,
        'curso':args.edad,
    }
    for llave,valor in datos.iteritems():
            print llave,valor