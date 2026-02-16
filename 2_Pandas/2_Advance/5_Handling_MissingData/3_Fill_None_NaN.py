import pandas as pd
Data = {
    "name" : ["Sumit" , None, "Shivam" , "Sunil" , "Supriya" , "raj" , "simran" , "param"],
    "Age" : [21 , None , 14 , 50 , 40 , 34 , 40 , 23],
    "Salary" : [50000,None,20000,42000,22033,42222,50000,40000],
    "Performance_Score" : [85 , None , 78 , 60 , 87 , 98 , 77 , 96]
}
df = pd.DataFrame(Data)
print(df)

"""
fill all NaN or None Value by 0
"""
# df.fillna(0,inplace=True)
# print(df)

# or we can do

df["Age"].fillna(int(df["Age"].mean()),inplace=True)
print(df)
"""
df["Age"] ye age ke column ko fill karega, then .fillna karke ham 
ham curly braces me " df["Age"].mean() " karke value nikalenge aur inplace True karke Age column me mean age fill kar denge.
"""


df["Salary"].fillna(int(df["Salary"].mean()),inplace=True)
print(df)


df["Performance_Score"].fillna(int(df["Performance_Score"].mean()) , inplace=True)
print(df)