nombre = []

nombre.append(str(input("Ingrese su primer nombre: ")).lower())
nombre.append(str(input("Ingrese su segundo nombre: ")).lower())



abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
 'x', 'y', 'z']

cantidad_letras = len(abc)

#Se crea un diccionario para tener varios contadores.
contador_letra = {}

#Se inicializan los contadores para cada letra.
for x in range(0, cantidad_letras):
	contador_letra["contador{0}".format(x)] = 0


#Se recorre el nombre de la lista.
#Se recorre cada letra de la lista con el abecedario.
#contador0 equivale a la 'a', contador1 a la 'b', y así sucesivamente.


for name in nombre:
	for letra in abc:
		if letra == 'a' and name[0] == letra:
			contador_letra['contador0'] += 1
		elif letra == 'b' and name[0] == letra:
			contador_letra['contador1'] += 1
		elif letra == 'c' and name[0] == letra:
			contador_letra['contador2'] += 1
		elif letra == 'd' and name[0] == letra:
			contador_letra['contador3'] += 1
		elif letra == 'e' and name[0] == letra:
			contador_letra['contador4'] += 1
		elif letra == 'f' and name[0] == letra:
			contador_letra['contador5'] += 1
		elif letra == 'g' and name[0] == letra:
			contador_letra['contador6'] += 1
		elif letra == 'h' and name[0] == letra:
			contador_letra['contador7'] += 1
		elif letra == 'i' and name[0] == letra:
			contador_letra['contador8'] += 1
		elif letra == 'j' and name[0] == letra:
			contador_letra['contador9'] += 1
		elif letra == 'k' and name[0] == letra:
			contador_letra['contador10'] += 1
		elif letra == 'l' and name[0] == letra:
			contador_letra['contador11'] += 1
		elif letra == 'm' and name[0] == letra:
			contador_letra['contador12'] += 1
		elif letra == 'n' and name[0] == letra:
			contador_letra['contador13'] += 1
		elif letra == 'ñ' and name[0] == letra:
			contador_letra['contador14'] += 1
		elif letra == 'o' and name[0] == letra:
			contador_letra['contador15'] += 1
		elif letra == 'p' and name[0] == letra:
			contador_letra['contador16'] += 1
		elif letra == 'q' and name[0] == letra:
			contador_letra['contador17'] += 1
		elif letra == 'r' and name[0] == letra:
			contador_letra['contador18'] += 1
		elif letra == 's' and name[0] == letra:
			contador_letra['contador19'] += 1
		elif letra == 't' and name[0] == letra:
			contador_letra['contador20'] += 1
		elif letra == 'u' and name[0] == letra:
			contador_letra['contador21'] += 1
		elif letra == 'v' and name[0] == letra:
			contador_letra['contador22'] += 1
		elif letra == 'w' and name[0] == letra:
			contador_letra['contador23'] += 1
		elif letra == 'x' and name[0] == letra:
			contador_letra['contador24'] += 1
		elif letra == 'y' and name[0] == letra:
			contador_letra['contador25'] += 1
		elif letra == 'z' and name[0] == letra:
			contador_letra['contador26'] += 1



for key in contador_letra:
	print('Letra:', abc[int(key.strip('contador'))].upper(), 'salió', contador_letra[key], 'veces.')
