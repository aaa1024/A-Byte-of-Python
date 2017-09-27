import os
import time

#1.只需要备份的文件与目录将被指定在一个列表中
source=['/home/a/桌面/python']
#在这里要注意到我们必须在字符串中使用双引号用以括起包含空格的名称

#2.备份文件必须存储在一个主备份目录中
target_dir='/home/a/swa/backup'

#如果目标目录不存在则创建目录
if not os.path.exists(target_dir):
    os.mkdir(target_dir)
#3.备份文件将打包压缩成.zip文件
#4.将当前日期作为主备份目录下的子目录名称
today=target_dir+os.sep+time.strftime('%Y%m%d')
#将当前时间作为zip文件的文件名
now=time.strftime('%H%M%S')

#zip文件名称格式
target=today+os.sep+now+'.zip'

#如果子目录尚不存在则创建一个
if not os.path.exists(today):
    os.mkdir(today)
    print('Successfully created directory',today)

#5.我们使用zip命令将文件打包成zip格式
zip_command='zip -r {0} {1}'.format(target,''.join(source))

#运行备份
print('Zip command is:')
print(zip_command)
print('Running:')
if os.system(zip_command)==0:
    print('Successful backup to',target)
else:
    print('Backup FAILED')

