#Filter
"""
Syntax: collection_casting(filter(function(boolean), collection(single)))
The function used in filter() must return a boolean value, either True or False. If it doesn't, the code will be incorrect.
Only a single collection (like a list or tuple) can be passed to the filter() function.
filter() is used with lists and tuples because they support indexing, allowing us to iterate and apply the filtering logic
"""
#Wap to show only even number.

#num is default input argument
#num2 is optional input argument

def is_even(num1, num2=0):
    if num1 % 2 == 0:
        return True
    else:
        return False
    
list1 = [2,3,6,7,12,13]
output1 = list(filter(is_even, list1))
print(output1)


def is_odd(num1, num2=0):
    if num1 % 2 != 0:
        return True
    else:
        return False
    
list2 = [2,3,6,7,12,13,15]
output2 = list(filter(is_odd, list2))
print(output2)

z=list(filter(lambda num1: num1 % 2 == 0,list2))
print(z)

Marks_Sci =(71,50,60,57,67,44)#all a
Marks_Nep =(45,50,67,70,63,45)#all b
Marks_Com =(56,67,55,71,47,49)#all c

per = list(map(lambda x,y,z: (x+y+z)/3, Marks_Sci,Marks_Nep,Marks_Com))
print(per)

pass_result = list(filter(lambda ob_per: ob_per>=60,per))
print(pass_result)
inone = list(filter(lambda ob_per:ob_per>=60, list(map(lambda x,y,z:(x+y+z)/3,Marks_Sci,Marks_Nep,Marks_Com))))
print(inone)

