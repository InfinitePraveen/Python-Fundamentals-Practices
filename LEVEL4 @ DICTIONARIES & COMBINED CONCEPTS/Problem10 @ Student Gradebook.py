# Create a dictionary called 'grades' with at least 5 students
# Each student has a list of 3 test scores
grades = {
    "Praveen" : [67, 97, 55],
    "Akash" : [34, 55, 67],
    "Bikash" : [33, 33, 55]
}
# 1. Print each student's name and average score
print("--- Student Averages ---")
for student, scores in grades.items():
    average = sum(scores) / len(scores)
    print(f"{student}: {average:.2f}")

# 2. Find the student with the highest average
print("\n------------------------")
highest_average = -1
top_student = ""

for student, scores in grades.items():
    average = sum(scores) / len(scores)
    if average > highest_average:
        highest_average = average
        top_student = student

print(f"Highest Average: {top_student} with a score of {highest_average:.2f}")

# 3. Add a new student
print("\n------------------------")
print("Adding new student: Bhawani...")
grades["Bhawani"] = [91, 85, 94]
print(f"Updated grades dictionary: {grades}")
print("\n------------------------")

# 4. Update a student's score
print("Updating Praveen's second score to 90...")
# Remember: Python lists are 0-indexed, so the second score is at index 1
grades["Praveen"][1] = 90
print(f"Praveen's new scores: {grades['Praveen']}")
