
password = 'pfjisokay '

HitList = ['RiceCrispy Treat','Roger Rabbit','Captin Crunch','Count Chocula','Cookie Crisp','Cinnamon Toast']

message = 'your target for today is,'

def hit_function(name):
    lst = []
    for i in HitList:
        msg = '{} {} {}'.format(name,message,i)
        lst.append(msg)
    return lst

 

def get_name():
    go = True
    while go:
        name = input("What is your handle??? ")
        if name == '':
            print('You need to enter your handle now...')
        elif name == 'Rex':
            print('Rex is not authorized... ')
        else:
            go = False
    lst = hit_function(name)
    for i in lst:
        print(i)
        print('then')


get_name()
