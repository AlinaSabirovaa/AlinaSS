import psycopg2

def create_tables():
    try:
        # Connect to the PostgreSQL database
        conn = psycopg2.connect(
            database="postgres",
            user="postgres",
            password="simbasimba.18",  # Replace with your password
            host="localhost"
        )
        cursor = conn.cursor()
        
        # Create the users table (username storage)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                user_id SERIAL PRIMARY KEY,
                username VARCHAR(50) UNIQUE NOT NULL
            );
        """)
        
        # Create the user_score table (score storage)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS user_score (
                score_id SERIAL PRIMARY KEY,
                user_id INT REFERENCES users(user_id),
                level INT NOT NULL,
                score INT NOT NULL,
                time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """)
        
        # Commit changes and close the connection
        conn.commit()
        print("Tables created successfully!")
    except (psycopg2.DatabaseError, Exception) as error:
        print("Error creating tables:", error)
    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    create_tables()
