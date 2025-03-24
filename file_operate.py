"""
1) File is actual data of any thing
Some file type are: .txt, .csv, .log, .json, .xml, etc
Syntax: 1)w mode for write only #1)xa vaney overwrite garxa xaina vaney new banauxa
        2)r mode for read only
        3)a mode for append as well as update content
Advance modes are: 4) wb mode for write binary
                   5) rb mode for read binary
                   6)x mode for write only
                   7)rw mode for
"""
#Write mode
"""
1. overwrite the content, if already this name's file exist in machine
2. if file doesn't exist it will create new one.
"""

csb = open('Computer.txt','w')
csb.write('This is the first practice')
csb.close()

#advance form
with open('data.txt','w') as file_pointer:
    file_pointer.write('This is the first line \n')
    file_pointer.write('This third line content')
    file_pointer.writelines(('First line appear \n', 'Second Line appear\n', 'Third line appear\n'))

#read mode
with open('data.txt','r')as f:
    gita=f.read()
print(gita)


#append mode
with open('Rima.txt','a')as r:
    r.write('\nThis is append content')
    r.write('\nThis is second append')

import pickle #to save the object or collection

# list_number = [1,2,3,4,5,6,7]
# with open('binod.pkl', 'wb') as po:
#     pickle.dump(list_number,po)

# with open('binod.pkl','rb')as lock:
#     h = pickle.load(lock)
#     print(h)
#     print(type(h))

# tuple_number = (1,2,3,4,5,6,7)
# with open('gita.pkl', 'wb') as po:
#     pickle.dump(tuple_number,po)

# with open('gita.pkl','rb')as lock:
#     h = pickle.load(lock)
#     print(h)
#     print(type(h))


# set_number = {1,2,3,4,5,6,7}
# with open('tapsu.pkl', 'wb') as po:
#     pickle.dump(set_number,po)

# with open('tapsu.pkl','rb')as lock:
#     h = pickle.load(lock)
#     print(h)
#     print(type(h))



dict_num = {'tapsu':'BIM','gita':True}
with open('diksha.pkl', 'wb') as po:#po means file pointer
    pickle.dump(dict_num,po)

with open('diksha.pkl','rb')as lock:
    h = pickle.load(lock)
    print(h)
    print(type(h))



import json
dict_data = {'Nepal':'KTM','Bhutan':'Thimpu','China':'Beijing'}

with open('datafile.txt','w')as opps:
    opps.write(json.dumps(dict_data))

with open('Bina.txt','w')as opps1:
    opps1.write(str(dict_data))


db = {}
b = pickle.dumps(db)
c = pickle.loads(b)
print(c)

#only write mode
#it can not create duplicate file in same place in your machine
"""
hi= open('Tina.txt','x')
hi.write('This is the only write mode and it cannot create duplicate file')
hi.close()
"""



import os
if os.path.exists("Tina.txt"):
    os.remove("Tina.txt")
    print("File deleted")
else:
    print("file doesn't exist")



import os
if os.path.exists("gita.pkl"):
    os.rename('gita.pkl','gita_ch.txt')
    print("File renamed")
else:
    print("File doesnt exists")


#seek function
tom = open('keshu', 'w')
tom.write('Simultaneoulsy perform like human')
tom.close

tom = open('keshu','r')
before1= tom.read()
print(before1)

tom.seek(3)
after1 = tom.read()
print(after1)
