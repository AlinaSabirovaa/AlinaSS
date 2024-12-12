import psycopg2 as pgsql

connection = pgsql.connect(
    host="localhost", dbname="postgres", user="postgres", password="simbasimba.18", port=5432
)
cur = connection.cursor()

# 1 - task: Create pattern for search
def createpattern():
    query = "SELECT * FROM phonebook WHERE "
    print("Do you want to search by first_name(0)/last_name(1)/break(any num) enter the number:")
    mode = int(input())
    if mode == 0:
        query += "last_name"
        print("Enter string")
        substr = input()
        print("""
            1-last_name is equal to string
            2-last_name starts with the string
            3-last_name ends with the string
            4-last_name contains the string
        """)
        mode1 = int(input())
        if mode1 == 1:
            query += f" = '{substr}'"
        elif mode1 == 2:
            query += f" ILIKE '{substr}%'"
        elif mode1 == 3:
            query += f" ILIKE '%{substr}'"
        else:
            query += f" ILIKE '%{substr}%'"
    elif mode == 1:
        query += "first_name"
        print("Enter string")
        substr = input()
        print("""
            1-first_name is equal to string
            2-first_name starts with the string
            3-first_name ends with the string
            4-first_name contains the string
        """)
        mode1 = int(input())
        if mode1 == 1:
            query += f" = '{substr}'"
        elif mode1 == 2:
            query += f" ILIKE '{substr}%'"
        elif mode1 == 3:
            query += f" ILIKE '%{substr}'"
        else:
            query += f" ILIKE '%{substr}%'"
    else:
        return "error"
    return query

# 2 - task: Insert or update a person in the phonebook
def insert(last_name, first_name, phone_num):
    try:
        cur.execute("SELECT count(*) FROM phonebook WHERE last_name = %s AND first_name = %s", (last_name, first_name))
        if cur.fetchone()[0] == 0:
            cur.execute("INSERT INTO phonebook (last_name, first_name, phone_num) VALUES (%s, %s, %s)", 
                        (last_name, first_name, phone_num))
        else:
            # Check if the phone number already exists before updating
            cur.execute("SELECT count(*) FROM phonebook WHERE phone_num = %s", (phone_num,))
            if cur.fetchone()[0] > 0:
                print(f"❌ Error: Phone number {phone_num} already exists for another contact.")
            else:
                cur.execute("UPDATE phonebook SET phone_num = %s WHERE last_name = %s AND first_name = %s", 
                            (phone_num, last_name, first_name))
        connection.commit()  # Commit after insert/update
    except Exception as e:
        print(f"❌ Error inserting data: {e}")
        connection.rollback()  # Rollback on error


# 3 - task: Loop to insert persons and check for correct input
def loopinsert():
    banned = []
    while True:
        print("Want to enter a person's data? yes/no")
        mode = input().strip().lower()
        if mode == "no":
            break
        person = input("Enter last name, first name, and phone number separated by spaces: ").split()

        # Check if person list has 3 elements
        if len(person) != 3:
            banned.append(person)
            print("❌ Incorrect format. Expected format: LastName FirstName PhoneNumber")
            continue
        
        # Check if the phone number is a valid number
        if not person[2].isdigit():
            banned.append(person)
            print("❌ Phone number should be numeric.")
            continue
        
        insert(*person)
    
    if banned:
        print("🚫 These entries were not added due to incorrect format:")
        for entry in banned:
            print(entry)

# 4 - task: Pagination query with optional offset and limit
def pagination():
    query = createpattern()
    if query == "error":
        return "error"
    
    print("Need offset? yes/no:")
    mode = input().strip().lower()
    if mode == "yes":
        print("Enter offset:")
        offset = int(input())
        query += f" OFFSET {offset}"
    
    print("Need limit? yes/no:")
    mode = input().strip().lower()
    if mode == "yes":
        print("Enter limit:")
        limit = int(input())
        query += f" LIMIT {limit}"
    
    query += ";"
    return query

# 5 - task: Delete entry from the phonebook
def delete():
    query = "DELETE FROM phonebook WHERE "
    cur.execute("SELECT * FROM phonebook")
    print(cur.fetchall())
    print("Do you want to delete by last_name(0)/first_name(1)/phone_num(2)? Enter the number:")
    mode = int(input())
    if mode == 0:
        print("Enter last_name to delete:")
        last_name = input()
        query += f"last_name = '{last_name}'"
    elif mode == 1:
        print("Enter first_name to delete:")
        first_name = input()
        query += f"first_name = '{first_name}'"
    else:
        print("Enter phone_num to delete:")
        phone_num = input()
        query += f"phone_num = {phone_num}"
    
    cur.execute(query)

# Main logic
s1 = createpattern()
if s1 != "error":
    cur.execute(s1 + ";")
    print(cur.fetchall())
insert("Li", "Sabi", 8787)
loopinsert()
s1 = pagination()
if s1 != "error":
    cur.execute(s1 + ";")
    print(cur.fetchall())
delete()

# Commit changes and close connection
connection.commit()
cur.close()
connection.close()
