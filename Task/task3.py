# To know the types of triangle
s1=int(input("Enter Side1: "))
s2=int(input("Enter Side2: "))
s3=int(input("Enter Side3: "))

if s1==s2==s3:
    print("It is a Equatrial Triangle")
elif s1==s2!=s3 or s1==s3!=s2 or s2==s3!=s1:
    print("It is a Isolas Triangle")
else:
    print("It is a Scalene")