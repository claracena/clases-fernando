'''
Isograms

An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

Example: (Input --> Output)

"Dermatoglyphics" --> true
"aba" --> false
"moOse" --> false (ignore letter case)
'''





























# My answer
def is_isogram_1(string):
    input = string.lower()
    contents = {}

    for i in input:
        if i not in contents:
            contents[i] = 1
        else:
            contents[i] += 1

    for i in contents.values():
        if i > 1:
            return False
            break
    
    return True

# Some answers submitted as example
def is_isogram_2(string):
    return len(string) == len(set(string.lower()))

def is_isogram_3(string):
    string = string.lower()
    for letter in string:
        if string.count(letter) > 1: return False
    return True

print(is_isogram_1('Dermatoglyphics'))
print(is_isogram_2('Dermatoglyphics'))
print(is_isogram_3('Dermatoglyphics'))
