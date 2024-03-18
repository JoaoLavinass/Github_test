from math import nan
from optparse import Values
import pandas as pd
import numpy as np

'''
student_data = [
    {'name': 'Alice', 'age': 20, 'city': 'New York'},
    {'name': 'Bob', 'age': 18, 'city': 'Los Angeles'},
    {'name': 'Charlie', 'age': 22, 'city': 'Chicago'},
]

cs = pd.DataFrame(student_data)

order = cs.sort_values(by='age', ascending=False) #sort the pandas DataFrame by age, descending


cs['grade'] = np.random.randint(0, 100, len(cs))

print(cs['grade'].mean())

cs.describe() #give me the mean, percentil, etc.
'''

df = pd.read_csv('imdb_top_1000.csv')

print(df.info())
#1: find the missing values in 'duration'

#print(pd.isnull(df)) #print missing values

#print(pd.isna(df).sum()) #print the missing values by each key

df['Certificate'].fillna('Passed', inplace=True) #filling the NaN values with Passed

value = pd.isnull(df['Meta_score']).value_counts() #count the number of True and False values

df['Meta_score'].mean()

df['Meta_score'].fillna(df['Meta_score'].mean(), inplace=True) #fill the missing values with the mean

print(pd.isna(df).sum()) 

print('AAAAAAAAAAAAA')


