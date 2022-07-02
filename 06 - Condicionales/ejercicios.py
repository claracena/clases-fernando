'''
Descripcion:
Ejercicio para comprar/vender una criptomoneda imaginaria
de manera automatica.

Objetivo:
Crear una logica condicional que evalue el precio de la moneda
imaginaria de manera automatica y compre o venda, segun el precio y
nuestra logica

Variables obtenidas:
    precio: 0 <= precio <= 100
    precio_maximo_de_compra: 40
    precio_minimo_de_venta: 60
'''

# Libreria para generar numero aleatorios
from random import random

# Funcion para generar un precio automatico
# precio = random() * 100

# Definicion de los precios maximos y minimos de compra y venta
# Si es menor o igual al precio_maximo_de_compra, comprar.
# Si es mayor o igual al precio_minimo_de_venta, vender.
# Si esta entre los dos precios, mantener.
precio_maximo_de_compra = 40
precio_minimo_de_venta = 60

# Funcion para evaluar el precio
def evaluar_precio(precio):
    # Escribir aca la logica condicional
    if precio <= precio_maximo_de_compra:
        print('comprar')
    elif precio >= precio_minimo_de_venta:
        print('vender')
    else:
        print('mantener')

if __name__ == '__main__':
    # print(precio)
    evaluar_precio(40)
    evaluar_precio(50)
    evaluar_precio(60)
