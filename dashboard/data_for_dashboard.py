import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# List of available courses
courses = ['Web Development', 'PowerBI', 'C++ DSA', 'Python', 'Java', 'MongoDB', 'Machine Learning']

def generate_course_data():
    num_courses = np.random.randint(3, 6)
    selected_courses = np.random.choice(courses, num_courses, replace=False)
    
    course_data = {}
    for course in courses:
        if course in selected_courses:
            completion = np.random.randint(0, 101)
            course_data[f"{course}_enrolled"] = 1
            course_data[f"{course}_completion"] = completion
            course_data[f"{course}_teacher_completion"] = np.random.randint(completion, 101)
        else:
            course_data[f"{course}_enrolled"] = 0
            course_data[f"{course}_completion"] = 0
            course_data[f"{course}_teacher_completion"] = 0
    
    return course_data

# Read the CSV file
df = pd.read_csv('modified_student_data.csv')

# Remove unnecessary columns and rename
columns_to_keep = ['school', 'sex', 'age', 'G1', 'G2', 'G3', 'name', 'email', 'password', 'attendance']
df = df[columns_to_keep]
df = df.rename(columns={'G1': 'first_year_marks', 'G2': 'second_year_marks', 'G3': 'third_year_marks'})

# Convert columns to numeric
numeric_columns = ['first_year_marks', 'second_year_marks', 'third_year_marks', 'attendance']
df[numeric_columns] = df[numeric_columns].apply(pd.to_numeric, errors='coerce')

# Convert marks to percentage
for year in ['first', 'second', 'third']:
    df[f'{year}_year_marks_percentage'] = (df[f'{year}_year_marks'] / 20) * 100

# Add attendance columns
df['first_year_attendance'] = df['attendance']
df['second_year_attendance'] = np.minimum(100, df['attendance'] + np.random.randint(-5, 6, size=len(df)))

# Calculate overall performance and attendance improvement
df['overall_performance'] = df[[f'{year}_year_marks_percentage' for year in ['first', 'second', 'third']]].mean(axis=1)
df['attendance_improvement'] = df['second_year_attendance'] - df['first_year_attendance']

# Generate and add course data
course_data = pd.DataFrame([generate_course_data() for _ in range(len(df))])
df = pd.concat([df, course_data], axis=1)

# Calculate total courses enrolled and average completion
df['total_courses_enrolled'] = df[[f"{course}_enrolled" for course in courses]].sum(axis=1)
df['average_course_completion'] = df[[f"{course}_completion" for course in courses]].mean(axis=1)

# Add study hours
df['daily_study_hours'] = np.random.randint(1, 9, size=len(df))

# Generate average monthly performance for each student
df['average_monthly_performance'] = np.random.uniform(60, 90, size=len(df))

# Reorder columns
column_order = [
    'name', 'email', 'password', 'school', 'sex', 'age',
    'first_year_marks_percentage', 'second_year_marks_percentage', 'third_year_marks_percentage',
    'first_year_attendance', 'second_year_attendance',
    'overall_performance', 'attendance_improvement',
    'total_courses_enrolled', 'average_course_completion',
    'daily_study_hours', 'average_monthly_performance'
] + [f"{course}_enrolled" for course in courses] + [f"{course}_completion" for course in courses] + [f"{course}_teacher_completion" for course in courses]

df = df[column_order]

# Save the modified data to a new CSV file
df.to_csv('enhanced_student_dashboard_data.csv', index=False)

print("Data processing complete. Enhanced data saved to 'enhanced_student_dashboard_data.csv'")
