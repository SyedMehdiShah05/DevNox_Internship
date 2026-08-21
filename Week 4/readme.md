# Week 4 — ML Foundations I

This week focuses on the **fundamentals of Machine Learning**, including statistical foundations, linear regression, logistic regression, gradient descent, classification metrics, sigmoid functions, and decision boundaries.

## 📚 Learning Objectives

By completing Week 4, you will learn how to:

* Calculate mean, median, variance, and standard deviation.
* Understand the mathematical foundation of linear regression.
* Implement gradient descent manually.
* Train Linear Regression using Scikit-learn.
* Evaluate regression models using MAE, MSE, and R².
* Understand and implement the sigmoid function.
* Train a Logistic Regression classifier.
* Evaluate classification models using accuracy, precision, and recall.
* Visualize a classifier's decision boundary.
* Build a complete beginner-level ML project.

## Task 1 — Statistics Fundamentals
### Objective

Calculate the following statistical measures manually and verify the results using NumPy:

* Mean
* Median
* Variance
* Standard Deviation
 
 
```python
np.mean()
np.median()
np.var()
np.std()
```

---

## Task 2 — Linear Regression From Scratch

### Objective

Implement **Simple Linear Regression** without using Scikit-learn.

The model follows:

```text
y = mx + b
```

where:

* `m` = slope
* `b` = intercept
* `x` = input feature
* `y` = predicted output

### Gradient Descent

The parameters are updated iteratively using:

```text
m = m - learning_rate × dm
b = b - learning_rate × db
```

### Concepts Covered

* Linear regression
* Mean Squared Error
* Gradient descent
* Learning rate
* Model parameters
* Prediction
* Loss minimization

---

## Task 3 — Scikit-learn Linear Regression

### Objective

Train a Linear Regression model using:

```python
from sklearn.linear_model import LinearRegression
```

The model is evaluated using:

### MAE

**Mean Absolute Error**

Measures the average absolute difference between actual and predicted values.

```text
MAE = average(|y - ŷ|)
```

### MSE

**Mean Squared Error**

Penalizes larger errors more heavily.

```text
MSE = average((y - ŷ)²)
```

### R² Score

Measures how well the model explains the variance in the target variable.

```text
R² = 1 → perfect prediction
R² = 0 → explains no variance
```

---

## Task 4 — Sigmoid Function

### Objective

Implement the sigmoid function manually.

The mathematical formula is:

```text
σ(x) = 1 / (1 + e⁻ˣ)
```

The sigmoid function converts any real-valued number into a value between:

```text
0 and 1
```

### Example

```text
x = -2  → approximately 0.119
x =  0  → 0.500
x =  2  → approximately 0.881
```

### Why It Is Important

Sigmoid is commonly used in **binary classification** to represent a probability.

For example:

```text
Probability >= 0.5 → Class 1
Probability <  0.5 → Class 0
```

---

# Task 5 — Logistic Regression

### Objective

Train a Logistic Regression classifier and evaluate its performance.

Example classification problem:

```text
Study Hours → Pass / Fail
```

### Metrics

The model is evaluated using:

* Accuracy
* Precision
* Recall

### Accuracy

Percentage of predictions that are correct.

```text
Accuracy = Correct Predictions / Total Predictions
```

### Precision

Of all students predicted as **Pass**, how many actually passed?

```text
Precision = TP / (TP + FP)
```

### Recall

Of all students who actually passed, how many were correctly identified?

```text
Recall = TP / (TP + FN)
```

---

# Task 6 — Decision Boundary

### Objective

Create a simple 2D classification dataset and visualize the classifier's **decision boundary**.

The visualization should show:

```text
Feature 1
   ↑
   |
   |       ● ● ●
   |      ● ●
   |
   |  ○ ○
   | ○ ○ ○
   |
   +----------------→ Feature 2
```

The decision boundary separates the two classes.

### Concepts Covered

* 2D classification
* Feature space
* Class separation
* Decision boundary
* Logistic Regression
* Matplotlib visualization

---

# 🚀 Task 7 : Mini Project 1— Marks Predictor & Pass/Fail Classifier

## Project Overview

The mini project combines two Machine Learning problems using **study hours** as the input feature.

### Model 1 — Regression

Predict the student's marks from the number of study hours.

```text
Study Hours → Regression Model → Predicted Marks
```

Example:

```text
Study Hours = 7
        ↓
Linear Regression
        ↓
Predicted Marks = 72
```

### Model 2 — Classification

Predict whether the student will pass or fail.

```text
Study Hours → Logistic Regression → Pass / Fail
```

Example:

```text
Study Hours = 7
        ↓
Logistic Regression
        ↓
PASS
```

---

## 📊 Mini Project Workflow

```text
             Dataset
                │
                ▼
        Data Preparation
                │
        ┌───────┴────────┐
        ▼                ▼
   Regression       Classification
        │                │
        ▼                ▼
Linear Regression  Logistic Regression
        │                │
        ▼                ▼
 Predicted Marks    Pass / Fail
        │                │
        ▼                ▼
 MAE, MSE, R²     Accuracy, Precision, Recall
```

---

## 📈 Regression Evaluation

The regression model should report:

```text
MAE
MSE
R² Score
```

Example output:

```text
Regression Results
------------------
MAE: 3.25
MSE: 14.82
R² Score: 0.94
```

---

## 🎯 Classification Evaluation

The classification model should report:

```text
Accuracy
Precision
Recall
```

Example:

```text
Classification Results
----------------------
Accuracy: 0.90
Precision: 0.91
Recall: 0.89
```

---

# 🛠️ Technologies Used

* **Python**
* **NumPy**
* **Pandas**
* **Matplotlib**
* **Scikit-learn**
* **Jupyter Notebook / VS Code**

 

# 🧠 Key Concepts Learned

| Topic               | What I Learned                      |
| ------------------- | ----------------------------------- |
| Mean                | Central tendency                    |
| Median              | Middle value of ordered data        |
| Variance            | Spread of data                      |
| Standard Deviation  | Typical distance from the mean      |
| Linear Regression   | Predict continuous values           |
| Gradient Descent    | Optimize model parameters           |
| MAE                 | Average absolute prediction error   |
| MSE                 | Squared prediction error            |
| R²                  | Explained variance                  |
| Sigmoid             | Converts values to 0–1              |
| Logistic Regression | Binary classification               |
| Accuracy            | Overall correctness                 |
| Precision           | Correctness of positive predictions |
| Recall              | Ability to find actual positives    |
| Decision Boundary   | Separates classes in feature space  |


Note :
```
Task 7 : Mini Practice Project 2 , Supervised Machine Learning
Task 7 : Mini Practice Project 3 , Regression Algorithms
Task 7 : Mini Practice Project 4 , Classification Algorithms
```
## 👨‍💻 Author

**Mehdi Mosvii**

BS Computer Science Student
Interested in **Data Science, Machine Learning, Deep Learning & Artificial Intelligence**

---

⭐ This repository documents is my Internship  **Week 4 Machine Learning Foundations** practice and progress.
