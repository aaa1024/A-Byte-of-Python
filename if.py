number=23
guess=int(input('Enter an integer: '))

if guess==number:
        #新块从这里开始
        print('Congratulations,you guessed it')
        #新块在这里结束
elif guess<number:
        #另一代码块
        print('No,it is a little higher than that')
else:
        print('No,it is a little lower than that')
print('Done')