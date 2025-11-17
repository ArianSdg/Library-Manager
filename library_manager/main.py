from app.ui.cli import CLI
from app.core.library_service import LibraryManager
from app.storage.file_storage import Storage

storage = Storage('data/books.json')
manager = LibraryManager(storage)
cli = CLI(manager)

cli.menu()