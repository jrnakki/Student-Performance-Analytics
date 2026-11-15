import csv

#Defining read_data() function
def read_data():
    data = []
    with open('student_scores.csv', 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            data.append(row)

    return data
            
#Defining clean_data() function
def clean_data():
    with open('student_scores.csv', 'r') as file:
        csv_reader = csv.DictReader(file)

        valid_students = []
        invalid_count = 0

        for row in csv_reader:
            name = row["Name"]
            marks = row["Marks"]

            if not name or not marks:
                invalid_count += 1
                continue

            try:
                marks = int(marks)
            except ValueError:
                invalid_count += 1
                continue
            
            if marks < 0 or marks > 100:
                invalid_count += 1
                continue
            
            valid_students.append((name,marks))

        return valid_students,invalid_count

#Defining analyse_data() function
def analyse_data(valid_students,invalid_count):
    total_students = len(valid_students)

    invalid_students = invalid_count

    Marks_list = []
    for student in valid_students:
        Marks_list.append(student[1])
    average_marks = sum(Marks_list) / len(Marks_list)

    max_marks = max(Marks_list)
    for student in valid_students:
        if student[1] == max_marks:
            max_marks_name = student[0]
            break

    min_marks = min(Marks_list)
    for student in valid_students:
        if student[1] == min_marks:
            min_marks_name = student[0]
            break

    passed_students = 0
    for student in valid_students:
        if student[1] >= 40:
            passed_students += 1

    pass_percentage = passed_students / total_students

    report = {
        "total_students": total_students,
        "invalid_students": invalid_count, 
        "average": average_marks,
        "highest": [max_marks,max_marks_name],
        "lowest": [min_marks,min_marks_name],
        "passed": passed_students,
        "pass_percentage": pass_percentage
    }
    return report

#Defining generate_report() function
def generate_report(report):
    print("\n====== STUDENT PERFORMANCE REPORT ======\n")
    print("Total Valid Students:",report["total_students"])
    print("Invalid Records Removed:",report["invalid_students"])
    print("\nAverage Marks:",report["average"])
    print("\nHighest Marks:",report["highest"][1],"(",report["highest"][0],")")
    print("Lowest Marks:",report["lowest"][1],"(",report["lowest"][0],")")
    print("\nStudents Passed:",report["passed"])
    print("Pass Percentage:",report["pass_percentage"])
    print("\n========================================\n")

#Defining main() function
def main():
    with open('student_scores.csv', 'w', newline="") as file:
        csv_writer = csv.writer(file)
    
        csv_writer.writerow(["Name","Marks"])
        csv_writer.writerow(["Asha","78"])
        csv_writer.writerow(["Ravi","35"])
        csv_writer.writerow(["Meera","92"])
        csv_writer.writerow(["Kabir","60"])
        csv_writer.writerow(["","50"])
        csv_writer.writerow(["Isha",""])
        csv_writer.writerow(["Dev","105"])

    data = read_data()#Calling read_data() function
    for dat in data:
        print(dat)
    valid_students,invalid_count = clean_data()#Calling clean_data() function
    report = analyse_data(valid_students,invalid_count)#Calling analyse_data() function
    generate_report(report)#Calling generate_report() function

main()#Calling main() function
