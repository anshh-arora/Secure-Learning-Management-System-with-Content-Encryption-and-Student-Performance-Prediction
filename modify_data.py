import pandas as pd
import random

# Load the original dataset
data = pd.read_csv("StudentsPerformance.csv")

# Generate unique student ID, names based on gender, emails, and passwords
def generate_student_data(df):
    male_names = ["Raj Verma", "Arun Kumar", "Vikram Reddy", "Rahul Nair", "Amit Malhotra"]
    female_names = ["Priya Sharma", "Neha Singh", "Anjali Patel", "Pooja Desai", "Riya Gupta"]

    student_data = []
    
    for idx, row in df.iterrows():
        student_id = idx + 1  # Unique student ID
        
        # Generate name based on gender
        if row['gender'] == 'male':
            name = random.choice(male_names)
        else:
            name = random.choice(female_names)
        
        # Generate email and password
        email_providers = ["gmail.com", "yahoo.com", "microsoft.com"]
        email = f"{name.split()[0].lower()}.{name.split()[1].lower()}@{random.choice(email_providers)}"
        password = f"{name.split()[0]}{random.randint(1000, 9999)}"
        
        # Append student data
        student_data.append([student_id, name, email, password])
    
    return student_data

# Generate student info with IDs, names, emails, and passwords
student_info = generate_student_data(data)
student_df = pd.DataFrame(student_info, columns=["student_id", "name", "email", "password"])

# Concatenate new columns with the original dataset
data_with_info = pd.concat([student_df, data], axis=1)

# Rename the subject columns
data_with_info.rename(columns={
    "math score": "Web Development",
    "reading score": "Python",
    "writing score": "Machine Learning"
}, inplace=True)

# Save the modified dataset to a CSV file
data_with_info.to_csv('modified_student_data.csv', index=False)

print("Modified dataset saved to 'modified_student_data.csv'")
