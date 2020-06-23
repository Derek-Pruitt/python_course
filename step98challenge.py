Fname = 'Derek'
Lname = 'Pruitt'
fname = 'Cecillia'
lname = 'Kiggans'
print('{} {}, is engaged to, {} {}'.format(Fname,Lname,fname,lname))


x = format(12,'b')   #'b' type gives the new binary format of 1100
print(x)


print("hexadecimal: {0:x}, percentage: {0:%}, {0:E}, {0:+} ".format(-12))


def getsum(num1,num2):
    answer = num1 + num2
    print('The answer is {}'.format(answer))
getsum(2,4)
myAdd = getsum
myAdd(2,4)
