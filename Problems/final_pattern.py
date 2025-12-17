# Array in Python


sa=[2,3,4,5,6,7]

# Adding elments to the list
sa.insert(1,12) #Add the element in 1 index position insert(index,value)
sa.append(89) #Add the element at the end of the list

# Updating element in a list
sa[3]=10  #Replace the element at the index

# Removing the element
sa.pop()  # Removes the last element
sa.remove(6) #Remove the 6 in the list
del sa[0] #Remove the 0 index element

print(sa)
sa.reverse()
print(sa)

# How to call a arrary
import array as arr

# How to intialise a array
a = arr.array('i', [1, 2, 3])
print(*a) #If we keep * and print we get the list printed [1,2,3]

a.insert(1, 4)  # Insert 4 at index 1
print(a)

print(a[3])
print(a.index(4))

# finding the missing ranges
# Input: arr[] = [14, 15, 20, 30, 31, 45], lower = 10, upper = 50
# Output: [[10, 13], [16, 19], [21, 29], [32, 44], [46, 50]]

def missingranges(arr,lower,upper):
    n=len(arr)
    new=[]

    if lower < arr[0]:
        new.append([lower,arr[0]-1])

    for i in range(n-1):
        if arr[i+1]-arr[i]>1:
            new.append([arr[i]+1,arr[i+1]-1])
        
    if upper > arr[-1]:
        new.append([arr[-1]+1,upper])
    
    return new

print(missingranges([13,14,15,18,19,25,26,27,31,32,33,36,45],10,50))

