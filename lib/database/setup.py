from database import conn,cursor

# Enable foreign key constraint enforcement
cursor.execute('PRAGMA foreign_keys = ON;')
def create_tables():

    # Create 'doctors' table if it does not exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS doctors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            gender TEXT,
            date_of_employment TEXT,
            phone_number INTEGER,
            department_id INTEGER,
            FOREIGN KEY (department_id) REFERENCES departments(id) ON DELETE SET NULL
        )
    ''')

    # Create 'patients' table if it does not exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS patients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            date_of_birth TEXT,
            gender TEXT,
            phone_number INTEGER,
            address TEXT
        )
    ''')

    # Create 'departments' table if it does not exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS departments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            location TEXT
        )
    ''')

    # Create 'appointments' table if it does not exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS appointments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            datetime TEXT NOT NULL,
            patient_id INTEGER,
            doctor_id INTEGER,
            FOREIGN KEY (patient_id) REFERENCES patients(id) ON DELETE CASCADE,
            FOREIGN KEY (doctor_id) REFERENCES doctors(id) ON DELETE CASCADE
        )
    ''')

    # Commit the transaction
    conn.commit()