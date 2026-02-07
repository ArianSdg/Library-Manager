GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

def format_book_line(i, book):
    status_color = GREEN if not book.is_borrowed else RED
    status_text = "Available" if not book.is_borrowed else "Borrowed"
    return f"{i}.{book.title} | {book.author} | {book.year} | {status_color}{status_text}{RESET}"

def format_list_results(books):
    result = ""
    for i, book in enumerate(books, 1):
        status_color = GREEN if not book.is_borrowed else RED
        status_text = "Available" if not book.is_borrowed else "Borrowed"
        result += f"{i}. {book.title} | {book.author} | {book.year} | {status_color}{status_text}{RESET}\n"
    return result

def sort_search_results(sort_option, searched_books):
    if sort_option == "1":
        return sorted(searched_books, key=lambda b: b.title.lower())
    elif sort_option == "2":
        return sorted(searched_books, key=lambda b: b.author.lower())
    elif sort_option == "3":
        return sorted(searched_books, key=lambda b: b.year)
    elif sort_option == "4":
        return sorted(searched_books, key=lambda b: b.is_borrowed)

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
                book_id = int(input("Book id: "))
                print(self.manager.delete_book(book_id))

            elif option == "3":
                book_id = int(input("Book id: "))
                print(self.manager.borrow_book(book_id))

            elif option == "4":
                book_id = int(input("Book id: "))
                print(self.manager.return_book(book_id))

            elif option == "5":
                search_input = input("Search the title or the author: ")
                searched_books = self.manager.search_books(search_input)

                sort_option = input("Sort by: 1.Title 2.Author 3.Year 4.Borrowed\n")
                final_result = sort_search_results(sort_option, searched_books)

                print(format_list_results(final_result))

            elif option == "6":
                print("How do you want to sort the list?")
                sort_option = input("1.Title\n2.Author\n3.Year\n4.Borrowed status\n")

                sorted_result = self.manager.list_books(sort_option)
                print(format_list_results(sorted_result))

            elif option == "0":
                break
            else:
                print("Invalid input!")