
import pandas

# the data fetched and loaded using pandas is termed as DataFrame
# Data frame is generally a 2D data structure, mutable in nature and may consist of heterogeneous data
dataFrame = pandas.read_csv('../../data/marks.csv')

# print the dataframe
# print(dataFrame)

# fetch top most 10 records from the dataframe
# print(dataFrame.head(10))

# fetch the last 1o records from the dataframe
# print(dataFrame.tail(10))

# display the types of data in the dataframe
# print(dataFrame.dtypes)

# a basic summary of the dataframe
# print(dataFrame.info())

# each column from the dataframe is considered to be a series
# e.g. fetch all the cities from the dataframe
# print(dataFrame["City"])

# the following code demonstrates that the series is a 1D array and hence
# returns the count of rows and not columns
# print(dataFrame["City"].value_counts())

# # the following code demonstrates the count of rows and columns both
# focus on the double square brackets [ [] ]
# print(dataFrame[["City", "Mark"]].shape)

# fetch all such records which are for city 'Delhi'
delhi_records = dataFrame[dataFrame["City"] == "Delhi"]
# print(delhi_records)

# fetch all such records which are for city 'Delhi' or 'Mumbai'
# delhi_records = dataFrame[dataFrame["City"].isin(["Delhi", "Mumbai"])]
# print(delhi_records)

# fetch records where value is not missing [NaN]
non_missing_value_records = dataFrame[dataFrame["City"].notna()]
# print(non_missing_value_records)

# fetch records where value is missing [NaN]
# missing_value_records = dataFrame[dataFrame["City"].isna()]
# print(missing_value_records)

# fetch column values as per criteria [where criteria and result columns are different]
# fetch city names of students whose marks are greater than 80
city_names_for_marks_greater_than_80 = dataFrame.loc[dataFrame["Mark"] > 80, "City"]
print(city_names_for_marks_greater_than_80)

# fetch the records on basis of record number
# e.g. fetch 21st to 25th records
# print(dataFrame.iloc[25: 27])

# print all the city names from the records [i.e. unique city names from the records]
unique_city_names = set(non_missing_value_records["City"])
# print(unique_city_names)

# print all the unique city names in sorted order
# using "sorted()"
# print(sorted(unique_city_names))

# alternate way to sort is
# using "sort()". For this we need a list
unique_city_names = list(unique_city_names)
# unique_city_names.sort()
# print(unique_city_names)

unique_city_names.sort(reverse=True)
# print(unique_city_names)

# fetch all such city names (unique) where the marks availed are more than 80
print(set(city_names_for_marks_greater_than_80))
