import pandas as pd
from material_selector import MaterialSelector

# df_test = pd.read_csv("constrained_new_chemical_compositions.csv", delimiter=",")
df_test = pd.read_csv("fully_constrained_new_chemical_compositions_10_more_3.csv", delimiter=",")


all_columns = df_test.columns.tolist()
material_columns = sorted([col for col in all_columns if col[0].isupper()])
ms = MaterialSelector()

valid = 0

for index, row in df_test.iterrows():
    d = {}

    for x in material_columns:
        d[x] = row[x]

    if ms.is_valid(d):
        valid += 1
        


print(valid, len(df_test))