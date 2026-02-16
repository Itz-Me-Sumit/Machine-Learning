# sorting data

import pandas as pd
Data = {
    "name" : ["Sumit" , "Shivam" , "Rani"],
    "Age" : [21 , 14 , 20],
    "Salary" : [60000 , 40000 , 45000],
    "Performance_Score" : [85 , 77 , 96]
}
df = pd.DataFrame(Data)
print(df)


"""
    to sort, syntax :- df.sort_value(pos1 , pos2 , pos3)
        - pos1 -> by="Column_Name"
        - pos2 -> ascending = True(Ascending) OR False(Descending)
        - pos3 -> inplace=True(change in original dala) OR False(make a copy)

"""

df.sort_values(by="Age" , ascending=False , inplace = True)
print(df)