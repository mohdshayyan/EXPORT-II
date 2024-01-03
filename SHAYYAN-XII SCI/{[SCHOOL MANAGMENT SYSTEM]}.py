#                                                                                       ---| PYTHON CODING |---
#                                                                                 ---|School Management System|---
#                                                                             ---|  Designed and Maintained By  |---
#                                                                       ---| SHAYYAN - Class XII SCI {2023-2024}|---

import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt
from datetime import datetime

# Making Connection
mydb = mysql.connector.connect(
host="localhost",
user='root',
password='root')
print(mydb, "connected to server")
print("\n")

print("-" * 165)
print(" " * 68 + "Welcome to School Management System")
print("-" * 165)

def create_database():
        cursor = mydb.cursor() # preparing a cursor object
        cursor.execute('CREATE DATABASE IF NOT EXISTS school')# Creating the Database if it doesn't exist
        cursor.execute('USE school')

# Creating the table if it doesn't exist
def create_students():
        cursor = mydb.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS students (Id INT PRIMARY KEY,name VARCHAR(255), age INT, gender VARCHAR(255), Class VARCHAR(255),date_added VARCHAR(255))')

# Define the function to add a new student
def add_student():
    Id = input("Enter Id of student: ")
    # Check if the Id already exists
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM students WHERE Id = %s", (Id,))
    existing_students = cursor.fetchone()

    if existing_students:
        print("student with this Id already exists. Please enter a different Id.")
    else:
            name = input("Enter student Name: ")
            age = input("Enter student's age: ")
            gender = input("Enter student gender(m/f): ")
            Class = input("Enter student Class: ")
            now = datetime.now()
            date_time = now.strftime("%Y-%m-%d %H:%M:%S")
            # Inserting Values
            sql = "INSERT INTO students (Id, name, age, gender, Class, date_added) VALUES (%s, %s, %s, %s, %s, %s)"
            val = (Id, name, age, gender, Class, date_time)
            cursor.execute(sql, val)# Executing the SQL query
            mydb.commit()# Committing the changes in the table
            print(cursor.rowcount, "record(s) inserted.")


# Define the function to view student details
def view_students():
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM students")
    result = cursor.fetchall() 
    print("Press (f) to see in the form of DataFrame")
    print("Press (i) to see the Separate Index values")
    print("Press (l) to see in the form of list")

    ch = input("Enter your choice: ")
    if ch=='i':
            result_list = [list(row) for row in result]
            lst1 = [row[0] for row in result_list]
            print("Id is:", lst1)
            lst2 = [row[1] for row in result_list]
            print('Name is:', lst2)
            lst3 = [row[2] for row in result_list]
            print('Age is', lst3)
            lst4 = [row[3] for row in result_list]
            print('Gender is: ', lst4)
            lst5 = [row[4] for row in result_list]
            print('Class is', lst5)            
            lst6 = [row[5] for row in result_list]
            print('Date_&_Time', lst6)            
    elif ch=='l':
            result_list = [list(row) for row in result]
            print(result_list)           
    elif ch=='f':
            result_list = [list(row) for row in result]
            lst1 = [row[0] for row in result_list]
            lst2 = [row[1] for row in result_list]
            lst3 = [row[2] for row in result_list]
            lst4 = [row[3] for row in result_list]
            lst5 = [row[4] for row in result_list]
            lst6 = [row[5] for row in result_list]            
            df = pd.DataFrame({'Id': lst1, 'Name': lst2, 'Age': lst3, 'Gender': lst4, 'Class': lst5,'Date_&_Time': lst6})
            print(df.to_markdown())

# Define the function to update student details
def update_student():
    Id = input("Enter student's Id: ")
    name = input("Enter student's Name: ")
    age = input("Enter studenlt's age: ")
    gender = input("Enter student's gender(m/f): ")
    Class = input("Enter student's Class: ")
    cursor = mydb.cursor()
    sql_up = "update students set name = %s, age = %s, gender = %s, Class = %s where Id = %s"
    val_up = (name, age, gender, Class,Id)
    cursor.execute(sql_up, val_up)
    mydb.commit()
    print(cursor.rowcount, "record(s) updated.")

# Define the function to delete student details
def delete_student():
    Id = input("Enter student Id: ")
    cursor = mydb.cursor()
    sql = "delete from students where Id = %s"
    val = (Id,)
    cursor.execute(sql, val)
    mydb.commit()
    print(cursor.rowcount, "record(s) deleted.")

# CREATING A TABLE
def create_Staff():
        cursor = mydb.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS Staff(Id INT,post varchar(50),name varchar(50),salary varchar(50),phone char(10),date_added VARCHAR(255),FOREIGN KEY (Id) REFERENCES students(Id))')

# Define the function to add a new staff
def add_staff():
    Id = input("Enter staff ID: ")
    # Check if the ID already exists
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM staff WHERE Id = %s", (Id,))
    existing_staff = cursor.fetchone()
    if existing_staff:
        print("Staff with this ID already exists. Please enter a different ID.")
        # You might want to add more logic here, like asking the user to re-enter the ID.
    else:
        post = input("Enter staff Post: ")
        name = input("Enter staff Name: ")
        salary = input("Enter staff Salary: ")
        phone = input("Enter staff Phone no: ")
        now = datetime.now()
        date_time = now.strftime("%Y-%m-%d %H:%M:%S")

        # Inserting Values
        sql = "INSERT INTO staff (Id, post, name, salary, phone, date_added) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (Id, post, name, salary, phone, date_time)
        cursor.execute(sql, val)
        mydb.commit()
        print(cursor.rowcount, "record(s) inserted.")


# Define the function to view student details
def view_staff():
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM staff")
    result = cursor.fetchall()
    print("Press (f) to see in the form of DataFrame")
    print("Press (i) to see the Separate Index values")
    print("Press (l) to see in the form of list")
    ch = input("Enter your choice: ")# Get the user's choice
    if ch=='i':
            result_list = [list(row) for row in result]
            lst1 = [row[0] for row in result_list]
            print("Id is:", lst1)
            lst2 = [row[1] for row in result_list]
            print('Post is:', lst2)
            lst3 = [row[2] for row in result_list]
            print('Name is:', lst3)
            lst4 = [row[3] for row in result_list]
            print('Salary is: ', lst4)
            lst5 = [row[4] for row in result_list]
            print('Phone_no is: ', lst5)
            lst6 = [row[5] for row in result_list]
            print('Date_&_Time is: ', lst6)                  
    elif ch=='l':
            result_list = [list(row) for row in result]
            print(result_list)            
    elif ch=='f':
            result_list = [list(row) for row in result]
            lst1 = [row[0] for row in result_list]
            lst2 = [row[1] for row in result_list]
            lst3 = [row[2] for row in result_list]
            lst4 = [row[3] for row in result_list]
            lst5 = [row[4] for row in result_list]
            lst6 = [row[5] for row in result_list]                  
            df=pd.DataFrame({'ID':lst1,'POST':lst2,'NAME':lst3,'SALARY':lst4,'PHONE':lst5,'Date_&_Time': lst6})
            print(df.to_markdown())    
            
# Define the function to update staff details
def update_staff():
    Id=input("Enter staff ID: ")
    post=input("Enter staff Post: ")
    name = input("Enter staff Name: ")
    salary = input("Enter staff Salary: ")
    phone = input("Enter staff Phone no: ")
    cursor = mydb.cursor()
    sql = "UPDATE staff set Id = %s , post= %s, name = %s, salary = %s, phone = %s WHERE Id = %s"
    val = (Id,post,name,salary, phone)
    cursor.execute(sql, val)
    mydb.commit()
    print(cursor.rowcount, "record(s) updated.")

# Define the function to delete staff details
def delete_staff():
    Id = input("Enter staff ID: ")
    cursor = mydb.cursor()
    sql = "DELETE FROM staff WHERE Id = %s"
    val = (Id,)
    cursor.execute(sql, val)
    mydb.commit()
    print(cursor.rowcount, "record(s) deleted.")

# CREATING A TABLE
def create_fee():
        cursor = mydb.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS fee(Id INT,Name varchar(50),Class varchar(50),Status varchar(50),Quarter varchar(50),PaidAmt INT,date_added VARCHAR(255),FOREIGN KEY (Id) REFERENCES students(Id))')

# Define the function to add Fee details
def fee():
    Id = input("Enter Payer's ID: ")
    # Check if the ID already exists
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM fee WHERE Id = %s", (Id,))
    existing_fee = cursor.fetchone()

    if existing_fee:
        print("fee with this ID already exists. Please enter a different Id.")
    else:
            Name = input("Enter Payer's Name: ")
            Class = input("Enter Payer's Class: ")
            Status = input("Enter Status (Paid/Due): ")
            Quarter = input("Enter Quarter: ")
            PaidAmt = input("Enter Paid Amount: ")
            now = datetime.now()
            date_time = now.strftime("%Y-%m-%d %H:%M:%S")
            # Inserting Values
            sql = "INSERT INTO fee (Id, Name, Class, Status, Quarter, PaidAmt, date_added) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            val = (Id, Name, Class, Status, Quarter, PaidAmt, date_time)
            cursor.execute(sql, val)
            mydb.commit()# Committing the changes in the table
            print(cursor.rowcount, "record(s) inserted.")

# Define the function to view Fee details
def view_fee():
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM fee")
    result = cursor.fetchall()
    print("Press (f) to see in the form of DataFrame")
    print("Press (i) to see the Separate Index values")
    print("Press (l) to see in the form of list")
# Get the user's choice
    ch = input("Enter your choice: ")
    if ch=='i':
            result_list = [list(row) for row in result]
            lst1 = [row[0] for row in result_list]
            print("Id is:", lst1)
            lst2 = [row[1] for row in result_list]
            print('Name is:', lst2)
            lst3 = [row[2] for row in result_list]
            print('Class is:', lst3)
            lst4 = [row[3] for row in result_list]
            print('Status is: ', lst4)
            lst5 = [row[4] for row in result_list]
            print('Quarter is:', lst5)
            lst6 = [row[5] for row in result_list]
            print('PaidAmt is:', lst6)    
            lst7 = [row[6] for row in result_list]
            print('Date_&_Time is:', lst7)            
    elif ch=='l':
            result_list = [list(row) for row in result]
            print(result_list)            
    elif ch=='f':
            result_list = [list(row) for row in result]
            lst1 = [row[0] for row in result_list]
            lst2 = [row[1] for row in result_list]
            lst3 = [row[2] for row in result_list]
            lst4 = [row[3] for row in result_list]
            lst5 = [row[4] for row in result_list]
            lst6 = [row[5] for row in result_list]
            lst7 = [row[6] for row in result_list]            
            df=pd.DataFrame({'Id':lst1,'Name':lst2,'Class':lst3,'Status':lst4,'Quarter':lst5,'PaidAmt':lst6,'Date_&_Time': lst7 })
            print(df.to_markdown())

# Define the function to update Fee details
def update_fee():
    Id = input("Enter student Id: ")
    Name = input("Enter student Name: ")
    Class = input("Enter student Class: ")
    Status = input("Enter student Status(Paid/Due): ")
    Quarter = input("Enter student Quarter: ")
    PaidAmt = input("Enter student PaidAmount: ")  
    cursor = mydb.cursor()
    sqlx = "UPDATE fee SET Name = %s, Class = %s, Status = %s, Quarter = %s,PaidAmt = %s WHERE Id = %s"
    valx = (Name,Class,Status,Quarter,PaidAmt,Id)
    cursor.execute(sqlx, valx)
    mydb.commit()
    print(cursor.rowcount, "record(s) updated.")
    
# Define the function to delete Fee details
def delete_fee():
    Id = input("Enter student Id: ")
    cursor = mydb.cursor()
    sqle = "DELETE FROM fee WHERE Id = %s"
    vale = (Id,)
    cursor.execute(sqle, vale)
    mydb.commit()
    print(cursor.rowcount, "record(s) deleted.")

    # Execute the selected option
    # Get the user's choice
def menu():# Menu function to display menu
    print("_" * 100)
    print("----------------Modules in School Management System ---------")
    print("Module_1: Student record Module ")
    print("Module_2: Staff record Module")
    print("Module_3: Fee record Module")
    print("Module_4: Graphs record")
    print("Module_5: Exit from the system")    
    print("_" * 100)
    
# Get the user's choice:
# if option first:
def getchoice():
    while True:
        create_database()
        create_students()
        create_Staff()
        create_fee()
        menu()
        print("")
        ch = input("Enter your choice: ")# Get the user's choice
        if ch=='1':
            print("PRESS (a): To Add New Student record                                       PRESS (b): View Student details ")
            print("PRESS (c): To Update Student details                                           PRESS (d): Delete Student details")
            ch = input("Enter your choice: ")# Get the user's choice            
            if ch=='a':
                add_student()
                input("Press ENTER KEY to continue.....")
                print()
            elif ch=='b':
                view_students()
                input("Press ENTER KEY to continue.....")
                print()
            elif ch=='c':
                update_student()
                input("Press ENTER KEY to continue.....")
                print()
            elif ch=='d':
                delete_student()
                input("Press ENTER KEY to continue.....")
                print()
## if option Second:
        elif ch=='2':
            print("PRESS (e) : Add New Staff record                                       PRESS (f) : View Staff details | ")
            print("PRESS (g) : UPDATE Staff details                                       PRESS (h) :Delete Staff details   ")
            opp =input("Enter your choice: ")# Get the user's choice
            if opp=='e':
                add_staff()
                input("Press ENTER KEY to continue.....")
                print()
            elif opp=='f':
                view_staff()
                input("Press ENTER KEY to continue.....")
                print()                
            elif opp=='g':
                update_staff()
                input("Press ENTER KEY to continue.....")
                print()                
            elif opp=='h':
                delete_staff()
                input("Press ENTER KEY to continue.....")
                print()                
### if option Third:
        elif ch=='3':
            print("PRESS (i): Add Fee deposit details                                        PRESS (j): View Fee details ")
            print("PRESS (k): Update Fee details                                                PRESS (l): Delete Fee details")
            opp = input("Enter your choice: ")# Get the user's choice            
            if opp=='i':
                fee()
                input("Press ENTER KEY to continue.....")
                print()                
            elif opp=='j':
                view_fee()
                input("Press ENTER KEY to continue.....")
                print()                
            elif opp=='k':
                update_fee()
                input("Press ENTER KEY to continue.....")
                print()                
            elif opp=='l':
                delete_fee()
                input("Press ENTER KEY to continue.....")
                print()                
                break
#### if option Fourth:
        elif ch=='4':
            print("Press (1) to see in the form of Graph b/w Name & Ages ")
            print("Press (2) to see in the form of Graph b/w Name & SALARY ")
            print("Press (3) to see in the form of Graph b/w Name & Paid Amount ")
            print("Press (4) to see in the form of Graph b/w Distribution of Students & Teachers ")#
            print("Press (5) to see in the form of Graph b/w Distribution of Students ID & Name ")
            print("Press (6) to see a Bar Graph b/w Number of Students and their Classes")
            
            ch = input("Enter your choice: ")# Get the user's choice
            if ch == '1':
                cursor = mydb.cursor()
                cursor.execute("SELECT * FROM students")
                result = cursor.fetchall() 
                result_list = [list(row) for row in result]
                lst1 = [row[0] for row in result_list]
                lst2 = [row[1] for row in result_list]
                lst3 = [row[2] for row in result_list]
                lst4 = [row[3] for row in result_list]
                lst5 = [row[4] for row in result_list]
                df = pd.DataFrame({'ID': lst1, 'Name': lst2, 'Age': lst3, 'Gender': lst4, 'Class': lst5})
    # Sort the dataframe by Age in ascending order
                df_sorted = df.sort_values(by='Age')
    # Get the sorted values for 'Name' and 'Age'
                Name = df_sorted['Name'].tolist()
                Age = df_sorted['Age'].tolist()
    # Create the bar chart
                plt.bar(Name, Age, color=['blue', 'green', 'red', 'orange', 'purple'])
                plt.xlabel('Name')
                plt.ylabel('Age')
                plt.title('Student Ages')    
    # Set the y-axis limits and ticks
                plt.ylim(0, 18)  # Set the y-axis limits from 0 to 18
                plt.yticks(range(19))  # Set the y-axis ticks from 0 to 18    
                plt.show()
#--------------------------------------------------------------------------------------------                
# Plotting pie chart
            elif ch == '2':
                cursor = mydb.cursor()
                cursor.execute("SELECT * FROM staff")
                result = cursor.fetchall()
                result_list = [list(row) for row in result]
                lst1 = [row[0] for row in result_list]
                lst2 = [row[1] for row in result_list]
                lst3 = [row[2] for row in result_list]
                lst4 = [row[3] for row in result_list]
                lst5 = [row[4] for row in result_list]
                df=pd.DataFrame({'ID':lst1,'POST':lst2,'NAME':lst3,'SALARY':lst4,'PHONE':lst5})            
                plt.pie(df['SALARY'], labels=df['NAME'], autopct='%1.1f%%')
                plt.title('Staff Salary Distribution')
                plt.show()
#--------------------------------------------------------------------------------------------                
#Plotting line chart
            elif ch == '3':
                cursor = mydb.cursor()
                cursor.execute("SELECT * FROM fee")
                result = cursor.fetchall()
                result_list = [list(row) for row in result]
                lst1 = [row[0] for row in result_list]
                lst2 = [row[1] for row in result_list]
                lst3 = [row[2] for row in result_list]
                lst4 = [row[3] for row in result_list]
                lst5 = [row[4] for row in result_list]
                lst6 = [row[5] for row in result_list]
                df=pd.DataFrame({'Id':lst1,'Name':lst2,'Class':lst3,'Status':lst4,'Quarter':lst5,'PaidAmt':lst6 })    
    # Sort the DataFrame by Quarter in ascending order
                df.sort_values(by='PaidAmt')    
                Name = df['Name']
                PaidAmt = df['PaidAmt']    
                plt.plot(Name, PaidAmt)
                plt.xlabel('Name')
                plt.ylabel('Paid Amount')
                plt.title('Fee Payment Over Quarters')
                plt.show()
#--------------------------------------------------------------------------------------------                
# Plotting pie chart No.of Students & Teachers:
            elif ch == '4':                    
                cursor = mydb.cursor()
                cursor.execute("SELECT * FROM students")
                result = cursor.fetchall()
                result_list = [list(row) for row in result]
                lst1 = [row[0] for row in result_list]
                lst2 = [row[1] for row in result_list]
                lst3 = [row[2] for row in result_list]
                lst4 = [row[3] for row in result_list]
                lst5 = [row[4] for row in result_list]
                df = pd.DataFrame({'ID': lst1, 'Name': lst2, 'Age': lst3, 'Gender': lst4, 'Class': lst5})
                cursor.execute("SELECT * FROM staff")
                result = cursor.fetchall()
                result_list = [list(row) for row in result]
                lst1 = [row[0] for row in result_list]
                lst2 = [row[1] for row in result_list]
                lst3 = [row[2] for row in result_list]
                lst4 = [row[3] for row in result_list]
                lst5 = [row[4] for row in result_list]
                df=pd.DataFrame({'ID':lst1,'POST':lst2,'NAME':lst3,'SALARY':lst4,'PHONE':lst5})            
                # Count the number of students
                cursor.execute("SELECT COUNT(*) FROM students")
                num_students = cursor.fetchone()[0]
                # Count the number of staff (teachers)
                cursor.execute("SELECT COUNT(*) FROM staff")
                num_teachers = cursor.fetchone()[0]             
                # Create a DataFrame for the data
                data = {'Category': ['Students', 'Teachers'], 'Count': [num_students, num_teachers]}
                df = pd.DataFrame(data)
                # Plotting the pie chart
                plt.figure(figsize=(6, 6))
                plt.pie(df['Count'], labels=df['Category'], autopct='%1.1f%%', startangle=140)
                plt.title('Distribution of Students and Teachers')
                plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
                # Show the chart
                plt.show()                
#--------------------------------------------------------------------------------------------
            elif ch=='5':  # Add this block for Line Graph b/w Name & Id
                    cursor = mydb.cursor()
                    cursor.execute("SELECT * FROM students")
                    result = cursor.fetchall()
                    result_list = [list(row) for row in result]
                    lst1 = [row[0] for row in result_list]
                    lst2 = [row[1] for row in result_list]
            # Create a line graph
                    plt.plot(lst1, lst2, marker='o')
                    plt.xlabel('ID')
                    plt.ylabel('Name')
                    plt.title('Line Graph: ID vs Name')
                    plt.show()
            elif ch=='6':
                    cursor = mydb.cursor()
                    cursor.execute("SELECT Class, COUNT(*) as NumStudents FROM students GROUP BY Class")
                    result = cursor.fetchall()
                    result_list = [list(row) for row in result]
                    classes = [row[0] for row in result_list]
                    num_students = [row[1] for row in result_list]
                    # Create a horizontal bar graph
                    plt.barh(classes, num_students, color='skyblue')
                    plt.xlabel('Number of Students')
                    plt.ylabel('Class')
                    plt.title('Number of Students in Each Class')
                    plt.show()
                           
        elif ch=='5':
                print()
                print("Exited !")
                print("Succesfully,")
                print("Thanks")
                print("For")
                print("Coming :-)")
                print()
                print()
                print()
                print()
                exit(0)
                break
        else:
                print("Invalid Choice!")
                press = input("Press Enter key To Continue..")
                menu()        
# Recall Choice function =>
getchoice()
# Disconnecting from the server =>
mydb.close()
