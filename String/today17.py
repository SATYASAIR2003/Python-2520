def checkuser():
    username=input("Enter user name: ")
    n=len(username)
    s=username.find(" ")
    a=username.isalpha()
    if n>12:
        return "The username is more than 12 characters"
    elif s !=-1:
        return "The user name can't contains spaces"
    elif a==False:
        return "The username should not contain digits"
    else:
        return f"Welcome {username}"

print(checkuser())