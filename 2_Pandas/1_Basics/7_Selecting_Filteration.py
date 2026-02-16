import pandas as pd
Data = {
    "name" : ["Sumit" , "Sumsita" , "Shivam" , "Sunil" , "Supriya" , "raj" , "simran" , "param"],
    "Age" : [21 , 18 , 14 , 50 , 40 , 34 , 40 , 23],
    "Salary" : [50000,35000,20000,42000,22033,42222,50000,40000],
    "Performance Score" : [85 , 90 , 78 , 60 , 87 , 98 , 77 , 96]
}

df = pd.DataFrame(Data)


# Selecting

    # single Attribue
print(df["Performance Score"])

    # Multiple Attribute
print(df[["name","Age"]])

# Filtering

print(df[df["Salary"]>20000])

print(df[ (df["Salary"] >= 40000) | (df["Salary"]) <= 80000 ])

print(df[ (df["Performance Score"] > 80) | (df["Age"] < 30) ])