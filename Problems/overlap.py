# arr1 = [[1, 3], [2, 4], [6, 8], [9, 10]]
# arr2= [[6, 8], [1, 9], [2, 4], [4, 7]]

# arr11 = sorted(arr1)
# arr22 =sorted(arr2)
# final=[]
# for i in arr22:
#     final.append(i)
#     if i[0]<final[-1][1]:
#         final.append(i)
# print(arr11)
# print(arr22)

# arr = [1,2,3,4,5,6,7,8]

# first = 0
# last = len(arr) - 1
# print(arr[first])
# print(arr[last])

# arr=[1,2,3,4,45,6,7,8]
# first=0
# last=len(arr)-1

# a=[1,3,6,0,2,7,0]
# b=sorted(a)
# c=[]
# d=[]
# coun=0
# for i in b:
#     if i!=0:
#         c.append(i)
#     else:
#         d.append(i)
# print(c+d)

# arr = [10, 20, 30, 40]

# for i, val in enumerate(arr):
#     print(i, val)

# a={}
# print(type(a))

# s = "I am learning Python programming language"
# print(s.split())

# n=int(input("Enter n: "))
# for i in range(n):
#     for j in range((i+1)):
#         print(chr(65+j),end="")
#     for j in range((n-j-1)*2):
#         print(" ",end="")
#     for j in range(i,-1,-1):
#         print(chr(65+j),end="")
#     print()
# for i in range(n-1):
#     for j in range(n-i-1):
#         print(chr(65+j).lower(),end="")
#     for j in range((i+1)*2):
#         print(" ",end="")
#     for j in range(n-i-2,-1,-1):
#         print(chr(65+j).lower(),end="")
#     print()


n=int(input("Enter n: "))
for i in range(n):
    for j in range(n-i-1):
        print(str(n-i+j),end="")
    print()