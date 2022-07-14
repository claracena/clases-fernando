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

def hola_mundo(a: int) -> str:
    '''Esto se llama TYPE HINTING'''
    print(f'Hola Mundo {a}')

hola_mundo('abc')
