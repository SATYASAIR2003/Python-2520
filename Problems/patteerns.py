# # Print a diamond
# n=int(input("Enter n: "))
# for i in range(n):
#     print(" "*(n-i-1),end="")
#     for j in range(i+1):
#         print("* ",end="")
#     print()

# for i in range(n-1):
#     print(" "*(i+1),end="")
#     for j in range(n-i-1):
#         print("* ",end="")
#     print()

# n =int(input("Enter a Al"))
# for i in range(n):
#     for j in range(i+1):
#         print(chr(64+j+1)+" ",end="")
#     print()

# for i in range(n-1):
#     for j in range(n-i-1):
#         print(chr(64+j+1)+" ",end="")
#     print()

# n=int(input("Enter a : "))
# for i in range(n):
#     print(" "*i,end="")
#     for j in range(n-i):
#         print(chr(64+j+1)+" ",end="")
#     print()

# n=int(input("Enter *: "))
# for i in range(1,n+1):
#     print(" "*(n-i),end="")
#     print("* "*(i))


# for i in range(n-1):
#     print(" "*(i+1),end="")
#     print("* "*(n-i-1))
# print()

# n=int(input("*: "))
# for i in range(n):
#     print("* "*(i+1))

# for i in range(n-1):
#     print("* "*(n-i-1))
# print()

# n=int(input("E *: "))
# for  i in range(n):
#     print(" "*(n-i-1)+"* "*(i+1))

# for i in range(n-1):
#     print(" "*(i+1)+"* "*(n-1-i))
# print()

# n=int(input("H *: "))
# for i in range(n):
#     print(" "*(n-i-1)+"* ",end="")
#     if i >=1:
#         print(" "*(2*i-1)+"*",end="")
#     print()
# for i in range(n):
#     print(" "*i+"* ",end="")
#     if i!=(n-1):
#         print(" "*(2*n-2*i-3)+"*",end="")
#     print()

# n=int(input("Enter a alpha: "))
# for i in range(n):
#     print(" "*i+chr(65+i),end="")
#     if i!=(n-1):
#         print(" "*(2*n-2*i-3),chr(65+i),end="")
#     print()

# n=int(input("Enter n: "))
# for i in range(n):
#     print(" "*(n-i-1),end="")
#     for j in range(i+1):
#         print(str(j+1),end="")
#     print()
# for i in range(n-1):
#     print(" "*(i+1),end="")
#     for j in range(n-i-1):
#         print(j+1,end="")
#     print()

# for i in range(7):
#     for j in range(5):
#         print("* ",end="")
#     print()

# for i in range(7):
#     for j in range(5):
#         if j == 0 or j == 4:
#             print("* ",end="")
#         else:
#             print("  ",end="")
#     print()

for i in range(7):
    for j in range(5):
        if (i in {0,3,6}) & (j in {1,2,3}):
            print("* ",end="")
        elif (i in {1,2,4,5})&(j in {4}):
            print("* ",end="")
        elif j==0:
            print("* ",end="")
        else:
            print("  ",end="")
    print()