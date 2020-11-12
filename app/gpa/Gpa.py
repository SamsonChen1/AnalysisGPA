import logging
from app.gpa.Course import Course, letter

logging.basicConfig(format='%(asctime)-15s:  %(message)s', level=logging.INFO)

class Gpa:
    def __init__(self, course_list):
        self.course_list = course_list

    def get_total_gpa(self) -> float:
        courses = self.course_list
        gpa_sum = 0
        num_of_valid_courses = 0
        if len(courses) > 0:
            for course in courses:
                grade = course.get_num_grade()
                if self.is_valid_gpa(grade):
                    num_of_valid_courses += 1
                    gpa_sum += grade
            if num_of_valid_courses > 0:
                return round(gpa_sum/num_of_valid_courses, 2)
        logging.warning("No valid courses that contains a GPA")
        return -1

    @staticmethod
    def is_valid_gpa(gpa) -> bool:
        return True if gpa in letter.keys() else False
