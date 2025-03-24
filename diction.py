dict1={'a':'hari', 'b':'Gita'}
print(dict1)
print(type(dict1))

dict2={'Nepal':'KTM','China':'Beijing','India':'Delhi','Bhutan':'Thimpu','boy':True,'girls':False, 7:9}
print(dict2)
print(dict2['Nepal'])
dict2['Nepal']='Dang'#to change the value according to the key
print(dict2)
dict2.update({'Lidiya':'Tulsipur'})#to add the value into the list
print(dict2)
dict2.pop('Nepal')
print(dict2)
dict2.clear()#to delete everything.
print(dict2)