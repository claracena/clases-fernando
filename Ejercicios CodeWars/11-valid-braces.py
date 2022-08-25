'''
Valid Braces

Write a function that takes a string of braces, and determines if the order of the braces is valid. It should return true if the string is valid, and false if it's invalid.

This Kata is similar to the Valid Parentheses Kata, but introduces new characters: brackets [], and curly braces {}. Thanks to @arnedag for the idea!

All input strings will be nonempty, and will only consist of parentheses, brackets and curly braces: ()[]{}.

What is considered Valid?
A string of braces is considered valid if all braces are matched with the correct brace.

Examples
"(){}[]"   =>  True
"([{}])"   =>  True
"(}"       =>  False
"[(])"     =>  False
"[({})](]" =>  False
'''























# My answer
def valid_braces_1(string):
    dict = {'(': ')', '[': ']', '{': '}'}
    stack = []

    if len(string) % 2 != 0:
        return False
    
    for element in string:
        if element in dict.keys():
            stack.append(element)
        else:
            if stack == []:
                return False
            remove = stack.pop()
            if element != dict[remove]:
                return False

    if stack == []:
        return True
    else:
        return False

# Some answers submitted as example
def valid_braces_2(string):
    braces = {"(": ")", "[": "]", "{": "}"}
    stack = []
    for character in string:
        if character in braces.keys():
            stack.append(character)
        else:
            if len(stack) == 0 or braces[stack.pop()] != character:
                return False
    return len(stack) == 0

def valid_braces_3(s):
  while '{}' in s or '()' in s or '[]' in s:
      s=s.replace('{}','')
      s=s.replace('[]','')
      s=s.replace('()','')
  return s==''

def valid_braces_4(s, previous = ''):
  while s != previous: previous, s = s, s.replace('[]','').replace('{}','').replace('()','')
  return not s

print(valid_braces_1('[({})](]'))
print(valid_braces_2('[({})](]'))
print(valid_braces_3('[({})](]'))
print(valid_braces_4('[({})](]'))
