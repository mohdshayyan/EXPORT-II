import mysql.connector
import matplotlib.pyplot as plt
import pandas as pd
# Connecting to the MySQL server
mydb = mysql.connector.connect(
    host="localhost",
    user='root',
    password='root'
)
print("-" * 165)
print(" " * 68 + "Welcome to Hospital Management System")
print("-" * 165)

# Creating a database
def create_database():
    cursor = mydb.cursor()
    cursor.execute('CREATE DATABASE IF NOT EXISTS Hosp')
    cursor.execute('USE Hosp')

# Creating Patients table
def create_patients_table():
    cursor = mydb.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS Patients (Id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), age INT, gender VARCHAR(10), contact VARCHAR(15))')

# Creating Doctors table
def create_doctors_table():
    cursor = mydb.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS Doctors (Id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), specialization VARCHAR(255), contact VARCHAR(15))')

# Creating Appointments table
def create_appointments_table():
    cursor = mydb.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS Appointments (Id INT AUTO_INCREMENT PRIMARY KEY, patient_id INT, doctor_id INT, date DATE, time VARCHAR(255))')

# Define the function to add a new patient
def add_patient():
    name = input("Enter patient name: ")
    age = int(input("Enter patient age: "))
    gender = input("Enter patient gender: ")
    contact = input("Enter patient contact number: ")
    cursor = mydb.cursor()
    sql = "INSERT INTO Patients (name, age, gender, contact) VALUES (%s, %s, %s, %s)"
    val = (name, age, gender, contact)
    cursor.execute(sql, val)
    mydb.commit()
    print(cursor.rowcount, "record(s) inserted.")

# Define the function to view patient details
def view_patients():
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM Patients")
    result = cursor.fetchall()
    print("Press (f) to see in the form of DataFrame")
    print("Press (l) to see in the form of line graph")    
    print("Press (h) to see in the form of histogram graph")    
    ch = input("Enter your choice: ")
    if ch=='f':
        result_list = [list(row) for row in result]
        lst1 = [row[0] for row in result_list]
        lst2 = [row[1] for row in result_list]
        lst3 = [row[2] for row in result_list]
        lst4 = [row[3] for row in result_list]
        df = pd.DataFrame({'Name': lst1, 'Age': lst2, 'Gender': lst3, 'contact': lst4})
        print(df.to_markdown())
    elif ch=='l':# Adding line chart
        plt.figure(figsize=(8, 6))
        plt.plot([row[0] for row in result], [row[2] for row in result], marker='o', linestyle='-', color='b')
        plt.xlabel('Patient ID')
        plt.ylabel('Age')
        plt.title('Age Distribution of Patients')
        plt.show()
    elif ch=='h':
        plt.figure(figsize=(8, 6))
        plt.hist([row[2] for row in result], bins=20, color='skyblue', edgecolor='black')
        plt.xlabel('Age')
        plt.ylabel('Number of Patients')
        plt.title('Age Distribution of Patients')
        plt.show()
            

# Define the function to update patient details
def update_patient():
    patient_id = int(input("Enter patient ID to update: "))
    name = input("Enter patient name: ")
    age = int(input("Enter patient age: "))
    gender = input("Enter patient gender: ")
    contact = input("Enter patient contact number: ")
    cursor = mydb.cursor()
    sql = "UPDATE Patients SET name = %s, age = %s, gender = %s, contact = %s WHERE Id = %s"
    val = (name, age, gender, contact, patient_id)
    cursor.execute(sql, val)
    mydb.commit()
    print(cursor.rowcount, "record(s) updated.")

# Define the function to delete patient details
def delete_patient():
    patient_id = int(input("Enter patient ID to delete: "))
    cursor = mydb.cursor()
    sql = "DELETE FROM Patients WHERE Id = %s"
    val = (patient_id,)
    cursor.execute(sql, val)
    mydb.commit()
    print(cursor.rowcount, "record(s) deleted.")

# Define the function to add a new doctor
def add_doctor():
    name = input("Enter doctor name: ")
    specialization = input("Enter doctor specialization: ")
    contact = input("Enter doctor contact number: ")
    cursor = mydb.cursor()
    sql = "INSERT INTO Doctors (name, specialization, contact) VALUES (%s, %s, %s)"
    val = (name, specialization, contact)
    cursor.execute(sql, val)
    mydb.commit()
    print(cursor.rowcount, "record(s) inserted.")

# Define the function to view doctor details
def view_doctors():
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM Doctors")
    result = cursor.fetchall()
    print("Press (f) to see in the form of DataFrame")
    print("Press (b) to see in the form of bar graph")    
    print("Press (p) to see in the form of pie graph")
    
    ch = input("Enter your choice: ")
    if ch=='f':
        result_list = [list(row) for row in result]
        lst1 = [row[0] for row in result_list]
        lst2 = [row[1] for row in result_list]
        lst3 = [row[2] for row in result_list]
        df = pd.DataFrame({'name': lst1, 'specialization': lst2, 'contact': lst3})
        print(df.to_markdown())
    elif ch == 'b':
        # Extracting data for the bar chart
        doctor_names = [row[1] for row in result]
        doctor_contacts = [row[3] for row in result]
        plt.figure(figsize=(10, 6))
        plt.bar(doctor_names, doctor_contacts, color='green')
        plt.xlabel('Doctor Names')
        plt.ylabel('Contact Numbers')
        plt.title('Contact Numbers of Doctors')
        plt.xticks(rotation=45, ha="right")
        plt.show()        
    elif ch == 'p':
        # Extracting data for the pie chart
        specializations = [row[2] for row in result]
        unique_specializations = list(set(specializations))
        specialization_counts = [specializations.count(spec) for spec in unique_specializations]
        # Plotting the pie chart
        plt.figure(figsize=(8, 8))
        plt.pie(specialization_counts, labels=unique_specializations, autopct='%1.1f%%', startangle=140)
        plt.title('Specialization Distribution of Doctors')
        plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        plt.show()

        
# Define the function to update doctor details
def update_doctor():
    doctor_id = int(input("Enter doctor ID to update: "))
    name = input("Enter doctor name: ")
    specialization = input("Enter doctor specialization: ")
    contact = input("Enter doctor contact number: ")
    cursor = mydb.cursor()
    sql = "UPDATE Doctors SET name = %s, specialization = %s, contact = %s WHERE Id = %s"
    val = (name, specialization, contact, doctor_id)
    cursor.execute(sql, val)
    mydb.commit()
    print(cursor.rowcount, "record(s) updated.")

# Define the function to delete doctor details
def delete_doctor():
    doctor_id = int(input("Enter doctor ID to delete: "))
    cursor = mydb.cursor()
    sql = "DELETE FROM Doctors WHERE Id = %s"
    val = (doctor_id,)
    cursor.execute(sql, val)
    mydb.commit()
    print(cursor.rowcount, "record(s) deleted.")

# Define the function to add a new appointment
def add_appointment():
    patient_id = int(input("Enter patient ID: "))
    doctor_id = int(input("Enter doctor ID: "))
    date = input("Enter appointment date (YYYY-MM-DD): ")
    time = input("Enter appointment time (HH:MM AM/PM): ")
    cursor = mydb.cursor()
    sql = "INSERT INTO Appointments (patient_id, doctor_id, date, time) VALUES (%s, %s, %s, %s)"
    val = (patient_id, doctor_id, date, time)
    cursor.execute(sql, val)
    mydb.commit()
    print(cursor.rowcount, "record(s) inserted.")

# Define the function to view appointment details
def view_appointments():
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM Appointments")
    result = cursor.fetchall()
    print("Press (f) to see in the form of DataFrame")
    print("Press (b) to see in the form of bar graph")
    print("Press (l) to see in the form of line graph")    
    ch = input("Enter your choice: ")
    if ch=='f':
        result_list = [list(row) for row in result]
        lst1 = [row[0] for row in result_list]
        lst2 = [row[1] for row in result_list]
        lst3 = [row[2] for row in result_list]
        lst4 = [row[3] for row in result_list]
        df = pd.DataFrame({'patient_id': lst1, 'doctor_id': lst2, 'date': lst3, 'time': lst4})
        print(df.to_markdown())
    elif ch == 'l':
        # Adding a line chart for appointment dates
        plt.figure(figsize=(10, 6))
        plt.plot([row[0] for row in result], [row[1] for row in result], marker='o', linestyle='-', color='b')
        plt.xlabel('Appointment ID')
        plt.ylabel('Patient ID')
        plt.title('Patient Distribution in Appointments')
        plt.show()        
    elif ch == 'b':
        # Extracting dates from the 'date' column
        dates = [row[3] for row in result]
        # Counting the occurrences of each date
        date_counts = {}
        for date in dates:
            date_counts[date] = date_counts.get(date, 0) + 1
        # Sorting the dates for better visualization
        sorted_dates = sorted(date_counts.keys())
        # Creating a bar chart
        plt.figure(figsize=(10, 6))
        plt.bar(sorted_dates, [date_counts[date] for date in sorted_dates])
        plt.xlabel('Date')
        plt.ylabel('Number of Appointments')
        plt.title('Number of Appointments on Each Date')
        plt.xticks(rotation=45)
        plt.show()

# Define the function to update appointment details
def update_appointment():
    appointment_id = int(input("Enter appointment ID to update: "))
    patient_id = int(input("Enter patient ID: "))
    doctor_id = int(input("Enter doctor ID: "))
    date = input("Enter appointment date (YYYY-MM-DD): ")
    time = input("Enter appointment time (HH:MM AM/PM): ")
    cursor = mydb.cursor()
    sql = "UPDATE Appointments SET patient_id = %s, doctor_id = %s, date = %s, time = %s WHERE Id = %s"
    val = (patient_id, doctor_id, date, time, appointment_id)
    cursor.execute(sql, val)
    mydb.commit()
    print(cursor.rowcount, "record(s) updated.")

# Define the function to delete appointment details
def delete_appointment():
    appointment_id = int(input("Enter appointment ID to delete: "))
    cursor = mydb.cursor()
    sql = "DELETE FROM Appointments WHERE Id = %s"
    val = (appointment_id,)
    cursor.execute(sql, val)
    mydb.commit()
    print(cursor.rowcount, "record(s) deleted.")

# Get the user's choice
def getchoice():
    while True:
        create_database()
        create_patients_table()
        create_doctors_table()
        create_appointments_table()
        
        print("1. Add Patient                            2. View Patients              3. Update Patient              4. Delete Patient")
        print("5. Add Doctor                             6. View Doctors               7. Update Doctor               8. Delete Doctor")
        print("9. Add Appointment                        10. View Appointments         11. Update Appointment         12. Delete Appointment")
        print("13. Exit")
        opp = input("Enter your choice: ")
        if opp == '1':
            add_patient()
            input("Press ENTER KEY to continue.....")
            print()
        elif opp == '2':
            view_patients()
            input("Press ENTER KEY to continue.....")
            print()
        elif opp == '3':
            update_patient()
            input("Press ENTER KEY to continue.....")
            print()
        elif opp == '4':
            delete_patient()
            input("Press ENTER KEY to continue.....")
            print()
        elif opp == '5':
            add_doctor()
            input("Press ENTER KEY to continue.....")
            print()
        elif opp == '6':
            view_doctors()
            input("Press ENTER KEY to continue.....")
            print()
        elif opp == '7':
            update_doctor()
            input("Press ENTER KEY to continue.....")
            print()
        elif opp == '8':
            delete_doctor()
            input("Press ENTER KEY to continue.....")
            print()
        elif opp == '9':
            add_appointment()
            input("Press ENTER KEY to continue.....")
            print()
        elif opp == '10':
            view_appointments()
            input("Press ENTER KEY to continue.....")
            print()
        elif opp == '11':
            update_appointment()
            input("Press ENTER KEY to continue.....")
            print()
        elif opp == '12':
            delete_appointment()
            input("Press ENTER KEY to continue.....")
            print()
        elif opp == '13':
            print('Exited !')
            break

# Recall Choice function
getchoice()
# Disconnecting from the server
mydb.close()
