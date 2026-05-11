import unittest
from models.student import Student
from models.grade import Grade
from services.grade_service import GradeService

class TestGradeService(unittest.TestCase):

    def setUp(self):
        self.service = GradeService()
        s = Student("Alice", 1)
        s.add_grade("Math", 90)
        s.add_grade("Physics", 80)
        self.service.add_student(s)

    def test_gpa_calculation(self):
        self.assertEqual(self.service.calculate_gpa(1), 85.0)

    def test_invalid_student(self):
        with self.assertRaises(ValueError):
            self.service.calculate_gpa(999)

    def test_top_students_is_generator(self):
        import types
        result = self.service.get_top_students()
        self.assertIsInstance(result, types.GeneratorType)

    def test_empty_grades(self):
        s = Student("Bob", 2)
        self.service.add_student(s)
        self.assertEqual(self.service.calculate_gpa(2), 0.0)

if __name__ == '__main__':
    unittest.main()