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
if any values are missing then we can remove that or can fill new another value
"""

# Removing Rows
df.dropna(axis=0,inplace=True)  #to remove row wise => axis=0
"""If a row have None or NaN value anywhere it will delete that whole row"""


df.dropna(axis=1,inplace=True)  #to remove column wise => axis=1
"""if a column have None or NaN value anywhere it will delete that whole column"""

print(df)


