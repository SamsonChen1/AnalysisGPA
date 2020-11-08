from app.gpa.Course import Course
from app.gpa.Transcript import Transcript

def main():
    tran_obj = Transcript("C:\\Users\\Samson\\PycharmProjects\\gpaCalculator\\resources\\Transcript.csv")
    transcript = tran_obj.get_transcript_content()
    term1_class = tran_obj.get_all_info_for_term(transcript, 1)
    for cls in term1_class:
        print(f"I took class {cls.class_name} and got the grade {cls.grade}")

if __name__ == "__main__":
    main()