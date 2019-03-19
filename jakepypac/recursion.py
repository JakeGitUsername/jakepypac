import numpy as np
def sum_array(array):

    '''Return sum of all items in array'''
    sum = 0
    for i in array:
        sum = sum + i
        return sum


def fibonacci(n):

    '''Return nth term in fibonacci sequence'''
   if n <= 1:
       return n
   else:
       return(fibonacci(n-1) + fibonacci(n-2))

def factorial(n):
    result = 1
    count = 2

    while count <= n:
        result = result * count
        count = count + 1

    return result

def reverse(word):

    '''Return word in reverse'''
    return word[::-1]
