# import independencies
import pandas as pd

# create/import data
data = {
    'Apples': [35, 41],
    'Bananas': [21, 34]
}

df = pd.DataFrame(data, index = ['2017 Sales', '2018 Sales'])  

df.to_csv('fruit.csv')

# print(df)

# create data fram from data

# export data frame to csv file
