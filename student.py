name = input("Enter Name: ")
age = int(input("Enter Age: "))
course = input("Enter Course: ")
marks = float(input("Enter Marks (out of 100): "))

if marks >= 40:
    status = "Pass"
else:
    status = "Fail"

print("----- Student Details -----")
print("Name   :", name)
print("Age    :", age)
print("Course :", course)
print("Marks  :", marks)
print("Status :", status)