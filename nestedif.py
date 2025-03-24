a=int(input('Enter the first number='))
b=int(input('Enter the second number='))

if b==0:
    print('This is null  number')
else:
    if b%2==0:
        print('This is even number')
    else:
        print('This is odd number')
    print('This is last ')

if a%2==0 and a%4==0:
    print('This number is exactly divisible by 2 and 4')
else:
    print('This is not divisible by 2 and 4')