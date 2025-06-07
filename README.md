
# Transcript Management System (CLI-Based)

A lightweight command-line tool to generate university transcripts for students, designed with versioned curriculum support and GPA/CGPA calculations. Built for GNU/Linux platforms.

---

## 📌 Features

- CLI-based interaction (no GUI)
- Handles multiple curriculum versions per department
- Stores data in structured JSON file
- Generates formatted PDF transcripts
- Supports:
  - Repeated courses (last grade used for CGPA)
  - Exempt courses (ignored from GPA/CGPA)
- Department-wide and university-wide transcript generation
- Curriculum parser supporting inline comments (`#`)

---

## 🛠 Technologies Used

- **Language:** Python 3.x
- **Storage:** JSON
- **Platform:** Linux / WSL on Windows
- **Transcript Export:** PDF

---

## ⚙️ How to Run

```bash
# Clone the repo
git clone https://github.com/ogurullah/sng242.git

# Run the program
python main.py
```

---


## 🧮 GPA & CGPA Rules

- **Repeated Courses:** Only the most recent grade is counted for CGPA.
- **GPA:** Calculated per semester using total points / total credits.
- **CGPA:** Cumulative points / credits, ignoring previous grades for repeated courses.
- **Exempt Courses:** Ignored from all GPA/CGPA calculations.

---

## 🔄 Roadmap

| Week | Goals |
|------|-------|
| 1    | Team setup, tech stack, build database, implement functions |
| 2    | GPA/CGPA engine, CLI commands, PDF output generation |
| 3    | Bug fixes, edge case tests, polishing, finalization |

---

## 📬 Contact

For questions, contact [celik.oguz@metu.edu.tr] or open an issue in the repository.
