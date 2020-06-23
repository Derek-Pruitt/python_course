

mySentence = 'loves the color'

color_list = ['denim','blue','purple','green','yellow','pink']

def color_function(name):                     #parameter
    lst = []
    for i in color_list:
        msg = "{} {} {}".format(name,mySentence,i)
        lst.append(msg)
    return lst                                #needs to be lined with the for or it wont go through the list


def get_name():
    go = True
    while go:
        name = input('What is your name? ')   #makes it run indefenitly
        if name == '':
            print('you need to provide your name!')
        elif name == 'Marxus':
            print('Marxus, you may not use this software.')
        else:
            go = False                        # exits while loop so it can call function to go through list
    lst = color_function(name)
    for i in lst:
        print(i)
        


get_name()

