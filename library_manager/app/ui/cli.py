GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

def format_book_line(i, book):
    status_color = GREEN if not book.is_borrowed else RED
    status_text = "Available" if not book.is_borrowed else "Borrowed"
    return f"{i}.{book.title} | {book.author} | {book.year} | {status_color}{status_text}{RESET}"

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

            option = input()

            if option == "1":
                title = input("Title: ")
                author = input("Author: ")
                try:
                    year = int(input("Year: "))
                except ValueError:
                    print("Invalid year! Must be a number.")
                    continue

                result = self.manager.add_book(title, author, year)
                print(result)

            elif option == "2":
                title = input("Title: ")
                self.manager.delete_book(title)

            elif option == "3":
                title = input("Title: ")
                print(self.manager.borrow_book(title))

            elif option == "4":
                title = input("Title: ")
                print(self.manager.return_book(title))

            elif option == "5":
                search_input = input("Search the title or the author: ")
                searched_books = self.manager.search_books(search_input)

                i = 1
                for s in searched_books:
                    print(f"{i}. {s.__str__()}")
                    i += 1

            elif option == "6":
                print("How do you want to sort the list?")
                status = input("1.Title\n2.Author\n3.Year\n4.Borrowed status\n")

                sorted_result = self.manager.list_books(status)
                final_result = ""

                for i, book in enumerate(sorted_result, 1):
                    final_result += format_book_line(i, book) + "\n"

            elif option == "0":
                break
            else:
                print("Invalid input!")