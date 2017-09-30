class P:
    name=''

p=P()
list=[]
list.append(P())
list[0].name='hhh'
list.append(P())
list[1].name='hahahha'
print(list[0].name)
print(list[1].name)