# CSCI 230: Programming Languages - Extra Credit Assignment 1 (Python)
# Alexandra Shellans
# 12/2/23

# Python program to calculate class grade with mulitple assignment categories/weights

# Welcome output
print("Welcome to Grader Guru! This program calculates a total grade for a course")
print("while taking into account various assignment types and weights.")
print()
print("To start the program, please enter 'Start'. To learn more about program features,")
command = input("please enter 'Help'. ")
print()

if command == "help" or command == "Help":
    print("In this program, you will be asked to provide the number and name(s) of")
    print("assignment categories, weight percentage values, and the grade percentage")
    print("earned for each assignment. Weights do not have to add up to 100%, so")
    print("calculating a total grade for in-progress classes with missing assignments")
    print("is acceptable. Grades must be entered as percentages; for example, if the")
    print("grade earned on an assignment is 45/50, entering 45 is not acceptable and")
    print("must be converted to a percentage (45/50 = 90%) and entered as 90 to be")
    print("counted correctly.")
    print()
    print("Program starting now... enter any key to continue")
    command = input()
    print()

# Ask user for/store number of assignment categories
numTypes = int(input("Please enter the number of assignment categories: "))
assnTypes = ["" for i in range(numTypes)]
print()

for n in range(numTypes):
    print("Enter the name of assignment type", n+1, end="")
    if n == 0:
        assnTypes[n] = input(" (Example: Exam, Homework, Project, etc.): ")
    else:
        assnTypes[n] = input(": ")
    
print()

# Ask user for/store weight values
weights = [0 for i in range(numTypes)]
print()
    
for w in range(numTypes):
    print("Please enter the weight percentage (%) for the", assnTypes[w], "category", end="")
    weights[w] = float(input(": "))

# Ask for/store number of assignments in each category
print()
numAssns = [0 for i in range(numTypes)]

for a in range(numTypes):
    print("Please enter the number of assignments in the", assnTypes[a], "category", end="")
    numAssns[a] = int(input(": "))

print()

# Ask user for/store grades for each assignment in each assignment type (inner and
# outer for-loops, respectively)
gradeAvgs = [0.0 for i in range(numTypes)]

for i in range(numTypes):
    numOfTypeI = numAssns[i]
    grades = [0.0 for k in range(numOfTypeI)]
                      
    for j in range(numOfTypeI):
        print("Please enter grade percentage (%) earned for", assnTypes[i], j+1, end="")
        grades[j] = float(input(": "))

    print()
    gradeAvgs[i] = sum(grades)/numAssns[i]

# Calculate and return total grade
weightedGrades= [0.0 for i in range(numTypes)]
                      
for i in range(numTypes):
    weightedGrades[i] = (weights[i]*gradeAvgs[i])/sum(weights)

totalGrade = "{:.2f}".format(sum(weightedGrades))
print("Your total grade for the class is:", totalGrade, "%.")
print("Thank you for using Grade Guru! :)")
