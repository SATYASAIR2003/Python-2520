Student_Id = (input("Enter your Id: "))
Student_Name=input("Enter your Name: ")
Attendance=int(input("Enter your Attendance: "))

# Ask Student To Enter Score / Marks
count=1
marks={}
while True:
    Score = (input("Do you want give Score(yes/no): "))
    if Score == "yes":
        Marks= int((input("Enter your Marks: ")))
        marks[f"Marks{count}"]=Marks
        count+=1
    else:
        print(marks)
        break

# Give me the number of scores
values=list(marks.values())
num=len(values)
print(num)

# Calculate Total Score (Score 1 + Score 2 + .... + Score N )
Total=0
for n in values:
    Total = Total+n 

# Give me the Average score
average=Total/num
print("Total Marks: ", Total)
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

    
