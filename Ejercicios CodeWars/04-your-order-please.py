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


























# My answer
def order_1(sentence):
    items = sentence.split()
    ordering = {}
    result = {}
    returned = ''

    if len(items) == 0:
        return ''
    
    for i, n in enumerate(items):
        for letter in n:
            if letter.isdigit():
                ordering[i] = int(letter) - 1

    ordering = dict(sorted(ordering.items(), key=lambda item: item[1]))

    for i, n in ordering.items():
        result[n] = items[i]

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
    result = []    #the list that will eventually become our setence
      
    split_up = sentence.split() #the original sentence turned into a list
  
    for i in range(1,10):
        for item in split_up:
            if str(i) in item:
                 result.append(item)    #adds them in numerical order since it cycles through i first
  
    return " ".join(result)

# print(order_1('g3ood 4of the2 pe6ople th5e Fo1r'))
# print(order_2('g3ood 4of the2 pe6ople th5e Fo1r'))
# print(order_3('g3ood 4of the2 pe6ople th5e Fo1r'))
