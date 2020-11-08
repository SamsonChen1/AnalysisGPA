import csv
import logging
from app.gpa.Course import Course

logging.basicConfig(format='%(asctime)-15s:  %(message)s', level=logging.INFO)

class Transcript:
    def __init__(self, file_name):
        self.file_name = file_name

    def get_transcript_content(self) -> list:
        transcript = []
        with open(self.file_name, newline='') as f:
            csv_content = csv.reader(f)
            next(f)     #skips the header of the transcript
            for row in csv_content:
                transcript.append(Course(int(row[0].strip()), row[1], row[2], row[3], row[4], row[5]))
        return transcript

    def get_all_info_for_term(self, transcript: list, term_num: int) -> list:
        term_info = []
        for course in transcript:
            if course.term == term_num:
                term_info.append(course)
        num_of_classes = len(term_info)
        if num_of_classes > 0:
            logging.info(f"Found {num_of_classes} classes taken during Term {term_num}")
        else:
            logging.warning(f"No classes was found for Term {term_num}")
        return term_info
