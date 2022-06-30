# Type listing
def mi_funcion(a: int = 3, b: int = 5) -> int:
    return a + b

x = mi_funcion('a', '3')
# print(x)

###################################################

x = range(1, 100)
y = 32

# print(f'x: {type(x)}')
# print(f'y: {type(y)}')

# print(*x) # unpacking

###################################################

# Dictionary (Arrays):
# Elementos que se conforman de pares key:value (clave:valor)
x = {'nombre': 'Fernando', 'apellido': 'Romero'}
y = [{'nombre': 'Fernando', 'apellido': 'Romero'}, {'nombre': 'Cesar', 'apellido': 'Aracena'}]

# print(x)
# print(x['nombre'])

# print(y[0]['apellido'])

# from pprint import pprint

z = [
        {'nombre': 'Fernando', 'apellido': 'Romero', 'hermanos': ['Ana', 'Maxi']},
        {'nombre': 'Cesar', 'apellido': 'Aracena', 'hermanos':
            [
                'Adrian',
                'Sandra',
                {'Lis': ['xxxxx', 'yyyyyy']}
            ]
        }
    ]

# print(z[1]['hermanos'][2]['Lis'][0])

######################################

# Metodos de tipos de datos
# a = '     fernando romero            '

# print(a.strip())

# letra = 0
# cant = 0
# for i in a:
#     x = a.count(i)
#     if x > cant:
#         letra = i
#         cant = x

# print(letra, cant)

# x = 3
# print(type(x))
# x = float(x)
# print(type(x))
# print(x)

# x = 3.9999999
# x = int(x)
# print(x)

# Singleton
# a = 10
# b = 10

# x = None
# y = None

# if x == None
# if x is not None

# print(id(x))
# print(id(y))

# 1 = True / Verdadero
# 0 = False / Falso

x = 5
y = 4

print(x==y)
