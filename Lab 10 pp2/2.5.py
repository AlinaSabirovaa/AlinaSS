import psycopg2

def insert_user():
    """Insert a new user into the users table."""
    username = input("Enter your username: ")

    try:
        # Connect to the PostgreSQL database
        conn = psycopg2.connect(
            database="postgres",
            user="postgres",
            password="simbasimba.18",  # Replace with your password
            host="localhost"
        )
        cursor = conn.cursor()

        # Insert new user into the users table
        cursor.execute("""
            INSERT INTO users (username) 
            VALUES (%s) 
            RETURNING user_id;
        """, (username,))
        
        # Fetch the inserted user's ID
        user_id = cursor.fetchone()[0]
        conn.commit()
        print(f"User {username} created successfully with ID: {user_id}")
        
    except (psycopg2.DatabaseError, Exception) as error:
        print("Error inserting user:", error)
    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    insert_user()
