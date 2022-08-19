'''
Trabajo con List Comprehension

List Comprehension es trabajar sobre o crear una lista usando distintas
operaciones como loops y condicionales directamente dentro de la lista en
una sola linea
'''

nombres = ['Alfredo', 'Martin', 'Roxanna', 'Julieta', 'Fernando']

# nombres_con_r = []
# for i in nombres:
#     if 'r' in i:
        # nombres_con_r.append(i)
# print(nombres_con_r)

nombres_con_r = [i for i in nombres if 'r' in i]
print(nombres_con_r)

'''
Ternary Operators

If/Else en una misma linea

en PHP seria:
<?php
(a > b ? a + b : a - b);
?>
'''

a, b = 10, 20

# Metodo tradicional
min = a if a < b else b
print(min)

# Evaluacion por tuplas
# En esta forma se evalua lo que esta entre corchetes y devuelve uno de los
# dos valores en los parentesis (valor si es falso, valor si es verdadero)
print((b, a) [a < b])

# Evaluacion con diccionario
print({True: a, False: b} [a < b])
