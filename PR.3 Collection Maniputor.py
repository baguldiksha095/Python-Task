print("=" * 40)
print("WELCOME TO THE STUDENT DATA ORGANIZER!")
print("=" * 40)

students = {}

subjects_offered = ["Math", "Science", "English"]

while True:
    print("\nSelect an Option:")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")

    choice = input("\nEnter your choice: ")

    match choice:

        case "1":
            print("\n----- ENTER STUDENT DETAILS -----")

            student_id = input("Student ID: ")

            if student_id in students:
                print("Student ID already exists!")
                continue

            name = input("Name: ")
            age = input("Age: ")
            grade = input("Grade: ")
            dob = input("DOB (YYYY-MM-DD): ")
            subjects = input("Subjects (comma-separated): ")

            students[student_id] = {
                "Name": name,
                "Age": age,
                "Grade": grade,
                "DOB": dob,
                "Subjects": subjects
            }

            print("\nStudent added successfully!")

        case "2":
            print("\n----- DISPLAY ALL STUDENTS -----")
            if not students:
                print("No student records found!")
            else:
                for student_id, details in students.items():
                    print(f"\nStudent ID: {student_id}")
                    for key, value in details.items():
                        print(f"{key}: {value}")
        case "3":
            print("\n----- UPDATE STUDENT INFORMATION -----")

            student_id = input("Enter Student ID to update: ")

            if student_id in students:
                print("Enter new details (press Enter to keep existing values):")

                for key in students[student_id]:
                    current_value = students[student_id][key]
                    new_value = input(f"{key} ({current_value}): ")

                    if new_value.strip():
                        students[student_id][key] = new_value

                print("\nStudent information updated successfully!")
            else:
                print("Student ID not found!")

        case "4":
            print("\n----- DELETE STUDENT -----")

            student_id = input("Enter Student ID to delete: ")

            if student_id in students:
                del students[student_id]
                print("Student deleted successfully!")
            else:
                print("Student ID not found!")

        case "5":
            print("\n----- SUBJECTS OFFERED -----")

            for subject in subjects_offered:
                print("-", subject)

        case "6":
            print("\nThank you for using the Student Data Organizer!")
            print("Exiting the program. Goodbye!")
            break

        case _:
            print("Invalid choice! Please select an option from 1 to 6.")