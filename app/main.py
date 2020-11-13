from app.gpa.Course import Course
from app.gpa.Transcript import Transcript
from app.gpa.Gpa import Gpa

def main():
    tran_obj = Transcript("C:\\Users\\Samson\\PycharmProjects\\AnalysisGpa\\resources\\Transcript.csv")
    print("______Overall GPA______")
    print(f"Total GPA:  {Gpa(tran_obj.transcript).get_total_gpa()}")
    print("\n\n______Each term's GPA______")
    for x in range(1, tran_obj.get_latest_term_num() + 1):
        gpa_obj = Gpa(tran_obj.get_all_info_for_term(x))
        print(f"Term {x}: Total GPA {gpa_obj.get_total_gpa()}")
    print("\n\n______Class Type GPA______")
    print("all class types are " + ", ".join(tran_obj.split_course_by_type(tran_obj.transcript).keys()))


if __name__ == "__main__":
    main()