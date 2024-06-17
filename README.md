# Zawadi Hospital Management System

## Table of Contents
1. [Project Overview](#project-overview)
2. [Key Features](#key-features)
3. [System Architecture](#system-architecture)
4. [Installation and Setup](#installation-and-setup)
5. [User Guide](#user-guide)
6. [Future Enhancements](#future-enhancements)
7. [Author](#author)
8. [License](#license)
9. [Contact](#contact)

## Project Overview

Zawadi Hospital Management System is a comprehensive, user-friendly, and efficient command-line interface (CLI) application designed to streamline the administrative processes of a hospital. Built with Python and utilizing SQLite for data storage, this system aims to simplify and automate key tasks related to doctors, patients, appointments, and departments.



## Key Features

**1. Doctor Management:**

* **Add Doctor:** Create new doctor profiles, capturing essential information like name, gender,date of employment contact details, and department.
* **Update Doctor:** Modify existing doctor profiles to reflect changes
* **Search Doctor:** Quickly locate specific doctor profiles based on id
* **List Doctors:** Display a comprehensive list of all registered doctors.
* **Dcotor's patients:** Display list of the patients the doctor attends to.
* **Doctor's appointments:** Display list of the doctor's appointments.
* **Delete Doctor:** Remove doctor profiles from the system when necessary.

**2. Patient Management:**

* **Add Patient:** Create new patient records, including name, date of birth, gender, phone number and address.
* **Update Patient:** Modify existing patient records to reflect changes.
* **Search Patient:** Locate specific patient records based on ID.
* **List Patients:** Display a list of all registered patients.
* **List patient's doctors:** Display a list of all doctors that attend to the patient.
* **Delete Patient:** Remove patient records from the system when appropriate.

**3. Appointment Scheduling:**

* **Schedule Appointment:** Create new appointments, specifying the patient, doctor and date-time.
* **Reschedule Appointment:** Modify existing appointments to adjust the date, time, or other details.
* **Locate Appointment:** Search for specific appointments based on id.
* **List Appointments:** Display a list of upcoming appointments.
* **List appointment's doctor:** Display the doctor for a specific appointment.
* **List appointment's patient:** Display the patient fot the appointment.
* **Cancel Appointment:** Remove appointments from the schedule when necessary.

**4. Department Administration:**

* **Add Department:** Create new department records, including department name and location.
* **Modify Department:** Update existing department records to reflect changes.
* **Search Department:** Locate specific department records based on id.
* **Display Departments:** Display a list of all registered departments.
* **Display Department's Doctors:** Display list of all doctors in the department.
* **Remove Department:** Delete department records from the system when no longer needed.

## System Architecture

* **Python:** The core programming language used for building the application.
* **SQLite:** A lightweight and efficient database for storing and managing the hospital's data.
* **CLI Framework:** Provides a user-friendly command-line interface for interacting with the system.
* **Data Validation:** Robust input validation mechanisms are implemented to ensure data integrity and prevent errors.


## Installation and Setup

1. **Prerequisites:**
    * Python 3.x installed on your system.
    * `pipenv` installed for managing project dependencies.

2. **Cloning the Repository:**
    * Clone the repository from GitHub: `git clone https://github.com/brianhilsden/Hospital-Management-System.git`

3. **Installing Dependencies:**
    * Install the required packages: `pipenv install`

4. **Activating the Virtual Environment:**
    * Activate the virtual environment: `pipenv shell`

5. **Running the Application:**
    * Execute the main script: `python lib/cli.py`

## User Guide

The application presents a menu-driven interface for navigating through different functionalities. Each section (doctors, patients, appointments, departments) has its own sub-menu for specific tasks. The user is guided through the menus with clear prompts and instructions.

## Future Enhancements

* **User Authentication:** Implement secure login functionality to restrict access to authorized users.
* **Graphical User Interface (GUI):** Develop a user-friendly GUI for improved accessibility and ease of use.

## Author
- Brian Omondi
- brianhilsden@gmail.com

## License

This project is licensed under the MIT license. See the `LICENSE` file for details.

## Contact

For any questions or feedback, please contact Brian Omondi at brianhilsden@gmail.com.