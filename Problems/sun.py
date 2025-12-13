# Printing n numbers
n=int(input("Enter a number: "))
for i in range(1,n+1):
    print(i)

# Checking weather a number is a even or odd
n=int(input("Enter a number: "))
for i in range(1,n+1):
    if i%2==0:
        print(f"{i} even")
    else:
        print(f"{i} odd")  

# Finding maximum of a number
a=int(input("Enter 1st number: "))
b=int(input("Enter 1st number: "))
if a>b:
    print("a is greater than b")
else:
    print("b is greater than a")

# swap two numbers
a=int(input("Enter 1st number: "))
b=int(input("Enter 2st number: "))
a,b=b,a
print(a)
print(b)

print("="*20)
# Checking a nuber is a even or odd using bitwise operator
n=int(input("Enter a number: "))
if (n & 1)==0:
    print("Even")
else:
    print("Odd")

a = [1, 2, 3]
a.append([4, 5])
print(len(a))

# Check prime number
n=int(input("Enter a number: "))
for i in range(2,n):
    if n%i==0:
        print("prime")
    else:
        print("Not Prime")