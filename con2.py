Math=int(input("Enter the marks of Math"))
Science=int(input("Enter the marks of Science"))
Social=int(input("Enter the marks of Social"))
Nepali=int(input("Enter the marks of Nepali"))
English=int(input("Enter the marks of English"))

Sum1=Math+Science+Social+Nepali+English
Percentage=(Sum1/500)*100

if Percentage== 100>=90:
    print('A+')
elif Percentage== 90>=80:
    print('A')
elif Percentage== 80>=70:
    print('B+')
elif Percentage== 70>=60:
    print('B')
elif Percentage== 60>=50:
    print('C+')
elif Percentage== 50>=40:
    print('D')
else:
    print('Fail')