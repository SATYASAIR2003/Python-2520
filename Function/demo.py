def math_ops(a,b):
    print(a+b)
    print(a-b)

math_ops(2,5)

def even(a):
    if a%2==0:
        print("even")
    else:
        print("odd")
even(5)

# position based arguments
def login(username, password):
    if username=="satya" and password=="satya123":
        print("sucess")
    else:
        print("fail")

login("satya123","satya")

# keyword based arguments
def login(username="satya", password="satya123"):
    if username=="satya" and password=="satya123":
        print("sucess")
    else:
        print("fail")

login()

# default based arguments
def myinfo(name,number,sec="A"):
    print(f"My name is {name}, and the roll number is {number}, of {sec} section")

myinfo("Satya","22")
myinfo("Sai","12")

# Arbitrary positional based arguments
def sum(*num):
    total=0
    for a in num:
        total +=a
    print(total)

sum(2,5,3,5,2)

# Arbitrary keyword based arguments
def info(**empl):
    print(empl)

info(name="Sai", rollno="21")

def trans(**mytrans):
    print(mytrans)
    # total=0
    for my in mytrans:
        print(mytrans[my])
        # total = total +mytrans[my]
        # print(total)

trans(jan=2000, feb=1000)
    


















# import builtins
# sum = lambda a,b: a+b
# print(sum(1,6))  

# dif = lambda a,b :a-b 
# print(dif(9,1))

# print((lambda a,b: a*b)(2,5))

# print((lambda a:"even" if a%2==0 else "odd" )(5))  

# print((lambda a:"even" if a%2==0 else "odd" )(3)) 

# print((lambda a: "divided by 3" if a%3==0 else "not")(3))


# # with Map 
# print(list(map(lambda num:  num*num , [1,2,3,4,5,6,8])))

# print(list(map(lambda num: num * num, [1,2,3,4,5])))

# print(list(map(lambda a: a*a,[2,4])))

# print(tuple(map(lambda a: a*a, (1,4,3,5,))))

# print(set(map(lambda a: a*a, {1,4,3,5,})))

# print(list(filter(lambda a: a%2==0,[1,2,3,4,5,6,7,8,1,2,3,4,5])))

# from functools import reduce

# print(reduce(lambda a,b: a*b,[1,2,3,4,5]))

# print(reduce(lambda a,b: a+b,[1,7,4,5,2]))

# # data[2."e",2,"b"]
# data=[2,None,2,None]
# print(list(filter(lambda a: a is not None, data )))

