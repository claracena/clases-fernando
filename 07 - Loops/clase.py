#########
# Loops #
#########

# Iterables
# lista = ['a', 'b', 'c', 'd', 'e']
# nombre = 'Fernando Romero'

# print(dir(nombre))

# FOR loops
#
# for n in lista:
#     if n == 'c':
#         print('encontre la letra c')
#         break
#     else:
#         print('esta no es la c')

# for letra in nombre:
#     print(letra)

# notas = [("Ashley", 93, 9.3), ("Brad", 95, 9.5), ("Cassie", 84, 8.4)]

# for alumno in notas:
#     print(alumno)

# for alumno in notas:
#     print(f'Alumno: {alumno[0]} - Nota: {alumno[1]}')

# for alumno in enumerate(notas):
#     print(alumno)

# for nombre, calificacion, otracali in notas:
#     if nombre == 'Brad':
#         continue
#     else:
#         print(f'Alumno: {nombre} - Nota: {calificacion} ({otracali}/10)')

# for i in range(1, 101):
#     print(i % 3)

######################################################
# ESTE FOR NO ESTA EN PYTHON
######################################################
'''
for (i=1; i<=100; i++) {
    .......
}
'''

# WHILE loops

# i = 1

# while i <= 100:

#     resultado = ''
#     if (i % 3 == 0): resultado += 'Fizz'
#     if (i % 5 == 0): resultado += 'Buzz'
#     if resultado == '': resultado = i
#     print(resultado)

#     i += 1

######################################################

# from random import random

# numero = int(random() * 100)

# print('numero = ', numero)

# while numero % 2 == 0:
#     print('numero en loop = ', numero)
#     numero = int(random() * 100)
#     print('nuevo numero = ', numero)

######################################################

# x = input('nombre: ')

# while x != 'Fer':
#     x = input('nombre: ')

######################################################

cartas = [[1,3,4,5,5,7,8,8,9,9], [2,2,3,4,4,5,6,6,6], [1,2,3,3]]

for lista in cartas:
    print(lista)
    for numero in lista:
        print(numero)

# numeros = cartas[1]
# for x in numeros:
#     print(x)
