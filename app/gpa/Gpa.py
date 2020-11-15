import logging

logging.basicConfig(format='%(asctime)-15s:  %(message)s', level=logging.INFO)

class Gpa:
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
        "F": 0,
        "WF": 0,
        "WU": 0
    }

    def __init__(self, course_list):
        self.course_list = course_list

    def get_total_gpa(self) -> float:
        invalid_grades = []
        gpa_sum = 0
        credit_sum = 0
        if len(self.course_list) > 0:
            for course in self.course_list:
                if self.is_valid_gpa(course.grade):
                    gpa_sum += course.get_grade_num() * float(course.credit)
                    credit_sum += course.credit
                else:
                    invalid_grades.append(course.grade)
            if credit_sum > 0:
                return round(gpa_sum/credit_sum, 3)
        logging.warning("No valid courses that contains a GPA{}"
                        .format((".  Grades Passed In: " + ", ".join(invalid_grades)) if len(invalid_grades) > 0 else ""))
        return -1

    @staticmethod
    def is_valid_gpa(gpa) -> bool:
        return True if gpa in Gpa.letter.keys() else False
