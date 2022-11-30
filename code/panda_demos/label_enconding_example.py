
# converting categorical data to numeric using label encoding

# Categorical data examples
#   gender: Male or Female
#   color: Red, Blue, Green, etc.
#   winning position: first, second, third, etc.

# sometimes there does not exist any natural ordering between categories.
# for example the color
# integer encoding is not appropriate in such situations

# so one-hot encoding can be used
# One-Hot encoding:
# introduces a new binary variable for each unique integer value

#  e.g. for color being any one from Red/Green/Blue
# red   green   blue
# 1     0       0
# 0     1       0
# 0     0       1


import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder

df = pd.read_csv('../../data/banking.csv', header=0)
df = df.dropna()

data_column_category = df.select_dtypes(exclude=[np.number]).columns
print(data_column_category)

# print(df[data_column_category].head())

# Creating the object instance
label_encoder = LabelEncoder()

for i in data_column_category:
    df[i] = label_encoder.fit_transform(df[i])
print("Label Encoded Data: ")
print(df.head())

# ##########################################

# demonstrate one-hot encoding
# Performing Onehot Encoding
onehot_encoder = OneHotEncoder(sparse=False)
onehot_encoded = onehot_encoder.fit_transform(df[data_column_category])

# Creating a dataframe with encoded data with new column name
onehot_encoded_frame = pd.DataFrame(onehot_encoded, columns=onehot_encoder.get_feature_names(data_column_category))
print(onehot_encoded_frame.head())
