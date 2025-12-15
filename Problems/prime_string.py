# n=input("Enter a number: ")
# coun=0
# if len(n)<4:
#     print("Invalid")
# else:
#     for ch in n:
#         ch=int(ch)
#         if ch>1:
#             for i in range(2,int(ch**0.5)+1):
#                 if ch%i==0:
#                     break
#             else:
#                     coun+=1
#     print(coun)

# n=int(input("Enter a number: "))
# a,b=0,1
# for i in range(1,n+1):
#      for j in range(i):
#           print(a,end=" ")
#           a,b=b,b+a
#      print()
    
# n=int(input("Enter a number: "))
# a=1
# for i in range(1,n+1):
#      for j in range(i):
#           print(a,end=" ")
#           a+=1
#      print()

# n=int(input("Enter a number: "))
# for i in range(1,n+1):
#      for j in range(i):
#           print("*",end=" ")
#      print()

# n=int(input("Enter a number: "))
# for i in range(1,n+1): 
#     print("*",end=" ")
# print()

n = int(input("Enter a number: "))
for i in range(1, n + 1):
    print("  " * (n - i), end="")   # leading spaces
    print("* " * i)
print()

n = int(input("Enter a number: "))
for i in range(1, n +1):
   # leading spaces
    print(" "*i,end="")
    print("* " * ((n+1)-i))
print()

n=int(input("EN: "))
for i in range(1,n+1):
    print(" "*(n-i)+"* "*i)

for i in range(n-1,0,-1):
    print(" "*(n-i)+"* "*i)
print()