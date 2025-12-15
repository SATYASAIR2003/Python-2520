marks=[80,85,75,90]
count=0
for n in marks:
    count+=1
    print(f"marks {count}: {n}")

# marks=[1,2,3,4,5,6,7]
# marks[int(input())]=int(input())
# print(marks)

marks=[1,2,3,"e","r",6,8]
print(marks[2:6:2])

marks=[1,2,3,4,5,6,7]
marks.append(4)
print(marks)
marks.sort()
print(marks)
marks.reverse()
print(marks)
marks.sort(reverse=True)
print(marks)
marks.insert(7,2)
print(marks)
marks.remove(3)
print(marks)
marks.pop(6)
print(marks)



"""
1. lists are mutable
2. Indexing is applicable in lists
3. Slicing is applicable in lists
4. There are many methods like
    pop()
    reverse()
    append()
    insert()
    clear()
    remove()
    sort()
    etcc
"""

# WAP to ask the user to give his three favorate movies and the output should be in list
movie1= input("Enter movie 1: ")
movie2= input("Enter movie 2: ")
movie3= input("Enter movie 3: ")
movies=[]
movies.append(movie1)
movies.append(movie2)
movies.append(movie3)
print(movies)

movies=[]
movies.append(input("Enter 1st movie: "))
movies.append(input("Enter 1st movie: "))
movies.append(input("Enter 1st movie: "))

print(movies)

# WAP to check weather the valuse in list are palindrome or not

laptop=[1,2,3,3,2,1]
copy_laptop= laptop.copy()
copy_laptop.reverse()
if copy_laptop == laptop:
    print("YES")
else:
    print("NO")

