#################
# Condicionales #
#################

# dia = 'nublado'
# estado = 'lloviendo'
# x = 5

# if dia != 'soleado':
#     print('llevar paraguas')
#     if estado != 'lloviendo':
#         print('llevar botas')
#         if x == 5:
#             print('y x es 5')

'''
si algo es verdadero -> si esto tambien es verdadero -> si esto tambien es verdadero ...
--------------------
si algo es verdadero
si algo es verdadero
si algo es verdadero
'''

# color = input('ingrese un color: ')

# if color == 'blanco':
#     print('el color es blanco')
# else:
#     print('el color NO es blanco')

# color = 'blanco'

# if color == 'blanco':
#     print('el color es blanco')
# elif color == 'negro':
#     print('el color NO es blanco. Es negro')
# elif color == 'azul':
#     print('el color NO es blanco. Es azul')
# elif color == 'gris':
#     print('el color NO es blanco. Es gris')
# elif color == 'amarillo':
#     print('el color NO es blanco. Es amarillo')
# else:
#     print('el color no es ninguno de los esperados')

'''
si algo es verdadero
o esto otro es verdadero
o esto otro es verdadero
y si ninguno es verdadero.....
'''

# Ejemplo practico

# edad = 12

# if edad >= 13:
#     print('bienvenido al sitio')
# else:
#     print('fuera de aca')

# Otro ejemplo practico

'''
10 = excelente alumno
8 - 9.9 = muy buen alumno
6 - 7.9 = buen alumno
4 - 5.9 = alumno regular
0 - 3.9 = exalumno
'''

nota = 7.3
alumno = ''

if nota == 10:
    alumno = 'excelente alumno'
elif nota >= 8:
    alumno = 'muy buen alumno'
elif nota >= 6:
    alumno = 'buen alumno'
elif nota >= 4:
    alumno = 'alumno regular'
else:
    alumno = 'exalumno'

print(alumno)
