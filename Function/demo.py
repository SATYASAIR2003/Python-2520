import builtins
sum = lambda a,b: a+b
print(sum(1,6))  

dif = lambda a,b :a-b 
print(dif(9,1))

print((lambda a,b: a*b)(2,5))

print((lambda a:"even" if a%2==0 else "odd" )(5))  

print((lambda a:"even" if a%2==0 else "odd" )(3)) 

print((lambda a: "divided by 3" if a%3==0 else "not")(3))


# with Map 
print(list(map(lambda num:  num*num , [1,2,3,4,5,6,8])))

print(list(map(lambda num: num * num, [1,2,3,4,5])))

print(list(map(lambda a: a*a,[2,4])))

print(tuple(map(lambda a: a*a, (1,4,3,5,))))

print(set(map(lambda a: a*a, {1,4,3,5,})))

print(list(filter(lambda a: a%2==0,[1,2,3,4,5,6,7,8,1,2,3,4,5])))

from functools import reduce

print(reduce(lambda a,b: a*b,[1,2,3,4,5]))

print(reduce(lambda a,b: a+b,[1,7,4,5,2]))

# data[2."e",2,"b"]
data=[2,None,2,None]
print(list(filter(lambda a: a is not None, data )))

