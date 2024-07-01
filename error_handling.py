from mysql.connector import Error

def handle_database_error(error):
    print(f"Database error occurred: {error}")

def handle_input_error(error_message):
    print(f"Input error: {error_message}")

def handle_generic_error(error_message):
    print(f"An error occurred: {error_message}")