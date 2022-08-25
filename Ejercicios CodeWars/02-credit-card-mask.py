'''
Credit Card Mask

Usually when you buy something, you're asked whether your credit card number,
phone number or answer to your most secret question is still correct. However,
since someone could look over your shoulder, you don't want that shown on your
screen. Instead, we mask it.

Your task is to write a function maskify, which changes all but the last four
characters into '#'.

Examples
"4556364607935616" --> "############5616"
     "64607935616" -->      "#######5616"
               "1" -->                "1"
                "" -->                 ""

// "What was the name of your first pet?"

"Skippy" --> "##ippy"

"Nananananananananananananananana Batman!"
-->
"####################################man!"
'''
















# My answer
def maskify_1(cc):
    output = ''
    counter = 0
    for i in range(len(cc)-1, -1, -1):
        if counter < 4:
            output += cc[i]
        else:
            output += '#'
        counter += 1
    return output[::-1]

# Some answers submitted as example
def maskify_2(cc):
    return "#"*(len(cc)-4) + cc[-4:]

def maskify_3(cc):
    l = len(cc)
    if l <= 4: return cc
    return (l - 4) * '#' + cc[-4:]

def maskify_4(cc):
    return '{message:#>{fill}}'.format(message=cc[-4:], fill=len(cc))
    
print(maskify_1('SF$SDfgsd2eA'))
print(maskify_2('SF$SDfgsd2eA'))
print(maskify_3('SF$SDfgsd2eA'))
print(maskify_4('SF$SDfgsd2eA'))
