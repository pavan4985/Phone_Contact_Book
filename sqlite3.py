import sqlite3
# Connect to SQLite database (or create it if it doesn't exist)
connect= sqlite3.connect('contact_book.db')
cursor= connect.cursor()

# Create table
cursor.execute('''
    CREATE TABLE contacts
    (ID INTEGER PRIMARY KEY,
    Name TEXT,
    Cell TEXT,
    Email TEXT)
''')
# Insert 5 rows of data
data= [
    (1, 'Chandu', '8644195865', 'chanduk@gmail.com'),
    (2, 'Mithun', '0987654321', 'mithun@gmail.com'),
    (3, 'vinay','8654255485','vinay@gmail.com'),
    (4, 'Pavan', '9620634188', 'pavan@gmail.com'),
    (5, 'Rahul', '9966355486', 'rahul@gmail.com'),
]
cursor.executemany('INSERT INTO contacts VALUES (?,?,?,?)', data)
# Commit the changes
connect.commit()
# Fetch all data
cursor.execute('SELECT * FROM contacts')
# Display all data
rows = cursor.fetchall()

print("ID\tName\t\tCell#\t\t\tEmail")
print("-" * 50)
for row in rows:
    print(f"{row[0]}\t{row[1]}\t\t{row[2]}\t\t{row[3]}")

# Close the connection
connect.close()