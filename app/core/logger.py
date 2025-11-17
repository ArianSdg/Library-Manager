from datetime import datetime


LOG_FILE = 'logs/activity.log'

def log_activity(action, book, message=""):
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%h %H-%M-%S")

    book_info = f"'{book.title}' by {book.author} {book.year}" if book else "N/A"

    if action == "ADD":
        log_message = f"[{timestamp}] ADD BOOK: {book_info} - {message}"
    elif action == "REMOVE":
        log_message = f"[{timestamp}] REMOVE BOOK: {book_info} - {message}"
    elif action == "BORROW":
        log_message = f"[{timestamp}] BORROW BOOK: {book_info} - {message}"
    elif action == "RETURN":
        log_message = f"[{timestamp}] RETURN BOOK: {book_info} - {message}"
    else:
        log_message = f"[{timestamp}] {action}: {message}"

    with open(LOG_FILE, "a") as f:
        f.write(log_message + "\n")