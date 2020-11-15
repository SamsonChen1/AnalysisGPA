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

    def split_course_by_attr(self, course_list, attr) -> dict:
        split_course = {}
        for course in course_list:
            if attr == "class_code":
                attr_value = course.get_subject_from_class_code()
            else:
                attr_value = course.__getattribute__(attr)
            if attr_value in split_course.keys():
                logging.info(f"Appending course {course.class_code} to the dict of {attr_value} for {attr}")
                split_course[attr_value].append(course)
            else:
                logging.info(f"Adding course {course.class_code} to the dict of {attr}")
                split_course[attr_value] = [course]
        logging.info(f"Found {len(split_course.keys())} different course types. {attr}: {', '.join(split_course.keys())}")
        return split_course