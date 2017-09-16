x=5

def func(x):
    # 这里使用的是参数里的那个x
    print('x is',x)
    #这是定义在func函数里的局部变量x
    x=50
    print('Change local x to',x)
#调用函数
func(x)
#主代码块里的x值不变
print('x is still',x)