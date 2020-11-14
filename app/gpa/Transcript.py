import csv
import logging
from app.gpa.Course import Course

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
                transcript.append(Course(int(row[0].strip()), row[1], row[2], row[3], int(row[4]), row[5]))
        logging.info(f"Extracted {len(transcript)} course(s) from the transcript")
        return transcript

    def get_latest_term_num(self) -> int:
        term = -1
        for course in self.transcript:
            if course.term > term:
                term = course.term
        return term

    def get_split_courses(self) -> (list, list):
        valid_courses = []
        invalid_courses = []
        for course in self.transcript:
            if course.grade in letter:
                valid_courses.append(course)
            else:
                invalid_courses.append(course)
        logging.info(f"Count of split courses found.   Valid: {len(valid_courses)}    Invalid: {len(invalid_courses)}")
        return valid_courses, invalid_courses

    def get_all_info_for_term(self, term_num: int) -> list:
        term_info = []
        for course in self.transcript:
            if course.term == term_num:
                term_info.append(course)
        num_of_classes = len(term_info)
        if num_of_classes > 0:
            logging.info(f"Found {num_of_classes} classes taken during Term {term_num}")
        else:
            logging.warning(f"No classes was found for Term {term_num}")
        return term_info

    def split_course_by_type(self, course_list) -> dict:
        courses_by_type = {}
        for course in course_list:
            curr_types = courses_by_type.keys()
            if course.class_type in curr_types:
                logging.info(f"Appending course {course.class_code} to the dict of type {course.class_type}")
                courses_by_type[course.class_type].append(course)
            else:
                logging.info(f"Adding course {course.class_code} to the dict of type {course.class_type}")
                courses_by_type[course.class_type] = [course]
        logging.info(f"Found {len(curr_types)} different course types. Types: {', '.join(curr_types)}")
        return courses_by_type
