import logging

logging.basicConfig(format='%(asctime)-15s:  %(message)s', level=logging.INFO)

letter = {
    "A+": 4.0,
    "A": 4.0,
    "A-": 3.7,
    "B+": 3.3,
    "B": 3,
    "B-": 2.7,
    "C+": 2.3,
    "C": 2.0,
    "C-": 1.7,
    "D+": 1.3,
    "D": 1.0,
    "D-": .7,
    "F": 0
}

class Course:
    def __init__(self, term, class_code, class_name, class_type, points, grade):
        self.term = term
        self.class_code = class_code
        self.class_name = class_name
        self.class_type = class_type
        self.points = points
        self.grade = self.convert_gpa_letter_to_num(grade)

    def convert_gpa_letter_to_num(self, letter_grade: str) -> float:
        global letter
        if letter_grade in letter.keys():
            return letter[letter_grade]
        else:
            return -1.0

    def get_subject_from_class_code(self) -> str:
        if "-" in self.class_code:
            return self.class_code.split("-")[0]
        else:
            return "N/A"
