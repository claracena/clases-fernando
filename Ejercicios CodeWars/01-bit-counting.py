'''
Bit Counting

Write a function that takes an integer as input, and returns the number of
bits that are equal to one in the binary representation of that number. You
can guarantee that input is non-negative.

Example: The binary representation of 1234 is 10011010010, so the function
should return 5 in this case
'''
def bit_counting(input):
    binary = bin(input) # 0b10011010010
    result = binary.count('1')
    return result

print(bit_counting(1234))


























# My answer
def count_bits_1(n):
    bins = bin(n).replace('0b', '')
    output = 0
    
    for i in bins:
        output += int(i)

    return output

# Best answer submitted as example
def count_bits_2(n):
    return bin(n).count("1")

# print(count_bits_1(1234))
# print(count_bits_2(1234))

