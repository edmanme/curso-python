dato= ("esto es una prueba")
text = dato
conteo = 0
for letra in text:
	if letra == "e":
		conteo += 1
print("el ",dato," tiene ", conteo," letras e")
print(text.upper())
print("la longitud de la cadena es de ", len(dato))