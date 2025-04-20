"""
Built-in Decorator: @property
The @property decorator allows you to define methods in a class that behave like attributes.
It is commonly used to control access to instance variables while still using attribute-style access.
It helps to get, set, or delete an attribute in a controlled way, using three techniques:

🔹 Techniques:
    -Getter: Retrieves the value of an existing attribute.

    -Setter: Sets or updates the value of an existing attribute.

    -Deleter: Deletes an existing attribute
"""

class Employee:
    def __init__(self,first_name,last_name,age,salary,address):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.__salary = salary
        self.address = address

    #getter method
    @property
    def full_name(self):
        return self.first_name + ' '+self.last_name
    
    #setter method
    @full_name.setter
    def full_name(self,name):
        self.first_name, self.last_name = name.split(' ')


object5 = Employee('Ram','Sharma',25,50000,'Kathmandu')
print(object5.first_name)
print(object5.full_name)

#setter method output
object5.full_name = 'Shyam Sharma'
print(object5.first_name)
print(object5.last_name)
 
 #complex example
class BankAccount:
   def __init__(self, name, balance):
      self.holder_name =name
      self.__balance =balance

      @property
      def holder_name(self):
          return self.first_name + ' ' + self.last_name
      
      @holder_name.setter
      def holder_name(self,value):
          self.first_name, self.last_name = value.split()[0],value.split([1])

account1 = BankAccount('Dikhsya Mgara', 10000)
print(account1.holder_name)
