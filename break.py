#如果有break，将不会执行else
a=True
while a:
    s=input('Enter something:')
    if s=='quit':
        break
    print('Length of the string is',len(s))
    a=False
else:
    print('That is have no been break')
print('Done')
