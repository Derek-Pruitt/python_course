name = "\"Derek Pruitt\","
MultiLine = '''  is doing great,
in the boot camp so far,
even though it is dificult some times!  '''
print(MultiLine[-16:-10])
print(len(MultiLine))
print(MultiLine.strip())
print(name.upper())
print(MultiLine.lower())
print(name.replace("Derek","The Great"))
a = "it" in MultiLine
print(a)
b = "it" not in MultiLine
print(b)
c = name
d = MultiLine
e = c + d
print(e)
#using seperate data types video

num1 = 25
num2 = 52
print(num1 ** num2)#Exponentiation
num1 **= .02#Assignment operator
print(num1)
print(num1<num2)#Comparison operator
print(num1>2 and num2<50)#Returns True if both statements are true
print(num1 == 25 or num2 == 52)#Returns True if one of the statements is true
print(not(1>0 and 5<10))#Reverse the result, returns False if the result is true
f = ['me','you','them']
g = ['our','house','great']
print(f is g)#Returns True if both variables are the same object
print(f is not g)#Returns True if both variables are not the same object
print('me' in f)##Returns True if a sequence with the specified value is present in the object
print('great' not in f)#Returns True if a sequence with the specified value is not present in the object
n1 = 10
n2 = 12
bo=n1 & n2;
print(bo,"" + bin(bo))
#tuples part in python course
animal = ('zebra','alligator','giraffe','goat','ox')
listofanimals = list(animal)
print(listofanimals)
print(animal)
listofanimals.append("honey badger")
print(listofanimals)
wow = 'this is getting somewhere for sure'
newwow= list(wow)
print(newwow)
newwow = wow.split(" ")
print(newwow)
#list and tuples video, python course
myList = [2,56,4,18]
print(len(myList))
for i in myList:
        print(i)
print(myList[2])
myList.append(5)
for i in myList:
    print(i)
print(myList)
#list challenge
House = ['floors','roof','bathroom','bedroom','closet','livingroom','kitchen']
print(House)
for x in House:
    print(x)
for i in House:#does the same as x
    print(i)
House.append('basement')
print(House)
House2 = House.copy()
print(House2)
HouseNums = House2 + myList
print(HouseNums)
House.reverse()
print(House)
#tuple challenge
MyTuple=('Hello','there','this','is','my','TUPLE')
print(MyTuple)
for i in MyTuple:
    print(i)
for x in MyTuple:#does the same as i
    print(x)
HowMany = MyTuple.count('is')#counts how many times this value appears
print(HowMany)
setup={'HP','windows','I5'}
print(setup)
setup.add('120GB')
print(setup)
setup2={'HP','windows','T9'}
print(setup2)
diff=setup.difference(setup2)
print(diff)
#dictionaries video
mydic = {"index1":1,"index2":2,"index3":355}
print(mydic)
print(mydic['index2'])
users={'em_1234':{'fname':'Bob','lname':'Smith','Phone':'909-496-8890'},
           'em_4321':{'fname':'Janet','lname':'Zoolander','Phone':'760-456-9990'} }
print(users['em_4321'])
print(users['em_4321']['Phone'])
print('User: {} {}\nPhone: {}'.format(users['em_4321']['fname'],
                                      users['em_4321']['lname'],
                                      users['em_4321']['Phone']))
#Dictionary challenge
Brent_Books={
        'Night Angle Series':{
                'Book1':'The Way of Shadows',
                'Book2':'Shadow\'s Edge',
                'Book3':'Beyond the Shadows'},
        'Lightbringer Series':{
                'Book1':'The Black Prism',
                'Book2':'The Blinding Knife',
                'Book3':'The Broken Eye',
                'Book4':'The Blood Mirror',
                'Book5':'The Burning White'}}
print(Brent_Books)
print(Brent_Books.get('Lightbringer Series'))
Brent_Books['Lightbringer Series']['Book1']='Thee Black Prism'
print(Brent_Books.get('Lightbringer Series'))
for x, y in Brent_Books.items():
  print(x, y)
Brent_Books['Night Angle Series']['Year']=2008
print(Brent_Books['Night Angle Series'])
#assignment
height=['6ft 2in','5ft 2in','5ft 11in']#a variable with multiple values
print(height)
#python data types video
name='Python Course'
print(name)
print(type(name))
#Boolean data type video
answer = True
print(type(answer))
answer = False
print(type(answer))
math1 = 365
math2 = 366
if math1 > math2:
        print('365 is greater than 366')
else:
        print('365 is not greater than 366')
me=20
you=19
if me > you:
        print(bool(''))#Returning false on purpose
else:
        print(True)
#Thank you tech academy for making this so fun to learn!!!





