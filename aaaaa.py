class P:
    name=''

p=P()
list=[]

list.append(p)
list[0].name='aaa'

list.append(P)
list[1].name='bbb'

list.append(P)
list[2].name='ccc'

print(list[0].name)
print(list[1].name)
print(list[2].name)