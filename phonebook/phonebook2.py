class People:
    name=''
    number=0
    n=0
    def say(self):
        print('{}\n\t名字:{}\n\t电话号码:{}'.format(self.n+1,self.name,self.number))
    def revise(self):
        number=input('请输入号码：')
p=People()
list=[]
def view():
    for i in list:
        i.say()
def add():
    list.append(People())
    print('现在一共有{}个联系人'.format(len(list)-1))
    edit(len(list)-1)
def edit(a,b=1):
    ct=0
    if(b==2):
        print('''\t1.名字:{}\n\t2.电话号码:{}'''.format(list[a].name, list[a].number))
        ct=int(input('请问你要修改什么？请输入对应的序号'))

    list[a].n=a
    if(b==1 or ct==1):
         list[a].name=input('请输入名字：')
    if(b==1 or ct==2):
        list[a].number=input('请输入电话号码：')
    if(b==1):
        print('已成功添加！')
    else:
        print('已成功修改！')
    list[a].say()
def revise():
    view()
    a=int(input('请输入你要修改的联系人的序号'))-1
    edit(a,2)
def find():
    n=input('请输入你要查找的联系人姓名：')
    for item in list:
        if item.name==n:
            item.say()
running=True
while running:
    print('''你可以输入下面的序号以执行对应的操作：
                1.查看所有联系人
                2.增加联系人
                3.修改联系人
                4.查找联系人
                5.退出''')


    a=int(input())
    if a==1:
        view()
    if a==2:
        add()
    if a==3:
        revise()
    if a==4:
        find()
    if a==5:
        running=False
