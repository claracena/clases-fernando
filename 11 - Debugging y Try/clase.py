# a = 5
# b = 2
# c = a * b
# d = a + b / c

# print(f'el resultado de d es {d}')

# def solution(word):
#     # Turn word into a list of letters
#     list_of_letters = list(word)
    
#     # iterate through the list turning it into "braille"
#     braille = ""
#     for i in list_of_letters:
#         # Handle uppercase
#         if i.isupper():
#             braille += "000001"
#             # Remove uppercase once handled
#             i = i.lower()
#         braille += get_braille(i)
#     # Output the braille
#     print(braille)
    
    
    
# def get_braille(letter):
#     # Dictionary to store the braille value of each letter
#     braille_dict = {
#         " ": "000000",
#         "a": "100000",
#         "b": "110000",
#         "c": "100100",
#         "d": "100110",
#         "e": "100010",
#         "f": "110100",
#         "g": "110110",
#         "h": "110010",
#         "i": "010100",
#         "j": "010110",
#         "k": "101000",
#         "l": "111000",
#         "m": "101100",
#         "n": "101110",
#         "o": "101010",
#         "p": "111100",
#         "q": "111110",
#         "r": "111010",
#         "s": "011100",
#         "t": "011110",
#         "u": "101001",
#         "v": "111001",
#         "w": "010111",
#         "x": "101101",
#         "y": "101111",
#         "z": "101011"
#     }
#     # return the braille matching the letter
#     return braille_dict[letter]

# solution('The quick brown fox jumps over the lazy dog')

# a = 5
# b = 0

# try:
#     x = a / b
#     print(x)
# except Exception as e:
#     print(type(e),__name__)

try: # Intentamos abrir el archivo
    f = open('archivo.txt', 'r')
    # print(f.read())
    # f.close()
except FileNotFoundError: # Capturamos el excepcion/error si el archivo no existe
    print('No se encontro el archivo')
except IsADirectoryError: # Capturamos el excepcion/error si estamos intentando abriendo un directorio y no un archivo
    print('Usted esta tratando de abrir un directorio')
except Exception as e: # Capturamos cualquier excepcion/error que no hayamos previsto
    print(type(e).__name__)
else: # Hacemos lo que vayamos a hacer con el archivo solo en caso de que lo podamos abrir en el try
    print(f.read())
finally: # Cerramos el archivo si o si... sin importar si hubo alguna excepcion/error
    f.close()
