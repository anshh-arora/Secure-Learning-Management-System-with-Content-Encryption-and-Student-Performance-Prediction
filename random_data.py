import pandas as pd
import numpy as np
import random

# List of male Indian names
male_names = [
    "Aarav", "Vivaan", "Aditya", "Vihaan", "Arjun", "Ayaan", "Reyansh", "Ishaan", "Karthik", 
    "Ansh", "Karan", "Arman", "Piyush", "Harsh", "Harshit", "Aditya", "Kunal", "Aman"
]

# List of female Indian names
female_names = [
    "Ananya", "Saanvi", "Aarohi", "Isha", "Diya", "Mira", "Kavya", "Navya", "Sia", 
    "Aanya", "Aisha", "Sakshi", "Gargi", "Neha", "Tanya", "Ritika", "Ishita"
]

indian_last_names = [
    "Arora", "Sharma", "Singh", "Puniya", "Gautam", "Verma", "Kapoor", "Dangwal", 
    "Chakarvarty", "Chaudhary", "Negi", "Goyal", "Gupta", "Rathore", "Pandey", 
    "Sethi", "Aggarwal", "Nain"
]

# Number of students
num_students = 10000

# Generate data
data = {
    "Student_ID": [i for i in range(1, num_students + 1)],
    "First Name": [random.choice(male_names + female_names) for _ in range(num_students)],
    "Last Name": [random.choice(indian_last_names) for _ in range(num_students)],
    "Age": np.random.randint(16, 25, size=num_students),
    "DSA_Marks": np.random.randint(20, 100, size=num_students),
    "PowerBI_Marks": np.random.randint(50, 100, size=num_students),
    "Web_Development_Marks": np.random.randint(30, 100, size=num_students),
    "SQL_Marks": np.random.randint(60, 100, size=num_students),
    "Machine_Learning_Marks": np.random.randint(10, 100, size=num_students),
    "Attendance (%)": np.random.randint(50, 100, size=num_students),
    "Previous_Year_Marks": np.random.randint(40, 95, size=num_students),
    "Study_Hours_per_Week": np.random.randint(5, 30, size=num_students),
}

# Create a DataFrame
df = pd.DataFrame(data)

# Generate the Gender column
df["Gender"] = df["First Name"].apply(lambda name: "Male" if name in male_names else "Female")

# Generate the Email column
df["Email"] = df["First Name"].str.lower() + "." + df["Last Name"].str.lower() + "@gmail.com"

# Generate the Password column
df["Password"] = df.apply(lambda row: row["First Name"].lower() + str(np.random.randint(1000, 2000)), axis=1)

# Save to CSV
file_path = 'student_data.csv'
df.to_csv(file_path, index=False)

file_path
