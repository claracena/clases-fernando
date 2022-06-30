'''
Descripcion:
Ejercicio para comprar/vender una crptomoneda imaginaria
de manera automatica.

Objetivo:
Crear una logica condicional que evalue el precio de la moneda
imaginaria de manera automatica y compre o venda, segun el precio y
nuestra logica

Variables obtenidas:
precio: 1 <= precio <= 100
precio_maximo_de_compra: 40
precio_minimo_de_venta: 60
'''

# Libreria para generar numero aleatorios
from random import random

# Funcion para generar un precio automatico
precio = random() * 100

# Definicion de los precios maximos y minimos de compra y vente
# Si es menor al precio_maximo_de_compra, comprar.
# Si es mayor al precio_minimo_de_venta, vender.
# Si esta entre los dos precios, mantener.
precio_maximo_de_compra = 40
precio_minimo_de_venta = 60

# Funcion para evaluar el precio
def evaluar_precio():
    # Escribir aca la logica condicional
    

if __name__ == '__main__':
    print(precio)
    evaluar_precio()
