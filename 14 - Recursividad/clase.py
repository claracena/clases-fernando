'''
Que es un factorial?

El factorial de un número entero positivo se define como el producto de
todos los números naturales anteriores o iguales a él

Se escribe como n!

Por ejemplo, el factorial de 6 se escribe 6! y es igual a:
1 * 2 * 3 * 4 * 5 * 6
'''

def mi_factorial(n):
    if n == 1:
        return 1
    else:
        return n * mi_factorial(n - 1)
    # 6 * mi_factorial(5)
    # 6 * 5 * mi_factorial(4)
    # 6 * 5 * 4 * mi_factorial(3)
    # 6 * 5 * 4 * 3 * mi_factorial(2)
    # 6 * 5 * 4 * 3 * 2 * mi_factorial(1)
    # 6 * 5 * 4 * 3 * 2 * 1 = 720

# print(mi_factorial(6))

####################################################################

'''
Secuencia Fibonacci

La sucesión de Fibonacci es una sucesión definida por recurrencia. Esto
significa que para calcular un término de la sucesión se necesitan los
términos que le preceden

Se trata de una secuencia infinita de números naturales; a partir del 0
y el 1, se van sumando a pares, de manera que cada número es igual a la
suma de sus dos anteriores, de manera que:

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55…
'''

def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

# n = 6
# for i in range(1, n + 1):
#     print(fib(i))

# fib(1) = 1 (por el if)
# fib(2) = 1 (por el if)
# fib(3) = 2 (porque es fib(n - 1) + fib(n - 2) y n - 1 = 2 y n - 2 = 1)

####################################################################

# lista = []

# def recur(n):
#     if n == 1:
#         return 1
#     else:
#         return n + recur(n - 1)

# n = 10
# for i in range(1, n + 1):
#     lista.append(recur(i))

# print(lista)

def generador(n):
    for i in range(1, n + 1):
        yield n + i

print(*generador(5))
