'''
Replace With Alphabet Position

Welcome.

In this kata you are required to, given a string, replace every letter with
its position in the alphabet.

If anything in the text isn't a letter, ignore it and don't return it.

"a" = 1, "b" = 2, etc.

Example
alphabet_position("The sunset sets at twelve o' clock.")
Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12
15 3 11" ( as a string )
'''























# My answer
import string

def alphabet_position_1(text):
    text = text.lower()
    alphabet = string.ascii_lowercase
    result = []

    for i in text:
        if i in alphabet:
            result.append(str(alphabet.index(i) + 1))
        

    return ' '.join(str(e) for e in result)

# Some answers submitted as example
def alphabet_position_2(text):
    return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def alphabet_position_3(text):
    if type(text) == str:
        text = text.lower()
        result = ''
        for letter in text:
            if letter.isalpha() == True:
                result = result + ' ' + str(alphabet.index(letter) + 1)
        return result.lstrip(' ')

print(alphabet_position_1('The sunset sets at twelve o\' clock.'))
print(alphabet_position_2('The sunset sets at twelve o\' clock.'))
print(alphabet_position_3('The sunset sets at twelve o\' clock.'))
