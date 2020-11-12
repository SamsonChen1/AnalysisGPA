from app.gpa.Course import Course
from app.gpa.Transcript import Transcript
from app.gpa.Gpa import Gpa

def main():
    tran_obj = Transcript("C:\\Users\\Samson\\PycharmProjects\\AnalysisGpa\\resources\\Transcript.csv")
    gpa_obj = Gpa(tran_obj.get_all_courses())
    print(f"total gpa {gpa_obj.get_total_gpa()}")

if __name__ == "__main__":
    main()