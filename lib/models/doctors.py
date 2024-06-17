from database.setup import conn
#Doctor class
cursor = conn.cursor()
class Doctor:
    all = {}
    def __init__(self,name,gender,date_of_employment,phone_number,department_id,id=None):
        self.name = name  # Initializing the doctor's name
        self.date_of_employment = date_of_employment  # Initializing the doctor's employment date
        self.gender = gender  # Initializing the doctor's gender
        self.phone_number = phone_number  # Initializing the doctor's phone number
        self.department_id = department_id  # Initializing the doctor's department ID
        self.id = id  # Initializing the doctor's ID (default is None)

    def __repr__(self):
        return f"<Doctor {self.id}: {self.name}>"  # String representation of the doctor object

    @property
    def name(self):
        return self._name  # Getting the doctor's name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and not hasattr(self, "_name") and len(value):
            self._name = value  # Setting the doctor's name if valid
        else:
            raise ValueError("Invalid name")  # Raising error if the name is invalid

    @property
    def gender(self):
        return self._gender  # Getting the doctor's gender

    @gender.setter
    def gender(self, value):
        if len(value) == 1 and isinstance(value, str):
            self._gender = value  # Setting the doctor's gender if valid
        else:
            raise ValueError("Invalid gender")  # Raising error if the gender is invalid

    @property
    def department_id(self):
        return self._department_id  # Getting the doctor's department ID

    @department_id.setter
    def department_id(self, value):
        # Checking if the department ID exists in the database
        sql = "SELECT id FROM departments WHERE id = ?"
        if cursor.execute(sql, (value,)).fetchone():
            self._department_id = value  # Setting the department ID if valid
        else:
            raise ValueError("Invalid department_id")  # Raising error if the department ID is invalid

    def save(self):
        # Inserting the doctor's details into the database
        sql = """INSERT INTO doctors (name,gender,date_of_employment,phone_number,department_id) VALUES (?,?,?,?,?)"""
        cursor.execute(sql, (self.name, self.gender, self.date_of_employment, self.phone_number, self.department_id))
        conn.commit()
        self.id = cursor.lastrowid  # Updating the doctor's ID
        type(self).all[self.id] = self  # Storing the doctor object in the class-level dictionary

    @classmethod
    def create(cls, name, gender, date_of_employment, phone_number, department_id):
        doctor = cls(name, gender, date_of_employment, phone_number, department_id)  # Creating a new doctor instance
        doctor.save()  # Saving the doctor instance to the database
        return doctor  # Returning the created doctor instance

    @classmethod
    def instance_from_db(cls, row):
        doctor = cls.all.get(row[0])  # Fetching the doctor instance from the class-level dictionary
        if doctor:
            doctor.gender = row[2]  # Updating the doctor's gender
            doctor.date_of_employment = row[3]  # Updating the employment date
            doctor.phone_number = row[4]  # Updating the phone number
            doctor.department_id = row[5]  # Updating the department ID
        else:
            doctor = cls(row[1], row[2], row[3], row[4], row[5])  # Creating a new doctor instance
            doctor.id = row[0]  # Setting the doctor's ID
            cls.all[doctor.id] = doctor  # Storing the doctor instance in the class-level dictionary
        return doctor  # Returning the doctor instance

    def update(self, field, value):
        if field == "department_id":
            # Checking if the department ID exists in the database
            sql = "SELECT id FROM departments WHERE id = ?"
            if not cursor.execute(sql, (value,)).fetchone():
                raise ValueError("Invalid department_id")  # Raising error if the department ID is invalid
        sql = f"UPDATE doctors SET {field} = ? WHERE id = ?"  # Preparing the SQL query to update the doctor's details
        cursor.execute(sql, (value, self.id))
        conn.commit()
        setattr(self, field, value)  # Update the attribute in the instance

    def delete(self):
        # Deleting the doctor from the database
        sql = "DELETE FROM doctors WHERE id = ?"
        cursor.execute(sql, (self.id,))
        conn.commit()
        del type(self).all[self.id]  # Removing the doctor from the class-level dictionary

    @classmethod
    def find_by_id(cls, id):
        # Fetching the doctor from the database by ID
        sql = "SELECT * FROM doctors WHERE id = ?"
        row = cursor.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None  # Returning the doctor instance or None

    @classmethod
    def get_all_doctors(cls):
        # Fetching all doctors from the database
        sql = "SELECT * FROM doctors"
        rows = cursor.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]  # Returning a list of doctor instances

    def get_patients(self):
        from models.patients import Patient
        # Fetching the doctor's patients from the database
        sql = "SELECT DISTINCT patients.* FROM patients INNER JOIN appointments ON patients.id = appointments.patient_id WHERE appointments.doctor_id = ?"
        rows = cursor.execute(sql, (self.id,)).fetchall()
        return [Patient.instance_from_db(row) for row in rows]  # Returning a list of patient instances

    def doc_appointments(self):
        from models.appointments import Appointment
        # Fetching the doctor's appointments from the database
        sql = "SELECT * FROM appointments WHERE doctor_id = ?"
        rows = cursor.execute(sql, (self.id,)).fetchall()
        return [Appointment.instance_from_db(row) for row in rows]  # Returning a list of appointment instances