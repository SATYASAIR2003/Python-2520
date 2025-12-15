# a=int(input("Enter a number: "))
# b=int(input("Enter a number: "))
# for i in range(a):
#     print(a)
#     a,b=b,a+b
# print(a)
# print(b)

def fib(n):
    a=[int(input()),int(input())]
    while len(a)<n:
        a.append(a[-1]+a[-2])
    print(a)
(fib(int(input())))

e="Satya"
print(e.capitalize())
