"""
Generally speaking, exceptions are errors that occur during the execution of a program.
They can help manage two types of errors:
1.Syntax Error: Occurs when the code is not written in the correct format.
2.Semantic/Logical Error: The code is written correctly, but it does not produce the expected result.
Normally, syntax errors are not handled using exception handling because they are detected at compile time.
Logical errors are detected at runtime, so we need to handle them using exception handling.
"""

# x= 0
# y = 1/x
# print(y)

"""
x=0
try:
    y=1/x
    print(y)

except ZeroDivisionError:
    print("ZeroDivisionError: You can't divide a number by zero")
"""

'''
Important: Once an error is found inside the try block, the program immediately jumps to the matching except block (if available). 
Any code after the error line inside the try block is skipped.
If there is no matching except block, and the error is not handled, the program will terminate.

To avoid unexpected termination, it is recommended to always include at least one generic except block 
(e.g., except Exception: or simply except:) at the end of the exception handling structure. This ensures that any unhandled errors
 are caught gracefully.
'''
# x=10
# try:
#     y=1/x
#     list_num = [1,2,3]
#     z = list_num[5]
#     print(z)
#     file = open("test.txt","r")
#     file.write("Hello")

# except ZeroDivisionError:
#     print("ZeroDivisionError: You cant divide a number by zero")
# except IndexError:
#     print("IndexError: List index out of range")
# except:
#     print("Some other exception occured")
# else:
#     print("No exception occured")
# finally:
#     print("This block will always execute")
# print(y)

'''next practice raise(throw in other language) customly error by raise'''


# def buy_share(amount,num):
#     if amount <=0 or num<=0:
#         raise ValueError("Amount and shares must be greater than zero")
#     return amount*num

# try:
#     price_of_kitta = buy_share(3000, 30)
#     print("Price of kitta is:", price_of_kitta)

# except ValueError:
#     print("ValueError: Amount and number of shares must be grater than zero")
#     price_of_kitta = None
# else:
#     print("Transaction Successful")
# finally:
#     print("This block will always be executed")

"""alternative part is assert is like a raise"""
'''
Difference between raise and assert
-----raise
Used to throw custom errors
You can choose the error type
Works with try-except
Used in real applications

-----assert
Used to check conditions during development
Raises AssertionError if condition is false
Can be disabled with python -O
Mainly for debugging/testing
'''

# def buy_share(amount,num):
#     assert amount >= 0 and num >= 0
#     return amount*num

# try:
#     price_of_kitta = buy_share(3000,-30)
#     print("Price of kitta:",price_of_kitta)
# except AssertionError:
#     print("calculation error: Amount and number shares must be greater than zero")
#     price_of_kitta = None
# else:
#     print("Transaction Successful")
# finally:
#     print("This block will always execute")
# #print(price_of_kitta)

'''Rename error via"as" and then we can keep information in variable'''
def increment(x):
    if type(x) != int:
        raise TypeError("Only integers are allowed")
    return x+1

try:
    #wrong argument pass in function
    result_info = increment("10")
    print("Result:",result_info)
except TypeError as keshu:
    print("TypeError:",keshu)
else:
    print('increment successful')
finally:
    print("This block will always execute")