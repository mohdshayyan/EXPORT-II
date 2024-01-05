import mysql.connector
import matplotlib.pyplot as plt
# Connecting to the MySQL server
mydb = mysql.connector.connect(
    host="localhost",
    user='root',
    password='root')

# Creating a database
def create_database():
    cursor = mydb.cursor()
    cursor.execute('CREATE DATABASE IF NOT EXISTS Hotel')
    cursor.execute('USE Hotel')
create_database()
# Creating tables if not exists
def create_tables():
    cursor = mydb.cursor()
    # Guests table
    cursor.execute('CREATE TABLE IF NOT EXISTS Guests (Id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), rno VARCHAR(255), typ VARCHAR(255), loc VARCHAR(255), guest INT, rent INT, status VARCHAR(255))')
    # Staff table
    cursor.execute('CREATE TABLE IF NOT EXISTS Staff (Id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), position VARCHAR(255), salary INT)')
    # RoomService table
    cursor.execute('CREATE TABLE IF NOT EXISTS RoomService (service_id INT AUTO_INCREMENT PRIMARY KEY, guest_id INT, service_name VARCHAR(255), service_charge INT)')
    mydb.commit()

# Function to add a new guest
def add_guest():
    name = input("Enter Guest Name: ")
    rno = input("Enter Room No.: ")
    typ = input("Enter Room type: ")
    loc = input("Enter Location details: ")
    guest = int(input("Enter maximum number of guests: "))
    rent = int(input("Enter Per Day Charges: "))
    status = input("Vacant/Empty: ")

    cursor = mydb.cursor()
    sql = "INSERT INTO Guests (name, rno, typ, loc, guest, rent, status) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    val = (name, rno, typ, loc, guest, rent, status)
    cursor.execute(sql, val)
    mydb.commit()
    print("Guest added successfully.")

# Function to view all guests
def view_guests():
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM Guests")
    result = cursor.fetchall()
    print("Press (r) to see the Record")    
    print("Press (l) to see in the form of line graph")
    print("Press (p) to see in the form of pie graph")    
    ch = input("Enter your choice: ")
    if ch=='r':
        for row in result:
            print(row)
    elif ch=='l':
        # Adding a line chart
        plt.figure(figsize=(8, 6))
        plt.plot([row[0] for row in result], [row[5] for row in result], marker='o', linestyle='-', color='b')
        plt.xlabel('Guest ID')
        plt.ylabel('Rent')
        plt.title('Rent Distribution of Guests')
        plt.show()
    elif ch=='p':
        # Adding a pie chart
        guest_names = [row[1] for row in result]
        rents = [row[5] for row in result]
        plt.figure(figsize=(8, 8))
        plt.pie(rents, labels=guest_names, autopct='%1.1f%%', startangle=140)
        plt.title('Rent Distribution of Guests')
        plt.axis('equal')
        plt.show()
# Function to update guest details
def update_guest():
    guest_id = int(input("Enter Guest ID to update: "))
    name = input("Enter Guest Name: ")
    rno = input("Enter Room No.: ")
    typ = input("Enter Room type: ")
    loc = input("Enter Location details: ")
    guest = int(input("Enter maximum number of guests: "))
    rent = int(input("Enter Per Day Charges: "))
    status = input("Vacant/Empty: ")

    cursor = mydb.cursor()
    sql = "UPDATE Guests SET name = %s, rno = %s, typ = %s, loc = %s, guest = %s, rent = %s, status = %s WHERE Id = %s"
    val = (name, rno, typ, loc, guest, rent, status, guest_id)
    cursor.execute(sql, val)
    mydb.commit()
    print("Guest details updated successfully.")

# Function to delete guest
def delete_guest():
    guest_id = int(input("Enter Guest ID to delete: "))
    cursor = mydb.cursor()
    sql = "DELETE FROM Guests WHERE Id = %s"
    val = (guest_id,)
    cursor.execute(sql, val)
    mydb.commit()
    print("Guest deleted successfully.")

# Function to add staff
def add_staff():
    name = input("Enter Staff Name: ")
    position = input("Enter Staff Position: ")
    salary = int(input("Enter Staff Salary: "))

    cursor = mydb.cursor()
    sql = "INSERT INTO Staff (name, position, salary) VALUES (%s, %s, %s)"
    val = (name, position, salary)
    cursor.execute(sql, val)
    mydb.commit()
    print("Staff added successfully.")

# Function to view all staff
def view_staff():
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM Staff")
    result = cursor.fetchall()
    print("Press (r) to see the Record")    
    print("Press (b) to see in the form of bar graph")
    print("Press (l) to see in the form of line graph")    
    ch = input("Enter your choice: ")
    if ch=='r':
        for row in result:
            print(row)
    elif ch=='b':
        # Adding a bar chart for staff salaries
        plt.figure(figsize=(8, 6))
        staff_names = [row[1] for row in result]
        staff_salaries = [row[3] for row in result]
        plt.bar(staff_names, staff_salaries, color='blue')
        plt.xlabel('Staff Names')
        plt.ylabel('Salaries')
        plt.title('Staff Salaries')
        plt.xticks(rotation=45, ha="right")
        plt.show()       
    elif ch=='l':
        # Adding a line chart for staff salaries
        plt.figure(figsize=(8, 6))
        staff_names = [row[1] for row in result]
        staff_salaries = [row[3] for row in result]
        plt.plot(staff_names, staff_salaries, color='blue')
        plt.xlabel('Staff Names')
        plt.ylabel('Salaries')
        plt.title('Staff Salaries')
        plt.xticks(rotation=45, ha="right")
        plt.show()
# Function to update staff details
def update_staff():
    staff_id = int(input("Enter Staff ID to update: "))
    name = input("Enter Staff Name: ")
    position = input("Enter Staff Position: ")
    salary = int(input("Enter Staff Salary: "))
    cursor = mydb.cursor()
    sql = "UPDATE Staff SET name = %s, position = %s, salary = %s WHERE Id = %s"
    val = (name, position, salary, staff_id)
    cursor.execute(sql, val)
    mydb.commit()
    print("Staff details updated successfully.")

# Function to delete staff
def delete_staff():
    staff_id = int(input("Enter Staff ID to delete: "))
    cursor = mydb.cursor()
    sql = "DELETE FROM Staff WHERE Id = %s"
    val = (staff_id,)
    cursor.execute(sql, val)
    mydb.commit()
    print("Staff deleted successfully.")

# Function to add room service
def add_room_service():
    guest_id = int(input("Enter Guest ID: "))
    service_name = input("Enter Service Name: ")
    service_charge = int(input("Enter Service Charge: "))

    cursor = mydb.cursor()
    sql = "INSERT INTO RoomService (guest_id, service_name, service_charge) VALUES (%s, %s, %s)"
    val = (guest_id, service_name, service_charge)
    cursor.execute(sql, val)
    mydb.commit()
    print("Room service added successfully.")

# Function to view all room services
def view_room_service():
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM RoomService")
    result = cursor.fetchall()
    print("Press (r) to see the Record")    
    print("Press (p) to see in the form of graph")
    print("Press (l) to see in the form of graph")    
    ch = input("Enter your choice: ")
    if ch=='r':
        for row in result:
            print(row)
    elif ch=='l':
        # Adding pie chart
        service_names = [row[2] for row in result]
        service_charges = [row[3] for row in result]
        plt.figure(figsize=(8, 8))
        plt.plot(service_names, service_charges, color='blue')
        plt.title('Distribution of Room Service Charges')
        plt.axis('equal')
        plt.show()
    elif ch=='p':
        # Adding pie chart
        service_names = [row[2] for row in result]
        service_charges = [row[3] for row in result]
        plt.figure(figsize=(8, 8))
        plt.pie(service_charges, labels=service_names, autopct='%1.1f%%', startangle=140)
        plt.title('Distribution of Room Service Charges')
        plt.axis('equal')
        plt.show()        
# Function to update room service details
def update_room_service():
    service_id = int(input("Enter Service ID to update: "))
    guest_id = int(input("Enter Guest ID: "))
    service_name = input("Enter Service Name: ")
    service_charge = int(input("Enter Service Charge: "))

    cursor = mydb.cursor()
    sql = "UPDATE RoomService SET guest_id = %s, service_name = %s, service_charge = %s WHERE service_id = %s"
    val = (guest_id, service_name, service_charge, service_id)
    cursor.execute(sql, val)
    mydb.commit()
    print("Room service details updated successfully.")

# Function to delete room service
def delete_room_service():
    service_id = int(input("Enter Service ID to delete: "))
    cursor = mydb.cursor()
    sql = "DELETE FROM RoomService WHERE service_id = %s"
    val = (service_id,)
    cursor.execute(sql, val)
    mydb.commit()
    print("Room service deleted successfully.")

# Get the user's choice
def get_choice():
    while True:
        create_tables()
        print("\nHotel Management System Menu:")
        print("1. Guest Operations")
        print("2. Staff Operations")
        print("3. Room Service Operations")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            guest_operations()
        elif choice == '2':
            staff_operations()
        elif choice == '3':
            room_service_operations()
        elif choice == '4':
            print("Exiting the system. Goodbye!")
#            break
        else:
            print("Invalid choice. Please enter a valid option.")

# Guest operations menu
def guest_operations():
    while True:
        print("\nGuest Operations:")
        print("1. Add Guest")
        print("2. View All Guests")
        print("3. Update Guest")
        print("4. Delete Guest")
        print("5. Back to Main Menu")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_guest()
        elif choice == '2':
            view_guests()
        elif choice == '3':
            update_guest()
        elif choice == '4':
            delete_guest()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please enter a valid option.")

# Staff operations menu
def staff_operations():
    while True:
        print("\nStaff Operations:")
        print("1. Add Staff")
        print("2. View All Staff")
        print("3. Update Staff")
        print("4. Delete Staff")
        print("5. Back to Main Menu")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_staff()
        elif choice == '2':
            view_staff()
        elif choice == '3':
            update_staff()
        elif choice == '4':
            delete_staff()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please enter a valid option.")

# Room Service operations menu
def room_service_operations():
    while True:
        print("\nRoom Service Operations:")
        print("1. Add Room Service")
        print("2. View All Room Services")
        print("3. Update Room Service")
        print("4. Delete Room Service")
        print("5. Back to Main Menu")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_room_service()
        elif choice == '2':
            view_room_service()
        elif choice == '3':
            update_room_service()
        elif choice == '4':
            delete_room_service()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please enter a valid option.")

# Run the Hotel Management System
get_choice()

# Disconnecting from the MySQL server
mydb.close()
