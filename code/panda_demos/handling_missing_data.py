
# here we will observe some approaches to handle missing data using pandas

import pandas as pandas

# read the csv file and generate a data frame to use

data_frame = pandas.read_csv('../../data/banking.csv')
# print(data_frame)
print(data_frame.describe())

# exclude the header from the data frame [just have header field as numbers rather than labelled headers]
# data_frame = pandas.read_csv('../data/banking.csv')
print(data_frame)

dtypes = data_frame.dtypes
print(dtypes)

# finding the summary for NA values
na_summary = data_frame.isna().sum()
print(na_summary)

# removing the entries having NA values
data_frame = data_frame.dropna()

na_summary = data_frame.isna().sum()
print(na_summary)
