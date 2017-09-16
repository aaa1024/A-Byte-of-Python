#用以练习运算符
a=31;b=22;

#加法
print("加法：{0}+{1}={2}".format(a,b,a+b))

#减法
print("减法：{0}-{1}={2}".format(a,b,a-b))

#乘法
print("乘法：{0}*{1}={2}".format(a,b,a*b))

#乘方
print("乘方：{0}^{1}={2}".format(a,b,a**b))

#除法
print("除法：{0}/{1}={2}".format(a,b,a/b))

#整除:x除以并对结果向下取整
print("整除：{0}//{1}={2}".format(a,b,a//b),end='\n\t  ')
print("{0}//{1}={2}".format(-a,b,-a//b))

#取模
print("取模：{0}%{1}={2}".format(a,b,a%b))

#以下部分涉及二进制

#输出a和b的二进制
print('{0}的二进制为{1}'.format(a,bin(a).replace('0b','')))
print('{0}的二进制为{1}'.format(b,bin(b).replace('0b','')))

#左移：将数字的位向左移指定的位数，即a乘以2的n次方
print("左移：{0}<<{1}={2}".format(a,b,a<<b))

#右移：将数字的位向右移动指定的位数
print("右移：{0}>>{1}={2}".format(a,b,a>>b))

#按位与
print("按位与：{0}&{1}={2}".format(a,b,a&b))

#按位或
print("按位或：{0}|{1}={2}".format(a,b,a|b))

#按位异或
print("按位异或：{0}^{1}={2}".format(a,b,a^b))

#按位取反
print("按位取反：~{0}={1}".format(a,~a))




