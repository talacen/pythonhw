import sqlite3

# Connect to SQLite database
conn = sqlite3.connect("roster.db")
cursor = conn.cursor()

# 1. Create the Roster table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Roster (
    Name TEXT,
    Species TEXT,
    Age INTEGER
);
""")

# 2. Populate the table with initial values
initial_data = [
    ("Benjamin Sisko", "Human", 40),
    ("Jadzia Dax", "Trill", 300),
    ("Kira Nerys", "Bajoran", 29)
]
cursor.executemany("INSERT INTO Roster (Name, Species, Age) VALUES (?, ?, ?);", initial_data)
conn.commit()

# 3. Update the name of Jadzia Dax to Ezri Dax
cursor.execute("UPDATE Roster SET Name = 'Ezri Dax' WHERE Name = 'Jadzia Dax';")
conn.commit()

# 4. Display the Name and Age of everyone classified as Bajoran
cursor.execute("SELECT Name, Age FROM Roster WHERE Species = 'Bajoran';")
bajorans = cursor.fetchall()
print("Bajoran Individuals:")
for name, age in bajorans:
    print(f"Name: {name}, Age: {age}")

# Close the connection
conn.close()
