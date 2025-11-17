# Library Manager

This project is a simple command-line library management system written in Python.  
It allows managing a list of books, searching, sorting, logging actions, and exporting data.

## Features

### Book Management
- Add new books
- Remove existing books
- Borrow and return books
- Prevent adding duplicate book entries

### Search and Filtering
- Search by title, author, or publication year
- Optional filtering by borrowed/available status
- Ability to sort search results

### Sorting Options
Books can be sorted by:
- Title
- Author
- Publication year
- Borrowed status

### Activity Logging
All actions (add, remove, borrow, return) are written to a log file with timestamps and status messages.

### Storage
The application uses JSON as the main storage format.  
On every save, a backup file is created automatically.  
A CSV export feature is also included.

### CSV Export
Books can be exported into a CSV file located in the `data` directory.

## Project Structure


## Running the Application

1. Install Python 3.10 or newer.
2. Clone the repository.
3. Run the program using:


## Future Improvements

- Graphical user interface
- API-based version using FastAPI
- Database storage (SQLite or PostgreSQL)
- Better search with fuzzy matching
- User accounts and loan history tracking

