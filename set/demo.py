new={1,4,"A",True}
print(type(new))
print(new)

new_1=set()
print(new_1)

new.add(2)
print(new)

new.remove(2)
print(new)


new.pop()
print(new)

# Union
a ={1,2,3,4,5,6}
b={5,6,7,8,9}
print(a.union(b))

marks={}
x=input("Enter your marks phy: ")
marks.update({"phy": x})

y=input("Enter your marks mat: ")
marks.update({"mat": y})

z=input("Enter your marks che: ")
marks.update({"che": z})

print(marks)

store={1,2,2.0}
print(store)

