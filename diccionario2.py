import random

NOMBRES = [
    'Ana',
    'Pedro',
    'Pablo',
    'Ernesto',
    'Ariel',
    'Carlos',
    'Luis',
    'Oscar',
    'Alicia',
    'Maria',
    'Alexandra'
]

CIUDADES = [
    'Managua',
    'Masaya',
    'Matagalpa',
    'Chinandega',
    'Somoto',
    'Rivas'
]


def generar_diccionario_estudiantes():
    estudiantes = {}

    for nombre in NOMBRES:
        estudiantes[nombre] = {
            'edad': random.randrange(16, 30),
            'anio': random.randrange(1, 5),
            'ciudad': random.choice(CIUDADES)
        }

    return estudiantes

if __name__ == '__main__':
    diccionario = generar_diccionario_estudiantes()
    for llave, valor in diccionario.iteritems():
        print llave, valor

mensaje = 'el estudiante llamado {nombre} con la edad de: {edad}, y que habita en la ciudad de {ciudad} y cursa el ano {anio}'

for nombre_estudiantes, datos in diccionario.iteritems():
    print mensaje.format(nombre=nombre_estudiantes, edad=datos['edad'],ciudad=datos['ciudad'], anio = datos['anio'])
    f = open('archivo.txt', 'a')
    f.write(mensaje.format(nombre=nombre_estudiantes, edad=datos['edad'], ciudad=datos['ciudad'], anio=datos['anio']))
    f.close()
mensaje = 'el estudiante {nombre} habita en la ciudad de {ciudad}'
for nombre_estudiantes, datos in diccionario.iteritems():
    if datos['ciudad'] == 'Managua':
        print mensaje.format(nombre=nombre_estudiantes,ciudad=datos['ciudad'])
        f = open('text.txt', 'a')
        f.write(mensaje.format(nombre=nombre_estudiantes, edad=datos['edad'],ciudad=datos['ciudad'], anio = datos['anio']))
        f.close()


