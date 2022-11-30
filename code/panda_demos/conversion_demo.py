import numpy as np
# this code demonstrates the conversion of data to different types [for usage]

import pandas as pandas

# first : summary of categorical data
data_frame = pandas.read_csv('../../data/students.csv')
# print(data_frame)

# compute statistics of grade
# print(data_frame['Grade'].value_counts().sort_values())

# compute statistics as per gender
# print(data_frame['Gender'].value_counts().sort_values())

# compute statistics as per gender then grade
gender_grades_data_frame = data_frame.value_counts(['Gender', 'Grade'])
print(gender_grades_data_frame)

# Many ML algorithms require all input and output variables to be numeric
# This leads to the requirement of converting from categorical data to numeric data

# Categorical data examples
#   gender: Male or Female
#   color: Red, Blue, Green, etc.
#   winning position: first, second, third, etc.

# Integer encoding:
#   each unique categorical value is assigned an integer value

# replace gender label as (Male: 1 and Female: 0)
gender_grades_data_frame = data_frame.replace({"Male": 1, "Female": 2})
print(gender_grades_data_frame)

# replace gender label as (Male: 1 and Female: 0, 1st class: 1, 2nd class:2, 3rd class:3)
gender_grades_data_frame = data_frame.replace({"Male": 1, "Female": 2, "1st Class": 1, "2nd Class": 2, "3rd Class": 3})
print(gender_grades_data_frame)
