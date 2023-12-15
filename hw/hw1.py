from functools import reduce

def product(x,y):
    return x*y

def sum(x,y):
    return x+y

def factorial(n):
    A = range(1,n+1)
    return reduce(product, A)

def mean(A):
    return reduce(sum, A)/len(A)
