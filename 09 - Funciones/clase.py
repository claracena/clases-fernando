# '''
# Las funciones sirven como base de OOP (Programacion Orientada a Objetos)
# y mas que nada ataca el problema de DRY (Don't Repeat Yourself).
# Es bueno tambien aplicar el KISS (Keep It Simple Stup**)
# '''

# def sumar(x, y):
#     '''Esta funcion sirve para sumar dos numeros de tipo float y regresa
#     el resultado'''
#     x = float(x)
#     y = float(y)
#     return x + y

# mi_suma = sumar(4, 5)
# print(mi_suma)

# help(sumar)

# -------------------------------------------------

# def hola_mundo(a: int) -> str:
#     '''Esto se llama TYPE HINTING'''
#     print(f'Hola Mundo {a}')

# hola_mundo('abc')

# -------------------------------------------------

# *ARGS Y **KWARGS

# def hola_mundo(a=5, b=2, c=0):
#     c = c
#     print(a / b)

# hola_mundo(5, 0, 2)
# hola_mundo(a=5, c=0, b=2)
# hola_mundo(10, 2)

# def function_args(primer_arg, *args):
#     print(f'Primer argumento: {primer_arg}')
#     for arg in args:
#         print(arg)

# function_args('Hola', 'Mundo', 3, 5, 7)

# kw = KeyWord
# def funcion_kwargs(**kwargs):
#     # print(dir(kwargs))
#     for clave, valor in kwargs.items():
#         print(f'Clave: {clave} - Valor: {valor}')

# funcion_kwargs(a=5, c=0, b=2)

# def mi_func(*args, **kwargs):
#     print(args[0], kwargs['nombre'])

# mi_func(1834, nombre='Fernando')
