import pandas as pd
import numpy as np


# series -- column + index
# dataframe -- table 

# ls = [1,2,3,4]
# arr = np.array(ls)
# ser = pd.Series(arr)
# print(ser)

ser2 = pd.Series(np.arange(50))
ser2 =ser2[(ser2 > 10) & (ser2 < 35)]


print(ser2)
