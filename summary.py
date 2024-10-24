import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load the dataset
data = pd.read_csv(r"C:\Users\jayp4\Downloads\archive\03-01-2018.csv", low_memory=False)

# Print the first few rows and the column names
print(data.head())
print(data.columns)

# Replace 'Label' with the actual name of your target variable
target_column = 'Label'  # This is your target variable

# Drop non-numeric columns (like 'Timestamp') and any other columns not needed for training
X = data.drop(columns=[target_column, 'Timestamp'])  # Features

# Convert 'Protocol' column to strings before encoding
if 'Protocol' in X.columns:
    le = LabelEncoder()
    X['Protocol'] = X['Protocol'].astype(str)  # Convert to string
    X['Protocol'] = le.fit_transform(X['Protocol'])

# Ensure all features are numeric
X = X.apply(pd.to_numeric, errors='coerce')

# Check for NaN or infinite values and handle them
print("Checking for NaN and infinite values...")
print("NaN values:", X.isna().sum().sum())
print("Infinite values:", (X == float('inf')).sum().sum())

# Replace NaN and infinite values
X = X.fillna(0)  # Replace NaN with 0 (you can choose other strategies)
X.replace([float('inf'), -float('inf')], 0, inplace=True)  # Replace infinity with 0

# Drop any rows with NaN values resulting from conversion (if any remain)
X = X.dropna()
y = data.loc[X.index, target_column]  # Ensure y matches the cleaned X

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and fit the Random Forest classifier
rf_classifier = RandomForestClassifier(random_state=42)
rf_classifier.fit(X_train, y_train)

# Make predictions
y_pred = rf_classifier.predict(X_test)

# Calculate confusion matrix
conf_matrix = confusion_matrix(y_test, y_pred)
class_report = classification_report(y_test, y_pred)

# Print confusion matrix and classification report
print("Confusion Matrix:")
print(conf_matrix)

print("\nClassification Report:")
print(class_report)

# Save results directory
results_dir = r"D:\GPU\IDS\results"
os.makedirs(results_dir, exist_ok=True)

# Save classification report to a text file
with open(os.path.join(results_dir, 'classification_report.txt'), 'w') as f:
    f.write(class_report)

# Plot confusion matrix
plt.figure(figsize=(10, 7))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', xticklabels=rf_classifier.classes_, yticklabels=rf_classifier.classes_)
plt.title('Confusion Matrix - Random Forest Classifier')
plt.xlabel('Predicted')
plt.ylabel('True')
plt.savefig(os.path.join(results_dir, 'confusion_matrix_random_forest.png'))  # Save confusion matrix as an image
plt.show()
