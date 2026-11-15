students = []

def add_student():
    name = input("Enter student name: ")
    age = input("Enter student age: ")
    roll_no = input("Enter roll number: ")
    course = input("Enter course: ")

    student = {
        "Name": name,
        "Age": age,
        "Roll No": roll_no,
        "Course": course
    }

    students.append(student)
    print("Student added successfully!")


def view_students():
    if not students:
        print("No students found!")
    else:
        for student in students:
            print(student)


def search_student():
    roll_no = input("Enter roll number: ")

    for student in students:
        if student["Roll No"] == roll_no:
            print("Student Found:", student)
            return

    print("Student not found!")


def main():
    while True:
        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            print("Thank you!")
            break
        else:
            print("Invalid choice!")


main()