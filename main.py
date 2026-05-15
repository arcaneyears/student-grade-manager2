from models.student import Student
from services.grade_service import GradeService
from utils.file_handler import load_from_csv, save_report_json
from utils.report_generator import generate_summary, print_top_students

def main():
    service = GradeService()
    records = load_from_csv("data/grades.csv")

    for row in records:
        sid = int(row['student_id'])
        student = Student(row['name'], sid)
        student.add_grade(row['course'], float(row['grade']))
        service.add_student(student)

    while True:
        print("\n1. Show all GPAs  2. Top students  3. Save report  4. Exit")
        choice = input("Choice: ").strip()
        if choice == '1':
            for s in service.get_all_students():
                print(f"{s.get_info()} | GPA: {service.calculate_gpa(s._id)}")
        elif choice == '2':
            print_top_students(service)
        elif choice == '3':
            report = generate_summary(service)
            save_report_json("data/report.json", report)
            print("Report saved.")
        elif choice == '4':
            break

if __name__ == '__main__':
    main()