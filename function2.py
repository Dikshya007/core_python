#Required argument
def sum1(x, y):
    add = x+y
    return add

c= sum1(1,2)
print(c)

#Default argument
def sum1(x=1, y=2):
    add = x+y
    return add

c= sum1()
print(c)

#some argument are default and some required
def sum1(x, y=2):
    add = x+y
    return add

c= sum1(1)
print(c)

#argument are defined at calling
def sum1(x, y):
    add = x+y
    return add

c= sum1(y=1,x=2)
print(c)


def listdisplay(*input1):
    list1= list(input1)
    tuple1=tuple(input1)
    set1=set(input1)
    return list1,tuple1,set1

c=listdisplay(1,2,3,4,5,7)
print(c)


def dict1(**input2):
    return input2

g=dict1(c1=1,c2=12,c3=23)
print(g)