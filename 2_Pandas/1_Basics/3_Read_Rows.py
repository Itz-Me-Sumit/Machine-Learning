"""

    head(n) :- show first n rows 
    tail(n) :- show last n rows
        
        - if we don't put n and keep it head()/tail() it'll return 5 rows    
"""

import pandas as pd
df = pd.read_json(r"C:\Users\Acer\OneDrive\Desktop\Machine Learning\2_Pandas\1_Basics\sample_Data.json" , encoding="latin1")

#display first 5 rows
print(df.head())

#display last 5 rows
print(df.tail())

#display first 20 rows
print(df.head(20))

#display last 20 rows
print(df.tail(20))