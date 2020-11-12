import logging
from app.gpa.Course import Course, letter

logging.basicConfig(format='%(asctime)-15s:  %(message)s', level=logging.INFO)

class Gpa:
    def __init__(self, course_list):
        self.course_list = course_list

    def get_total_gpa(self) -> float:
        invalid_grades = []
        gpa_sum = 0
        num_of_valid_courses = 0
        if len(self.course_list) > 0:
            for course in self.course_list:
                if self.is_valid_gpa(course.grade):
                    num_of_valid_courses += 1
                    gpa_sum += course.get_grade_num()
                else:
                    invalid_grades.append(course.grade)
            if num_of_valid_courses > 0:
                return round(gpa_sum/num_of_valid_courses, 2)
        logging.warning("No valid courses that contains a GPA{}"
                        .format((".  Grades Passed In: " + ", ".join(invalid_grades)) if len(invalid_grades) > 0 else ""))
        return -1

    @staticmethod
    def is_valid_gpa(gpa) -> bool:
        return True if gpa in letter.keys() else False
