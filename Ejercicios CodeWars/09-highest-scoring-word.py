'''
Highest Scoring Word

Given a string of words, you need to find the highest scoring word.

Each letter of a word scores points according to its position in the alphabet:
a = 1, b = 2, c = 3 etc.

You need to return the highest scoring word as a string.

If two words score the same, return the word that appears earliest in the
original string.

All letters will be lowercase and all inputs will be valid.
'''

























# My answer
import string

def high_1(x):
    alphabet = string.ascii_lowercase
    weights = {}
    phrase = x.split()

    for word in phrase:
        counter = 0
        for letter in word:
            counter += alphabet.index(letter) + 1
        weights[word] = counter

    ordered = dict(sorted(weights.items(), key=lambda x : x[1], reverse=True))

    return list(ordered.keys())[0]

# Some answers submitted as example
def high_2(x):
    return max(x.split(), key=lambda k: sum(ord(c) - 96 for c in k))

def high_3(x):
    words=x.split(' ')
    list = []
    for i in words:
        scores = [sum([ord(char) - 96 for char in i])]
        list.append(scores)
    return words[list.index(max(list))]

# print(high_1('what time are we climbing up the volcano'))
# print(high_2('what time are we climbing up the volcano'))
# print(high_3('what time are we climbing up the volcano'))
