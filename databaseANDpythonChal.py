# AUTHOR:       Derek Pruitt

#REASON:        This is for a class assigment for the Tech Acadamey

import sqlite3

connection = sqlite3.connect('Database_Python_Chal.db')
c = connection.cursor()
c.execute('CREATE TABLE Roster(Name TEXT, Species TEXT, Iq INT)')
c.execute('INSERT INTO Roster VALUES("Jean-Baptiste Zorg","Human",122),("Korben Dallas","Meat Popsicle",100),("Ak\'not","Mangalore",-5)')
c.execute("UPDATE Roster SET Species = 'Human' WHERE Species = 'Meat Popsicle'  ")
look = "SELECT Name, Iq FROM Roster WHERE Species = 'Human'"
c.execute(look)
result = c.fetchall()
for x in result:
    print(x)
connection.commit()
connection.close()
