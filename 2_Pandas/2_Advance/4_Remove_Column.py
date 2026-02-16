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
    Remove Row:-
    df.drop(index , inplace=True)
"""

# # simple Row_Remove
# df.drop(3,inplace=True)  # index 3 will remove
# print(df)

# # delete Multiple row : just put all rows in array
# df.drop([1,2,5], inplace=True)
# print(df)

# # remove first and last row
# df.drop(df.index[0], inplace=True)      # first row
# df.drop(df.index[-1], inplace=True)     # last row


# conditional Row remove
df = df[df["Performance_Score"] >= 90]  
""" Jo ye condition Satisfy karega wahi data me present rahega """
print(df)