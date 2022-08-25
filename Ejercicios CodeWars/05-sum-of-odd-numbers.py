'''
Sum of odd numbers

Given the triangle of consecutive odd numbers:

             1
          3     5
       7     9    11
   13    15    17    19
21    23    25    27    29
...
Calculate the sum of the numbers in the nth row of this triangle (starting at
index 1) e.g.: (Input --> Output)

1 -->  1
2 --> 3 + 5 = 8
'''























# My answer
def row_sum_odd_numbers_1(n):
    return sum(range(1, (n * n) + n, 2)[-n:])

# Some answers submitted as example
def row_sum_odd_numbers_2(n):
    return n ** 3

def row_sum_odd_numbers_3(n):
    return sum(range(n*(n-1)+1, n*(n+1), 2))

print(row_sum_odd_numbers_1(5))
print(row_sum_odd_numbers_2(5))
print(row_sum_odd_numbers_3(5))