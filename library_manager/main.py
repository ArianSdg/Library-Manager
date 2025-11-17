from ui.cli import CLI
from core.manager import LibraryManager
from core.storage import Storage

storage = Storage('data/books.json')
manager = LibraryManager(storage)
cli = CLI(manager)

cli.menu()