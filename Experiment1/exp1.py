import pandas as pd
import numpy as np

dataset1 = pd.read_csv("crime.csv")
print(dataset1.head())
print(dataset1.tail())
print(type(dataset1))

print(dataset1.isnull().tail())
print(dataset1.isnull().sum())
print(dataset1[dataset1.Robbery.isnull()])
print(dataset1['Robbery'].value_counts())

for col in dataset1.columns:
    print(dataset1[col].value_counts())

dataset_length = len(dataset1)
dataset_col = len(dataset1.columns)
print(dataset1.describe())
print(dataset1.Murder.describe())
print(dataset1.skew(numeric_only=True))
print(dataset1.var(numeric_only=True))
print(dataset1.kurtosis(numeric_only=True))
print(dataset1.dtypes)

arr_0d = np.array(42)
print(arr_0d)

arr_1d = np.array([1, 2, 3, 4, 5]) 
print(arr_1d)

arr_2d = np.array([[1, 2, 3], [4, 5, 6]]) 
print(arr_2d)

arr_3d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(arr_3d)
print("Dimensions:", arr_3d.ndim)

arr = np.array([1, 2, 3, 4])
print(arr[0])
print(arr[1])
print(arr[2] + arr[3])

arr_2d_idx = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('2nd element on 1st row: ', arr_2d_idx[0, 1])
print('5th element on 2nd row: ', arr_2d_idx[1, 4])
