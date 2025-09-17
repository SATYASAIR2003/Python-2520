Student_Id = int(input("Enter your Id: "))
Student_Name=input("Enter your Name: ")
Attendance=int(input("Enter your Attendance: "))
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
values=list(marks.values())
print(len(values[:]))

    
