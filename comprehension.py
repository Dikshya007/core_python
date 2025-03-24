"""
Why Use Comprehension?
Programming can consume memory in two ways: either at compile time or runtime.
Compile Time: If a program is executed, it is compiled by the compiler before runtime. During compilation, the program allocates memory
addresses for variables and other structures, and the memory is consumed at that point.

For example:num=[1,4,5,7,8,12,56,76,89,90,95]
            print(num)
Here, the list num is created at compile time, and memory is allocated at the same time.
Runtime: In programming, some blocks of code are compiled by the compiler at runtime, after the whole program is compiled. This means that memory is allocated or released dynamically during execution.
Comprehensions are often referred to as "lazy evaluators." They are compiled at the time of the full compilation, but they consume memory at runtime when the code is executed
"""


#WAP to replace even number with 'even' and odd number with 'odd'
#Hint: list_name=[2,3,6,8,14,17,20,7,9,4]
"""
list_name=[2,3,6,8,14,17,20,7,9,4]
h = ['even' if list_data %2 == 0 else 'odd' for list_data in list_name]
print(h)
print(type(h))

tuple_name=(2,3,6,8,14,17,20,7,9,4)
s = ['even' if tuple_data %2 == 0 else 'odd' for tuple_data in tuple_name]
print(s)
print(type(s))

set_name={2,3,6,8,14,17,20,7,9,4}
j = ['even' if set_data %2 == 0 else 'odd' for set_data in set_name]
print(j)
print(type(j))
"""

#WAP to find if 1 comes in list then yes/ if 2 comes in list then no/otherwise idle.
list_name=[1,0,3,2,5,7,1]
y =['yes' if data3 == 1 else 'No' if data3 == 2 else 'idle' for data3 in list_name]
print(y)

tuple_name=(1,0,3,2,5,7,1)
n =['yes' if data4 == 1 else 'No' if data4 == 2 else 'idle' for data4 in tuple_name]
print(n)

set_name={1,0,3,2,5,7,1}
o =['yes' if data5 == 1 else 'No' if data5 == 2 else 'idle' for data5 in set_name]
print(o)

def ch_even_odd(num):
    #this solution by function.
    if (num % 2 == 0):
        return 'even'
    else:
        return 'odd'
    
p = [ch_even_odd(num) for num in list_name]
print(p)

#WAP to find if 1 comes in list then yes/ if 2 comes in list then no/otherwise idle.
def ch_idle(n1):
    if(n1 == 1):
        return 'yes'
    elif(n1 ==2):
        return 'no'
    else:
        return 'idle'

d = [ch_idle(n1) for n1 in list_name]
print(d)

#WAP to find if 1 comes in list then yes/ if 2 comes in list then no/otherwise idle.
def ch_idle(n1):
    if(n1 == 1):
        return 'yes'
    elif(n1 ==2):
        return 'no'
    else:
        return 'idle'

d = [ch_idle(n1) for n1 in list_name]
print(d)

#WAP to find if 1 comes in list then yes/ if 2 comes in list then no/otherwise idle.
def ch_tup(n2):
    if(n2 == 1):
        return 'yes'
    elif(n2 ==2):
        return 'no'
    else:
        return 'idle'

g = [ch_tup(n1) for n1 in tuple_name]
print(g)

#WAP to find if 1 comes in list then yes/ if 2 comes in list then no/otherwise idle.
def ch_set(n3):
    if(n3 == 1):
        return 'yes'
    elif(n3 ==2):
        return 'no'
    else:
        return 'idle'

t = [ch_set(n3) for n3 in set_name]
print(t)



