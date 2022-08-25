'''
Isograms

An isogram is a word that has no repeating letters, consecutive or
non-consecutive. Implement a function that determines whether a string that
contains only letters is an isogram. Assume the empty string is an isogram.
Ignore letter case.

Example: (Input --> Output)

"Dermatoglyphics" --> true
"aba" --> false
"moOse" --> false (ignore letter case)
'''
def is_isogram(string):
    string = string.lower()
    contenedor = ''
    for letra in string:
        if letra not in contenedor:
            contenedor += letra
        else:
            return False
    return True

print(is_isogram('Constantinopla'))

# Paso a paso de la primer respuesta con SET()
# palabra = 'moOse'
# print(len(palabra))

# palabra2 = palabra.lower()
# palabra2 = set(palabra2)
# palabra2 = len(palabra2)
# print(palabra2)

# print(palabra == palabra2)

# primero = [5,6,4,3,34,5,536,243,3,2,5,6,7,4]
# segundo = [5,6,4,3,34,5,536,243,3,2,5,6,7,4,4,3,5,6]

# print(set(primero))
# print(set(segundo))
# print(set(primero) == set(segundo))
























# My answer
def is_isogram_1(string):
    input = string.lower()
    contents = {}
    # Al final el diccionario con 'moOse' quedaria asi:
    # contents = {'m': 1, 'o': 2, 's': 1, 'e': 1}

    for i in input:
        if i not in contents:
            contents[i] = 1
        else:
            contents[i] += 1

    for i in contents.values():
        if i > 1:
            return False
    
    return True

# Some answers submitted as example
def is_isogram_2(string):
    return len(string) == len(set(string.lower()))

def is_isogram_3(string):
    string = string.lower()
    for letter in string:
        if string.count(letter) > 1: return False
    return True

# print(is_isogram_1('Dermatoglyphics'))
# print(is_isogram_2('Dermatoglyphics'))
# print(is_isogram_3('Dermatoglyphics'))
