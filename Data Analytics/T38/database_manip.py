import sqlite3
db=sqlite3.connect('Blank_db')
cursor=db.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS python_programming(id INT, name VARCHAR(30), grade INT)
''') #create table
db.commit #table created, cursor.execute makes sql command

cursor=db.cursor()
id1=55
name1='Carl Davis'
grade1=61

id2=66
name2='Dennis Fredrickson'
grade2=88

id3=77
name3='Jane Richards'
grade3=78

id4=12
name4='Peyton Sawyer'
grade4=45

id5=2
name5='Lucas Brooke'
grade5=99

cursor.execute('''INSERT INTO python_programming(id, name, grade) VALUES (?, ?, ?) ''', (id1, name1, grade1)) #insert rows with values defined above

cursor.execute('''INSERT INTO python_programming(id, name, grade) VALUES (?, ?, ?) ''', (id2, name2, grade2))

cursor.execute('''INSERT INTO python_programming(id, name, grade) VALUES (?, ?, ?) ''', (id3, name3, grade3))

cursor.execute('''INSERT INTO python_programming(id, name, grade) VALUES (?, ?, ?) ''', (id4, name4, grade4))

cursor.execute('''INSERT INTO python_programming(id, name, grade) VALUES (?, ?, ?) ''', (id5, name5, grade5))
db.commit()

grade2 = 80
grade1 = 60
cursor.execute(''' SELECT * FROM python_programming WHERE grade BETWEEN ? AND ? ''', (grade1, grade2)) #60<=grade<=80
cursor.fetchall() #show rows with given condition

name='Dennis Fredrickson'
cursor.execute(''' DELETE FROM python_programming WHERE name=?''', [name]) #delete rows with given condition

idd=-999999
iddd=54
cursor.execute(''' UPDATE python_programming SET grade=75 WHERE id BETWEEN ? AND ?''', (idd, iddd)) #for rows with id <55, grade set to 75, BETWEEN includes ends
db.commit() #command executed
db.close() #close database with saved changes
