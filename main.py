import json
import os
from collections import defaultdict
from fpdf import FPDF

# Will be used to convert letter grades to point grades
GRADINGS = {
    "AA": 4.0, "BA": 3.5, "BB": 3.0, "CB": 2.5, "CC": 2.0,
    "DC": 1.5, "DD": 1.0, "FD": 0.5, "FF": 0.0, "NA": 0.0,
}

# Will be used to exclude certain grades from GPA/CGPA calculations
EXCLUDED_GRADES = {"EX", "W", "I"}

# Load data from our database file
def load_data(file_path="data.json"):
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)
    
def calculate_gpa(semester_courses):

    total_points = 0.0  # float
    total_credits = 0   # int

    for course in semester_courses:
        grade = course["grade"]
        if grade in EXCLUDED_GRADES:
            continue  # Skip excluded grades

        # Convert letter grade to point grade
        points = GRADINGS.get(grade, 0)
        # 0 is for any unrecognized grade

        credits = course["credits"]
        total_points += points * credits
        total_credits += credits

    # Calculate GPA only if there are credits
    if total_credits > 0:
        gpa = total_points / total_credits
        return round(gpa, 2)
    else:
        return 0.0

def calculate_cgpa(semesters):
    # Dictionary for storing the latest grade for each course
    # Since a course can be taken multiple times, we need to keep track of the latest valid grade 
    latest_grades = {}

    # Go through each semester and collect the latest valid grade for each course
    # This will overwrite any previous grades for the same course code because loop goes over courses in chronological order
    for semester in semesters:
        for course in semester["courses"]:
            grade = course["grade"]
            code = course["code"]

            if grade in EXCLUDED_GRADES: #Skip excluded grades
                continue

            # Update the latest grade (overwrites if course was taken before)
            latest_grades[code] = course

    total_points = 0.0 #float
    total_credits = 0 #int

    for course in latest_grades.values():
        grade = course["grade"]
        credits = course["credits"]

        # Convert letter grade to point grade
        points = GRADINGS.get(grade, 0)
        # 0 is for any unrecognized grade

        total_points += points * credits
        total_credits += credits

    # Final CGPA calculation
    if total_credits > 0:
        cgpa = total_points / total_credits
        return round(cgpa, 2)
    else:
        return 0.0

def generate_pdf(student, gpa_data, cgpa, output_dir="transcripts"):
    os.makedirs(output_dir, exist_ok=True)
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"Transcript for {student['name']} ({student['student_id']})", ln=True)
    pdf.cell(200, 10, txt=f"Department: {student['department']} | Curriculum: {student['curriculum_version']}", ln=True)
    pdf.ln(5)
    for sem, (gpa, courses) in gpa_data.items():
        pdf.set_font("Arial", style="B", size=11)
        pdf.cell(200, 10, txt=f"{sem} - GPA: {gpa}", ln=True)
        pdf.set_font("Arial", size=10)
        for c in courses:
            pdf.cell(200, 8, txt=f"{c['code']}: {c['name']} ({c['grade']})", ln=True)
        pdf.ln(2)
    pdf.set_font("Arial", style="B", size=12)
    pdf.cell(200, 10, txt=f"CGPA: {cgpa}", ln=True)
    path = os.path.join(output_dir, f"{student['student_id']}_transcript.pdf")
    pdf.output(path)
    print(f"Transcript saved: {path}")

def generate_transcript(student):
    gpa_data = {}
    for semester in student["semesters"]:
        gpa = calculate_gpa(semester["courses"])
        gpa_data[semester["name"]] = (gpa, semester["courses"])
    cgpa = calculate_cgpa(student["semesters"])
    generate_pdf(student, gpa_data, cgpa)

def main():
    data = load_data()
    print("----- Transcript Generator -----")
    print("1. Generate transcript for a student with ID:")
    print("2. Generate transcripts for a departments all students:")
    print("3. Generate transcripts for all students in the university:")
    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        student_id = input("Enter student ID: ")
        student = next((s for s in data["students"] if s["student_id"] == student_id), None)
        if student:
            generate_transcript(student)
        else:
            print("Student not found.")

    elif choice == "2":
        dept_code = input("Enter department code (e.g., CMPE): ").upper()
        students = [s for s in data["students"] if s["department"] == dept_code]
        if not students:
            print("No students found in that department.")
        for student in students:
            generate_transcript(student)

    elif choice == "3":
        for student in data["students"]:
            generate_transcript(student)
    else:
        print("Invalid choice. Exiting.")

if __name__ == "__main__":
    main()
