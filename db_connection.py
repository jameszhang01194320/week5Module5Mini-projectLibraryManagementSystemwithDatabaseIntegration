import mysql.connector # importing mysql conenctor library that we  pip installed
from mysql.connector import Error # importing MySQL Error package to deal with specific errors

# CRUD operations
# Create
# Retrieve
# Update
# Delete

def create_connection():
    # To establish connection to our database we need some parameters first
    db_name = "lms"
    user = "root" # selecting which user
    password = "8832"
    host = "127.0.0.1" # localhost == 127.0.0.1

    # Establish our connection
    try:
        connection = mysql.connector.connect(
            database = db_name,
            user = user,
            password = password,
            host = host
        )

        if connection.is_connected():
            print("Connected to MySQL database successful!")
            return connection

        
    except Error as e:
        print(f"Error: {e}")
        return None