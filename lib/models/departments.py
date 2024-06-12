from database.setup import conn
cursor = conn.cursor()
class Department:
    all = {}
    def __init__(self, name, location, id=None):
        self.name = name
        self.location = location
        self.id = id

    def __repr__(self):
        return f"<Department {self.id}: {self.name}>"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and not hasattr(self, "_name") and len(value):
            self._name = value
        else:
            raise ValueError("Invalid name")

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, value):
        if isinstance(value, str) and len(value):
            self._location = value
        else:
            raise ValueError("Invalid location")

    def save(self):
        sql = """INSERT INTO departments (name, location) VALUES (?, ?)"""
        cursor.execute(sql, (self.name, self.location))
        conn.commit()
        self.id = cursor.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, name, location):
        department = cls(name, location)
        department.save()
        return department

    @classmethod
    def instance_from_db(cls, row):
        department = cls.all.get(row[0])
        if department:
            department.location = row[2]
        else:
            department = cls(row[1], row[2])
            department.id = row[0]
            cls.all[department.id] = department

        return department

    def update(self):
        sql = """UPDATE departments SET name = ?, location = ? WHERE id = ?"""
        cursor.execute(sql, (self.name, self.location, self.id))
        conn.commit()

    def delete(self):
        sql = "DELETE FROM departments WHERE id = ?"
        cursor.execute(sql, (self.id,))
        conn.commit()
        del type(self).all[self.id]

    @classmethod
    def find_by_id(cls, id):
        sql = "SELECT * FROM departments WHERE id = ?"
        row = cursor.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def get_all_departments(cls):
        sql = "SELECT * FROM departments"
        rows = cursor.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    def dept_doctors(self):
        from models.doctors import Doctor
        sql = "SELECT * FROM doctors WHERE doctors.department_id = ? "
        rows = cursor.execute(sql,(self.id,)).fetchall()
        return [Doctor.instance_from_db(row) for row in rows]