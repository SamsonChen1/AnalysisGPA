from app.gpa.Course import Course
from app.gpa.Transcript import Transcript

def main():
    tran_obj = Transcript("C:\\Users\\Samson\\PycharmProjects\\AnalysisGpa\\resources\\Transcript.csv")
    print(f"total gpa {tran_obj.get_total_gpa(tran_obj.get_split_courses()[0])}")

if __name__ == "__main__":
    main()