




class Human:
        name = ''
        hair = ''
        hair_color = ''
        height = ''
        weight = ''
        age = ''
        race = ''
        def info(self):
            print('{}\n{}\n{}\n{}\n{}\n{}\n{}'.format(self.name,self.hair,self.hair_color,self.height,self.weight,self.age,self.race))


class Person(Human):
    def __init__(self,name,hair,hair_color,height,weight,age,race):
        self.name = name
        self.hair = hair
        self.hair_color = hair_color
        self.height = height
        self.weight = weight
        self.age = age
        self.race = race

       
       



if __name__=='__main__':
    p1 = Person('Joe Dirt','Mulet','Blond','5ft 7in','180lb','40','White')
    print(p1.info())
    
