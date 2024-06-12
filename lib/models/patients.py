from database.setup import conn
cursor = conn.cursor()
class Patient:
    all = {}
    def __init__(self,name,date_of_birth,gender,phone_number,address,id = None):
        self.name = name
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.phone_number = phone_number
        self.address = address
        self.id = id
    

    def __repr__(self):
        return f"<Patient {self.id}: {self.name}>"


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
        
    def save(self):
        sql = """INSERT INTO patients (name,date_of_birth,gender,phone_number,address) VALUES (?,?,?,?,?)"""
        cursor.execute(sql,(self.name,self.date_of_birth,self.gender,self.phone_number,self.address))
        conn.commit()
        self.id = cursor.lastrowid
        type(self).all[self.id] = self
    
    @classmethod
    def create(cls,name,date_of_birth,gender,phone_number,address):
        patient = cls(name,date_of_birth,gender,phone_number,address)
        patient.save()
        return patient
    
    @classmethod
    def instance_from_db(cls,row):
        patient = cls.all.get(row[0])
        if patient:
            patient.date_of_birth = row[2]
            patient.gender = row[3]
            patient.phone_number = row[4]
            patient.address = row[5]

        else:
            patient = cls(row[1],row[2],row[3],row[4],row[5])
            patient.id = row[0]
            cls.all[patient.id] = patient

        return patient
    

    def update(self):
        sql = """UPDATE patients SET name = ?, date_of_birth = ?, gender=?, phone_number = ?, address = ? WHERE id = ?"""
        cursor.execute(sql,(self.name,self.date_of_birth,self.gender,self.phone_number,self.address,self.id))
        conn.commit()

    def delete(self):
        sql = "DELETE FROM patients WHERE id = ?"
        cursor.execute(sql,(self.id,))
        conn.commit()
        del type(self).all[self.id]


    @classmethod
    def find_by_id(cls,id):
        sql = "SELECT * FROM patients WHERE id = ?"
        row = cursor.execute(sql,(id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def get_all_patients(cls):
        sql = "SELECT * FROM patients"
        rows = cursor.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    def pt_doctors(self):
        from models.doctors import Doctor
        sql = "SELECT doctors.* FROM doctors INNER JOIN appointments ON doctors.id = appointments.doctor_id WHERE appointments.patient_id = ?"
        rows = cursor.execute(sql,(self.id,)).fetchall()
        return [Doctor.instance_from_db(row) for row in rows]
    
    def pt_appointments(self):
        from models.appointments import Appointment
        sql = "SELECT * FROM appointments WHERE appointments.patient_id = ?"
        rows = cursor.execute(sql,(self.id,)).fetchall()
        return [Appointment.instance_from_db(row) for row in rows]


