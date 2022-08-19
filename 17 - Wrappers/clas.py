import time
from functools import wraps

# Creamos un decorador para "envolver" cada funcion que querramos
# medir su tiempo de ejecucion
def temporizador(func):
    '''Este decorador es un simple timer'''
    @wraps(func)
    def wrapper(*args, **kwargs):
        '''El wrapper'''
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        print(f'La funcion tardo {end_time - start_time} segundos')
    return wrapper

# Creamos una funcion y la "decoramos" con nuestro decorador creado
# previamente
@temporizador
def mi_funcion(n):
    '''Esta funcion sirve como prueba para el temporizador que creamos
    como decorador. El decorador se llama @temporizador
    '''
    for i in range(n):
        time.sleep(0.1)

'''
Es lo mismo que decir:
mi_funcion = temporizador(mi_funcion)
'''

# Llamamos la funcion con el/los parametros que necesitemos
mi_funcion(1)

print(mi_funcion.__doc__)

# Vamos a ver que diferencia encontramos si usamos la funcion
# wraps que esta en functools

