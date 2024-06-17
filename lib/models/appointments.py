from database.setup import conn
cursor = conn.cursor()

class Appointment:
    all = {}

    def __init__(self, datetime,patient_id,doctor_id, id=None):
        # Initialize attributes for appointment
        self.datetime = datetime
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.id = id

    def __repr__(self):
        # Representation of the appointment instance
        return f"<Appointment {self.id}: {self.datetime}>"

    def save(self):
        # SQL to insert a new appointment into the database
        sql = """INSERT INTO appointments (datetime, patient_id,doctor_id) VALUES (?, ?,?)"""
        cursor.execute(sql, (self.datetime, self.patient_id,self.doctor_id))
        conn.commit()
        self.id = cursor.lastrowid # Get the id of the newly inserted row
        type(self).all[self.id] = self # Store the appointment in the class dictionary

    @property
    def doctor_id(self):
        return self._doctor_id

    @doctor_id.setter
    def doctor_id(self, value):
        # SQL to check if the doctor exists in the doctors table
        sql = "SELECT id FROM doctors WHERE id = ?"
        if cursor.execute(sql, (value,)).fetchone():
            self._doctor_id = value
        else:
            raise ValueError("Invalid doctor_id")

    @property
    def patient_id(self):
        return self._patient_id

    @patient_id.setter
    def patient_id(self, value):
        # SQL to check if the patient exists in the patients table
        sql = "SELECT id FROM patients WHERE id = ?"
        if cursor.execute(sql, (value,)).fetchone():
            self._patient_id = value
        else:
            raise ValueError("Invalid patient_id")

    @classmethod
    def create(cls, datetime, patient_id,doctor_id):
        # Create a new appointment instance and save it
        appointment = cls(datetime, patient_id,doctor_id)
        appointment.save()
        return appointment

    @classmethod
    def instance_from_db(cls, row):
        # Retrieve the appointment instance from the class dictionary
        appointment = cls.all.get(row[0])
        if appointment:
            appointment.datetime = row[1]
            appointment.patient_id = row[2]
            appointment.doctor_id = row[3]
        else:
            # Create a new appointment instance from the database row
            appointment = cls(row[1], row[2],row[3])
            appointment.id = row[0]
            cls.all[appointment.id] = appointment

        return appointment

    def update(self, field, value):
        # Validate doctor_id or patient_id before updating
        if field == "doctor_id":
            sql = "SELECT id FROM doctors WHERE id = ?"
            if not cursor.execute(sql, (value,)).fetchone():
                raise ValueError("Invalid doctor_id")
        elif field == "patient_id":
            sql = "SELECT id FROM patients WHERE id = ?"
            if not cursor.execute(sql, (value,)).fetchone():
                raise ValueError("Invalid patient_id")

        # SQL to update the appointment field in the database
        sql = f"UPDATE appointments SET {field} = ? WHERE id = ?"
        cursor.execute(sql, (value, self.id))
        conn.commit()
        setattr(self,field,value)

    def delete(self):
        # SQL to delete the appointment from the database
        sql = "DELETE FROM appointments WHERE id = ?"
        cursor.execute(sql, (self.id,))
        conn.commit()
        del type(self).all[self.id] # Remove the appointment from the class dictionary

    @classmethod
    def find_by_id(cls, id):
        # SQL to find an appointment by id
        sql = "SELECT * FROM appointments WHERE id = ?"
        row = cursor.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def get_all_appointments(cls):
        # SQL to get all appointments from the database
        sql = "SELECT * FROM appointments"
        rows = cursor.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    def apt_doctor(self):
        from models.doctors import Doctor
        # SQL to get the doctor associated with this appointment
        sql = "SELECT * FROM doctors WHERE id = ?"
        row = cursor.execute(sql,(self.doctor_id,)).fetchone()
        return Doctor.instance_from_db(row)

    def apt_patient(self):
        from models.patients import Patient
        # SQL to get the patient associated with this appointment
        sql = "SELECT * FROM patients WHERE id = ?"
        row = cursor.execute(sql,(self.patient_id,)).fetchone()
        return Patient.instance_from_db(row)