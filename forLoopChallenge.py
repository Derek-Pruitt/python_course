Person = {
    'Fname:':'Derek',
    'Lname:':'Pruitt',
    'Age:':'32',
    'Address:':'189 south cheyeene st, Laramie, Wy. 82070',
    'Phone:':'307-343-2010'}
for x,y in Person.items():
    if y == 'Derek':
        continue
    if y == '32':
        break
    print(x,y)

for i in range(10):
    print(i)
else:
    print('we finally reached TEN!')
