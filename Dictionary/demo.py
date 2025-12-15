myinfo = {"name":"Sai","age":"21","city":"Vizag"}
myinfo["lan"] = "Telugu"
print(myinfo)
myinfo.update({"soft":"Python","Course":"Data"})
print(myinfo)
myinfo.pop("soft")
print(myinfo)

for keys, values in myinfo.items():
    print(keys,":",values)

print(myinfo.values())
print(myinfo.get("name"))

student={
    "name":"Satya",
    "sec":"C",
    "sub":{"mat":98,
           "phy":99,
           "che":80
           },
    "id":"C8"
    }
print(student["sub"]["phy"])
print(student.keys())
pairs=(list(student.items()))
print(pairs[0])
print(student.get("name"))
student_ne={"city":"hyd","name":"Satyasai"}
student.update(student_ne)
print(student)