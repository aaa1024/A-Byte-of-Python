x=50

def func():
    #表示所用的x是全局变量x
    global x
    print('x is',x)
    x=5
    print('Change global x to',x)

func()
print('the value of x is',x)