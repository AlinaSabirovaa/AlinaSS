import psycopg2

def insert_multiple_data():
    """Insert multiple records into the PhoneBook table."""
    # Define the updated records to be inserted
    records = [
        ('Bill', 'Kil', '87774422455'),
        ('Nanny', 'Kil', '87774422458'),
        ('Simba', 'Mufasa', '87774422453'),
        ('Sheikhof', 'Dubai', '87774422451')
    ]

    # SQL query for insertion
    insert_query = """
        INSERT INTO PhoneBook (first_name, last_name, phone_num) 
        VALUES (%s, %s, %s)
    """

    try:
        # Establish connection
        conn = psycopg2.connect(
            database="postgres",
            user="postgres",
            password="simbasimba.18",  # Replace with your password
            host="localhost"
        )
        cursor = conn.cursor()

        # Execute the insert query for each record
        cursor.executemany(insert_query, records)

        # Commit the changes
        conn.commit()
        print("Multiple records inserted successfully!")

    except (psycopg2.DatabaseError, Exception) as error:
        print("Error:", error)

    finally:
        cursor.close()
        conn.close()

# Call the function to insert multiple records
insert_multiple_data()
