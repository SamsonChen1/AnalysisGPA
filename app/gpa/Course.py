import logging
from app.gpa.Gpa import Gpa

logger = logging.getLogger(__name__)

class Course:
    def __init__(self, term, class_code, class_name, class_type, credit, grade):
        self.term: int = term
        self.class_code: str = class_code
        self.class_name: str = class_name
        self.class_type: str = class_type
        self.credit: int = credit
        self.grade: str = grade

    def get_grade_num(self) -> float:
        if self.grade in Gpa.letter.keys():
            return Gpa.letter[self.grade]
        else:
            return -1.0

    def get_subject_from_class_code(self) -> str:
        if "-" in self.class_code:
            return self.class_code.split("-")[0]
        else:
            return "N/A"

    def get_attr_value(self, attr_name):
        return getattr(self, attr_name)
