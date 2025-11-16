class CLI:
    def __init__(self, manager):
        self.manager = manager

    def menu(self):
        while True:
            print(" Select an option. ")
            print("1. Add a book.")
            print("2. Delete a book.")
            print("3. Borrow a book.")
            print("4. Return a book.")
            print("5. Search a book.")
            print("6. List the books.")
            print("0. Exit")

            option = int(input())

            if option == 1:
                title = input("Title: ")
                author = input("Author: ")
                year = input("Year: ")
                self.manager.add_book(title, author, year)