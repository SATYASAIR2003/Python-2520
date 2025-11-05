import pandas as pd
info={
  "name":["Satya","Sai","Vamsi","Harish","Sunny","Deva"],
  "rollno":[22,23,12,25,6,17],
  "sec":["A","A","B","A","C","C"]
}

df = pd.DataFrame(info)
print(df)
print(df["sec"])

print(df.loc[0,"name"])
print(type(df))
print(df.info())
