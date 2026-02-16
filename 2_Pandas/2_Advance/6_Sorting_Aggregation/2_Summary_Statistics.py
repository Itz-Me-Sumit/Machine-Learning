import pandas as pd
Data = {
    "name" : ["Sumit" , "Shivam" , "Rani"],
    "Age" : [21 , 14 , 20],
    "Salary" : [60000 , 40000 , 45000],
    "Performance_Score" : [85 , 77 , 96]
}

df = pd.DataFrame(Data)

avg_salary = df["Salary"].mean()
print(avg_salary)