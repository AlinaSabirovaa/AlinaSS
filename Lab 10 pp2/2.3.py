import psycopg2

def delete_data():
    """Delete data from the phonebook by first name or phone number."""
    identifier = input("Enter first name or phone number to delete: ")
    
    # Establish connection to the database
    conn = psycopg2.connect(
        database="postgres",
        user="postgres",
        password="simbasimba.18",  # Replace with your password
        host="localhost"
    )
    cursor = conn.cursor()
    
    # Check if identifier is a phone number or name
    if identifier.isdigit():
        cursor.execute("DELETE FROM phonebook WHERE phone_num = %s", (identifier,))
    else:
        cursor.execute("DELETE FROM phonebook WHERE first_name = %s", (identifier,))
    
    conn.commit()
    print("Data deleted successfully!")
    
    cursor.close()
    conn.close()

if __name__ == "__main__":
    delete_data()
