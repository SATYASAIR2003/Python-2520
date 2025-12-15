a=int(input("Enter a number: "))
if a<2:
    print("Not a prime number")
else:
    for i in range(2,int(a**0.5)+1):
        if a%i==0:
            print("Not a prime number")
            break
        else:
            print("Prime number")

# a=int(input())
# for i in range(1,a+1):
#         if a%i==0:
#             print(i)
            