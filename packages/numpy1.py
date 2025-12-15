import numpy as np
a= np.array([[1,2,34],[3,6,2]])
print(type(a))
print(a)

# This is using the numpy package
a= np.array([1,2,34])*2
print(a)

# This is using traditional python
# s = [1,2,3,4,5]
# for s in s:
#     print(s*2)

a= np.array([[1,2,3,4],[3,6,2,8],[1,2,34,5],[2,4,7,1]])
print(a.dtype)
print(a.shape)
print(a)

b=np.identity(4)
print(b)
print("=="*80)
print(a+b)

print(a*b)
