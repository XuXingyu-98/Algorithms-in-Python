import pandas as pd
import numpy as np

price = pd.Series([1.0, 1.4, 5], index=['a', 'b', 'c'])
quantity = pd.Series([5, 10, 8], index=['a', 'b', 'c'])
liters = pd.Series([1.5, 0.3, 1], index=['a', 'b', 'c'])
df = pd.DataFrame({'Price': price, 'Quantity': quantity, 'Liters': liters})
print(df)

arr = np.arange(6).reshape((3, 2))
df = pd.DataFrame(arr, columns=['c1', 'c2'], index=['a', 'b', 'c'])
print(df)
print(df.index)
print(df.columns)
print(df.values)
# get the first column
print(df['c1'])
# get the first row
print(df.loc['a'])