import pandas as pd
import random
import numpy as np

# Load the dataset with the correct delimiter (semicolon in this case)
df = pd.read_csv("student-mat.csv", delimiter=';')

# Check the column names to ensure they are correctly separated
print(df.columns)

# Add a name column based on gender ('sex' column)
male_names = ["Ansh", "Karan", "Piyush", "Anshul", "Vivek", "Ram", "Abdul"]
female_names = ["Mary", "Khushi", "Manisha", "Preeti", "Varsha"]

df['name'] = df['sex'].apply(lambda x: random.choice(male_names) if x == 'M' else random.choice(female_names))

# Add email column (using the generated name)
df['email'] = df['name'].str.lower() + '@gmail.com'

# Add password column (using the name + random 4 digit number)
df['password'] = df['name'].str.lower() + df['sex'].apply(lambda x: str(random.randint(1000, 9999)))

# Add random attendance percentage (between 50 and 100)
df['attendance'] = np.random.randint(50, 101, df.shape[0])

# Adjust the grades G1, G2, G3 based on attendance
df.loc[df['attendance'] < 60, ['G1', 'G2', 'G3']] = df.loc[df['attendance'] < 60, ['G1', 'G2', 'G3']] - 1
df.loc[df['attendance'] > 90, ['G1', 'G2', 'G3']] = df.loc[df['attendance'] > 90, ['G1', 'G2', 'G3']] + 1

# Save the modified dataset to a CSV file
df.to_csv('modified_student_data.csv', index=False)

print("Modified dataset saved to 'modified_student_data.csv'")
