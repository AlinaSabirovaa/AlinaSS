import psycopg2

def query_data():
    """Query data from the phonebook table."""
    name = input("Enter first name to search: ")
    
    # Establish connection to the database
    conn = psycopg2.connect(
        database="postgres",
        user="postgres",
        password="simbasimba.18",  # Replace with your password
        host="localhost"
    )
    cursor = conn.cursor()
    
    # Query the phonebook with the provided first name
    cursor.execute("SELECT * FROM phonebook WHERE first_name = %s", (name,))
    results = cursor.fetchall()
    
    if results:
        for row in results:
            print(row)
    else:
        print(f"No records found for {name}")
    
    cursor.close()
    conn.close()

if __name__ == "__main__":
    query_data()
