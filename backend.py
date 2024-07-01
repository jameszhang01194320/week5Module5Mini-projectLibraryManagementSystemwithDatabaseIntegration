import mysql.connector
from mysql.connector import Error
import re
import error_handling

def create_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='lms',
            user='root',
            password='8832'
        )
        if connection.is_connected():
            return connection
    except Error as e:
        error_handling.handle_database_error(e)
        return None

# Input validation functions
def validate_name(name):
    if re.match("^[A-Za-z0-9\s]+$", name):
        return True
    else:
        error_handling.handle_input_error("Invalid name. Please enter a valid name containing only letters, numbers, and spaces.")
        return False

def validate_email(email):
    if re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email):
        return True
    else:
        error_handling.handle_input_error("Invalid email. Please enter a valid email address.")
        return False

def validate_title(title):
    if re.match("^[A-Za-z0-9\s\.\,\!\?\-]+$", title):
        return True
    else:
        error_handling.handle_input_error("Invalid title. Please enter a title containing only letters, numbers, and basic punctuation.")
        return False
def user_exists(user_id):
    try:
        connection = create_connection()
        if connection:
            cursor = connection.cursor()
            cursor.execute("SELECT id FROM users WHERE id = %s", (user_id,))
            result = cursor.fetchone()
            cursor.close()
            return result is not None
    except Error as e:
        error_handling.handle_database_error(e)
    finally:
        if connection:
            connection.close()
    return False

def book_exists(book_id):
    try:
        connection = create_connection()
        if connection:
            cursor = connection.cursor()
            cursor.execute("SELECT id FROM books WHERE id = %s", (book_id,))
            result = cursor.fetchone()
            cursor.close()
            return result is not None
    except Error as e:
        error_handling.handle_database_error(e)
    finally:
        if connection:
            connection.close()
    return False



# Book Operations
def add_book(title):
    connection = create_connection()
    if connection is None:
        return

    cursor = connection.cursor()
    try:
        cursor.execute("INSERT INTO books (title) VALUES (%s)", (title,))
        connection.commit()
        print("Book added successfully!")
    except Error as e:
        error_handling.handle_database_error(e)
    except Exception as e:
        error_handling.handle_generic_error(e)
    finally:
        cursor.close()
        connection.close()

def borrow_book(user_id, book_id):
    connection = create_connection()
    if connection is None:
        return

    cursor = connection.cursor()
    try:
        cursor.execute("SELECT availability FROM books WHERE id = %s", (book_id,))
        result = cursor.fetchone()
        
        if result is None:
            print("Book not found.")
        else:
            availability = result[0]
            if availability:
                cursor.execute("INSERT INTO borrowed_books (user_id, book_id, borrow_date) VALUES (%s, %s, CURDATE())", (user_id, book_id))
                cursor.execute("UPDATE books SET availability = 0 WHERE id = %s", (book_id,))
                connection.commit()
                print("Book borrowed successfully!")
            else:
                print("Book is not available.")
    except Error as e:
        error_handling.handle_database_error(e)
    except Exception as e:
        error_handling.handle_generic_error(e)
    finally:
        cursor.close()
        connection.close()

def return_book(user_id, book_id):
    if not user_exists(user_id):
        error_handling.handle_input_error(f"User ID {user_id} does not exist.")
        return
    if not book_exists(book_id):
        error_handling.handle_input_error(f"Book ID {book_id} does not exist.")
        return
    connection = create_connection()
    if connection is None:
        return

    cursor = connection.cursor()
    try:
        cursor.execute("UPDATE borrowed_books SET return_date = CURDATE() WHERE user_id = %s AND book_id = %s AND return_date IS NULL", (user_id, book_id))
        cursor.execute("UPDATE books SET availability = 1 WHERE id = %s", (book_id,))
        connection.commit()
        print("Book returned successfully!")
    except Error as e:
        error_handling.handle_database_error(e)
    except Exception as e:
        error_handling.handle_generic_error(e)
    finally:
        cursor.close()
        connection.close()

def search_book(title):
    connection = create_connection()
    if connection is None:
        return

    cursor = connection.cursor()
    try:
        cursor.execute("SELECT * FROM books WHERE title LIKE %s", ('%' + title + '%',))
        books = cursor.fetchall()
        if books:
            for book in books:
                print(book)
        else:
            print("No books found.")
    except Error as e:
        error_handling.handle_database_error(e)
    except Exception as e:
        error_handling.handle_generic_error(e)
    finally:
        cursor.close()
        connection.close()

def display_all_books():
    connection = create_connection()
    if connection is None:
        return

    cursor = connection.cursor()
    try:
        cursor.execute("SELECT * FROM books")
        books = cursor.fetchall()
        if not books:
            print("No books found in the library.")
        else:
            for book in books:
                print(book)
    except Error as e:
        error_handling.handle_database_error(e)
    except Exception as e:
        error_handling.handle_generic_error(e)
    finally:
        cursor.close()
        connection.close()

# User Operations
def add_user(name, email):
    try:
        connection = create_connection()
        if connection.is_connected():
            cursor = connection.cursor()

            # Check if user with the same email exists
            cursor.execute("SELECT id FROM users WHERE email = %s", (email,))
            existing_user = cursor.fetchone()
            if existing_user:
                print(f"User with email '{email}' already exists.")
            else:
                # Insert new user
                insert_query = "INSERT INTO users (name, email) VALUES (%s, %s)"
                user_data = (name, email)
                cursor.execute(insert_query, user_data)
                connection.commit()
                print("User added successfully!")

            cursor.close()
            connection.close()

    except Error as e:
        if e.errno == 1062:
            print(f"Database Error: Duplicate entry '{email}' for key 'users.email'")
        else:
            error_handling.handle_database_error(e)
    except Exception as e:
        error_handling.handle_generic_error(e)

def view_user_details(user_id):
    try:
        connection = create_connection()
        if connection:
            cursor = connection.cursor()

            # Retrieve user details
            cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
            user = cursor.fetchone()

            if user:
                print(f"User ID: {user[0]}, Name: {user[1]}, Email: {user[2]}")
            else:
                print(f"User with ID '{user_id}' not found.")

            cursor.close()
            connection.close()

    except Error as e:
        print(f"Database Error: {e}")
    except Exception as e:
        print(f"Error: {e}")


def display_all_users():
    connection = create_connection()
    if connection is None:
        return

    cursor = connection.cursor()
    try:
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
        if not users:
            print("No users found.")
        else:
            for user in users:
                print(user)
    except Error as e:
        error_handling.handle_database_error(e)
    except Exception as e:
        error_handling.handle_generic_error(e)
    finally:
        cursor.close()
        connection.close()
