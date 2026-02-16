import pandas as pd
Data1 = {
    "name" : ["Sumit" , "Sumsita" , "Shivam" , "Sunil" , "Supriya" , "raj" , "simran" , "param" , "Anand"],
    "Age" : [21 , 18 , 14 , 50 , 40 , 34 , 40 , 23 , 33],
    "Salary" : [50000,35000,20000,42000,22033,42222,50000,40000,44000],
    "Performance Score" : [85 , 90 , 78 , 60 , 87 , 98 , 77 , 96 , 89]
}
Data2 = {
    "name" : ["Sumit" , "Shivam" , "Rani" , "Mayuri" , "Anjali" , "Akasmat"],
    "Age" : [21 , 14 , 20 , 20 , 22 , 33],
    "Salary" : [60000 , 20000 , 45000 , 50000 , 56000 , 44000],
    "Performance_Score" : [85 , 77 , 96 , 89 , 90 , 78]
}

df1 = pd.DataFrame(Data1)
df2 = pd.DataFrame(Data2)


# Row Wise concatination
df_concate_RowWise=pd.concat([df1,df2] , axis=0 , ignore_index=True)
print(df_concate_RowWise)

# Column Wise Concatination
df_concate_ColumnWise=pd.concat([df1,df2] , axis=1 , ignore_index=True)
print(df_concate_ColumnWise)
