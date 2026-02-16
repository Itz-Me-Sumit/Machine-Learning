"""
    Missing Data can be of two type
        1) NaN(Not a Number)  2)None(If Objects are missing)

"""

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
syntax :- df.isnull() -> if data is not present True will returned else False
"""
print(df.isnull())


"""
number of missing value :- df.isnull().sum()
"""

print(df.isnull().sum())