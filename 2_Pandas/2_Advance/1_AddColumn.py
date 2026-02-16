import pandas as pd
Data = {
    "name" : ["Sumit" , "Sumsita" , "Shivam" , "Sunil" , "Supriya" , "raj" , "simran" , "param"],
    "Age" : [21 , 18 , 14 , 50 , 40 , 34 , 40 , 23],
    "Salary" : [50000,35000,20000,42000,22033,42222,50000,40000],
    "Performance Score" : [85 , 90 , 78 , 60 , 87 , 98 , 77 , 96]
}
df = pd.DataFrame(Data)
print(df)

# adding a another column using assignment operator
df["Bonus"] = df["Salary"]*0.1
print(df)

"""
Adding Column by insert() Method... here we can chose index too
    - Application:
        df.insert( Location(index) , Column_Name , Data )
"""

df.insert(0 , "Increment" , df["Salary"]*0.05)
print(df)

df.insert(6 , "New_Salary" , df["Salary"]+df["Salary"]*0.05
)
print(df)