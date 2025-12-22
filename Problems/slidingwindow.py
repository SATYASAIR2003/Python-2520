# a=list(input("a: "))
# k=int(input("k: "))
# for i in range(a):
#     for j in range(i,k+1):
#         max()

# a=[5,9,1,8,7]
# h=3
# n=len(a)
# ans=[]
# for i in range(n):
#     for j in range(i,n):
#         an=[]
#         for k in range(i,j+1):
#             an.append(a[k])
#         # print(an)
#         ans.append(an)
# print(ans)
# max1=[]
# for i in ans:
#     if len(i)==h:
#         sum1=0
#         for k in i:
#             sum1=sum1+k
#         max1.append(sum1)
# print(max(max1))

# a="SAI"
# n=len(a)
# an=[]
# for i in range(n):
#     for j in range(i,n):
#         tem=""
#         for k in range(i,j+1):
#             tem+=a[k]
#         # print(tem)
#         an.append(tem)
# print(an)

a=input("Enter: ")
n=len(a)
l=0
h=3
b=[]
count=0
for i in range(n):
    for k in range(i,n):
        tem=""
        # print(i,k)
        for r in range(i,k+1):
            tem+=a[r]
        if len(tem)==h and len(tem)==len(set(tem)):
            print(tem)
            count+=1
print(count)
