import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Mawin11@Mayur",
    database="tka"
)
cursor=mydb.cursor()

def addBook(isbn,title,author,quantity,year):
    cursor.execute("insert into books values (%s,%s,%s,%s,%s)",(isbn,title,author,quantity,year))
    mydb.commit()
    print("Book Added Successfully")

def removeBook(isbn):
    cursor.execute("delete from books where isbn=%s",(isbn,))
    print("Book Removed.")
    mydb.commit()

def searchBook(title):
    cursor.execute("select * from books where title like %s",("%"+title+"%",))
    results=cursor.fetchall()
    if not results:
        print("No books found.")
    for result in results:
        print(f"isbn:{result[0]}")
        print(f"title:{result[1]}")
        print(f"author:{result[2]}")
        print(f"quantity:{result[3]}")
        print(f"year published:{result[4]}\n")

def ListBooks():
    cursor.execute("select * from books")
    print(f"\nisbn\ttitle\t\tauthor\t\tquantity\tyear")
    print("-"*70)
    for i in cursor:
        print(f"{i[0]}\t{i[1]}\t{i[2]}\t{i[3]}\t\t{i[4]}")

def updateBook(isbn,title,author,quantity,year):
    cursor.execute("""update books 
                      set title=%s,author=%s,quantity=%s,year=%s 
                      where isbn=%s""",(title,author,quantity,year,isbn))
    mydb.commit()
    print("Book updated successfully")

def addMember(name,email):
    cursor.execute("insert into members(name,email) values(%s,%s)",(name,email))
    mydb.commit()
    print("Member added.")
def removeMember(member_id):
    cursor.execute("delete from members where member_id=%s",(member_id,))
    mydb.commit()
    print("Member removed.")

    
def borrowBook(member_id,isbn):
    cursor.execute("select quantity from books where isbn=%s",(isbn,))
    book=cursor.fetchone()
    if not book:
        print("Book not found.")
        return
    if book[0]<=0:
        print("No copies available to borrow.")
        return
    cursor.execute("insert into borrowed_books(member_id,isbn) values(%s,%s)",(member_id,isbn))
    cursor.execute("update books set quantity=quantity-1 where isbn=%s",(isbn,))
    mydb.commit()
    print("Book borrowed successfully!")

def returnBook(member_id,isbn):
    cursor.execute("select borrow_id from borrowed_books where member_id=%s and isbn=%s limit 1",(member_id,isbn))
    borrow=cursor.fetchone()
    if not borrow:
        print("This member has not borrowed this book.")
        return
    cursor.execute("delete from borrowed_books where borrow_id=%s",(borrow[0],))
    cursor.execute("update books set quantity=quantity+1 where isbn=%s",(isbn,))
    mydb.commit()
    print("Book returned successfully...")

def listBorrowedBooks():
    cursor.execute("""select b.borrow_id,m.name,bk.title,b.borrow_date
                      from borrowed_books b
                      join members m on b.member_id=m.member_id
                      join books bk on b.isbn=bk.isbn""")
    results=cursor.fetchall()
    if not results:
        print("No books are currently borrowed.")
    else:
        print("\nBorrowed Books:")
        print("ID\tMember\t\tBook Title\t\tDate")
        print("-"*70)
        for i in results:
            print(f"{i[0]}\t{i[1]}\t{i[2]}\t\t{i[3]}")

def showMembers():
    cursor.execute("select * from members")
    results=cursor.fetchall()
    if not cursor:
        print("No members found")
    else:
        print("\nMembers List:")
        print("ID\tName\t\tEmail")
        print("-"*50)
        for r in results:
            print(f"{r[0]}\t{r[1]}\t{r[2]}")

def Main():
    while True:
        print("\nLibrary management system-------------.")
        print("|BOOKS TABLE                          |")
        print("|    1.Add Book                       |")
        print("|    2.Remove Book                    |")
        print("|    3.Search Books                   |")
        print("|    4.List All Books                 |")
        print("|    5.Update Book Details            |")
        print("|MEMBERS TABLE                        |")
        print("|    6.Add Member                     |")
        print("|    7.Remove Member                  |")
        print("|    8.Show Members                   |")
        print("|BORROWED BOOKS TABLE                 |")        
        print("|    9.Return Book                    |")
        print("|    10.Borrow Book                   |")
        print("|    11.List Borrowed Books           |")
        print("|12.Exit                              |")
        print("|_____________________________________|\n")
        c=input("Choose option:")
        
        if c=="1":
            isbn=input("ISBN:")
            title=input("Title:")
            author=input("Author:")
            qty=int(input("Quantity:"))
            year=int(input("Year:"))
            addBook(isbn,title,author,qty,year)
        elif c=="2":
            isbn=input("Enter ISBN to remove:")
            removeBook(isbn)
        elif c=="3":
            title=input("Enter title to search:")
            searchBook(title)
        elif c=='4':
            ListBooks()
        elif c=='5':
            isbn=input("ISBN of book to update:")
            title=input("New Title:")
            author=input("New Author:")
            qty=int(input("New Quantity:"))
            year=int(input("New Year:"))
            updateBook(isbn,title,author,qty,year)
   #-----------------------------------------------------------------         
        elif c=="6":
            name=input("Member Name:")
            email=input("Member Email:")
            addMember(name,email)
        elif c=="7":
            mid=int(input("Enter Member ID to remove:"))
            removeMember(mid)
        elif c=="8":
            showMembers()
    #--------------------------------------------------------------        
        elif c=="9":
            mid=int(input("Member ID:"))
            isbn=input("ISBN:")
            returnBook(mid,isbn)
        elif c=="10":
            mid=int(input("Member ID:"))
            isbn=input("ISBN:")
            borrowBook(mid,isbn)            
        elif c=="11":
            listBorrowedBooks()
            
        elif c=='12':
            break
        else:
            print("Incorrect choice...")
    cursor.close()
    mydb.close()
Main()
