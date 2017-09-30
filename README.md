# python
phonebook2.py
  第一个小项目，虽然很简单但也填了不少坑。
  在python里类也属于对象，如果要将类实例化，则要在类名后面加（）
  list=[]，中括号里是可以空的

错误的做法：
class P:
    name=''

p=P()
list=[]
list.append(p)
list[0].name='hhh'
list.append(p)
list[1].name='hahahha'
print(list[0].name)
print(list[1].name)
这样子会导致list里的元素都是修改同一个p


正确的做法应该是每次appdend一个P（）：
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
