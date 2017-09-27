import os
import time
source=['/home/a/桌面/python'] #这是文件来源
target_dir='/home/a/桌面/backup'#这是备份存放目录
#如果不存在此目录，那就新建一个
if not os.path.exists(target_dir):
    os.mkdir(target_dir)
today=target_dir+os.sep+time.strftime("%Y%m%d")#在存放路径里建立一个名为“今天”的路径，他的名称是年月日
#如果不存在，则创建一个
if not os.path.exists(today):
    os.mkdir(today)
    print('Mk today')
#最终文件存放目录为back里按日期命名的文件夹
now=time.strftime("%H:%M")
target=today+os.sep+now+'.zip'

zip_command='zip -r {0} {1}'.format(target,''.join(source))
print('Running')
print(zip_command)
if os.system(zip_command)==0:
    print('Successful backuped to',target)
else:
    print('BACK FAILED')