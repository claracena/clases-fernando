'''
Your order, please

Your task is to sort a given string. Each word in the string will contain a
single number. This number is the position the word should have in the result.

Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

If the input string is empty, return an empty string. The words in the input
String will only contain valid consecutive numbers.

Examples
"is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
"4of Fo1r pe6ople g3ood th5e the2"  -->  "Fo1r the2 g3ood 4of th5e pe6ople"
""  -->  ""
'''
def order(sentence):
    if sentence == '':
        return sentence
        
    lista = sentence.split(' ')

    lista.sort(key=lambda x : sorted(x))

    return ' '.join(lista)

print(order("is2 Thi1s T4est 3a"))
























# My answer
def order_1(sentence):
    items = sentence.split()
    ordering = {} # {0: 1, 1: 0, 2: 3, 3: 2}
    result = {}
    returned = ''

    if len(items) == 0:
        return ''
    
    for i, n in enumerate(items):
        for letter in n:
            if letter.isdigit():
                ordering[i] = int(letter) - 1

    ordering = dict(sorted(ordering.items(), key=lambda item: item[1]))
    # {1: 0, 0: 1, 3: 2, 2: 3}

    for i, n in ordering.items():
        result[n] = items[i]
        # {0: 'Thi1s', 1: 'is2', 2: '3a', 3: 'T4est'}

    for n in result.values():
        if returned != '':
            returned += ' '
        returned += str(n)
    
    return returned

# Some answers submitted as example
def order_2(words):
  return ' '.join(sorted(words.split(), key=lambda w:sorted(w)))

def order_3(sentence):
    if not sentence:
        return ""
    result = [] #the list that will eventually become our setence
      
    split_up = sentence.split() #the original sentence turned into a list
  
    for i in range(1,10):
        for item in split_up:
            if str(i) in item:
                 result.append(item) #adds them in numerical order since it cycles through i first
  
    return " ".join(result)

print(order_1('is2 Thi1s T4est 3a'))
print(order_2('is2 Thi1s T4est 3a'))
print(order_3('is2 Thi1s T4est 3a'))
