import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import tensorflow as tf

# Step 1: Load the data
data = {
    'Student_ID': [1, 2, 3, 4, 5],
    'First Name': ['Vihaan', 'Kavya', 'Navya', 'Aditya', 'Vihaan'],
    'Last Name': ['Arora', 'Gautam', 'Dangwal', 'Arora', 'Gautam'],
    'Age': [21, 23, 23, 24, 24],
    'Gender': ['Male', 'Female', 'Female', 'Male', 'Female'],
    'DSA_Marks': [58, 77, 90, 93, 54],
    'PowerBI_Marks': [59, 87, 95, 88, 55],
    'Web_Development_Marks': [66, 65, 67, 76, 80],
    'SQL_Marks': [80, 81, 63, 87, 85],
    'Machine_Learning_Marks': [71, 78, 72, 55, 79],
    'Email': ['vihaan.arora@gmail.com', 'kavya.gautam@gmail.com', 'navya.dangwal@gmail.com', 'aditya.arora@gmail.com', 'vihaan.gautam@gmail.com'],
    'Password': ['vihaan1234', 'kavya1234', 'navya1234', 'aditya1234', 'vihaan1234']
}

df = pd.DataFrame(data)

# Step 2: Data Cleaning and Preprocessing
# Remove unnecessary columns
df = df.drop(['Student_ID', 'First Name', 'Last Name', 'Email', 'Password'], axis=1)

# Encode categorical variables
df['Gender'] = df['Gender'].map({'Male': 0, 'Female': 1})

# Split features and target
X = df.drop('Machine_Learning_Marks', axis=1)
y = df['Machine_Learning_Marks']

# Step 3: Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 4: Feature Scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Step 5: Build the Neural Network Model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(1)
])

model.compile(optimizer='adam', loss='mse', metrics=['mae'])

# Step 6: Train the model
history = model.fit(X_train_scaled, y_train, epochs=100, batch_size=32, validation_split=0.2, verbose=0)

# Step 7: Evaluate the model
loss, mae = model.evaluate(X_test_scaled, y_test, verbose=0)
print(f"Test MAE: {mae:.2f}")

# Step 8: Make predictions
predictions = model.predict(X_test_scaled)