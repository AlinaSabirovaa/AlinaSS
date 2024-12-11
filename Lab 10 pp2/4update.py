import psycopg2

def update_data():
    """Update data in the PhoneBook table."""
    
    # These are the existing values to update
    old_first_name = 'Bill'
    old_last_name = 'Kil'
    
    # New values to update the record with
    new_first_name = 'Sydney'
    new_last_name = 'Kim'
    new_phone_num = '87794561223'
    
    # Establish connection to the database
    conn = psycopg2.connect(
        database="postgres",
        user="postgres",
        password="simbasimba.18",  # Replace with your password
        host="localhost"
    )
    cursor = conn.cursor()
    
    # Check if the user exists with the given old first name and last name
    cursor.execute("SELECT * FROM phonebook WHERE first_name = %s AND last_name = %s", (old_first_name, old_last_name))
    user = cursor.fetchone()

    if user:
        # Print the current data for confirmation
        print(f"Current data for {old_first_name} {old_last_name}: {user}")
        
        # Update the user's data
        cursor.execute("""
            UPDATE phonebook 
            SET first_name = %s, last_name = %s, phone_num = %s
            WHERE first_name = %s AND last_name = %s
        """, (new_first_name, new_last_name, new_phone_num, old_first_name, old_last_name))

        # Commit the changes to the database
        conn.commit()
        print(f"User {old_first_name} {old_last_name} updated successfully to {new_first_name} {new_last_name} with phone number {new_phone_num}.")
    else:
        print(f"User {old_first_name} {old_last_name} not found in the PhoneBook.")

    # Close cursor and connection
    cursor.close()
    conn.close()

if __name__ == '__main__':
    update_data()
