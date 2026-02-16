import pandas as pd
Data = {
    "name" : ["Sumit" , "Samai", "Shivam" , "Sunil" , "Supriya" , "raj" , "simran" , "param"],
    "Age" : [21 , None , 14 , 50 , 40 , 34 , 40 , 23],
    "Salary" : [50000,None,20000,42000,22033,42222,50000,40000],
    "Performance_Score" : [85 , None , 78 , 60 , 87 , 98 , 77 , 96]
}
df = pd.DataFrame(Data)
print(df)

"""
to fill arbitary data into None or NaN place we have to use .interpolate(),
    - we can use multiple methods : "linear" , "polynomial" , "time" , etc
    - we have "axis=0" for row and "axis=1" for column.

"""


df["Age"]=df["Age"].interpolate(method="linear" , axis=0 )
print(df)