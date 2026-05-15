class GradeService:
    def __init__(self):
        self._students = {}

    def add_student(self, student):
        self._students[student._id] = student

    def calculate_gpa(self, student_id):
        student = self._students.get(student_id)
        if not student:
            raise ValueError(f"Student {student_id} not found")
        grades = student.get_grades()
        if not grades:
            return 0.0
        return round(sum(grades.values()) / len(grades), 2)

    def get_top_students(self, n=5):
        ranked = sorted(
            self._students.values(),
            key=lambda s: self.calculate_gpa(s._id),
            reverse=True
        )
        for student in ranked[:n]:
            yield student

    def filter_by_course(self, course_name):

        return list(filter(
            lambda s: course_name in s.get_grades(),
            self._students.values()
        ))

    def get_all_students(self):
        return list(self._students.values())