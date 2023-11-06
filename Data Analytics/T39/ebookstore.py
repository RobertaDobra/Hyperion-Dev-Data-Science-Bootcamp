import sqlite3
db = sqlite3.connect('ebookstore_db')
cursor = db.cursor()  

#create table called books
cursor.execute('''
    CREATE TABLE IF NOT EXISTS books (id INTEGER, Title TEXT, Author TEXT,
                   	Qty INTEGER)
''') #creates table with columns and constraints on column values
db.commit()

cursor = db.cursor()
id1 = 3001
Title1 = "A Tale of Two Cities"
Author1 = "Charles Dickens"
Qty1 = 30

id2 = 3002
Title2 = "Harry Potter and the Philosopher's Stone"
Author2 = "J.K. Rowling"
Qty2 = 40

id3 = 3003
Title3 = "The Lion, the Witch and the Wardrobe"
Author3 = "C.S. Lewis"
Qty3 = 25

id4 = 3004
Title4 = "The Lord of the Rings"
Author4 = "J.R.R. Tolkien"
Qty4 = 37

id5 = 3005
Title5 = "Alice in Wonderland"
Author5 = "Lewis Carroll"
Qty5 = 12


records = [(id1, Title1, Author1, Qty1), (id2, Title2, Author2, Qty2),
          (id3, Title3, Author3, Qty3), (id4, Title4, Author4, Qty4),
          (id5, Title5, Author5, Qty5)]
cursor.executemany(''' INSERT OR REPLACE INTO books(id, Title, Author, Qty) VALUES(?,?,?,?)''', records)
db.commit()

while True: #program will run indefinitely
    print("Type 1 to enter a book")
    print("Type 2 tp update a book")
    print("Type 3 to delete a book")
    print("Type 4 to search for a book")
    print("Type 0 to exit")

    action = str(input("Enter corresponding number to indicate what you would like to do: "))

    if action == "1":
        cursor = db.cursor()
        id = int(input("id: "))
        Title = input("Title: ")
        Author = input("Author: ")
        Qty = int(input("Qty: "))
        cursor.execute(''' INSERT OR REPLACE INTO books (id, Title, Author, Qty) VALUES (?,?,?,?)''', (id, Title, Author, Qty))
        db.commit()

    elif action == "2":
        cursor = db.cursor()
        Title = input("Enter title of book to update: ")
        variable = input("Enter what would you like to update about the book: id/Title/Author/Qty : ").lower() #what the user would like to update about the book entered by Title

        if variable == "id":
            id = str(input("id: "))
            cursor.execute(''' UPDATE books SET id = ? WHERE Title = ?''', (id, Title))
            db.commit()

        elif variable == "Title":
            Title2 = str(input("Title: "))
            cursor.execute(''' UPDATE books SET Title = ? WHERE Title = ?''', (Title2, Title))
            db.commit()

        elif variable == "Author":
            Author = str(input("Author: "))
            cursor.execute(''' UPDATE books SET Author = ? WHERE Title = ?''', (Author, Title))
            db.commit()

        elif variable == "Qty":
            Qty = int(input("Qty: "))
            cursor.execute(''' UPDATE books SET Quantity = ? WHERE Title = ?''', (Qty, Title))
            db.commit()
            
        else:
            print("Invalid input. Start program again")

    elif action == "3":
        cursor = db.cursor()
        id = int(input("Please enter the ID number of the book you want to delete: "))
        cursor.execute('''DELETE FROM books WHERE id = ?''', [id]) #deletes rows
        db.commit()
        
    elif action == "4":
        cursor = db.cursor()
        searchkey = str(input("Enter Title/Author to search for Title or Author respectively: "))
            
        if searchkey == "Title":
            Title = input("Please enter the title of the book you are looking for : ")
            cursor.execute('''SELECT * from books WHERE Title = ?''', [Title])
            book = cursor.fetchall() #shows all rows given condition
            print(book)
            
        elif searchkey == "Author":
            Author = input("Please enter the name of the author of the book you're looking for:")
            cursor.execute('''SELECT * from books WHERE Author = ?''', [Author])
            book = cursor.fetchall()
            print(book)     

        else:
            print("Invalid input. Start program again. ")

    elif action == "0":
        db.close()