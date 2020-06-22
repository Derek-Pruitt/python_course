#continue stament
MyAge = 0
while MyAge < 32:
    MyAge += 1
    if MyAge == 10:
        continue
    print('{} you are not 32 yet.'.format(MyAge))
    
   #else stament
i = 1
while i < 10:
    print('{} you are not TEN yet.'.format(i))
    i += 1
else:
    print('you are now TEN!')
    
#break stament
Bob = 1
while Bob < 20:
    print('Bob is {}'.format(Bob))
    if Bob == 20:
        break
    Bob += 1
    
