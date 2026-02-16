import pandas as pd
Data = {
    "name" : ["Sumit" , "Sumsita" , "Shivam" , "Sunil" , "Supriya" , "raj" , "simran" , "param"],
    "Age" : [21 , 18 , 14 , 50 , 40 , 34 , 40 , 23],
    "Salary" : [50000,35000,20000,42000,22033,42222,50000,40000],
    "Performance_Score" : [85 , 90 , 78 , 60 , 87 , 98 , 77 , 96]
}
df = pd.DataFrame(Data)
print(df)

"""
- Removing Column

    Syntax => df.drop(columns = ["Column_Name"] , inplace=True )

"""
#remove one column
# df.drop(columns = ["Performance_Score"] , inplace=True)
# print(df)

#remove multiple column
df.drop(columns = ["Performance_Score" , "Age"] , inplace=True)
print(df)

"""


"""