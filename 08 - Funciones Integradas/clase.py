# x = 2.4
# print(type(x))
# y = int(x) # type casting
# print(type(y))

#################
# ZIP()
#################

# Nombres = ['Pepe', 'Maria', 'Miguel']
# Edades = [21, 25, 32, 43, 23, 22]

# unidos = zip(Nombres, Edades)

# print(list(unidos))

#################
# MAX()
#################

# x = [1, 2, 3, 4, 5, 6, 7, 8]

# print(max(x))

#################
# BIN()
#################

# binary = bin(19)

# print(binary)

#################
# DIR()
#################

# x = [1 ,2 ,3]

# print(dir(x))

#################
# ENUMERATE()
#################

# nombres = ['Maria', 'Jose', 'Miguel', 'Camila']
# puestos = {1: 'Junior', 2: 'Mid-level', 3: 'Senior'}

# for persona in nombres:
#     print(persona)

# for posicion, persona in enumerate(nombres):
#     print(posicion, persona)

# resultado = {}
# for numero, persona in enumerate(nombres, 1):
#     for puesto in puestos:
#         if numero == puesto:
#             resultado[persona] = puestos[puesto]
#             break

# print(resultado)



nums = [1, 2, 3, 4, 5, 6, 7, 8, 5]

result = []
good_list = [] # 1, 2, 3, 4, 5, 6, 7, 8, 9
lenght = range(len(nums)) # rango de 0 a 8

for i in lenght:
    good_list.append(i + 1) # agrega de 0+1 a 8+1

for i, n in enumerate(nums):
    if n != good_list[i]:
        result.append(n)
        result.append(good_list[i])

print(result)

#################
# LEN()
#################

# x = [4, 5, 3, 6, 4, 5]

# x.insert(len(x), 9)

# print(x)


