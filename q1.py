import psycopg2

# Connect to the student database
def connect():
    try:
        # 
        con = psycopg2.connect(
            host = "localhost",
            database = "COMP3005A3Q1", # Update depending on your DB name
            user = "postgres",
            password = "student", # Update depending on your account password
            port = "5432"
        )
        print("Successfully connected to DB")
        return con
    except(Exception, psycopg2.Error) as error:
        print("Couldn't connect to DB: ", error)
        return None

# Retrieves all students from DB and prints to console
def getAllStudents(connection):
    print("All students")
    try:
        # Select ALL command
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM students")
            rows = cursor.fetchall()
            for r in rows:
                print(r)
    except psycopg2.Error as error:
        print("Error printing students: ", error)

# Appends new student to DB
def addStudent(connection, fname, lname, email, date):
    try:
        # Add new entry command
        with connection.cursor() as cursor:
            cursor.execute("""INSERT INTO students (first_name, last_name, email, enrollment_date)
                           VALUES(%s,%s,%s,%s)
                           RETURNING student_id, first_name, last_name, email, enrollment_date;
                           """, (fname, lname, email, date)
                            )
            
            # Printing added student
            newStu = cursor.fetchone()
            print("\nStudent", newStu, "successfully added")
            connection.commit()

    except psycopg2.Error as e:
        print("Error adding student: ", e)

# Updates email of matching sutdent ID with passed in email
def updateEmail(connection, sId, email):
    try:
        with connection.cursor() as cursor:
            cursor.execute("""UPDATE students
                           SET email = %s
                           WHERE student_id = %s
                           RETURNING student_id, first_name, last_name, email, enrollment_date;
                           """, (email, sId))
            
            # Printing updated student
            newStu = cursor.fetchone()
            print("\nStudent email changed: ", newStu)
            connection.commit()

    except psycopg2.Error as e:
        print("Error updating email: ", e)

# Uses gonerId to ssearch through DB to delete chosen student
def deleteStudent(connection, gonerId):
    try:
        with connection.cursor() as cursor:
            cursor.execute("""DELETE FROM students 
                           WHERE student_id = %s
                           RETURNING student_id, first_name, last_name, enrollment_date;
                           """, (gonerId,))
            
            # Printing deleted student
            goner = cursor.fetchone()
            print("\nStudent deleted", goner)
            connection.commit()

    except psycopg2.Error as e:
        print("Error deleting student: ", e)
    

def main():
    num = ""
    # Showing CRUD menu until user chooses to exit
    while num != "5":
        num = input("""Choose your option: 
1 - Print all students: 
2 - Add student: 
3 - Update student email: 
4 - Delete Student: 
5 - Exit program\n""")
        match num:
            case "1":
                getAllStudents(con)
            case "2":
                fname = input("Enter Student First Name: ")
                lname = input("Enter Student Last Name: ")
                email = input("Enter Student email: ")
                date = input("Enter student Enrollment date (YYYY-MM_DD): ")
                addStudent(con, fname, lname, email, date)
            case "3":
                sId = input("Enter ID of student whose email to update: ")
                nEmail = input("Enter new Email address: ")
                updateEmail(con, sId, nEmail)
            case "4":
                gonerId = input("Enter ID of student you want to delete: ")
                deleteStudent(con, gonerId)
            case "5":
                print("Exiting program...")
            case _:
                print("Enter valid input")


if __name__ == "__main__":
    global con
    con = connect()
    main()
    con.close()