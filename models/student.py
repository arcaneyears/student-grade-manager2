class Person:
    def __init__(self, name, person_id):
        self._name = name
        self._id = person_id

    def get_info(self):
        return f"ID: {self._id}, Name: {self._name}"

class Student(Person):
    def __init__(self, name, student_id):
        super().__init__(name, student_id)
        self._grades = {}

    def add_grade(self, course, grade):
        self._grades[course] = grade

    def get_grades(self):
        return self._grades

    def get_info(self):
        return f"Student {self._id}: {self._name}"