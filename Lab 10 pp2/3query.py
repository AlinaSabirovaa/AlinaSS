import psycopg2

def query_data():
    """Retrieve and print all records from the PhoneBook table."""
    try:
        # Establish connection to the database
        conn = psycopg2.connect(
            database="postgres",
            user="postgres",
            password="simbasimba.18",  # Replace with your password
            host="localhost"
        )
        
        conn.autocommit = True
        cursor = conn.cursor()
        
        # SQL query to retrieve all records
        cursor.execute("SELECT * FROM PhoneBook")
        
        # Fetch all rows
        phonebook_data = cursor.fetchall()
        
        # Print the records
        print("PhoneBook records:")
        for row in phonebook_data:
            print(row)
        
    except (psycopg2.DatabaseError, Exception) as error:
        print("Error:", error)
    finally:
        # Close the connection
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    query_data()
