import psycopg2

def get_user_level():
    """Get the current level of a user from the database."""
    username = input("Enter your username to check current level: ")

    try:
        # Connect to the PostgreSQL database
        conn = psycopg2.connect(
            database="postgres",
            user="postgres",
            password="simbasimba.18",  # Replace with your password
            host="localhost"
        )
        cursor = conn.cursor()

        # Check if the user exists
        cursor.execute("""
            SELECT u.username, us.level
            FROM users u
            LEFT JOIN user_score us ON u.user_id = us.user_id
            WHERE u.username = %s
            ORDER BY us.time DESC
            LIMIT 1;
        """, (username,))
        
        user_info = cursor.fetchone()

        if user_info:
            print(f"User: {user_info[0]}, Current Level: {user_info[1]}")
        else:
            print("User not found!")

    except (psycopg2.DatabaseError, Exception) as error:
        print("Error fetching user level:", error)
    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    get_user_level()
