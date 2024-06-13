from database.setup import conn
cursor = conn.cursor()
class Doctor:
    all = {}
    def __init__(self,name,gender,date_of_employment,phone_number,department_id,id = None):
        self.name = name
        self.date_of_employment = date_of_employment
        self.gender = gender
        self.phone_number = phone_number
        self.department_id = department_id
        self.id = id


    def __repr__(self):
        return f"<Doctor {self.id}: {self.name}>"


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,value):
        if isinstance(value,str) and not hasattr(self,"_name") and len(value):
            self._name = value
        else:
            raise ValueError("Invalid name")

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self,value):
        if len(value) == 1 and isinstance(value,str):
            self._gender = value
        else:
            raise ValueError("Invalid gender")

    @property
    def department_id(self):
        return self._department_id

    @department_id.setter
    def department_id(self, value):
        sql = "SELECT id FROM departments WHERE id = ?"
        if cursor.execute(sql, (value,)).fetchone():
            self._department_id = value
        else:
            raise ValueError("Invalid department_id")

    def save(self):
        sql = """INSERT INTO doctors (name,gender,date_of_employment,phone_number,department_id) VALUES (?,?,?,?,?)"""
        cursor.execute(sql,(self.name,self.gender,self.date_of_employment,self.phone_number,self.department_id))
        conn.commit()
        self.id = cursor.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls,name,gender,date_of_employment,phone_number,department_id):
        doctor = cls(name,gender,date_of_employment,phone_number,department_id)
        doctor.save()
        return doctor

    @classmethod
    def instance_from_db(cls,row):
        doctor = cls.all.get(row[0])
        if doctor:
            doctor.gender = row[2]
            doctor.date_of_employment = row[3]
            doctor.phone_number = row[4]
            doctor.department_id = row[5]


        else:
            doctor = cls(row[1],row[2],row[3],row[4],row[5])
            doctor.id = row[0]
            cls.all[doctor.id] = doctor

        return doctor


    def update(self, field, value):
        if field == "department_id":
            sql = "SELECT id FROM departments WHERE id = ?"
            if not cursor.execute(sql, (value,)).fetchone():
                raise ValueError("Invalid department_id")

        sql = f"UPDATE doctors SET {field} = ? WHERE id = ?"
        cursor.execute(sql, (value, self.id))
        conn.commit()
        setattr(self, field, value)

    def delete(self):
        sql = "DELETE FROM doctors WHERE id = ?"
        cursor.execute(sql,(self.id,))
        conn.commit()
        del type(self).all[self.id]


    @classmethod
    def find_by_id(cls,id):
        sql = "SELECT * FROM doctors WHERE id = ?"
        row = cursor.execute(sql,(id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def get_all_doctors(cls):
        sql = "SELECT * FROM doctors"
        rows = cursor.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    def get_patients(self):
        from models.patients import Patient
        sql = "SELECT DISTINCT patients.* FROM patients INNER JOIN appointments ON patients.id = appointments.patient_id WHERE appointments.doctor_id = ?"
        rows = cursor.execute(sql,(self.id,)).fetchall()
        return [Patient.instance_from_db(row) for row in rows]

    def doc_appointments(self):
        from models.appointments import Appointment
        sql = "SELECT * FROM appointments WHERE doctor_id = ?"
        rows = cursor.execute(sql,(self.id,)).fetchall()
        return [Appointment.instance_from_db(row) for row in rows]