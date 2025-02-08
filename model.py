import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt

# Step 1: Load Dataset
data = pd.read_csv('loan_data.csv')

# Step 3: Visualization Examples

# 1. Bar plot of Loan_Status
plt.figure(figsize=(6, 4))
data['Loan_Status'].value_counts().plot(kind='bar', color=['blue', 'orange'])
plt.title('Loan Status Distribution')
plt.xlabel('Loan Status (0: No, 1: Yes)')
plt.ylabel('Count')
plt.show()

# 2. Histogram of Applicant Income
plt.figure(figsize=(8, 5))
plt.hist(data['ApplicantIncome'], bins=30, color='green', edgecolor='black')
plt.title('Distribution of Applicant Income')
plt.xlabel('Applicant Income')
plt.ylabel('Frequency')
plt.show()

# 3. Scatter plot: ApplicantIncome vs LoanAmount
plt.figure(figsize=(8, 5))
plt.scatter(data['ApplicantIncome'], data['LoanAmount'], alpha=0.5, color='purple')
plt.title('Applicant Income vs Loan Amount')
plt.xlabel('Applicant Income')
plt.ylabel('Loan Amount')
plt.show()

# 4. Pie chart of Property Area distribution
property_area_counts = data['Property_Area'].value_counts()
labels = ['Urban', 'Semiurban', 'Rural']
plt.figure(figsize=(6, 6))
plt.pie(property_area_counts, labels=labels, autopct='%1.1f%%', startangle=140, colors=['gold', 'lightblue', 'lightgreen'])
plt.title('Property Area Distribution')
plt.show()


# Step 3: Preprocessing the Dataset
data['LoanAmount']=data['LoanAmount'].fillna(data['LoanAmount'].median())
data['Credit_History']=data['Credit_History'].fillna(data['Credit_History'].median())
data['Loan_Amount_Term']=data['Loan_Amount_Term'].fillna(data['Loan_Amount_Term'].median())

# Step 4: Encode Categorical Variables
data['Property_Area'] = data['Property_Area'].map({'Urban': 2, 'Semiurban': 1, 'Rural': 0})
data['Self_Employed'] = data['Self_Employed'].map({'Yes': 1, 'No': 0})
data['Loan_Status'] = data['Loan_Status'].map({'Y': 1, 'N': 0})
data['Self_Employed']=data['Self_Employed'].fillna(data['Self_Employed'].median())
print(data.isnull().sum())
print(data.head(5))

# Step 5: Split Data into Features (X) and Target (y)
X = data.drop(columns=['Loan_Status','Loan_ID'])
y = data['Loan_Status']

# Step 6: Scale Numerical Features
scaler = StandardScaler()
X[['ApplicantIncome', 'LoanAmount', 'Loan_Amount_Term']] = scaler.fit_transform(
    X[['ApplicantIncome', 'LoanAmount', 'Loan_Amount_Term']])

# Step 7: Split into Train and Test Sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 8: Train Logistic Regression Model
model=RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
y_pred=model.predict(X_test)


# Step 9: Evaluate the Model
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

# Step 10: Save the model for deployment
import pickle
with open('loan_eligibility_model.pkl', 'wb') as file:
    pickle.dump(model, file)
print(f"Model saved to loan_eligibility_model.pkl")


