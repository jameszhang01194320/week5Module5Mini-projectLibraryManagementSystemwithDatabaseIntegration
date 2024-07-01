import backend
import error_handling

def main_menu():
    while True:
        print("Welcome to the Library Management System with Database Integration!")
        print("Main Menu:")
        print("1. Book Operations")
        print("2. User Operations")
        print("3. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            book_operations()
        elif choice == '2':
            user_operations()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            error_handling.handle_input_error("Invalid choice. Please try again.")

def book_operations():
    while True:
        print("Book Operations:")
        print("1. Add a new book")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. Search for a book")
        print("5. Display all books")
        print("6. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter book title: ")
            if backend.validate_title(title):
                backend.add_book(title)
            else:
                error_handling.handle_input_error("Invalid book title. Please enter a valid title.")
        elif choice == '2':
            user_id = input("Enter your user ID: ")
            book_id = input("Enter book ID: ")
            backend.borrow_book(user_id, book_id)
        elif choice == '3':
            user_id = input("Enter your user ID: ")
            book_id = input("Enter book ID: ")
            backend.return_book(user_id, book_id)
        elif choice == '4':
            title = input("Enter book title to search: ")
            backend.search_book(title)
        elif choice == '5':
            backend.display_all_books()
        elif choice == '6':
            break
        else:
            error_handling.handle_input_error("Invalid choice. Please try again.")

def user_operations():
    while True:
        print("User Operations:")
        print("1. Add a new user")
        print("2. View user details")
        print("3. Display all users")
        print("4. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter user name: ")
            email = input("Enter user email: ")
            if backend.validate_name(name) and backend.validate_email(email):
                backend.add_user(name, email)
            else:
                error_handling.handle_input_error("Invalid user name or email. Please enter valid details.")
        elif choice == '2':
            user_id = input("Enter user ID: ")
            backend.view_user_details(user_id)
        elif choice == '3':
            backend.display_all_users()
        elif choice == '4':
            break
        else:
            error_handling.handle_input_error("Invalid choice. Please try again.")

if __name__ == "__main__":
    try:
        main_menu()
    except Exception as e:
        error_handling.handle_generic_error(e)
