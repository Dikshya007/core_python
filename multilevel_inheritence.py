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

access1 = Hostess(skill='Flight Manage', scale='170000',First_Name='Rima Lama', age1=25, contact='9848130395')
print(access1.name + ' has ' + access1.salary + ' salary and her contact is '+ access1.phone +' and duties is ' +access1.able )

class Air_Craft_Engineer(Hostess):
    def __init__(self, qlf, skill, scale, First_Name, age1, contact):
        super().__init__(skill, scale, First_Name, age1, contact)
        self.academic = qlf

access2 = Air_Craft_Engineer(qlf='Bachelors in Aerospace Engineering', scale='2500000', First_Name='Sulav Thapa', age1=26, contact='9875642311', skill='Making Plane')
print(access2.name + ' has a qualification in ' + access2.academic)