#Reduce
"""
The reduce function reduces the use of iterative techniques by taking a large collection and merging its elements iteratively (one by one) into a single output according to a given logic.

It requires the functools library to work. You can import it like this:
from functools import reduce
Syntax:
variable = function, collection)
"""
#wap to calculate sum of list
from functools import reduce
list_num=[1,2,3,4,5]
print(reduce(lambda x,y:x+y,list_num))