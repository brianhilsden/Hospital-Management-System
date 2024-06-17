from database.setup import create_tables
from helpers import (
    exit_program,
    add_doctor,
    update_doctor,
    find_doctor_by_id,
    get_all_doctors,
    get_doc_patients,
    get_doc_appointments,
    delete_doctor,
    add_department,
    update_department,
    find_department_by_id,
    get_all_departments,
    get_department_doctors,
    delete_department,
    add_appointment,
    update_appointment,
    find_appointment_by_id,
    get_all_appointments,
    get_appointment_doctor,
    get_appointment_patient,
    delete_appointment,
    add_patient,
    update_patient,
    find_patient_by_id,
    get_all_patients,
    get_patient_appointments,
    get_patient_doctors,
    delete_patient

)


def main():
    create_tables() # Setup the initial database tables
    while True:
        menu() # Show the main menu
        choice = input("> ") # Get user input
        if choice == "0":
            exit_program() # Exit the program
        elif choice == "1":
            doctors() # Go to doctors management
        elif choice == "2":
            patients() # Go to patients management
        elif choice == "3":
            appointments() # Go to appointments management
        elif choice == "4":
            departments() # Go to departments management
        else:
            print("Invalid choice") # Handle invalid input


def menu():
    print("Welcome to Zawadi hospital management system. Kindly select an option:")
    print("0. Exit the program")
    print("1. Doctor Management")
    print("2. Patient Management")
    print("3. Appointment Management")
    print("4. Department Management")
    print("-----------------------------")
    print()

def doctors():
    while True:
        doctors_menu() # Show the doctors menu
        choice = input("> ") # Get user input for doctors management
        if choice == "b":
            break # Go back to the main menu
        elif choice == "0":
            exit_program() # Exit the program
        elif choice == "1":
            add_doctor() # Add a new doctor
        elif choice == "2":
            update_doctor() # Update doctor details
        elif choice == "3":
            find_doctor_by_id() # Find a doctor by their ID
        elif choice == "4":
            get_all_doctors() # List all doctors
        elif choice == "5":
            get_doc_patients() # List patients for a specific doctor
        elif choice == "6":
            get_doc_appointments() # List appointments for a specific doctor
        elif choice == "7":
            delete_doctor() # Delete a doctor
        else:
            print("Invalid entry") # Handle invalid input



def doctors_menu():
    print("Doctors Management")
    print("b. Go back to main menu")
    print("0. Exit program")
    print("1. Add new doctor")
    print("2. Update doctor details")
    print("3. Find doctor by id")
    print("4. List all doctors")
    print("5. List patients for specific doctor")
    print("6. List appointments for specific doctor")
    print("7. Delete a doctor")
    print("-----------------------------")
    print()


def patients():
    while True:
        patients_menu() # Show the patients menu
        choice = input("> ") # Get user input for patients management
        if choice == "b":
            break # Go back to the main menu
        elif choice == "0":
            exit_program() # Exit the program
        elif choice == "1":
            add_patient() # Add a new patient
        elif choice == "2":
            update_patient() # Update patient details
        elif choice == "3":
            find_patient_by_id() # Find a patient by their ID
        elif choice == "4":
            get_all_patients() # List all patients
        elif choice == "5":
            get_patient_appointments() # List appointments for a specific patient
        elif choice == "6":
            get_patient_doctors() # List doctors for a specific patient
        elif choice == "7":
            delete_patient() # Delete a patient
        else:
            print("Invalid entry") # Handle invalid input


def patients_menu():
    print("Patient Management")
    print("b. Go back to main menu")
    print("0. Exit program")
    print("1. Add new patient")
    print("2. Update patient details")
    print("3. Find patient by id")
    print("4. List all patients")
    print("5. List appointments for specific patient")
    print("6. List doctors for specific patient")
    print("7. Delete a patient")
    print("-----------------------------")
    print()


def appointments():
    while True:
        appointments_menu() # Show the appointments menu
        choice = input("> ") # Get user input for appointments management
        if choice == "b":
            break # Go back to the main menu
        elif choice == "0":
            exit_program() # Exit the program
        elif choice == "1":
            add_appointment() # Add a new appointment
        elif choice == "2":
            update_appointment() # Update appointment details
        elif choice == "3":
            find_appointment_by_id() # Find an appointment by its ID
        elif choice == "4":
            get_all_appointments() # List all appointments
        elif choice == "5":
            get_appointment_doctor() # Find doctor for a specific appointment
        elif choice == "6":
            get_appointment_patient() # Find patient for a specific appointment
        elif choice == "7":
            delete_appointment() # Delete an appointment
        else:
            print("Invalid entry") # Handle invalid input


def appointments_menu():
    print("Appointments Management")
    print("b. Go back to main menu")
    print("0. Exit program")
    print("1. Add new appointment")
    print("2. Update appointment details")
    print("3. Find appointment by id")
    print("4. List all appointments")
    print("5. Find doctor for specific appointment")
    print("6. Find patient for specific appointment")
    print("7. Delete an appointment")
    print("-----------------------------")
    print()


def departments():
    while True:
        departments_menu() # Show the departments menu
        choice = input("> ") # Get user input for departments management
        if choice == "b":
            break # Go back to the main menu
        elif choice == "0":
            exit_program() # Exit the program
        elif choice == "1":
            add_department() # Add a new department
        elif choice == "2":
            update_department() # Update department details
        elif choice == "3":
            find_department_by_id() # Find a department by its ID
        elif choice == "4":
            get_all_departments() # List all departments
        elif choice == "5":
            get_department_doctors() # List doctors in a specific department
        elif choice == "6":
            delete_department() # Delete a department
        else:
            print("Invalid entry") # Handle invalid input


def departments_menu():
    print("Department Management")
    print("b. Go back to main menu")
    print("0. Exit program")
    print("1. Add new department")
    print("2. Update department details")
    print("3. Find department by id")
    print("4. List all departments")
    print("5. List doctors in specific department")
    print("6. Delete a department")
    print("-----------------------------")
    print()


if __name__ == "__main__":
    main()