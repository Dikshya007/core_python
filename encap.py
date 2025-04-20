"""
🔐 Encapsulation in Python
Encapsulation is the mechanism of restricting access to some of an object's components. 
It helps in protecting the internal state of an object and controlling how it’s accessed or modified.
Python does not enforce strict access control, but it provides naming conventions to indicate the intended level of access:

  1. Public Members
   Instance variable names that do not start with an underscore (_) are considered public.
   They can be accessed and modified from outside the class.

  2. Protected Members
   Instance variable names that start with a single underscore (_) are considered protected.
   These should not be accessed directly from outside the class, but can be accessed by the class itself and its subclasses (child classes).
   This is more of a convention than a strict rule.

  3. Private Members
   Instance variable names that start with two underscores (__) are considered private.
   These cannot be accessed directly from outside the class.
   Python performs name mangling to make them harder to access, typically renaming them internally to _ClassName__variableName
"""

class BankAccount:
    interest_rate = 0.7
    def __init__(self, Name, Balance, security):
        self.holder_name = Name #public member
        self._balance = Balance #protected member
        self.__security = security #Private member

    def deposit(self, amount):
        self._balance +=amount
        print(self.holder_name + ' deposited')
    #Backdoor technique
    def get_security(self):
        return self.__security


user1 = BankAccount(Balance=20000, Name='Gahana', security='dkl4684')
user1.deposit(3000)
user2 = BankAccount('Tapsu Wagle',27000, 'oihle484' )
user2.deposit(6000)
#public
print(user1.holder_name)
print(user2.holder_name)
print(user1._balance)
#print(user1.__security)
print(user1.get_security())
print(user2.get_security())
