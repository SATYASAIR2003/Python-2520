a="Satya"
b=23
print("Hi my name is {} and age is {}.".format(a,b))

print("Hi {} how is job at {} and how are you doing.".format("Harish","Infosis"))

print("{2} where are you man here {1} is waiting for you since {0}.".format("Morning","Anu","Vamsi"))

print("{name} is a very {} boy".format("good",name="Deva"))

d=103
print("the binary number of 103 is {:b}".format(d))
print("the octal number of 103 is {:o}".format(d))

def table(a,b):
    for i in range(a,b):
        print("{:8d} {:8d} {:8d} {:8d}".format(i, i*2, i**3, i**4))

table(3,10)

# Split method is used to convert string into list split()
aa= "Satya Sai Vamsi Harish"
print(aa.split())
print(list(aa))

ab = [1,2,"Sa"]
print(type(ab))
print(type(repr(ab)))

ac="Saaatyke"
abc=set(ac)
print(abc)
print(type(abc))
print(dict.fromkeys(ac))

acd=["1","2","3","4","5"]
print(list(map(int,acd)))
print([int(items) for items in acd])

adc=[]
for i in range(len(acd)):
    # i=int(i)
    adc.append(int(acd[i]))
    # acd[i]=int(acd[i])
print(adc)

def listTraversal(arr):
    #code here
    for i in (arr):
        print(i,end =" ")

listTraversal([1,2,3,4])
