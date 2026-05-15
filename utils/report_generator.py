def generate_summary(service):
    report = {}
    for student in service.get_all_students():
        gpa = service.calculate_gpa(student._id)
        report[student._id] = {
            "name": student._name,
            "gpa": gpa,
            "grades": student.get_grades()
        }
    return report

def print_top_students(service, n=3):
    print(f"\n--- Top {n} Students ---")
    for student in service.get_top_students(n):
        gpa = service.calculate_gpa(student._id)
        print(f"  {student.get_info()} | GPA: {gpa}")