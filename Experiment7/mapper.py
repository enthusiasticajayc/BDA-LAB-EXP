import pandas as pd
import pickle

data = pd.read_csv('data.csv')

mid = len(data) // 2
slice1 = data.iloc[:mid, :]
slice2 = data.iloc[mid:, :]

def mapper(data_slice):
    mapped = []
    for index, row in data_slice.iterrows():
        mapped.append((row['quality'], row['volatile acidity']))
    return mapped

map1 = mapper(slice1)
map2 = mapper(slice2)

shuffled = {3.0: [], 4.0: [], 5.0: [], 6.0: [], 7.0: [], 8.0: []}

for i in [map1, map2]:
    for j in i:
        if j[0] in shuffled:
            shuffled[j[0]].append(j[1])

with open('shuffled.pkl', 'wb') as file:
    pickle.dump(shuffled, file)

print("Data has been mapped and saved to shuffled.pkl.")