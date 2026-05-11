class Grade:
    LETTER_MAP = {
        (90, 100): 'A',
        (80, 89):  'B',
        (70, 79):  'C',
        (60, 69):  'D',
        (0,  59):  'F'
    }
    def __init__(self, student_id, course, score):
        self.student_id = student_id
        self.course = course
        self.score = score

    def get_letter(self):
        for (low, high), letter in self.LETTER_MAP.items():
            if low <= self.score <= high:
                return letter