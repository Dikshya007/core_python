"""
Method Resolution Order (MRO)
Method Resolution Order (MRO) is the order in which Python looks for a method in a hierarchy of classes.
 It defines the sequence in which classes are searched when trying to invoke a method, starting from the class of the object and
 moving up through the inheritance hierarchy.
MRO is especially important in the context of multiple inheritance, where a single method might be found in multiple parent classes.
 In such cases, Python uses MRO to determine which class's method will be called.
"""
class Copilot:
    def __init__(self,First_Name,age1,contact):
        self.name = First_Name
        self.age = age1
        self.phone = contact


class Hostess(Copilot):
    def __init__(self,skill,scale,First_Name,age1,contact):
        super().__init__(First_Name,age1,contact)
        self.able = skill
        self.salary = scale

class AircraftEng(Hostess):
    def __init__(self,age_of_eng,interest_of_eng,skill,scale,First_Name,age1,contact):
        super().__init__(skill,scale,First_Name,age1,contact)
        self.ag = age_of_eng
        self.interest=interest_of_eng

class Pilot(AircraftEng):
    def __init__(self,name_pilot,age_of_eng, interest_of_eng,skill,scale,First_Name,age1,contact):
        super().__init__(age_of_eng, interest_of_eng,skill,scale,First_Name,age1,contact)
        self.nam = name_pilot

class mutual(Pilot):
    def __init__(self,gap,skill,scale,First_Name,age1,contact,age_of_eng,interest_of_eng,name_pilot):
        super().__init__(First_Name,age1,contact,age_of_eng,interest_of_eng,name_pilot,skill,scale)
        self.lackup= gap
        
    
objectfinal = mutual(skill='Mechanic',scale='50000', First_Name='Tapsu Magar', age1='20',gap='mina',
                      contact='5454515114',age_of_eng='Sohil Yadav',interest_of_eng='Dancing',name_pilot='Jyoti Oli')
print(objectfinal.nam)
print(mutual.__mro__)