def calculator():
    a=int(input("Enter a value: "))
    b=int(input("Enter b value: "))
    operator=input("Enter operator(+ - * / ): ")
    if operator == "+":
        return a+b
    elif operator=="-":
        return a-b
    elif operator=="*":
        return a*b
    elif operator=="/":
        return a/b
    else:
        return "Invalid"
    
print(calculator())