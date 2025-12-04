def palindrome(a):
    # a=input("Enter a name: ")
    if a == a[::-1]:
        print("Yes")
    else:
        print("Not")

palindrome(input("Enter a name: "))