"""
 Built-in Decorator: @classmethod
@classmethod
→ Generally used when there is a need to define methods that create instances of the class itself.
It helps in creating objects of a specific class.
🔹 Important: The cls parameter is mandatory when using the @classmethod decorator.
"""
class Employee:
    def __init__(self, name, age, salary, address):
        self.name = name
        self.age = age
        self.__salary = salary
        self._address = address

    def increment_salary(self, increment):
        self.__salary += increment

    def print_salary(self):
        print("Salary:", self.__salary)

    @classmethod
    def create_obj_from_string(cls, emp_str):
        name, age, salary, address = emp_str.split(",")
        return cls(name, int(age), float(salary), address)
    
    @classmethod
    def create_obj_from_file(cls, file_path):
        list_obj = []
        with open(file_path,'r') as f:
            line = f.readline()
            while line != '':
                name,age, salary, address = line.split(',')
                age, salary = int(age),float(salary)
                list_obj.append(cls(name,age,salary,address))
                line = f.readline()
        return list_obj

ram = Employee.create_obj_from_string("Ram,25,50000,Kathmandu")
ram.print_salary()
employee = Employee.create_obj_from_file('employee.txt')
print(employee[1].age)
print(employee[2].name)