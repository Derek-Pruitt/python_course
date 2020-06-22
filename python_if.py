#if, else statements
num1 = 12
key = False

if num1 == 12:
    if key:  #dont need to write key value. if not key will = True and vice versa
        print('num1 is equal to 12 and they have the key')
    else:
        print('num1 is equal to 12 and they do not have the key') 
elif num1 < 12:
    print('num1 is less than  12')
else:
    print('num1 is not equal to 12')

    #assignment
age = isinstance(32,int)  # change age to see dif result

if age > 26:
    print('You are Older than 26,')
    if age > 50:
        print('and you are over the hill!')
    elif age == 32:
        print(bool(32))
        print('you are also 32!')
    else:
        print('But you are not over the hill yet.')
elif age < 18:
    print('Your almost an adult!')
else:
    print('Congadulations you are an adult!')
print(age)
