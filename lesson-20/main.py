import pandas as pd
# data1 = {'ProductID': [1, 2, 3],
#          'ProductName': ['Widget', 'Gadget', 'Doodad'],
#          'Category': ['Tools', 'Electronics', 'Toys']}
# df1 = pd.DataFrame(data1)

# data2 = {'ProductID': [1, 2, 4],
#          'Price': [19.99, 29.99, 15.99],
#          'Stock': [100, 200, 150]}
# df2 = pd.DataFrame(data2)

# df3 = pd.merge(df1, df2, on='ProductID', how='inner')
# print(df3)


# Data for students
data_students = {'StudentID': [1, 2, 3],
                 'Name': ['Anna', 'Bill', 'Cathy'],
                 'Major': ['Math', 'Physics', 'Chemistry']}

students = pd.DataFrame(data_students)

# Data for courses
data_courses = {'CourseID': [101, 102, 103],
                'CourseName': ['Calculus', 'Mechanics', 'Organic Chemistry'],
                'Credits': [4, 3, 4]}

courses = pd.DataFrame(data_courses)

# Data for enrollments
data_enrollments = {'StudentID': [1, 1, 2],
                    'CourseID': [101, 102, 103],
                    'Grade': ['A', 'B+', 'A-']}

enrollments = pd.DataFrame(data_enrollments)

df1 = pd.merge(enrollments, students, on='StudentID', how='inner') 
df1 = pd.merge(df1, courses, on='CourseID', how='inner')
df2 = df1[['Name', 'Major', 'CourseName', 'Credits', 'Grade']]

print(df2)
