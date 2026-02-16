import pandas as pd
Data = {
    "name" : ["Sumit" , "Shivam" , "Rani" , "Mayuri" , "Anjali"],
    "Age" : [21 , 14 , 20 , 20 , 22],
    "Salary" : [60000 , 40000 , 45000 , 50000 , 56000],
    "Performance_Score" : [85 , 77 , 96 , 89 , 90]
}
df = pd.DataFrame(Data)

Grouped = df.groupby("Age")["Salary"].sum()
print(Grouped)