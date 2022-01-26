#pandas program to create and display a one-dimensional array-like object containing an array of data
import pandas as pd
ds = pd.Series([2, 4, 6, 8, 10])
print(ds)
#to convert a Panda module Series to Python list and it’s type
ds1 = pd.Series([2, 4, 6, 8, 10])
print("Pandas Series and type")
print(ds1)
print(type(ds1))
print("Convert Pandas Series to Python list")
print(ds1.tolist())
print(type(ds1.tolist()))
