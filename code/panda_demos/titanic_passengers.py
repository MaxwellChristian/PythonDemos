import matplotlib
# using the titanic.csv for various statistics related to the passengers of Titanic

import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline

titanic_dataframe = pd.read_csv('../../data/titanic_dataset/train.csv')

# Information about the data set
titanic_dataframe.info()

# Number of passengers in each class
print(titanic_dataframe.groupby('Pclass')['Pclass'].count())

# Student exercise
# Number of men and women in each of the passenger class
print(titanic_dataframe.groupby(['Gender', 'Pclass'])['Gender'].count())

# Number of passengers who survived in each class grouped by gender.
# Also total was found for each class grouped by gender.
print(titanic_dataframe.pivot_table('Survived', 'Gender', 'Pclass', aggfunc=np.sum, margins=True))

# Passengers who survived and who didn't survive grouped by class and gender
table = pd.crosstab(index=[titanic_dataframe.Survived,titanic_dataframe.Pclass], columns=[titanic_dataframe.Gender, titanic_dataframe.Embarked])
print(table)

# unstacked table
print(table.unstack())

# describe the age of passengers
print(titanic_dataframe.Age.describe())

# Another way to plot a histogram of ages is shown below
print(titanic_dataframe['Age'].hist(bins=50))
