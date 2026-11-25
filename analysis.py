import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('pokemon.csv')

data = data[['Name','Generation','Weight','Height','Type1','Type2','Ability1','Ability2','Ability_Hidden','Category','Mega_Evolution_Flag','Total']]

data['Type_Combo'] = data['Type1'] + ',' + data['Type2']
data['Type_count'] = data[['Type1', 'Type2']].notna().sum(axis=1)
data['Type_Combo'] = data['Type_Combo'].fillna("No")
data['Type_Combo'] = data['Type_Combo'].apply(
    lambda x: ','.join(sorted(set(x.split(','))))
)

data['Ability_Combo'] = data[['Ability1', 'Ability2']].apply(
    lambda row: ','.join(sorted(set(row.dropna()))),
    axis=1
)
data['Ability_count'] = data[['Ability1', 'Ability2']].notna().sum(axis=1)

data['Mega_Evolution_Flag'] = data['Mega_Evolution_Flag'].fillna("No")
data['Mega_Evolution_Flag'] = data['Mega_Evolution_Flag'].replace("Mega","Yes")

data['Ability_Hidden'] = data['Ability_Hidden'].fillna("No")
print(data.head())

print(data.info())
# data.to_csv("pokemon_data.csv",index=False)
