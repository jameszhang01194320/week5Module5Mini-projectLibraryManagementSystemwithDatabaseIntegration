Module 5: Mini-project | Library Management System with Database Integration

Create User Interface (UI) and Menu
****
Main Menu:
1. Book Operations
2. User Operations
3. Quit
 Book Operations:
Book Operations:
1. Add a new book 
2. Borrow a book 
3. Return a book
4. Search for a book
5. Display all books
 User Operations:
User Operations:
1. Add a new user
2. View user details
3. Display all users


Use MySQL create DATABASE lms(Library Managemnet System)

Create the database tables for the Library Management System.

Books Table:

CREATE TABLE books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    availability BOOLEAN DEFAULT 1
);
(For the BOOLEAN data type, the values can be  0 for False or 1 for True)

Users Table:

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(250) NOT NULL UNIQUE
);

Borrowed Books Table:

CREATE TABLE borrowed_books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    book_id INT NOT NULL,
    borrow_date DATE NOT NULL,
    return_date DATE,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (book_id) REFERENCES books(id)
);

Database Connection:

create_connection():
    # To establish connection to our database we need some parameters first
    db_name = "lms"
    user = "root" # selecting which user
    password = "8832"
    host = "127.0.0.1" # localhost == 127.0.0.1

Create functions for adding new books, and users to the database.
Implement functions for borrowing books
Implement functions for returning books

Develop functions for searching books by title.
Define functions for displaying all books, all users.
Implement functions for user registration and viewing user details.
User Interface Functions:

Create a user-friendly command-line interface (CLI) with clear menu options.
Implement functions to handle user interactions using the input() function.
Validate user input using regular expressions (regex) to ensure proper formatting.
Error Handling:

Use try, except, else, and finally blocks to manage errors gracefully.
Handle exceptions related to database operations, input validation, and other potential issues.
Provide informative error messages to guide users.
Clean Code Principles:

Use meaningful variable and function names that convey their purpose.
Write clear comments and docstrings to explain the functionality of functions and classes.
Follow PEP 8 style guidelines for code formatting and structure.
Ensure proper indentation and spacing for readability.
Modular Design:

Organize code into separate modules to promote modularity and maintainability.
Create distinct modules for database operations, user interactions, error handling, and core functionalities.
