# name_student="Satya"
# grade="A"
# print(name_student+grade)
# print(f"My name is {name_student}" ,grade)
# print(name_student.upper())

# print(dir(name_student))

# Student_id_va = False
# while not Student_id_va:
#     student_id=input("Enter the Id: ")
#     if student_id.startswith("-") or student_id.startswith("0"):
#         print("Enter a positive number")
#     elif student_id.isdigit():
#         student_id=int(student_id)
#         if student_id>0:
#             Student_id_va = True
#         else:
#             print("Enter numbers only")
#     else:
#         print("Enter a valid number")  
    
# print(student_id)



# Student_name_va = False
# while True:
#     student_name=input("Enter name: ")
#     caps=student_name.isalpha()
#     if not caps:
#         print("Only alphabets")
#         continue
#     spaces=student_name.strip()
#     names=student_name.split()
#     count=sum(len(student_name))
#     formated_name=" ".join(names).title()



#     # if not spaces:
#     #     print("Spaces not allowed")
#     #     continue
#     # count=sum(student_name)
#     # if count<=3:
#     #     print("Charcters should be more the three")
#     break

student_name=input("Enter name: ")
    # caps=student_name.isalpha()
    # if not caps:
    #     print("Only alphabets")
    #     continue
spaces=student_name.strip()
print(spaces)

student_name=input("Enter name: ")
names=student_name.split()
print(names)

student_name=int(input("Enter name: "))

count=sum(len(student_name) )
print(count)

student_name=input("Enter name: ")
formated_name=" ".join(names).title()
print(formated_name)







    
    