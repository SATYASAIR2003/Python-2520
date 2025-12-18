n=[1,2,3,4,4,6]
a=len(n)
seen=[]
duplicte=[]
total=0
total1=a*(a+1)//2
for i in n:
    if i in seen:
        duplicte.append(i)
    else:
        seen.append(i)

for i in seen:
    total=total+i

miss=total1-total
print(duplicte[0],miss)
