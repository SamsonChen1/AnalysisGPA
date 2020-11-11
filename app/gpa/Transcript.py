import csv
import logging
from app.gpa.Course import Course, letter

logging.basicConfig(format='%(asctime)-15s:  %(message)s', level=logging.INFO)

class Transcript:
    def __init__(self, file_name):
        self.file_name = file_name
        self.transcript = self.get_transcript_content()

    def get_transcript_content(self) -> list:
        transcript = []
        with open(self.file_name, newline='') as f:
            csv_content = csv.reader(f)
            next(f)     #skips the header of the transcript
            for row in csv_content:
                transcript.append(Course(int(row[0].strip()), row[1], row[2], row[3], row[4], row[5]))
        return transcript

    def get_all_courses(self) -> list:
        return [course for course in self.transcript]

    def get_split_courses(self) -> (list, list):
        valid_courses = []
        invalid_courses = []
        for course in self.transcript:
            if course.grade in letter:
                valid_courses.append(course)
            else:
                invalid_courses.append(course)
        return valid_courses, invalid_courses

    def get_total_gpa(self, course_list) -> float:
        gpa_sum = 0
        num_of_courses = len(course_list)
        if num_of_courses > 0:
            for course in course_list:
                gpa_sum += course.get_num_grade()
            return round(gpa_sum/num_of_courses, 2)
        else:
            logging.warning("No valid courses that contains a GPA")
            return -1

    def get_total_valid_gpa(self) -> float:
        return self.get_total_gpa(self.get_split_courses()[0])

    def get_all_info_for_term(self, term_num: int) -> list:
        term_info = []
        for course in self.get_all_courses():
            if course.term == term_num:
                term_info.append(course)
        num_of_classes = len(term_info)
        if num_of_classes > 0:
            logging.info(f"Found {num_of_classes} classes taken during Term {term_num}")
        else:
            logging.warning(f"No classes was found for Term {term_num}")
        return term_info
