import logging
from app.gpa.Gpa import Gpa
from app.gpa.Transcript import Transcript

logging.basicConfig(format='%(asctime)-15s %(name)s:  %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

class Results:
    def __init__(self, template_filepath):
        self.transcript = Transcript(template_filepath)

    def get_overall_gpa(self):
        return Gpa(self.transcript.transcript).get_total_gpa()

    def get_each_terms_gpa(self):
        term_gpa = {}
        for num in range(1, self.transcript.get_latest_term_num() + 1):
            gpa_obj = Gpa(self.transcript.get_all_info_for_term(num))
            term_gpa[num] = gpa_obj.get_total_gpa()
        return term_gpa

    def get_each_class_type_gpa(self):
        type_gpa = {}
        for key, courses in self.transcript.split_course_by_attr(self.transcript.transcript, "class_type").items():
            courses_gpa = Gpa(courses)
            type_gpa[key] = courses_gpa.get_total_gpa()
        return type_gpa

    def get_each_subject_gpa(self):
        type_gpa = {}
        for key, courses in self.transcript.split_course_by_attr(self.transcript.transcript, "class_code").items():
            courses_gpa = Gpa(courses)
            type_gpa[key] = courses_gpa.get_total_gpa()
        return type_gpa

