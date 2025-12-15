# new={1,4,"A",True}
# print(type(new))
# print(new)

# new_1=set()
# print(new_1)

# new.add(2)
# print(new)

# new.remove(2)
# print(new)


# new.pop()
# print(new)

# # Union
# a ={1,2,3,4,5,6}
# b={5,6,7,8,9}
# print(a.union(b))

# marks={}
# x=input("Enter your marks phy: ")
# marks.update({"phy": x})

# y=input("Enter your marks mat: ")
# marks.update({"mat": y})

# z=input("Enter your marks che: ")
# marks.update({"che": z})

# print(marks)

# store={1,2,2.0}
# print(store)

# a=(1 + 2j) * (3 + 4j)
# print(a)

# a=[10,20]
# b=["Satya","Sai"]
# for i in a:
#     for j in b:
#         print(i,j)

# # True = False
# # while True:
# #     print(True)
# #     break
# # SyntaxError: cannot assign to True

# li = ['a', 'b', 'c', 'd']
# print("".join(li))

# def func(a, b=[]):
#     b.append(a)
#     return b

# print(func(1))
# print(func(2))

def REVERSE(a): 
	a.reverse() 
	return(a)
print(REVERSE([2,3,4,5]))

def YKNJS(a): 
	b = [] 
	b.extend(REVERSE(a)) 
	print(b)
print(YKNJS([2,3,5]))

li = ['a', 'b', 'c'] * -3
print(li)