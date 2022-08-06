# f = open('archivo.txt', 'r')
# print(f.read())
# f.close()

# f = open('escritura.txt', 'w')
# f.write('Lorem Ipsum x10000')
# f.close()

# f = open('escritura.txt', 'a')
# f.write('\nMas lipsum')
# f.close()

# f = open('escritura.txt', 'r')
# print(f.read())
# f.close()

'''
r = Read
w = Write
a = Append
'''

with open('archivo.txt', 'w') as f:
    f.write('Lorem Ipsum\n')

with open('archivo.csv', 'w') as f:
    f.write('id,nombre,apellido\n')

with open('archivo.csv', 'a') as f:
    f.write('1,Fernando,Romero\n')

# import os

# archivo = 'share-vehicle-electric.csv'

# if os.path.exists(archivo):
#     try:
#         with open(archivo, 'r') as f:
#             print(f.read())
#     except Exception as e:
#         print(e)
# else:
#     print('el archivo no existe')
