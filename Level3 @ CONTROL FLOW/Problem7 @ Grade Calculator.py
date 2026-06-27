# Ask the user for their exam score (0-100)
exam_score = int(input("Enter your exam score: "))

# Print the corresponding letter grade:
# 90-100: A
# 80-89:  B
# 70-79:  C
# 60-69:  D
# Below 60: F

if exam_score > 0 & exam_score < 100:
    if exam_score >= 90:
        print("Grade A")
    elif exam_score >= 80:
        print("Grade B")
    elif exam_score >= 70:
        print("Grade C")
    elif exam_score >= 60:
        print("Grade D")
    elif exam_score < 60:
        print("Grade F")
else:
    print("Invalid Input") # Handle invalid input (negative or >100)