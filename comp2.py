num8=[7,3,5,8,10]
num7=[6,5,2,8,20]
w= [x*y for x in num8 for y in num7]
print(w)

dist=[1,4,7,3,5,8]
dict_name = {t1:'even' if t1 % 2 == 0 else 'odd' for t1 in dist}
print(dict_name)