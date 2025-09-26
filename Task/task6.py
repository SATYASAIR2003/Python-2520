# Student_Id = (input("Enter your Id: "))
Student_id_va = False
while not Student_id_va:
    student_id=input("Enter the Id: ")
    if student_id.startswith("-") or student_id.startswith("0"):
        print("Enter a positive number")
    elif student_id.isdigit():
        student_id=int(student_id)
        if student_id>0:
            Student_id_va = True
        else:
            print("Enter numbers only")
    else:
        print("Enter a valid number")  

Student_Name=input("Enter your Name: ")
Student_Name.isalpha
Attendance=int(input("Enter your Attendance: "))

# Ask Student To Enter Score / Marks
count = 1
total_score = 0
Yes="yes"

while True:
    Score = input("Do you want to give Score (yes/no): ")
    
    if Score == Yes:
        Marks = int(input(f"Enter your Marks {count}: "))
        total_score += Marks
        count += 1
    else:
        print("Number of scores entered:", count - 1)
        break

num=count-1

# Give me the Average score
average=total_score/num
print(f"Id: {student_id}")
print(f"Name: {Student_Name}")
print(f"Attendance: {Attendance}")
print("Total Marks: ", total_score)
print("Average Marks: ", average)

# Based On Average Score, Grade the Student

if(average>=85):
    print("Grade A")
elif(average>=70):
    print("Grade B")
elif(average>=50):
    print("Grade C")
else:
    print("Fail")
    
# Attendance Criteria
if (Attendance<75):
    print("Warning Low Attendance")
else:
    print("Ok Good Attendance")

# Award Eligibility 
if(Attendance>=75 and average>=85 ):
    print("Eligible for Award")
else:
    print("Not Eligible for Award")