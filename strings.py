myString = "hello, World"

#print(dir(myString))# el texto al imprimir son los diferentes metodos q podemos utilizar sobre los strings

print(myString.upper())
print(myString.lower())
print(myString.swapcase())
print(myString.capitalize())#la primera letra se transforma en mayuscula
print(myString.replace('hello','bye'))
print(myString.replace('hello','bye').upper())#reemplaza la palabra hello x bye y el resultado lo pone en mayusculas
print(myString.count('l'))#cuenta cuantas veces se repite la l
print(myString.startswith('hola'))
print(myString.startswith('hello'))# sirve para buscar caracteres true si coinciden al inicio
print(myString.endswith('World')) # sirve para buscar caracteres true si coinciden al final

print(myString.split())#separa por el espacio vacio
print(myString.split(','))#separa por la coma
print(myString.find(','))#busca la posicion de la coma
print(len(myString))#longitud del arreglo
print(myString.index('e'))# indice de la palabra e
print(myString.isalpha())
print(myString.isnumeric())
print(myString[4])
print(myString[-1])

name = "Cesar"

print("my name is: "+name)
print(f"my name is: {name}")
print("my name is: {0}".format(name))