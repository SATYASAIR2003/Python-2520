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