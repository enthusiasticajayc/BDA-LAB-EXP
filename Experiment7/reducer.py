import pickle

with open('shuffled.pkl','rb') as file:
    shuffled = pickle.load(file)

def reduce(shuffled_dict):
    reduced = {}
    for i in shuffled_dict:
        if len(shuffled_dict[i]) > 0:
            reduced[i] = sum(shuffled_dict[i])/len(shuffled_dict[i])
    return reduced

final = reduce(shuffled)
print("Average volatile acidity in different classes of wine: ")
for k, v in final.items():
    print(k,':', v)
