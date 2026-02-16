import pandas as pd

data = {
    "Name" : ["sumit" , "Anjali" , "shivam" , "Susmita"],
    "Age" : [22 , 21 , 14 , 18],
    "City" : ["Begusarai" , "NatwarBirbal" , "Mokama" , "Simariya"]
}

df = pd.DataFrame(data)
print(df)

# df.to_csv("output.csv" , index=False)
# df.to_excel("Output.xlsx" , index=False)
df.to_json("Output.json" , index=False)