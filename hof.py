#Higher order function
"""
A higher-order function is a powerful function. It is a function that takes another function as an argument or returns a function as a result.
Higher-order functions can be:
1)Python built-in higher-order functions
2)User-defined higher-order functions
"""
#1. Python builtin higher order function
#Map
#filter
#reduce

# Marks_Sci =[71,50,60,57,67,44]#all a
# Marks_Nep =[45,50,67,70,63,45]#all b
# Marks_Com =[56,67,55,71,47,49]#all c

# def avg1(a,b,c):
#     return (a+b+c)/3

# x = list(map(avg1,Marks_Sci,Marks_Nep,Marks_Com))
# print(x)

# Marks_Sci ={71,50,60,57,67,44}#all a
# Marks_Nep ={45,50,67,70,63,45}#all b
# Marks_Com ={56,67,55,71,47,49}#all c

# def avg1(a,b,c):
#     return (a+b+c)/3

# x = set(map(avg1,Marks_Sci,Marks_Nep,Marks_Com))
# print(x)

Marks_Sci =(71,50,60,57,67,44)#all a
Marks_Nep =(45,50,67,70,63,45)#all b
Marks_Com =(56,67,55,71,47,49)#all c

def avg1(a,b,c):
    return (a+b+c)/3

x = tuple(map(avg1,Marks_Sci,Marks_Nep,Marks_Com))
print(x)
y=list(map(lambda i, j, k:(i+j+k)/3,Marks_Sci,Marks_Nep,Marks_Com))
print(y)

g=[3,4,6,7]
w=[1,7,2,8]
import math
c= list(map(lambda a,b:math.sqrt(a**2+b**2),g,w))
print(c)