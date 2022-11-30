
import pandas as pandas

# data frame with students information [key field being student id]
data_students = pandas.read_csv('../../data/students.csv')
print(data_students)

# data frame for the marks and city information [key field being student id]
city_and_marks_frame = pandas.read_csv('../../data/marks.csv')
print(city_and_marks_frame)

# merge the data for the students' information and marks' information to a single data frame
data_frame = pandas.merge(data_students, city_and_marks_frame, on='Student_id')
print(data_frame)

dtypes = data_frame.dtypes
print('Data frame dtypes: ', dtypes)

# display the data frame sorted on age, marks, city
data_frame = data_frame.sort_values(by=['Age', 'Mark', 'City'])
print(data_frame)

# display the data frame sorted on
# age [ascending] then
# marks [descending] and then
# city [ascending]
data_frame = data_frame.sort_values(by=['Age', 'Mark', 'City'], ascending=[True, False, True])
print(data_frame)

print("NA summary")
print(data_frame.isna().sum())

# display the data frame sorted on age, marks, city [NA values must be first]
print("Sort [NA first]")
data_frame = data_frame.sort_values(by=['City', 'Mark', 'Age'], ascending=[True, False, True], na_position='first')
print(data_frame)
