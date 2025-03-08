import csv

# Function to calculate the average of a list of scores
def calculate_average(scores):
    return sum(scores) / len(scores)

# Read the data from "student_grades.csv"
students = {}
with open('Student_grades.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        name = row['Name']
        # Convert subject scores to integers and calculate the average
        scores = [int(row['Maths']), int(row['Science']), int(row['English'])]
        average_score = calculate_average(scores)
        # Store the student's name and their corresponding average score
        students[name] = average_score

# Write the results to a new CSV file "student_average_grades.csv"
with open('student_average_grades.csv', mode='w', newline='') as file:
    fieldnames = ['Name', 'Average']
    csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
    
    csv_writer.writeheader()
    for name, average in students.items():
        csv_writer.writerow({'Name': name, 'Average': average})


print("Check 'student_average_grades.csv'") 