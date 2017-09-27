#coding=UTF-8

class Robot:
    '''表示有一个带有名字的机器人'''
    population=0 #因为它属于Robot类，所以它是类变量

    def __init__(self,name):
        """初始化数据"""
        self.name=name#它属于对象self，所以它是对象变量
        #当一个对象变量和一个类变量名称相同时，类变量将会被隐藏
        print("Initializing {}".format(self.name))
        #当有人被创建时，机器人将会增加人口数量
        Robot.population+=1

    def die(self):
        """我挂了"""
        print("{} is being destroyed!".format(self.name))

        Robot.population-=1
        if Robot.population==0:
            print("{} was last one.".format(self.name))
        else:
            print("There are still {:d} robot working.".format(Robot.population))

    def say_hi(self):
        """"来自机器人的问候
        没问题，你做得到。"""
        print("Greetings,my master call me {}.".format(self.name))

    @classmethod#类方法
    def how_many(cls):
        """打印出当前的人口数量"""
        print("We have {:d} robots.".format(cls.population))

droid1=Robot("R2-D2")
droid1.say_hi()
Robot.how_many()

droid2=Robot("C-3PO")
droid2.say_hi()
Robot.how_many()
print("\nRobot can do some work here.\n")

print("Robot have finished their work.So let's destroy them.")
droid1.die()
droid2.die()

Robot.how_many()
