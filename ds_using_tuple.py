#我会推荐你总是使用括号
#来指明元组的开始与结束
#尽管括号是一个可选选项
#明了胜过晦涩，显示优于隐式
zoo=('python','elephant','penguin')
print('Number of animals in the zoo is',len(zoo))
new_zoo='monkey','camel',zoo
print('Number of cages in the new zoo is',len(new_zoo))#笼子的个数是
print('All animals in zoo are',new_zoo)
print('Animals brought from old zoo are',new_zoo[2])
print('Last animal brought from old zoo is',new_zoo[2][2])
print('Number of animals in the is',len(new_zoo)-1+len(new_zoo[2]))