#----------------- LIBRARY MANAGEMENT SYSTEM ----------------

# Create a library class
# Method :
        # Display all books
        # Customer lend books(name who lend the book if not present)
        # someone donate Book
        # return book customer
# Disctionary(book - name of person)
# Create a main function and run a infinite while loop for their input



class Library :
    def __init__(self, list, name) -> None:
        self.bookslist = list
        self.name = name
        self.lendDict = {}     # It is an null dictionary to add lender book

    # Method to display book to the user
    def displayBook(self) :
        print(f"we have following books in our library {self.name}")      # 'self.name' will print library name
        for book in self.bookslist :
            print(book)

    def lendBook(self, user, book) :
        if book not in self.lendDict.keys() :
            self.lendDict.update({book : user})          # If that book is not in lenddict then book has given to user
            print("Lender-book database has been updated. You can take the book now")
        else :
            print(f"Book is already beign used by {self.lendDict[book]}")    # If book is in lenddict then this
                                                                            # will print user name who own the book

    def addBook(self, book) :
        self.bookslist.append(book)    # This will add if someone donates book
        print("Book has been added to the list")
    
    def returnBook(self, book) :
        self.lendDict.pop(book)  # Who want to return book, His/Her name will remove from booklist

if __name__=='__main__' :
    kushal = Library(['Python', 'Rich Dad Poor Dad' ,'Psycology of money', 'java', 'c++'], "CodeWithKushal" )

    while (True) :
        print(f"Welcome to the{kushal.name} library . Enter your choice to continue")
        print("1. Display book")
        print("2. Lend a book")
        print("3. Add a book")
        print("4. Return a book")
        # user_choice = int(input())
        user_choice = input()       # Infinite loop for choices

        if user_choice not in ['1', '2', '3', '4'] :  # If user give wrong input, give him chance for right input
            print("Please enter a valid choice")
            continue

        else :
            user_choice = int(user_choice)

        if user_choice == 1 :
            kushal.displayBook()

        elif user_choice == 2 :
            book = input("Enter the name of the you want to lend\n")
            user = input("Enter your name\n")
            kushal.lendBook(user, book)

        elif user_choice == 3 :
            book = input("Enter the book you want to add\n")
            kushal.addBook(book)

        elif user_choice == 4 :
            book = input("Enter the book you want to return\n")
            kushal.returnBook(book)

        else :
            print("Not a valid option")

        
        print("Press q to quit and c to continue")
        user_choice2 = ""
        while(user_choice2 != "q" and user_choice2 != "c") :  # Give infinite chance to input valid
            user_choice2 = input()

            if user_choice2 == "q" :
                exit()

            elif user_choice2 == "c" :
                continue
            
            else :
                print("Invalid choice")