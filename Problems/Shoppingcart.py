Goods=[]
prises=[]
total=0
while True:
    items=input("Enter a item(x to quit the cart): ")
    if items.lower()=="x":
        break
    else:
        Goods.append(items)
        prise=int(input(f"Enter prise of {items}: $"))
        prises.append(prise)

print("------Your Cart------")

for i in Goods:
    print(i,end=" ")
print()
for i in prises:
    total+=i
print(f"The total amount is {total}")