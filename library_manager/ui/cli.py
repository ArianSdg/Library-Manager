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
            elif option == 2:
                title = input("Title: ")
                self.manager.delete_book(title)
            elif option == 3:
                title = input("Title: ")
                self.manager.borrow_book(title)
            elif option == 4:
                title = input("Title: ")
                self.manager.return_book(title)
            elif option == 5:
                search_input = input("Search the title or the author: ")
                self.manager.search_books(search_input)
            elif option == 6:
                books_list = self.manager.list_books()
                print(books_list)
            elif option == 0:
                break
            else:
                print("Invalid input!")