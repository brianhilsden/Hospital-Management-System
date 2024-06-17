from models.appointments import Appointment
from models.departments import Department
from models.doctors import Doctor
from models.patients import Patient

# Function to perform a helper function
def helper_1():
    print("Performing useful function#1.")

# Function to exit the program
def exit_program():
    print("Goodbye!")
    exit()

# Function to add a doctor
def add_doctor():
    doctor_name = input("Enter doctor's name: ")
    gender = input("Enter gender, M or F: ")
    date_of_employment = input("Enter employment date: ")
    phone_number = int(input("Enter phone number: "))
    department_id = int(input("Enter department ID: "))

    try:
       doctor = Doctor.create(doctor_name, gender, date_of_employment, phone_number, department_id)
       print("Doctor added successfully.")
    except Exception as e:
       print(f"Error occurred: {e}")

    input("\nPress Enter to continue...")

# Function to update a doctor's details
def update_doctor():
    doc_id = int(input("Enter doctor id: "))
    doctor = Doctor.find_by_id(doc_id)
    if doctor:
        field = input("Enter field to update (name, gender, date_of_employment, phone_number, department_id): ")
        value = input(f"Enter new value for {field}: ")
        try:
           doctor.update(field, value)
           print(f"Doctor with id {doc_id} updated successfully.")
        except Exception as e:
            print(f"Error occurred: {e}")
    else:
        print(f"Doctor with id {doc_id} does not exist")
    input("\nPress Enter to continue...")

# Function to find a doctor by ID
def find_doctor_by_id():
    doc_id = int(input("Enter doctor id: "))
    doctor = Doctor.find_by_id(doc_id)
    if doctor:
        print(f"Doctor is: {Doctor.find_by_id(doc_id)}")
    else:
        print(f"Doctor with id {doc_id} does not exist")
    input("\nPress Enter to continue...")

# Function to get all doctors
def get_all_doctors():
    doctors = Doctor.get_all_doctors()
    for doc in doctors:
        print(doc)
    input("\nPress Enter to continue...")

# Function to get patients of a doctor
def get_doc_patients():
    doc_id = int(input("Enter doctor id: "))
    doc = Doctor.find_by_id(doc_id)
    if doc:
        patients = doc.get_patients()
        for patient in patients:
            print(patient)
    else:
        print(f"Doctor with id {doc_id} does not exist")
    input("\nPress Enter to continue...")

# Function to get appointments of a doctor
def get_doc_appointments():
    doc_id = int(input("Enter doctor id: "))
    doc = Doctor.find_by_id(doc_id)
    if doc:
        appointments = doc.doc_appointments()
        for appointment in appointments:
            print(appointment)
    else:
        print(f"Doctor with id {doc_id} does not exist")
    input("\nPress Enter to continue...")

# Function to delete a doctor
def delete_doctor():
    doc_id = int(input("Enter doctor id: "))
    doctor = Doctor.find_by_id(doc_id)
    if doctor:
        doctor.delete()
        print(f"Doctor with id {doc_id} deleted successfully.")
    else:
        print(f"Doctor with id {doc_id} does not exist")
    input("\nPress Enter to continue...")

# Function to add a department
def add_department():
    department_name = input("Enter department name: ")
    location = input("Enter location: ")

    try:
      department = Department.create(department_name, location)
      print("Department added successfully.")
    except Exception as e:
            print(f"Error occurred: {e}")

    input("\nPress Enter to continue...")

# Function to update a department's details
def update_department():
    dep_id = int(input("Enter department id: "))
    department = Department.find_by_id(dep_id)
    if department:
        field = input("Enter field to update (name, location): ")
        value = input(f"Enter new value for {field}: ")

        try:
           department.update(field, value)
           print(f"Department with id {dep_id} updated successfully.")
        except Exception as e:
           print(f"Error occurred: {e}")

    else:
        print(f"Department with id {dep_id} does not exist")
    input("\nPress Enter to continue...")

# Function to find a department by ID
def find_department_by_id():
    dep_id = int(input("Enter department id: "))
    department = Department.find_by_id(dep_id)
    if department:
        print(f"Department is: {Department.find_by_id(dep_id)}")
    else:
        print(f"Department with id {dep_id} does not exist")
    input("\nPress Enter to continue...")

# Function to get all departments
def get_all_departments():
    departments = Department.get_all_departments()
    for dep in departments:
        print(dep)
    input("\nPress Enter to continue...")

# Function to get doctors in a department
def get_department_doctors():
    dept_id = int(input("Enter department id: "))
    dept = Department.find_by_id(dept_id)
    if dept:
        doctors = dept.dept_doctors()
        for doctor in doctors:
            print(doctor)
    else:
        print(f"Department with id {dept_id} does not exist")
    input("\nPress Enter to continue...")

# Function to delete a department
def delete_department():
    dep_id = int(input("Enter department id: "))
    department = Department.find_by_id(dep_id)
    if department:
        department.delete()
        print(f"Department with id {dep_id} deleted successfully.")
    else:
        print(f"Department with id {dep_id} does not exist")
    input("\nPress Enter to continue...")

# Function to add an appointment
def add_appointment():
    scheduled_date = input("Enter scheduled date: ")
    patient_id = int(input("Enter patient ID: "))
    doctor_id = int(input("Enter doctor ID: "))

    try:
        appointment = Appointment.create(scheduled_date, patient_id, doctor_id)
        print("Appointment added successfully.")
    except Exception as e:
        print(f"Error occurred: {e}")

    input("\nPress Enter to continue...")
def update_appointment():
    appt_id = int(input("Enter appointment id: "))
    appointment = Appointment.find_by_id(appt_id)
    if appointment:
        # Prompt for the field to update
        field = input("Enter field to update (scheduled_date, patient_id, doctor_id): ")
        value = input(f"Enter new value for {field}: ")

        try:
            # Update the appointment with the new value
            appointment.update(field, value)
            print(f"Appointment with id {appt_id} updated successfully.")
        except Exception as e:
            # Handle any errors during update
            print(f"Error occurred: {e}")

    else:
        # Appointment not found
        print(f"Appointment with id {appt_id} does not exist")
    input("\nPress Enter to continue...")

def find_appointment_by_id():
    appt_id = int(input("Enter appointment id: "))
    appointment = Appointment.find_by_id(appt_id)
    if appointment:
        # Print the appointment details
        print(f"Appointment is: {Appointment.find_by_id(appt_id)}")
    else:
        # Appointment not found
        print(f"Appointment with id {appt_id} does not exist")
    input("\nPress Enter to continue...")

def get_all_appointments():
    appointments = Appointment.get_all_appointments()
    for appt in appointments:
        # Print each appointment
        print(appt)
    input("\nPress Enter to continue...")

def get_appointment_doctor():
    appt_id = int(input("Enter appointment id: "))
    appointment = Appointment.find_by_id(appt_id)
    if appointment:
        # Retrieve and print the doctor for the appointment
        doc = appointment.apt_doctor()
        print(f"The doctor is: {doc}")
    else:
        # Appointment not found
        print(f"Appointment with id {appt_id} does not exist")
    input("\nPress Enter to continue...")

def get_appointment_patient():
    appt_id = int(input("Enter appointment id: "))
    appointment = Appointment.find_by_id(appt_id)
    if appointment:
        # Retrieve and print the patient for the appointment
        patient = appointment.apt_patient()
        print(f"The patient is: {patient}")
    else:
        # Appointment not found
        print(f"Appointment with id {appt_id} does not exist")
    input("\nPress Enter to continue...")

def delete_appointment():
    appt_id = int(input("Enter appointment id: "))
    appointment = Appointment.find_by_id(appt_id)
    if appointment:
        # Delete the appointment
        appointment.delete()
        print(f"Appointment with id {appt_id} deleted successfully.")
    else:
        # Appointment not found
        print(f"Appointment with id {appt_id} does not exist")
    input("\nPress Enter to continue...")

def add_patient():
    patient_name = input("Enter patient's name: ")
    date_of_birth = input("Enter date of birth: ")
    gender = input("Enter gender, M or F: ")
    phone_number = int(input("Enter phone number: "))
    address = input("Enter address: ")

    try:
        # Create and add a new patient
        patient = Patient.create(patient_name, date_of_birth, gender, phone_number, address)
    except Exception as e:
        # Handle any errors during creation
        print(f"Error occurred: {e}")
    print("Patient added successfully.")
    input("\nPress Enter to continue...")

def update_patient():
    patient_id = int(input("Enter patient id: "))
    patient = Patient.find_by_id(patient_id)
    if patient:
        # Prompt for the field to update
        field = input("Enter field to update (name, date_of_birth, gender, phone_number, address): ")
        value = input(f"Enter new value for {field}: ")

        try:
            # Update the patient with the new value
            patient.update(field, value)
        except Exception as e:
            # Handle any errors during update
            print(f"Error occurred: {e}")
        print(f"Patient with id {patient_id} updated successfully.")
    else:
        # Patient not found
        print(f"Patient with id {patient_id} does not exist")
    input("\nPress Enter to continue...")

def find_patient_by_id():
    patient_id = int(input("Enter patient id: "))
    patient = Patient.find_by_id(patient_id)
    if patient:
        # Print the patient details
        print(f"Patient is: {Patient.find_by_id(patient_id)}")
    else:
        # Patient not found
        print(f"Patient with id {patient_id} does not exist")
    input("\nPress Enter to continue...")

def get_all_patients():
    patients = Patient.get_all_patients()
    for patient in patients:
        # Print each patient
        print(patient)
    input("\nPress Enter to continue...")

def get_patient_appointments():
    patient_id = int(input("Enter patient id: "))
    patient = Patient.find_by_id(patient_id)
    if patient:
        # Retrieve and print appointments for the patient
        appointments = patient.pt_appointments()
        for appointment in appointments:
            print(appointment)
    else:
        # Patient not found
        print(f"Patient with id {patient_id} does not exist")
    input("\nPress Enter to continue...")

def get_patient_doctors():
    patient_id = int(input("Enter patient id: "))
    patient = Patient.find_by_id(patient_id)
    if patient:
        # Retrieve and print doctors for the patient
        doctors = patient.pt_doctors()
        for doctor in doctors:
            print(doctor)
    else:
        # Patient not found
        print(f"Patient with id {patient_id} does not exist")
    input("\nPress Enter to continue...")

def delete_patient():
    patient_id = int(input("Enter patient id: "))
    patient = Patient.find_by_id(patient_id)
    if patient:
        # Delete the patient
        patient.delete()
        print(f"Patient with id {patient_id} deleted successfully.")
    else:
        # Patient not found
        print(f"Patient with id {patient_id} does not exist")
    input("\nPress Enter to continue...")