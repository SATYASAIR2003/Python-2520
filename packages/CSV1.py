import csv
data = [
    ["name","age","marks"],
    ["Satya",22,90],
    ["Sai",23,91],
    ["Vamsi",22,95],
    ["Harish",21,99],
    ["Sunny",20,96]
]

with open("Student_info.csv","w",newline="")as file:
    writer=csv.writer(file)
    writer.writerows(data)