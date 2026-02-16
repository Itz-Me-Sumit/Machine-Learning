import pandas as pd
Data = {
    "name" : ["Sumit" , "Sumsita" , "Shivam" , "Sunil" , "Supriya" , "raj" , "simran" , "param"],
    "Age" : [21 , 18 , 14 , 50 , 40 , 34 , 40 , 23],
    "Salary" : [50000,35000,20000,42000,22033,42222,50000,40000],
    "Performance Score" : [85 , 90 , 78 , 60 , 87 , 98 , 77 , 96]
}
df = pd.DataFrame(Data)
print(df)

"""
    .loc[] -> thorugh this we can access any specific Rows,column,cell or A set of row, column etc and can modify it.

    syntax => df.loc[row_index , "Column_Name"] = New_Data

"""
# Updating Salary of Row 3(index 2)
df.loc[2 , "Salary"] = 55000
print(df)