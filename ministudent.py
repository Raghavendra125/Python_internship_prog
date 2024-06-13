    
# storing the student details in list of dictionaries
students = [
    {"usn": "CS001", "name": "Amar", "branch": "CSE", "year": "2"},
    {"usn": "CS010", "name": "Bhuvan", "branch": "ECE", "year": "3"},
    {"usn":"ME001","name":"kishan","branch":"ME","year":"3"},
    {"usn":"ME002","name":"vignesh","branch":"ME","year":"3"}
    
]
# Admin Credentials
admin_username = "administrator"
admin_password = "admin@123"

# Admin Login
def admin_login():
    print(" -----ADMIN LOGIN----- ")
    adminuser = input("Enter admin username: ")
    adminpasswd = input("Enter admin password: ")
    if adminuser == admin_username and adminpasswd == admin_password:
         disp_menu()
          
    else:
        print("Invalid credentials.")
        return False

username ="myname"
password ="me@123" 
# User Login
def user_login():
    print(" -----USER LOGIN-----")
    stduser = input("Enter  username: ")
    stdpasswd = input("Enter  password: ")
    if stduser == username and stdpasswd == password:
        disp_students()
    else:
        print("Invalid credentials.")
        return False
    

# CRUD Operations
def create_student():
        usn = input("Enter USN: ")
        name = input("Enter name: ")
        branch = input("Enter branch: ")
        year = input("Enter year: ")
        students.append({"usn": usn, "name": name, "branch": branch, "year": year})
        print("Student added successfully.")
        disp_menu()

def disp_students():
        print("Student Information:")
        for student in students:
            print(f"USN: {student['usn']}, Name: {student['name']}, Branch: {student['branch']}, Year: {student['year']}")
        

def update_student():
        usn = input("Enter USN of student to update: ")
        for student in students:
            if student["usn"] == usn:
                student["name"] = input("Enter updated name: ")
                student["branch"] = input("Enter updated branch: ")
                student["year"] = input("Enter updated year: ")
                print("Student updated successfully.")
                return
        print("Student not found.")
        disp_menu()

def delete_student():
        usn = input("Enter USN of student to delete: ")
        for student in students:
            if student["usn"] == usn:
                students.remove(student)
                print("Student deleted successfully.")
                return
        print("Student not found.")
        disp_menu()

#  Menu
def disp_menu():
    print("\nMenu:")
    print("1. view Student Information")
    print("2. Create Student")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        disp_students()
    elif choice == "2":
        create_student()
    elif choice == "3":
        update_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        exit()
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
while True:
    ch = input("PLEASE SELECT WHO ARE USING THE API\n(1) Admin\n(2) Student\n(3) exit\n")
    if ch == "1":
        admin_login()
    elif ch == "2":
        user_login()
    elif ch == "3":
        exit()


