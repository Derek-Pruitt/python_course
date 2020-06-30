
##Python:       3.8.3 

##author:       Derek J. Pruitt

##purpose:      For learning Python. Text based Game




def start(nice=0,mean=0,name=''):
    #get user's name
    name = describe_game(name)
    nice,mean,name = nice_mean(nice,mean,name)
    
def describe_game(name):
    """
        check if this is a new game or not.
        if it is new, get the user's name.
        if it is not a new game, thank the plyer for playing
        again and continue with the game
    """
    #meaning if I dont have the user's name,
    #then they are a new player and we need to get thier name
    if name != "":
        print("\nThank you for playing again, {}!".format(name))
    else:
        stop = True
        while stop:
            if name == "":
                name = input("\nWhat is your name? \n>>> ").capitalize()
                if name != "":
                    print("\nWelcome, {}!".format(name))
                    print("\nIn this game, you will be greeted \nby several differnt people. \nyou can choose to be nice or mean")
                    print("but at the end of the game your fate \nwill be sealed by your actions.")
                    stop = False
    return name

def nice_mean(nice,mean,name):
           #question 1
            show_score(nice,mean,name)
            pick = input("\nA Big man walks up to you \nand asks the time. \nWill you be nice or mean? (N/M) \n>>>: ").lower()
            if pick == "n":
                print("\nThey thank you and walk away smiling...")
                nice = (nice + 1)
                
                show_score(nice,mean,name)
            if pick == "m":
                print("\nThey glare at you and says they will see you later \nthen storms off...")
                mean = (mean + 1)
               
                
                show_score(nice,mean,name)
            #question 2
            pick = input("\nA Dog walks up to you \nand asks where the nearest fire hydrant is. \nWill you be nice or mean? (N/M) \n>>>: ").lower()
            if pick == "n":
                print("\nIt thanks you and walk away smiling...")
                nice = (nice + 1)
                
                show_score(nice,mean,name)
            if pick == "m":
                print("\nIt glare at you and nips your ankle \nthen storms off...")
                mean = (mean + 1)
               
                
                show_score(nice,mean,name)
            #question 3
            pick = input("\nA werewolf walks up to you \nand asks where a good stake house is. \nWill you be nice or mean? (N/M) \n>>>: ").lower()
            if pick == "n":
                print("\It thanks you and offer you to go along...")
                nice = (nice + 1)
                
                show_score(nice,mean,name)                
            if pick == "m":
                print("\nWhile walking away backwards \nit tells you maybe youll \nbe the stake house...")
                mean = (mean + 1)
               
                
                show_score(nice,mean,name)
            #question 4
            pick = input("\nA vampire up to you \nand asks where the nearest hotel is \nas its almost sunup. \nWill you be nice or mean? (N/M) \n>>>: ").lower()
            if pick == "n":
                print("\nIt thanks you smiling \nthen vanishes in a cloud of smoke...")
                nice = (nice + 1)
                
                show_score(nice,mean,name)
            if pick == "m":
                print("\nIt hypnotizes you and makes you \npunch yourself in the stomach \nthen turns into a bat and poops on your head...")
                mean = (mean + 1)

                show_score(nice,mean,name)
            score(nice,mean,name)   # pass the 3 variables to the score()



            
   


def show_score(nice,mean,name):
    print('\n{}, your current total: \n({}, Nice) and ({}, Mean)'.format(name,nice,mean))

def score(nice,mean,name):
    # scroe function is being passed the values stored within the 3 variables
    if nice > 2: # if condition is valid, call win function passing in the variables so it can use them
        win(nice,mean,name)
    if mean > 2: # if condition is valid, call lose function passing in the variables so it can use them
        lose(nice,mean,name)
    else:        # else, call nice_mean function passing in the variables so it can use them
        nice_mean(nice,mean,name)
        

def win(nice,mean,name):
    # substitue the {} wildcard with our own variable values
    print("\nNice job {}, you are a decent person! \nEveryone Loves you and you've \nmade lots of friends along the way!".format(name))
    # call again function and pass in the variable
    again(nice,mean,name)

def lose(nice,mean,name):
    # substitue the {} wildcard with our own variable values
    print("\nAhhh too bad, game over! \n{}, you live in a getto \nget beaten up every day \nand you live alone in a cardboard box!".format(name))
    # call again function and pass in the variable
    again(nice,mean,name)

def again(nice,mean,name):
    stop = True
    while stop:
        choice = input("\nDo you want to play again? (Y/N):\n>>> ").lower()
        if choice == "y":
            stop = False
            reset(nice,mean,name)
        if choice == 'n':
            print("\nOh, so sad, sorry to see you go!")
            stop = False
            quit()
        else:
            print("\nEnter (Y) for 'YES', (N) for 'NO':\n>>> ")

def reset(nice,mean,name):
    nice = 0
    mean = 0
    # Notice, I do not reset the name because they want to play again
    start(nice,mean,name)


    
            
        








if __name__ == '__main__':
    start()
