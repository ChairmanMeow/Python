'''
Created on Jan 7, 2013

@author: Victor
'''
#Q1
from operator import add, sub
def a_plus_abs_b(a, b):
    """Return a+abs(b), but without calling abs."""
    if b > 0:
        op = add
    else:
        op = sub
    return op(a, b)

print a_plus_abs_b(2, -4)
print a_plus_abs_b(1, 4)

#Q2
def two_of_three(a, b, c):
    """Return x**2 + y**2, where x and y are the two largest of a, b, c."""
    return a ** 2 + b ** 2 + c ** 2 - min(a ** 2, b ** 2, c ** 2)

#Q3
def if_function(condition, true_result, false_result):
    """Return true_result if condition is a true value, and false_result otherwise."""
    if condition:
        return true_result
    else:
        return false_result
    

def with_if_statement():
    if c():
        return t()
    else:
        return f()

def with_if_function():
    return if_function(c(), t(), f())

def c():
    return True
def t():
    return 1
def f():
    return 'penis' / 1

#print (with_if_statement())
#print (with_if_function())

#Q4
def hailstone(n):
    """Print the hailstone sequence starting at n, returning its length."""
    length=1
    while(n != 1):
        if n % 2:
            n = 3 * n + 1
        else:
            n = n / 2
        print n
        length+=1
    return length
print hailstone(125)

       
        
