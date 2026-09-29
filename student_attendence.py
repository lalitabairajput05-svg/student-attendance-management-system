# Student Attendance Management System

def add_student():
    roll = input("Enter roll number: ")
    name = input("Enter student name: ")

    # check if roll number already exists
    try:
        f = open("attendance.txt", "r")
        for line in f:
            row = line.strip().split(",")
            if row[0] == roll:
                print("Roll number already exists!")
                f.close()
                return
        f.close()
    except:
        pass

    f = open("attendance.txt", "a")
    f.write(roll + "," + name + ",0,0\n")
    f.close()
    print("Student added successfully!")


def mark_attendance():
    try:
        f = open("attendance.txt", "r")
        students = []
        for line in f:
            students.append(line.strip().split(","))
        f.close()
    except:
        print("No student records found!")
        return

    if len(students) == 0:
        print("No students in file.")
        return

    print("\n--- Student List ---")
    for i in range(len(students)):
        print(str(i + 1) + ". " + students[i][0] + " - " + students[i][1])

    num = int(input("\nSelect student number: "))
    if num < 1 or num > len(students):
        print("Invalid student number!")
        return

    status = input("Enter P for Present or A for Absent: ").upper()
    if status == "P":
        students[num - 1][2] = str(int(students[num - 1][2]) + 1)
        print("Marked as Present")
    elif status == "A":
        students[num - 1][3] = str(int(students[num - 1][3]) + 1)
        print("Marked as Absent")
    else:
        print("Please enter only P or A")
        return

    # update file
    f = open("attendance.txt", "w")
    for s in students:
        f.write(s[0] + "," + s[1] + "," + s[2] + "," + s[3] + "\n")
    f.close()


def view_attendance():
    try:
        f = open("attendance.txt", "r")
    except:
        print("No records found!")
        return

    print("\n------------------------------------------------------------")
    print("Roll No\t\tName\t\tPresent\tAbsent\tPercentage")
    print("------------------------------------------------------------")

    for line in f:
        row = line.strip().split(",")
        p = int(row[2])
        a = int(row[3])
        total = p + a

        if total > 0:
            pct = (p / total) * 100
        else:
            pct = 0

        print(row[0] + "\t\t" + row[1] + "\t\t" + str(p) + "\t" + str(a) + "\t" + str(round(pct, 2)) + "%")

    f.close()
    print("------------------------------------------------------------")


def search_student():
    r = input("Enter roll number to search: ")

    try:
        f = open("attendance.txt", "r")
    except:
        print("No records found!")
        return

    found = 0
    for line in f:
        row = line.strip().split(",")
        if row[0] == r:
            p = int(row[2])
            a = int(row[3])
            total = p + a

            if total > 0:
                pct = (p / total) * 100
            else:
                pct = 0

            print("\n--- Student Details ---")
            print("Roll Number :", row[0])
            print("Name        :", row[1])
            print("Present     :", p)
            print("Absent      :", a)
            print("Attendance  :", round(pct, 2), "%")
            found = 1
            break

    f.close()

    if found == 0:
        print("Student not found!")


def main():
    while True:
        print("\n--- ATTENDANCE MANAGEMENT SYSTEM ---")
        print("1. Add Student")
        print("2. Mark Attendance")
        print("3. View Attendance")
        print("4. Search Student")
        print("5. Exit")

        ch = input("Enter choice (1-5): ")

        if ch == "1":
            add_student()
        elif ch == "2":
            mark_attendance()
        elif ch == "3":
            view_attendance()
        elif ch == "4":
            search_student()
        elif ch == "5":
            print("Exiting program. Thank you!")
            break
        else:
            print("Invalid choice, try again.")


main()
