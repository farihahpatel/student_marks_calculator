
# Student Marks Calculator

print("================================")
print("     STUDENT MARKS CALCULATOR")
print("================================")

# Get student name
name = input("Enter student name: ")

# Enter marks for five subjects
print("\nEnter marks out of 100:")

english = float(input("English: "))
maths = float(input("Mathematics: "))
science = float(input("Science: "))
computer = float(input("Computer: "))
history = float(input("History: "))

# Calculate total and percentage
total = english + maths + science + computer + history
percentage = total / 5

# Calculate grade
if min(english, maths, science, computer, history) < 35:
    grade = "F"
    result = "Fail"
elif percentage >= 90:
    grade = "A+"
    result = "Pass"
elif percentage >= 80:
    grade = "A"
    result = "Pass"
elif percentage >= 70:
    grade = "B"
    result = "Pass"
elif percentage >= 60:
    grade = "C"
    result = "Pass"
elif percentage >= 35:
    grade = "D"
    result = "Pass"
else:
    grade = "F"
    result = "Fail"

# Display result
print("\n================================")
print("          STUDENT RESULT")
print("================================")

print("Student Name:", name)
print("Total Marks:", total, "/ 500")
print("Percentage:", percentage, "%")
print("Grade:", grade)
print("Result:", result)

print("================================")
print("       THANK YOU!")
