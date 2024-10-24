This project focuses on implementing and comparing different machine learning models to detect network intrusions. The models used are Logistic Regression, Naive Bayes, and Random Forest, with a focus on evaluating their performance using various classification metrics.

Project Structure
classification_report.txt: General classification report for the models.
classification_report_logistic_regression.txt: Classification report for Logistic Regression.
classification_report_naive_bayes.txt: Classification report for Naive Bayes.
confusion_matrix_logistic_regression.png: Confusion matrix visualization for Logistic Regression.
confusion_matrix_naive_bayes.png: Confusion matrix visualization for Naive Bayes.
confusion_matrix_random_forest.png: Confusion matrix visualization for Random Forest.
logistic.py: Script to run Logistic Regression for intrusion detection.
naive.py: Script to run Naive Bayes for intrusion detection.
summary.py: Script to summarize and compare the results of the different models.
Prerequisites
Make sure you have the following installed on your system:

Python 3.x
Pip (Python package manager)
Required libraries: scikit-learn, matplotlib, pandas, and numpy
You can install the required libraries using the command:

bash
Copy code
pip install -r requirements.txt
Alternatively, you can install them manually:

bash
Copy code
pip install scikit-learn matplotlib pandas numpy
Running the Project
To run this project on your local machine, follow the steps below:

1. Clone the Repository
bash
Copy code
git clone https://github.com/your-username/intrusion-detection-systems.git
cd intrusion-detection-systems
2. Running Logistic Regression
Run the Logistic Regression model with the following command:

bash
Copy code
python logistic.py
This will output a confusion matrix and a classification report for Logistic Regression.

3. Running Naive Bayes
Run the Naive Bayes model with the following command:

bash
Copy code
python naive.py
This will output a confusion matrix and a classification report for Naive Bayes.

4. Summary and Comparison
Run the summary script to compare the results from all models:

bash
Copy code
python summary.py
This script will print out key metrics from the classification reports and provide a comparative analysis of the models.

Results
The classification reports give detailed metrics such as precision, recall, F1-score, and accuracy for each model.
The confusion matrices provide a visual representation of the model performance on test data.
Contributing
Feel free to contribute to the project by opening a pull request. For major changes, please open an issue first to discuss what you would like to change.

License
This project is licensed under the MIT License.
