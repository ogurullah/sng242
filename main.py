import json

with open('data.json', 'r') as file:
    data = json.load(file)
    if data: 
        print("Data loaded successfully.")
    else:
        print("No data found in the file.")

# Example of how to access and print data from the loaded JSON
# Uncomment the following lines to see the structure of the data

#for dept_code, dept_info in data["departments"].items():
#    print(f"{dept_code} - {dept_info['name']}")

#Example of how to access student data

#for student in data["students"]:
#    name = student["name"]
#    dept = student["department"]
#    print(f"{name} is in {dept}")

def get_student_by_id(student_id):
    for student in data["students"]:
        if student["student_id"] == student_id:
            print(f"Found student: {student['name']}")
            return student
    print("Student not found.")
    return None

get_student_by_id("20241001")


def get_department_by_id(department_id):
    for department in data["departments"].values():

        # Assuming department_id is a string, adjust if necessary
        if isinstance(department_id, int):
            department_id = str(department_id)
        elif not isinstance(department_id, str):
            print("Invalid department_id type. Must be a string or convertible to string.")
            return None
        
        if department["department_id"] == department_id:
            print(f"Found department: {department['name']}")
            return department
    print("Department not found.")
    return None

get_department_by_id("389")
get_department_by_id(389)  # Example with integer input
get_department_by_id("999")  # Example with non-existent ID

        
