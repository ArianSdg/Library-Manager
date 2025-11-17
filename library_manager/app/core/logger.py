from datetime import datetime


LOG_FILE = 'logs/activity.log'

def log_activity(action, book, message=""):
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%h %H-%M-%S")

    if action == "ADD":
        log_message = f"[{timestamp}] ADD BOOK: '{book.title}' by {book.author} {book.year} - {message}"
    elif action == "REMOVE":
        log_message = f"[{timestamp}] REMOVE BOOK: '{book.title}' by {book.author} {book.year} - {message}"
    elif action == "BORROW":
        log_message = f"[{timestamp}] BORROW BOOK: '{book.title}' by {book.author} {book.year} - {message}"
    elif action == "RETURN":
        log_message = f"[{timestamp}] RETURN BOOK: '{book.title}' by {book.author} {book.year} - {message}"
    else:
        log_message = f"[{timestamp}] {action} - {message}"

    with open(LOG_FILE, "a") as f:
        f.write(log_message + "\n")