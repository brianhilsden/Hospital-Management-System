from database.setup import conn
cursor = conn.cursor()
class Appointment:
    all = {}
    def __init__(self, datetime,patient_id,doctor_id, id=None):
        self.datetime = datetime
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.id = id

    def __repr__(self):
        return f"<Appointment {self.id}: {self.datetime}>"

    def save(self):
        sql = """INSERT INTO appointments (datetime, patient_id,doctor_id) VALUES (?, ?,?)"""
        cursor.execute(sql, (self.datetime, self.patient_id,self.doctor_id))
        conn.commit()
        self.id = cursor.lastrowid
        type(self).all[self.id] = self

    @property
    def doctor_id(self):
        return self._doctor_id

    @doctor_id.setter
    def doctor_id(self, value):
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
        sql = "SELECT id FROM patients WHERE id = ?"
        if cursor.execute(sql, (value,)).fetchone():
            self._patient_id = value
        else:
            raise ValueError("Invalid patient_id")

    @classmethod
    def create(cls, datetime, patient_id,doctor_id):
        appointment = cls(datetime, patient_id,doctor_id)
        appointment.save()
        return appointment

    @classmethod
    def instance_from_db(cls, row):
        appointment = cls.all.get(row[0])
        if appointment:
            appointment.datetime = row[1]
            appointment.patient_id = row[2]
            appointment.doctor_id = row[3]
        else:
            appointment = cls(row[1], row[2],row[3])
            appointment.id = row[0]
            cls.all[appointment.id] = appointment

        return appointment

    def update(self, field, value):
        if field == "doctor_id":
            sql = "SELECT id FROM doctors WHERE id = ?"
            if not cursor.execute(sql, (value,)).fetchone():
                raise ValueError("Invalid doctor_id")
        elif field == "patient_id":
            sql = "SELECT id FROM patients WHERE id = ?"
            if not cursor.execute(sql, (value,)).fetchone():
                raise ValueError("Invalid patient_id")

        sql = f"UPDATE appointments SET {field} = ? WHERE id = ?"
        cursor.execute(sql, (value, self.id))
        conn.commit()
        setattr(self,field,value)

    def delete(self):
        sql = "DELETE FROM appointments WHERE id = ?"
        cursor.execute(sql, (self.id,))
        conn.commit()
        del type(self).all[self.id]

    @classmethod
    def find_by_id(cls, id):
        sql = "SELECT * FROM appointments WHERE id = ?"
        row = cursor.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def get_all_appointments(cls):
        sql = "SELECT * FROM appointments"
        rows = cursor.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    def apt_doctor(self):
        from models.doctors import Doctor
        sql = "SELECT * FROM doctors WHERE id = ?"
        row = cursor.execute(sql,(self.doctor_id,)).fetchone()
        return Doctor.instance_from_db(row)
    
    def apt_patient(self):
        from models.patients import Patient
        sql = "SELECT * FROM patients WHERE id = ?"
        row = cursor.execute(sql,(self.patient_id,)).fetchone()
        return Patient.instance_from_db(row)