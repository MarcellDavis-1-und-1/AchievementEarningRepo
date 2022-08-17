import mysql.connector
import getpass
def log_in(password):
    global mydb
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password=password
    )
    mycursor = mydb.cursor()
    mycursor.execute("USE STUDENTMANAGEMENTADVANCED;")
    mycursor.execute("SELECT * FROM STUDENT;")
    for x in mycursor:
        print(x)
    mycursor.execute("")
# Press the green button in the gutter to run the script.
def print_all_commands():
    print("h: show all commands\n"
          "exit: quit program"
          "add student: Add to table student"
          "print students: Show all entries in student"
          "add exam: Add to table exam"
          "add exam res: Add to table examRes")
def add_student():
    print("ENTERING STUDENT\n")
    name = input("Enter name: ")
    first_name = input("\nEnter first name: ")
    nationality = input("\nEnter nationality: ")
    birthday = input("\nEnter birthday (YYYY-MM-DD): ")
    mycursor = mydb.cursor()
    mycursor.execute(f"INSERT INTO STUDENT (name, firstName, nationality, birthday) VALUES ('{name}', '{first_name}', '{nationality}', '{birthday}');")
def print_students():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM STUDENT;")
def add_exam():
    print("ENTERING EXAM")
    moduleName = input("Enter module name: ")
    professor = input("Enter professor name: ")
    fieldName = input("Enter field name: ")
    mycursor = mydb.cursor()
    mycursor.execute(f"INSERT INTO EXAM (fieldId, professorName, moduleName)"
                     f"VALUES ((SELECT F.Id FROM FIELD F WHERE F.NAME = '{fieldName}'), '{professor}', '{moduleName}');")
    mycursor.execute("COMMIT;")
def add_exam_res():
    print("ENTERING EXAM RES")
    studentName = input("Enter student last name: ")
    studentFirstName = input("Enter student first name: ")
    examId = input("Enter exam id: ")
    grade = input("Enter grade: ")
    mycursor = mydb.cursor()
    mycursor.execute(f"INSERT INTO EXAMRES (examId, grade) VALUES ({examId}, {grade});")
    mycursor.execute("COMMIT;")
    mycursor.execute(f"INSERT INTO STUDENTEXAMRES (studentId, examResId) VALUES ((SELECT S.id FROM STUDENT S WHERE S.name = '{studentName}' AND S.firstName = '{studentFirstName}'),"
                     f"(SELECT ER.id FROM EXAMRES ER JOIN EXAM E ON ER.examId = E.id WHERE E.id = {examId}))")
    mycursor.execute("COMMIT;")

def input_loop():
        action = input("What do you want to do ?(press h to see command list):")
        if (action == 'exit'):
            exit(0)
        if (action == 'h'):
            print_all_commands()
        if (action == 'add student'):
            add_student()
        if (action == 'print students'):
            print_students()
        if (action == 'add exam'):
            add_exam()
        if (action == 'add exam res'):
            add_exam_res()
        input_loop()


if __name__ == '__main__':
    log_in(getpass.getpass("Please enter your password: "))
    input_loop()
