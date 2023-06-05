import pandas as pd

# convert into dataframe
df = pd.read_excel("rarity.xlsx")

dict = df.to_dict()
print(dict)