"""
Object-Oriented Programming (OOP)
In Python, everything is an object. Even though you might use procedural programming techniques, Python treats everything behind the scenes as objects.

OOP is used to model and store real-world entities, enabling you to create your own data types where you can store and manage data.

A class is used to represent real-world entities, and it typically starts with a capital letter to follow naming conventions.

Syntax:
class <class_name>(parent_class(optional)):
    # Description of the class
    # Attributes (data that stores specific values)
    # Behavior (methods that modify attributes or define the behavior of the class
"""
print("-------Start attribute--------")
#Different objects can depend on to one class.objects arenot depended upon each other.
class Teacher:
    age = 22
    name = 'Diksha G. Magar'

object1 = Teacher()
print(type(object1))
print(object1.age)

object2 = Teacher()
print(object2.name)
object2.name='Tapsu P.Magar'#creates different memory address and stores the new data too
print(object2.name)
print(object1.name)

#practice:-
class Student:
    name= 'Gita Budhathoki'#attributes
    age= 22
    faculty = 'BIM'

    def inc_age(self):#behavior------>function
        self.age +=1 #self is a pointer------>function

object3 = Student()#object
# print(object3.name)
# print(object3.age)
print(object3.faculty)
object3.age=50
object3.inc_age()
print(object3.age)

object4 = Student()
object4.age=20
object4.inc_age()
print(object4.age)





"""
Here, inc_age() function represents as behavior is these class 
and self-pointer passed in thaht function.
Self is pointer like "this pointer" in java
A class has many objects and multiple objects are using same method/behavior/function
this condition we can not define which object called the funtion then we can't pass argument
of particular object. So, we slove problem by passing self_pointer in the function
as a argument form. When self-pointer is passed in a function then self_pointer decide
automatically which objects of argument is passed int he function and finally, the funtion can use argument according to calling object.
"""
#So when object called inc-age(self) function of class Student and in this situation,
#self automatically invoked age_argumnet for object5 in the inc_age function. 

"""
ekchoti constructor lagayo vaney aafae chalxa
In class, To change or update all attributes dynamically via using constructor
To accessing all attributes from anywhere,
construcor is also a behavior. Constructor is self automatically called or run during the objects created in programs
"""

# class Learn:
#     name = 'Muna Budha'

#     def __init__(self):
#         print('This function is automatically called during object is created')


# object7 = Learn()
# object8 = Learn()

"""
Here, __init__ constructor function is automatic run two time because
Learn class has two objects(object1 and object2)
Note: in python, constructor is automatically called(run) during class of objects are
creating state in the class
"""
class Database1:
    def __init__(self,name,age,salary):
        self.arg1 =name
        self.arg2 =age
        self.arg3 =salary

        print(self.arg1 + ' is created')#plus for strings
        print(self.arg2 , ' years old')#comma for integers
        print(self.arg3 , 'salary income')

    def __del__(self):
        print(self.arg1+ ' This constructor is deleted')

data_ob1 = Database1('Mina', 67, 6000)
"""
It forcefully deletes the object and construction. It doesnt do it.
Because python has authomatic garbage collection method and this method deeleted the object 
during object is override or useless
Note: After del object then can not called next time that object.
"""
data_ob1 = Database1('Gita', 57, 7000)
