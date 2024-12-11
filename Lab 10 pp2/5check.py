import psycopg2

def fetch_data():
    """Fetch and print all data from the PhoneBook table."""
    
   
    conn = psycopg2.connect(
        database="postgres",
        user="postgres",
        password="simbasimba.18", 
        host="localhost"
    )
    cursor = conn.cursor()
    
    # Query the PhoneBook table
    cursor.execute("SELECT * FROM phonebook")
    
    # Fetch all rows and print them
    phonebook_data = cursor.fetchall()
    for row in phonebook_data:
        print(row)
    
    # Close connection
    cursor.close()
    conn.close()

if __name__ == "__main__":
    fetch_data()
