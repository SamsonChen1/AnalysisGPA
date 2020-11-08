import csv
import logging

logging.basicConfig(format='%(asctime)-15s:  %(message)s', level=logging.INFO)

class Course:
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

    def __init__(self, file_name):
        self.file_name = file_name

    def get_transcript_content(self) -> list:
        transcript = []
        with open(self.file_name, newline='') as f:
            csv_content = csv.reader(f)
            next(f)
            for row in csv_content:
                transcript.append({"term": int(row[0].strip()), "class_code": row[1], "class_name": row[2], "class_type": row[3],
                                   "points": row[4], "grade": self.convert_gpa_letter_to_num(row[5])})
        return transcript

    def convert_gpa_letter_to_num(self, letter_grade: str) -> int:
        if letter_grade in self.letter.keys():
            return self.letter[letter_grade]
        else:
            return -1


    def get_all_info_for_term(self, transcript: list, term_num: int) -> list:
        term_info = []
        for cls in transcript:
            if cls["term"] == term_num:
                term_info.append(cls)
        num_of_classes = len(term_info)
        if num_of_classes > 0:
            logging.info(f"Found {num_of_classes} classes taken during Term {term_num}")
        else:
            logging.warning(f"No classes was found for Term {term_num}")
        return term_info
