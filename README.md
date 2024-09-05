# Secure Learning Management System with Content Encryption and Student Performance Prediction

## Project Overview

The objective of this project is to develop a comprehensive learning management system that incorporates content encryption features and leverages neural networks for student performance prediction. Our system will provide a secure platform where students can learn various subjects, read educational articles, and stay updated with daily news in the education sector. Additionally, it will include personalized dashboards and prediction models to enhance the learning experience.

# Project Structure
lms_project/
│
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   ├── forms.py
│   ├── utils.py
│   └── ml_model.py
│
├── static/
│   ├── css/
│   └── js/
│
├── templates/
│   ├── base.html
│   ├── login.html
│   ├── dashboard.html
│   ├── course_content.html
│   └── performance_prediction.html
│
├── instance/
│   └── config.py
│
├── migrations/
│
├── tests/
│
├── venv/
│
├── config.py
├── run.py
└── requirements.txt


## Main Architecture

### 1. Website Development

The web application will be designed to offer the following functionalities:
- **Learning Platform:** A section where students can access educational content, including articles and daily news updates related to education.
- **Personalized Dashboards:** Each student will have a personalized dashboard that provides insights into their academic performance. This will include:
  - **Focus Areas:** Highlight subjects where the student needs improvement.
  - **Strengths:** Identify subjects where the student is performing well.

### 2. Power BI Integration

- **Dynamic Dashboards:** We will create interactive dashboards in Power BI that are integrated into the web page. The dashboards will update dynamically to reflect changes in the underlying data. This will provide real-time insights and analytics for students and teachers.
- **Integration Details:** The dashboards will be embedded into the web application and will refresh automatically when data changes in Power BI.

### 3. Predictive Modeling

- **Neural Network Model:** We will develop a predictive model using neural networks to forecast student performance. This model will be deployed on the web server and will be used for the following purposes:
  - **Teacher Access:** Teachers will have full access to the predictive model, allowing them to view detailed predictions and performance insights for their students.
  - **Student Access:** Students will have limited access, receiving motivational feedback and actionable recommendations instead of direct performance predictions. This approach is designed to encourage improvement and maintain motivation.

## Team Roles

- **Armaan and Piyush (Web Development):** 
  - **Armaan:** Responsible for creating and designing web pages, including the learning platform and the personalized dashboard for students.
  - **Piyush:** Focused on integrating Power BI dashboards into the web application and ensuring dynamic updates. Also responsible for implementing the user interface and experience.

- **Ansh and Karan (Data Science):**
  - **Model Development:** Develop and train the neural network model for predicting student performance.
  - **Deployment:** Deploy the predictive model on a Flask server and ensure it integrates seamlessly with the web application.
  - **Karan** Create and configure Power BI dashboards for integration into the web application.


