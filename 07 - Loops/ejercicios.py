'''
FizzBuzz:

Imprimir una lista en órden de 1 a 100, pero reemplazar los múltiplos de 3
por la palabra Fizz y los múltiplos de 5 por la palabra Buzz. Si el número
es múltiplo de 3 y 5, reemplazarlo por la palabra FizzBuzz.
'''

def ejecutar():
    # Escribir el codigo abajo de este comentario, reemplazando pass
    # for i in range(1, 101):
    #     if (i%3 == 0):
    #         print('Fizz')
    #     if (i%5 == 0):
    #         print('Buzz')
    #     if (i%3 != 0) and (i%5 != 0):
    #         print(i)

    # for i in range(1, 101):
    #     if (i % 3 == 0) and (i % 5 != 0):
    #         print('Fizz')
    #     elif (i % 3 != 0) and (i % 5 == 0):
    #         print('Buzz')
    #     elif (i % 3 == 0) and (i % 5 == 0):
    #         print('FizzBuzz')
    #     elif (i % 3 != 0) and (i % 5 != 0):
    #         print(i)

    for i in range(1, 101):

        resultado = ''

        if (i % 3 == 0): resultado += 'Fizz'
        if (i % 5 == 0): resultado += 'Buzz'
        
        if resultado == '': resultado = i

        print(resultado) 

if __name__ == '__main__':
    ejecutar()
