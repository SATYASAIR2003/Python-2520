import pandas as pd
df = pd.read_csv("Student_info.csv")
print(df)

print(df.head())
print("="*100)
print(df['marks'].sort_values(ascending=False))
print(df.drop('age',axis=1,inplace=True))
print(df.drop(1,axis=0,inplace=True))
print(df)