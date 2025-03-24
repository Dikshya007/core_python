# set1={1,2,3,4,5,6,7,'amc',1,True,'dang','amc'}
# print(type(set1))
# print(set1)
# set1.add('dino')
# print(set1)
# set1.remove(2)
# print(set1)
# set1.pop()
# print(set1)
# set1.discard('watch')
# print(set1)
# set1.discard('dino')
# print(set1)

"""
set1={1,2,3,4,5,6,7,'amc',1,True,'dang','amc'}
set2={9,10,12,1}

first=['data1','data2','data3']
f=set(first)    #set constructor
second=['am','bm','cm']
s=set(second)

b=set1.union(set2)
print(b)
print(f.union(s))
"""

#transforming tuple into the set and computing as a set
third=('l1','l2','l3','gita')
t=set(third)
fourth=('s1','s2','s3','gita')
h=set(fourth)
print(t.union(h))
print(t.intersection(h))
print(t.difference(h))
print(t|h)
print(t&h)