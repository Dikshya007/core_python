"""
Inheritance is a technique for making reusable common code and removing redundancy in code. 
It allows a class to inherit features (methods and properties) from another class, promoting code reuse.
In inheritance, we have the following relationships:
Parent → Child
Base → Derived
Superclass → Subclass
"""
"""
This means that all attributes and functions are static, and they don't require objects to be created in the parent or child class for access.
"""

print('-----Case_1 start-----')
"""

class Employer: #parent class
    name = 'Sulav Thapa'
    age = 21
    pan_no = 784455

class Engineer(Employer): #child class
    salary = 7000
    expertises = "Civil construction"

object1 = Engineer()
print(object1.name)

class Accountant(Engineer):
    work = 'Fincancing'

object3 = Accountant()
print(object3.name)

"""



"""
data1 = int(input('Enter the data='))
class Employeer:
    def __init__(self):
        self.first_class = data1

object1 = Employeer()
num = object1.first_class

class Engineer(Employeer):
    if num % 2 == 0:
        d1 = num
        print('This number is even {}'.format(d1))
    else:
        d1 = num
        print('This number is odd {}'.format(d1))

class Accountant(Engineer):
    work = "calculate"

object7 = Accountant()
print(object7.d1)
"""


"""
Case:3
Constructor used in based class and derived class.
Here, based class and derived class use dynamically attribute or function.
But, Here, It is necessary to passed parameters of parent in child class of constructor
function and again set constructor for parent class with paramenters.
"""

class Aircraft:
    def __init__(self,name,age,pan):
        self.full_name = name
        self.age_student = age
        self.pan_card= pan

class Pilot(Aircraft):
    salary = 170000
    expertises = 'Aircraft engine'

object1 = Pilot('Hari Sharma',34,545111)
print(object1.full_name)

class Copilot:
    def __init__(self,f_name,age,address):
        self.a1 = f_name 
        self.age2 = age
        self.a3 = address
        

    # def __init__(self, new_name):
    #     self.a1= new_name


class Hostess(Copilot):
    def __init__(self, expertise, salary, f_name, age, address):
        Copilot.__init__(self,f_name,age,address)
        self.exp=expertise
        self.pay=salary

objectn = Hostess(expertise="Speaking", salary='3000', f_name='Mina Lamsal',address='Dang', age=24)
print(objectn.a1 +" has " + objectn.pay + " salary from " + objectn.a3)
    
