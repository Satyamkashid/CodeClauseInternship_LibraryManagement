# Library Management System in Python using Object Oriented Programming

class Library:
    def __init__(self, book_list, name):
        self.book_list = book_list
        self.name = name
        self.lendDict = {}

    # Function Name : DisplayBooks
    # Description : It will display all the books in library
    # Author Name : Satyam Sanjay Kashid
    # Date : 01/11/2023

    def DisplayBooks(self):
        print(f"We have the following books in the library: {self.name}")
        for book in self.book_list:
            print(book)

    # Function Name : lendBook
    # Description : It will lend the book from library
    # Author Name : Satyam Sanjay Kashid
    # Date : 01/11/2023

    def lendBook(self, user, book):
        if book in self.book_list:
            if book not in self.lendDict:
                self.lendDict[book] = user
                print("Lender-Book Database has been updated. You can take the book now.")
            else:
                print(f"This book is already in use by {self.lendDict[book]}.")
        else:
            print("Book not available in the library.")

    # Function Name : AddBook
    # Description : It will add the given book in library
    # Author Name : Satyam Sanjay Kashid
    # Date : 01/11/2023

    def AddBook(self, book):
        self.book_list.append(book)
        print("The book has been added to the library.")

    # Function Name : returnBook
    # Description : It will return the book
    # Author Name : Satyam Sanjay Kashid
    # Date : 01/11/2023

    def returnBook(self, book):
        if book in self.lendDict:
            self.lendDict.pop(book)
            print("The book has been returned.")
        else:
            print("This book is not currently on loan.")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# 
# Entry point Function
# 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

def main():
    print("-------------------Task By CodeClause----------------------")
    print("-------------------Library Management System---------------")

    book_list = ['Python', 'C++', 'Java', 'Machine Learning', 'Html']
    Satyam = Library(book_list, 'Satyam Library')

    while True:
        print(f"Welcome to the {Satyam.name}. Enter your choice to continue")
        print("1: Display Books")
        print("2: Lend a Book")
        print("3: Add a Book")
        print("4: Return a Book")

        user_choice = input()

        if user_choice not in ['1', '2', '3', '4']:
            print("Invalid input. Please enter a valid choice.")
            continue

        user_choice = int(user_choice)

        if user_choice == 1:
            Satyam.DisplayBooks()

        elif user_choice == 2:
            book = input("Enter the name of the book you want to lend: ")
            user = input("Enter your name: ")
            Satyam.lendBook(user, book)

        elif user_choice == 3:
            book = input("Enter the name of the book you want to add: ")
            Satyam.AddBook(book)

        elif user_choice == 4:
            book = input("Enter the name of the book you want to return: ")
            Satyam.returnBook(book)

        else:
            print("Enter a valid choice.")

        user_choice = input("Press 'q' to quit and 'c' to continue: ")

        if user_choice == 'q':
            exit()
        elif user_choice == 'c':
            continue
        else:
            print("Invalid input. Continuing...")
            continue

if __name__ == "__main__":
    main()
