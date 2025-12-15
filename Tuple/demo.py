"""
1. Tuples are like strings
2. They are immutable
3. Indexing and Slicing are applicable
4. Methods like 
    index() == To get the index value, here we give the value in the tuple
    count()
"""

# WAP to count numer of grades in a tuple
grades=("A","B","C","A","C","A","B","C","B","D")
print(grades.count("D"))

# WAP to print above tuple in  list and sort
Grades= list(grades) 
print(Grades)
Grades.sort()
print(Grades)




