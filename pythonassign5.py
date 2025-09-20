x = {}
n = int(input("Enter number of students you want to enroll: ",))
for i in range (n):
    name = input("Enter name:",)
    marks = int(input("Enter marks:"))
    x[name] = marks

print("OK!, Students are now enrolled.")
name1 = input("Enter the student's name to check: ")
if name1 in x :
    print(f"{name1}'s marks: ", x[name1])
else:
    print("Student not found.")    
