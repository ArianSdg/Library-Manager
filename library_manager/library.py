



manager = LibraryManager('data/books.json')
manager.add_book("arian", "arian", "1995")
manager.add_book("amir", "arian", "1995")
manager.add_book("azar", "arian", "1995")
print(manager.delete_book("amir"))
manager.borrow_book("azar")