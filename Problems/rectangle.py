a=int(input("Enter a value: "))
b=int(input("Enter b value: "))
for i in range(a):
    for j in range(b):
        print(j,end=" ")
    print()

a=["Satya","Sai","Ravi"]
a.reverse()
print(a)
print(list(reversed(a)))

b="IVAR"
print("".join(reversed(b)))


def city():
    city1=["Delhi","Chennai","Hyderbad","Vizag","Vizianagaram"]
    return city1

letters=list("abcdefghijklmnopqrstuvwxyz")
city()
for word in city():
    temp = letters.copy()
    possible = True

    for ch in word.lower():
        if ch in temp:
            temp.remove(ch)
        else:
            possible = False
            break

    if possible:
        print(word)
        letters = temp