i=1
n=int(input())
while i<=20:
    print(n*i)
    i+=1

# WAP to print each element in a loop using a for loop
store=[1,2,3,4,5,"Snacks","Lays","Soyasticks","Sevmurmur"]
for a in store:
    print(a)

# WAP to print each element in a loop using a while loop
store=[1,2,3,4,5,"Snacks","Lays","Soyasticks","Sevmurmur"]
idx=0
while idx<len(store):
    print(store[idx])
    idx+=1 

# search for number x in a tupple
num = (1,4,2,5,2,6,2,7,1,8,9,5)
i=0
x = int(input())
while i<len(num):
    if x==num[i]:
        print(f"found at {i}")
        break
    else:
        print("Finding")
    i+=1
print("End of loop")


# continue
i=0
while i<10:
    if i==5:
        i+=1
        continue
    print(i)
    i+=1

print("===========================")
# WAP to print each element in a list using for loop
numn=[1,6,4,8,4,9,3,8,3,]
for a in numn:
    print(a)

# # WAP to search a number in a list using a for loop
# numn=[1,6,4,8,4,9,3,8,3,]
# y=int(input())
# a=0
# for a in numn:
#     if numn[a] == y:
#         print("Found at")

i=1
for i in range(21):
    print(i)

i=10
for i in range(10,0,-1):
    print(i)

n= int(input())
i=1
for i in range(10):
    print(n*i)

print("=================================")

# WAP to print the sum of n numbers using while loop
i=1
sum=0
while i<=10:
    sum+=i
    i+=1
print(sum)

# WAP to print the sum of n numbers using for loop
i=1
sum=0
for i in range(10):
    sum+=i
print(sum)