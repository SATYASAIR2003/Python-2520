def weig_con():
    Weight=float(input("Enter weight: "))
    unit=input("Enter unit in kg or g: ")
    if unit=="g":
        return Weight/1000,"kg"
    elif unit=="kg":
        return Weight*1000,"g"
    else:
        return "Invalid"
    
value,unit = weig_con()
if value != "Invalid":
    print(f"Converted weight is {value} {unit}")
else:
    print(unit)
    
print(weig_con())