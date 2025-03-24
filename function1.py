"""
Functions:
A function is a block of code that takes a number of inputs (arguments) and transforms them into an output.

Example:
f(x) = x + 1

Properties:
It can take 0 or more inputs (arguments/parameters in languages like Java, C).
It can return 0 or more values.
However, in languages like C or Java, a function can return only one value at a time during execution.
Syntax:
def <function_name>(arg1, arg2, ..., argn):
    # Description of the function
    # Logic (simple or complex)
    # Return output (optional

Note:
Insert 2 blank lines before and after the function definition to maintain proper formatting in Python.
"""


# def name():
#     #this is simple python function.
#     print('Hello')


# name()  #function call without argument

# for i in range(10):
#     name()



x=int(input('Enter the first number ='))
y=int(input('Enter the second number ='))

def arthimetic(a,b):
    adding = a + b
    sub1= a - b
    multi= a * b
    div1= a/b
    return adding,sub1,multi,div1

c=arthimetic(x,y)#function call
print(c)
h,i,j,k = arthimetic(x,y)
print('This is variable unpacking and store adding at=',h)
print('This is variable unpacking and store sub1 at=',i)
print('This is variable unpacking and store multi at=',j)
print('This is variable unpacking and store div1 at=',k)


"""
p=int(input("Enter the principal="))
t=int(input("Enter the time="))
r=int(input("Enter the interest rate="))

def SI(a,b,c):
    SI = (a*b*c)/100
    return SI

Simple_Interest=SI(p,t,r)
print (Simple_Interest)"
"""

