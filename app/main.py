from app.gpa.Results import Results

def main():
    results = Results("C:\\Users\\Samson\\PycharmProjects\\AnalysisGpa\\resources\\Transcript.csv")
    print("______Overall GPA______")
    print(f"Total GPA:  {results.get_overall_gpa()}")
    print("\n______Each term's GPA______")
    for key, gpa in results.get_each_terms_gpa().items():
        print(f"Term {key}: Total GPA {gpa}")
    print("\n______Class Type GPA______")
    for key, gpa in results.get_each_class_type_gpa().items():
        print(f"Class Type ({key}): Total GPA {gpa}")
    print("\n______Subject GPA______")
    for key, gpa in results.get_each_subject_gpa().items():
        print(f"Subject ({key}): Total GPA {gpa}")

if __name__ == "__main__":
    main()