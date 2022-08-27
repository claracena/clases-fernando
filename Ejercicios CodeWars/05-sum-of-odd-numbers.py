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

1 --> 1
2 --> 3 + 5 = 8
3 --> 7 + 9 + 11 = 27
4 --> 13 + 15 + 17 + 19 = 64
5 --> 21 + 23 + 25 + 27 + 29 = 125
6 --> 31 + 33 + 35 + 37 + 39 + 41 = 216
'''
def row_sum_odd_numbers(n):
    rango = range(1, (n*n) + n, 2) # 1, 3, 5... 29

    return sum(list(rango[-n:])) # Solo los ultimos n posiciones del rango

print(row_sum_odd_numbers(5))





















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
