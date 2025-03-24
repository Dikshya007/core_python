class Pilot:
    def __init__(self,fname,contact,gender):
        self.name = fname
        self.phone = contact
        self.htype = gender

class Copilot:
    def __init__(self,qlf,age):
        self.academic=qlf
        self.age=age

class Engineer(Pilot,Copilot):
    def __init__(self,fname, contact, gender, qlf, age):
        Pilot.__init__(self,fname,contact,gender)
        Copilot.__init__(self,qlf,age)

class Hostess:
    name = 'Anu'

class Software_Engineer(Engineer, Hostess):
    def __init__(self, fname, contact, gender, qlf, age):
        Engineer.__init__(self,fname, contact, gender, qlf, age)

objectlast = Software_Engineer(fname='Rima', contact='9864571232', gender='Female', qlf='BIT',age='50')
print(Software_Engineer.__mro__)
print(objectlast.name)