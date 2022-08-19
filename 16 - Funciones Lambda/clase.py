'''
Funcion Lambda: Funciones anonimas (sin nombre) para realizar acciones
rapidas. En vez de definirlas con "def" como una funcion normal, las
definimos con la palabra clave "lambda"
'''

# como hacemos normalmente una funcion para calcular el cubo de un numero
def cubo_func(a):
    return a * a * a
print(cubo_func(3))

# como hariamos la misma funcion usando lambda
cubo = lambda a: a * a * a
print(cubo(3))

# Lambda dentro de otra funcion
def mi_func(n):
    return lambda a : a * n

duplicador = mi_func(2)
triplicador = mi_func(3)

print(duplicador(30))
print(triplicador(30))

lista = [(lambda i : i * i)(i) for i in range(10)]
print(lista)
