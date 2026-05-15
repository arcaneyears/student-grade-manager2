# Student Grade Management System

A Python command-line application for managing students, courses, and grades. Built as a final project for Introduction to Programming 2.

## Features

- Add students and assign grades per course
- Calculate GPA for each student
- View top-performing students
- Generate reports saved as JSON
- Load and save data using CSV files

## How to Run

1. Clone the repository:
   ```
   git clone https://github.com/your-team/student-grade-manager.git
   cd student-grade-manager
   ```

2. (Optional) Create a virtual environment:
   ```
   python -m venv venv
   venv\Scripts\activate      # Windows
   source venv/bin/activate   # Mac/Linux
   ```

3. Run the program:
   ```
   python main.py
   ```

4. Run tests:
   ```
   python -m unittest discover tests/
   ```

## Data Format

Place your input file at `data/grades.csv` with the following format:

```
student_id,name,course,grade
1,John,Math,85
2,Alice,Physics,90
```

| Column | Type | Description |
|---|---|---|
| student_id | integer | Unique ID for each student |
| name | string | Full name of the student |
| course | string | Course name |
| grade | float | Numeric grade (0–100) |

Generated reports are saved to `data/report.json` automatically.

## Project Structure

```
student-grade-manager/
├── models/          # OOP classes: Student, Course, Grade
├── services/        # Business logic: GPA calculation, rankings
├── utils/           # File I/O and report generation
├── tests/           # Unit tests
├── data/            # Input CSV and output JSON
└── main.py          # Entry point / CLI menu
```

## Team Members

| Name | Role |
|---|---|
| Member 1 | models/ — Student, Course, Grade classes |
| Member 2 | services/ — GradeService, GPA logic |
| Member 3 | utils/ — File I/O, report generator |
| Member 4 | tests/ + main.py — Unit tests, CLI menu |
