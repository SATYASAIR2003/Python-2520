try:
# Always runs
    a = int(input())
    b = int(input())
    c=a/b
except:
# runs only when error occurs
    print("Error ocured")
else:
# runs only when there is no error
    print("No error")
    print(c)
finally:
# Always runs
    av=45
    ad=24
    asd=av+ad
    print(asd)