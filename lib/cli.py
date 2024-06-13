# lib/cli.py
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
    create_tables()
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            doctors()
        elif choice == "2":
            patients()
        elif choice == "3":
            appointments()
        elif choice == "4":
            departments()
        else:
            print("Invalid choice")


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
        doctors_menu()
        choice = input("> ")
        if choice == "b":
            break
        elif choice == "0":
            exit_program()
        elif choice == "1":
            add_doctor()
        elif choice == "2":
            update_doctor()
        elif choice == "3":
            find_doctor_by_id()
        elif choice == "4":
            get_all_doctors()
        elif choice == "5":
            get_doc_patients()
        elif choice == "6":
            get_doc_appointments()
        elif choice == "7":
            delete_doctor()
        else:
            print("Invalid entry")



def doctors_menu():
    print("Doctors Management")
    print("b. Go back")
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
        patients_menu()
        choice = input("> ")
        if choice == "b":
            break
        elif choice == "0":
            exit_program()
        elif choice == "1":
            add_patient()
        elif choice == "2":
            update_patient()
        elif choice == "3":
            find_patient_by_id()
        elif choice == "4":
            get_all_patients()
        elif choice == "5":
            get_patient_appointments()
        elif choice == "6":
            get_patient_doctors()
        elif choice == "7":
            delete_patient()
        else:
            print("Invalid entry")


def patients_menu():
    print("Patient Management")
    print("b. Go back")
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
        appointments_menu()
        choice = input("> ")
        if choice == "b":
            break
        elif choice == "0":
            exit_program()
        elif choice == "1":
            add_appointment()
        elif choice == "2":
            update_appointment()
        elif choice == "3":
            find_appointment_by_id()
        elif choice == "4":
            get_all_appointments()
        elif choice == "5":
            get_appointment_doctor()
        elif choice == "6":
            get_appointment_patient()
        elif choice == "7":
            delete_appointment()
        else:
            print("Invalid entry")


def appointments_menu():
    print("Appointments Management")
    print("b. Go back")
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
        departments_menu()
        choice = input("> ")
        if choice == "b":
            break
        elif choice == "0":
            exit_program()
        elif choice == "1":
            add_department()
        elif choice == "2":
            update_department()
        elif choice == "3":
            find_department_by_id()
        elif choice == "4":
            get_all_departments()
        elif choice == "5":
            get_department_doctors()
        elif choice == "6":
            delete_department()
        else:
            print("Invalid entry")


def departments_menu():
    print("Department Management")
    print("b. Go back")
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
