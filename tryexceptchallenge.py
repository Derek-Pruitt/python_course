
def Person():
    Fname = input("\nPlease enter your fist name:  ")
    Lname = input("\nPlease enter your last name:  ")
    age = input("\nPlease enter your age:  ")
    return Fname,Lname,age


def userName():
    go = True
    while go:
        Fname,Lname,age = Person()
        try:
            WholeName = Fname + Lname
            age2 = int(age)
            go = False
        except ValueError as e:
            print("{}: \n\nYou did not provide a numeric value".format(e))
            print('\n\nPlease enter a numeric value for age...')
        finally:
            print('\nThank you!')
            

                
       
    print("{}{}".format(WholeName,age2))


if __name__=='__main__':
    userName()
            
