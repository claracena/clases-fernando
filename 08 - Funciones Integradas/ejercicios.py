'''
Escribir un programa que muestre el siguiente patron:
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
'''

n = 5
x = []
for i in range(1, n + 1):
    # if i != 0:
    for j in range(1,i+1):
        # print(j, end=" ")
        x.append(j)
    print(*x)
    x = []
    # print("")


'''
Imprimir la lista en orden inverso usando un loop. Se puede usar reversed()
y un for loop o un for loop y len()
lista = [10, 20, 30, 40, 50]
'''

# lista = [10, 20, 30, 40, 50] 

# for i in reversed(lista):
#   print(i)

# long = len(lista) - 1

# for i in range(long, -1, -1):
#     print(lista[i])

# a = ("John", "Charles", "Mike")
# b = (8, 7)

# x = zip(a, b, strict=True)

# #use the tuple() function to display a readable version of the result:

# print(tuple(x))
