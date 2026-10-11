import pandas as pd

marks = pd.Series([85, 90, 78, 92, 88], index=["English", "Maths", "Science", "History", "Geography"])

df = pd.DataFrame({
    "Name": ["Aarav", "Riya", "Kabir", "Anaya", "Ishaan"],
    "English": [85, 90, 78, 92, 88],
    "Maths": [90, 85, 80, None, 95],
    "Science": [88, 92, 85, 90, None]
})

df.to_csv("marks.csv", index=False)

df = pd.read_csv("marks.csv")

print(marks)
print(df)
print(df.head())
print(df.info())
print(df.isnull().sum())

df = df.fillna(0)

print(df)
print(df["English"] + df["Maths"] + df["Science"])

df["Total"] = df[["English", "Maths", "Science"]].sum(axis=1)
df["Average"] = df[["English", "Maths", "Science"]].mean(axis=1)

print(df)
print(df["Total"].mean())
print(df["Average"].mean()) 