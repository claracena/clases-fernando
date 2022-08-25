'''
Playing with digits

Some numbers have funny properties. For example:

89 --> 8¹ + 9² = 89 * 1

695 --> 6² + 9³ + 5⁴ = 1390 = 695 * 2

46288 --> 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51

Given a positive integer n written as abcd... (a, b, c, d... being digits) and
a positive integer p

we want to find a positive integer k, if it exists, such that the sum of the
digits of n taken to the successive powers of p is equal to k * n.
In other words:

Is there an integer k such as:
(a ^ p + b ^ (p+1) + c ^(p+2) + d ^ (p+3) + ...) = n * k

If it is the case we will return k, if not return -1.

Note: n and p will always be given as strictly positive integers.

dig_pow(89, 1) should return 1 since 8¹ + 9² = 89 = 89 * 1
dig_pow(92, 1) should return -1 since there is no k such as 9¹ + 2² equals 92 * k
dig_pow(695, 2) should return 2 since 6² + 9³ + 5⁴= 1390 = 695 * 2
dig_pow(46288, 3) should return 51 since 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51
'''






















# My answer
def dig_pow_1(n, p):
    my_n = str(n)
    temp = []
    output = -1

    for i in my_n:
        temp.append(int(i) ** p)
        p += 1
    
    if sum(temp) % n == 0:
        output = int(sum(temp) / n)
        return output
    else:
        return output

# Some answers submitted as example
def dig_pow_2(n, p):
    s = 0
    for i,c in enumerate(str(n)):
        s += pow(int(c),p+i)
    return s/n if s%n==0 else -1

def dig_pow_3(n, p):
    k, fail = divmod(sum(int(d)**(p + i) for i, d in enumerate(str(n))), n)
    return -1 if fail else k

print(dig_pow_1(46288, 3))
print(dig_pow_2(46288, 3))
print(dig_pow_3(46288, 3))
