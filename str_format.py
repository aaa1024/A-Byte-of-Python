#print("hello world")#注意到print是一个函数
age=20
name='Swaroop'
country='America'

print('{0} was {1} years old when he wrote this book in {2}'.format(name,age,country))
print('why is {0} playing with that python?'.format(name))

#对于浮点数'0.333'保留小数点（.）后三位

print('{0:.3f}'.format(1.0/3))
#使用下标填充文本，并保持文字处于中间位置
#使用(^)定义'__hello___'字符串长度为11
print('{0:_^11}'.format('hello'))
print('{name} wrote {book}'.format(name='Swaroop',book='A byte of Python'))
print('what\'s your name?')
print(r"Newlines are indicated by \n")