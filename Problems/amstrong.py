num = int(input())
a = len(str(num))
tem=num
total=0
while tem>0:
    b = tem%10
    total+=b**a
    tem//=10

if total==num:
    print("yes")
else:
    print("no")