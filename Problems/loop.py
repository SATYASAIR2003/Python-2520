# sum of n numbers
n=int(input("Enter a number: "))
total = 0
for i in range(1,n+1):
    total = i+total
print(total)

# Fatorial of n number
n=int(input("Enter a number: "))
pro = 1
for i in range(1,n+1):
    pro*=i
print(pro)

# Multiplication table
n=int(input("Enter a number: "))
for i in range(1,11):
    print(f"{n} x {i} = {n*i}")

# Find prime number
a=int(input("Enter a number: "))
if a<2:
    print("Not Prime number")
else:
    for i in range(2,int(a**0.5+1)):
        if a%i==0:
            print("Not Prime")
            break
    else:
            print("Prime number")

# Count the frequency in a string
a=input("Enter a word: ")
ch=input("Enter a char: ")
count=0
for i in a.lower():
     if i==ch.lower():
          count+=1
print(count)

# Print the first character that does not repeat
a=input("Enter a word: ")
for i in a.lower():
     if a.count(i)==1:
          print(i)
          break

# Remove repeating characters
a=input("Enter a word: ")
cha=""
for i in a:
    if a.count(i)==1:
        cha+=i
print(cha)

# Remove Duplicate characters
a=input("Enter a key: ")
d=""
for i in a:
     if i not in d:
          d+=i
print(d)

    
    