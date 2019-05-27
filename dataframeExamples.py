#   ANOTHER EXAMPLE OF USING PANDAS.
#   THIS TIME, WE ARE CODING WITH DATAFRAMES.

#   IMPORT LIBRARIES AND MODULES
import numpy as np
import pandas as pd


def header(msg):
        print('-' * 50)
        print('[' + msg + ' ]')

# 1.    LOAD HARD-CODED DATA INTO A DATAFRAME
header("1. Load hard-coded data into a df")
df1 = pd.DataFrame(
    [['Jan', 58, 42, 74, 22, 2.95],
    ['Fev',61,45,78,26,3.02],
    ['Mar',65,48,84,25,2.34],
    ['Apr',67,54,85,32,3.45],
    ['May',58, 42, 74, 22, 2.95],
    ['Jun',61,45,78,26,3.02],
    ['Jul',65,48,84,25,2.34],
    ['Aug',67,54,85,32,3.45],
    ['Sep',65,48,84,25,2.34],
    ['Oct',58, 42, 74, 22, 2.95],
    ['Nov',61,45,78,26,3.02],
    ['Dec',58, 42, 74, 22, 2.95]],
    index = [0,1,2,3,4,5,6,7,8,9,10,11],
    columns = ['month', 'avg_high','avg_low','record_high','record_low','avg_precipitation'])

print(df1)


# 2.    LOAD TEXT FILE INTO A DATAFRAME
header("2. Load text file into a dataframe")
filename = "../documents/dataset/Fremont_weather.txt"
df2 = pd.read_csv(filename)
print(df2)


# 3.    PRINT FIRST 5 OR LAST 3 ROWS OF DF
header("3. df.head()")
print(df2.head())
header("3. df.tail(3)")
print(df2.tail(3))


# 4.    GET DATA TYPES, INDEX, COLUMNS, VALUES
header("4. df.types")
print(df2.dtypes)

header("4. df.index")
print(df2.index)

header("4. df.columns")
print(df2.columns)

header("4. df.values")
print(df2.values)

