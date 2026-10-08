import os

path = "patient_database/patients"

def add_patient(path=path):

    print("\n------ADD PATIENT-----\n")
    patient_firstname = input("Enter Patient First Name : \n").strip()
    patient_lastname = input("\nEnter Patient Last Name : \n").strip()

    try:
        patient_dob = int(input("\nEnter Patient Date of Birth (DDMMYYYY) :\n"))
    except TypeError:
        print("YOU MUST ONLY USE NUMBERS FOR THE DATE OF BIRTH")
        patient_dob = int(input("\nEnter Patient Date of Birth (DDMMYYYY) :\n"))

    try:
        patient_telephone = input("\nEnter Patient Telephone : \n")
    except TypeError:
        print("ONLY USE NUMBERS FOR THE TELEPHONE")
        patient_telephone = input("\nEnter Patient Telephone (0123456789) : \n")

    try:
        patient_id = int(input("\nEnter Patient ID : \n"))
    except TypeError:
        print("ONLY USE NUMBERS FOR THE ID!")
        patient_id = int(input("\nEnter Patient ID (123456) : \n"))

    if not os.path.exists(f"{path}/{patient_id}_{patient_firstname}"):
        os.mkdir(f"{path}/{patient_id}_{patient_firstname}")
        print("Folder made")

        
    if not os.path.exists(f"{path}/{patient_id}_{patient_firstname}/Info"):
        os.mkdir(f"{path}/{patient_id}_{patient_firstname}/Info")
        print(f"Info Folder Created.")

    if not os.path.exists(f"{path}/{patient_id}_{patient_firstname}/Events"):
        os.mkdir(f"{path}/{patient_id}_{patient_firstname}/Events")
        print(f"Events Folder Created.")

    if not os.path.exists(f"{path}/{patient_id}_{patient_firstname}/Appointments"):
        os.mkdir(f"{path}/{patient_id}_{patient_firstname}/Appointments")
        print(f"Appointments Folder Created.")

    with open(f"{path}/{patient_id}_{patient_firstname}/Info/Basic_Information.txt", "w") as f:
        f.write(f"-----{patient_firstname} {patient_lastname} - BASIC INFORMATION-----\n\n\nFirst Name:\n{patient_firstname}\n\nLast Name:\n{patient_lastname}\n\nPatient ID:\n{patient_id}\n\nPatient DOB:\n{patient_dob}\n\nPatient Tel.:\n+44 {patient_telephone[1:]}\n\n\n-----END-----")


def add_appointment(path=path):
    patient_id = input("Enter Patient ID : \n")
    patient_firstname = input("\nEnter Patient Firstname : \n")
    current_date = input("\nEnter Current Date (DDMMYYYY) : \n")

    doctor_name = input("\n\n\nEnter Doctor name : \n")
    scheduled_date = input("\nEnter Appointment Date (DDMMYYYY) : \n")
    scheduled_length = input("\nEnter length of Appointment (Hours) : \n")
    scheduled_reason = input("\nEnter reason of Appointment : \n")


    with open(f"{path}/{patient_id}_{patient_firstname}/Appointments/{scheduled_date[0:2]}-{scheduled_date[2:4]}-{scheduled_date[4:]}.txt", 'w') as file:
        file.write(f"-----APPOINTMENT------\n\n\nAppointment Date :\n{scheduled_date[0:2]}-{scheduled_date[2:4]}-{scheduled_date[4:]}\n\nAppointment Length :\n{scheduled_length}\n\nAppointment Reason :\n{scheduled_reason}\n\nDoctor Name :\n{doctor_name}\n\n\n-----END-----")

def finish_appointment(path=path):
    patient_id = input("Enter Patient ID : \n")
    patient_firstname = input("\nEnter Patient Firstname : \n")
    scheduled_date = input("\nEnter Appointment Date (DDMMYYYY) : \n")

    appointment_status = input("\n\nHow did the appointment go : \n")

    with open(f"{path}/{patient_id}_{patient_firstname}/Appointments/{scheduled_date[0:2]}-{scheduled_date[2:4]}-{scheduled_date[4:]}.txt", 'a') as file:
            file.write(f"\n\n-----APPOINTMENT FINISHED-----\n{appointment_status}\n\n-----END-----")


while True:
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n------HOPITAL------")
    print("1. Create Patient Entry")
    print("2. Create Patient Appointment")
    print("3. Finish Patient Appointment")
    choice = int(input("Make Selection : \n"))

    if choice == 1:
        add_patient()
    elif choice == 2:
        add_appointment()
    elif choice == 3:
        finish_appointment()
