# User details Check
User_Name="Om Kalal"
Password="om@kalal97"
User_Input=input("Enter User name: ")
User_pass=input("Enter User password: ")

if User_Name==User_Input and Password!=User_pass:
    print("You password is wrong")
elif User_Name!=User_Input and Password==User_pass:
    print("You userename is wrong")
elif User_Name!=User_Input and Password!=User_pass:
    print("You entered wrong details ")
else:
    print("You sucessfully loged in")
