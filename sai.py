n=int(input("Enter a number: "))
print("* "*n)

n=int(input("Enter a number: "))
for i in range(n):
    print('*',end=" ")
print()

n=int(input("Enter a number: "))
for i in range(1,n+1):
    for j in range(1,n+1):
        print("*",end=" ")
    print()

n=int(input("n: "))
for i in range(1,n+1):
    print((str(i)+" ")*n)
print()

n=int(input("n: "))
for i in range(1,n+1):
    print("A "*n)
print()

n=int(input("Enter n: "))
for i in range(n):
    print((chr(65+i)+" ")*(i+1))
print()

n=int(input("n: "))
for i in range(n):
    print("* "*(n-i))
print()

n=int(input("n: "))
for i in range(n):
    for j in range(n-i):
        print(str(j+1),end=" ")
    print()

n=int(input("Enter a n: "))
for i in range(n):
    print(" "*(n-i-1),(str(i+1)+" ")*(i+1))
print()

n=int(input("Enter a n: "))
for i in range(n):
    print(" "*(n-i-1),end="")
    for j in range(i+1):
        print((chr(64+n-j)+" "),end="")
    print()
    # print(" "*(n-i-1),(chr(69-1)+" ")*(i+1))
# print()

n = int(input("Enter n: "))
for i in range(n):
    for j in range(i+1):
        print(chr(65+j),end=" ")
    print()
for i in range(n-1):
    for j in range(n-i-1):
        print(chr(65+j),end=" ")
    print()