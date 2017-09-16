number=23
runing=True

while runing:
    guess=int(input('Enter an integer:'))

    if guess==number:
        print('Congratulation,you guessed it.')
        runing=False
    elif guess>number:
        print('No,is a little lower than that')
    else:
        print('No,it is a little higher than that')
else:
    print('The while loop is over')

print('Done')
