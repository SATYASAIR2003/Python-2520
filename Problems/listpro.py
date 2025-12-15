# Reverse a string
a="SatyakondaytaS"
print(a[::-1])

# Check weather given string is a palindrome or not
a=input("Enter a name: ")
if a == a[::-1]:
    print("Yes")
else:
    print("No")

# Count vowels in a string
a=input("Enter a word: ")
count=0
for i in a:
    if i in "aeiouAEIOU":
        count+=1
print(count)

# Count the characters
a=input("Enter a word: ")
co=0
for i in a:
    co+=1
print(co)

