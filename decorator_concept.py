"""
First, it's important to understand user-defined higher-order functions before we can easily grasp the concept of decorators.
"""
#user define higher order
def print_func(user_define_function):
    print(user_define_function())

def get_user_info():
    return 'Name','Tapsu', 'age','20','Kathmandu' 

print_func(get_user_info)

#decorator
# def us_dollar_conv(comfunc):
#     print(comfunc()*137)

# def get_salary():
#     return 500

# def pay_fee():
#     return 300

# us_dollar_conv(get_salary)
# us_dollar_conv(pay_fee)

def us_conv(cust_func):
    def wrapper():
        return cust_func()*137
    return wrapper

@us_conv
def re_salary():
    return 17000

@us_conv
def pay_fee():
    return 4700

salary_calc=re_salary()
FeePay = pay_fee()
print('Employee has {}'.format(salary_calc)+' and due fee is {}'.format(FeePay))


#use case of decorator
from datetime import datetime
def log_file(func):
    def wrapper():
        with open('log_details.txt','a') as f:
            f.write('The user ' + func.__name__+ ' activity at '+ str(datetime.now()) +'\n')
            func()

    return wrapper

@log_file
def login():
    print('User Login')

@log_file
def logout():
    print('User Logout')

login()
logout()


#Dikshya@17