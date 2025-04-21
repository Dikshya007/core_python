"""
Built-in Decorator:
2. @staticmethod

Normally in Python, if you want to call a method or function inside a class, you must create an object and call the method using that 
object. Otherwise, you can't directly call the method.
This limitation is resolved by using the @staticmethod decorator. If a method doesn't use any object-specific data
 (i.e., it doesn't access self), then it can be made static using this decorator.
Such methods can be called without creating an object, which makes them more memory-efficient.

Important: Static methods do not require the self parameter.
"""

class Employee:
    def __init__(self,name,age,salary,address):
        self.name = name
        self.age = age
        self._salary = salary
        self.address = address

    def curr_con_usd_npr(amt_in_npr):
        return amt_in_npr * 139

#static decorator called without object        
print(Employee.curr_con_usd_npr(1250))