import psycopg2 


conn = psycopg2.connect(
    database="postgres",
    user="postgres",
    password="simbasimba.18",  
    host="localhost"
)

conn.autocommit = True
cursor = conn.cursor()

# Create PhoneBook table
sql = '''
CREATE TABLE IF NOT EXISTS PhoneBook (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255),
    phone_num VARCHAR(15) NOT NULL UNIQUE
)
'''

cursor.execute(sql)
print("PhoneBook table created successfully!")

# Close the connection
conn.close()
