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

d = {"a": 10, "b": 20, "c": 30}
keys = list(d.keys())

i = 0
while i < len(keys):
    key = keys[i]
    print(key, d[key])
    i += 1
