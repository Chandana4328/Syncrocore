BOOK_TITLES=[]
NAME_OF_THE_AUTHORS=[]
BOOK_AVALIABILITY=[]
print("The Library Database ")
number_of_books=int(input("Enter the number of books:"))
for i in range(number_of_books):
    titles=input("Enter the name of the book->")
    author=input("Enter the name of the author->")
    status=input("Enter the status->")
    BOOK_TITLES.append(titles)
    NAME_OF_THE_AUTHORS.append(author)
    BOOK_AVALIABILITY.append(status)
print(BOOK_TITLES)
print(NAME_OF_THE_AUTHORS)
print(BOOK_AVALIABILITY)
print("Displaying the list of Book Details->")
for i in range(len(BOOK_TITLES)):
    print(f"{BOOK_TITLES[i]},{NAME_OF_THE_AUTHORS[i]},{BOOK_AVALIABILITY[i]}")
print("Enter the TITLE to search by LIBRARIAN-->")
titles=input("Enter the title:")
index=BOOK_TITLES.index(titles)
if titles in BOOK_TITLES:
    index = BOOK_TITLES.index(titles)
    status = BOOK_AVALIABILITY[index]
    print(f"The book '{titles}' is {status}")
else:
    print("Book not found in the database")
print()
Converted_list=[]
for i in BOOK_TITLES:
    Converted_list.append(i.upper())
print("DISPALYING THE UPPER_CASE LIST OF THE BOOKS->",Converted_list)
count=0
for i in BOOK_AVALIABILITY:
    if i=="available":
        count=count+1
        print(i)
print("THE TOTAL NUMBER OF BOOK AVAILABlE ARE:->",count)
print()
'''
new_bookname=[]
for i in BOOK_TITLES:
    if new_bookname not in BOOK_TITLES:
        print("enter the name of the book")
        book_name=input()
        new_bookname.append(book_name)
    else:
        print("book is already avaibale")
print(new_bookname)'''