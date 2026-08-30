# Week 5 — ML Foundations II

This week focuses on important **supervised learning, ensemble learning, unsupervised learning, clustering, and model validation techniques** using Python and Scikit-learn.

The week contains six practice tasks and one mini project.

---

## 📚 Topics Covered

* K-Nearest Neighbors (KNN)
* Decision Trees
* Random Forest
* Feature Importance
* K-Means Clustering
* Elbow Method
* DBSCAN
* K-Fold Cross-Validation
* Student Segmentation
* Feature Scaling
* PCA Visualization

---

# 📁 Project Structure

```text
Week5/
│
├── Task1_KNN/
│
├── Task2_DecisionTree/
│
├── Task3_RandomForest/
│   
├── Task4_KMeans/
│  
├── Task5_DBSCAN/
│   
├── Task6_CrossValidation/
│
└── MiniProject_StudentSegmentation/


---

# 🧠 Task 1 — K-Nearest Neighbors From Scratch

## Objective

Implement the **K-Nearest Neighbors (KNN)** classification algorithm without using Scikit-learn's KNN implementation.

## Concepts

* Euclidean distance
* Nearest neighbors
* Majority voting
* Classification
* Effect of `k`
* Feature scaling

## Euclidean Distance

The distance between two points is calculated using:

```text
d = √((x₁ - x₂)² + (y₁ - y₂)²)
```

## Workflow

```text
New Data Point
      ↓
Calculate Distance
      ↓
Sort Distances
      ↓
Select K Nearest Points
      ↓
Majority Voting
      ↓
Prediction
```

## Example

For:

```text
New point = [172, 68]
K = 3
```

The algorithm finds the three closest training samples and predicts the class using majority voting.

---

# 🌳 Task 2 — Decision Tree Classifier

## Objective

Train a Decision Tree classifier and visualize the resulting tree.

## Dataset

The Iris dataset is used for classification.

## Concepts

* Root node
* Decision nodes
* Leaf nodes
* Gini impurity
* Entropy
* Information gain
* Maximum tree depth
* Overfitting
* Underfitting

## Workflow

```text
Dataset
   ↓
Feature Selection
   ↓
Find Best Split
   ↓
Create Decision Nodes
   ↓
Continue Splitting
   ↓
Leaf Node
   ↓
Prediction
```

## Visualization

The trained Decision Tree is visualized using:

```python
from sklearn.tree import plot_tree
```

Experiment with different values of:

```python
max_depth=1
max_depth=3
max_depth=None
```

and observe how tree complexity changes.

---

# 🌲 Task 3 — Random Forest

## Objective

Train a Random Forest classifier and compare it with a single Decision Tree.

Random Forest is an ensemble learning method that combines multiple Decision Trees.

## Workflow

```text
Training Dataset
       ↓
 ┌─────┼─────┐
 ↓     ↓     ↓
Tree  Tree  Tree
 1     2     3
 ↓     ↓     ↓
Prediction
       ↓
Majority Voting
       ↓
Final Prediction
```

## Comparison

The following metrics are compared:

* Decision Tree accuracy
* Random Forest accuracy
* Feature importance

## Feature Importance

Random Forest provides an estimate of how useful each feature is for making predictions.

Example:

```text
Feature              Importance
--------------------------------
Petal length           0.XX
Petal width            0.XX
Sepal length           0.XX
Sepal width            0.XX
```

---

# 🔵 Task 4 — K-Means From Scratch

## Objective

Implement the K-Means clustering algorithm without relying on Scikit-learn's K-Means implementation.

## K-Means Algorithm

```text
Choose K
   ↓
Initialize Centroids
   ↓
Calculate Distances
   ↓
Assign Points to Clusters
   ↓
Calculate New Centroids
   ↓
Repeat
   ↓
Final Clusters
```

## Important Concepts

* Centroids
* Euclidean distance
* Cluster assignment
* Iteration
* Convergence
* Within-cluster sum of squares
* Inertia

---

# 📉 Elbow Method

The Elbow Method is used to determine a suitable number of clusters.

The model is trained with different values of `K`.

```text
K = 1
K = 2
K = 3
K = 4
...
```

The inertia is recorded for each value.

The approximate point where the decrease in inertia becomes smaller is called the **elbow**.

```text
Inertia
  │\
  │ \
  │  \
  │   \__
  │      \__
  │         \__
  └────────────────
       K
```

---

# 🟣 Task 5 — DBSCAN

## Objective

Apply DBSCAN clustering and compare its results with K-Means.

DBSCAN stands for:

**Density-Based Spatial Clustering of Applications with Noise**

## Main Parameters

### `eps`

Maximum distance between two samples for them to be considered neighbors.

### `min_samples`

Minimum number of neighboring samples required to form a dense region.

## Workflow

```text
Data
 ↓
Find Dense Regions
 ↓
Expand Clusters
 ↓
Identify Sparse Points
 ↓
Clusters + Noise
```

DBSCAN labels noise points as:

```text
-1
```

## K-Means vs DBSCAN

| Feature                     | K-Means | DBSCAN           |
| --------------------------- | ------- | ---------------- |
| Requires number of clusters | Yes     | No               |
| Handles noise               | No      | Yes              |
| Detects arbitrary shapes    | Limited | Yes              |
| Main parameters             | K       | eps, min_samples |
| Distance-based              | Yes     | Yes              |
| Outlier detection           | Limited | Yes              |

---

# 🔄 Task 6 — K-Fold Cross-Validation

## Objective

Evaluate a machine learning model using **K-Fold Cross-Validation**.

Instead of using only one train/test split, the dataset is divided into multiple folds.

For example, with `k=5`:

```text
Fold 1 → Test
Fold 2 → Training
Fold 3 → Training
Fold 4 → Training
Fold 5 → Training

Fold 1 → Training
Fold 2 → Test
...
```

Every sample gets an opportunity to be part of the validation set.

## Evaluation

The final score is calculated using:

```text
Mean Accuracy
+
Standard Deviation
```

Example:

```text
Fold 1 = 0.93
Fold 2 = 0.96
Fold 3 = 0.90
Fold 4 = 0.96
Fold 5 = 0.93

Average ≈ 0.936
```

---

# 🎓Task 7 :  Mini Project — Student Segmentation

## Objective

Use unsupervised learning to group students according to their study habits and academic behavior.

## Features

The dataset contains features such as:

| Feature       | Description                 |
| ------------- | --------------------------- |
| `study_hours` | Average study hours per day |
| `sleep_hours` | Average sleep hours         |
| `attendance`  | Attendance percentage       |
| `quiz_score`  | Average quiz score          |

---

## Machine Learning Workflow

```text
Student Dataset
       ↓
Data Exploration
       ↓
Data Cleaning
       ↓
Feature Scaling
       ↓
Elbow Method
       ↓
Select K
       ↓
K-Means Clustering
       ↓
Cluster Profiling
       ↓
PCA Visualization
       ↓
Interpretation
```

---

# 🔍 Feature Scaling

Before applying K-Means, the features are standardized using `StandardScaler`.

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)
```

Scaling is important because K-Means uses distance calculations.

For example:

```text
Study Hours → 1–10
Attendance → 50–100
Quiz Score → 40–100
```

Without scaling, features with larger numerical ranges can have a disproportionate influence on the distance calculation.

---

# 📊 Cluster Profiling

After clustering:

```python
df["cluster"] = kmeans.fit_predict(X_scaled)
```

the clusters are analyzed using:

```python
cluster_profile = df.groupby("cluster").mean()

print(cluster_profile)
```

Possible interpretations:

```text
Cluster 0 → Low-engagement students
Cluster 1 → Average/consistent students
Cluster 2 → Highly engaged students
```

These descriptions should be based on the actual cluster statistics rather than assigned arbitrarily.

---

# 📈 PCA Visualization

PCA is used to reduce the multidimensional dataset to two dimensions for visualization.

```python
from sklearn.decomposition import PCA

pca = PCA(n_components=2)

X_pca = pca.fit_transform(X_scaled)
```

This allows the clusters to be visualized in a 2D scatter plot.

---

# 🛠️ Technologies Used

* Python
* NumPy
* Pandas
* Matplotlib
* Seaborn
* Scikit-learn
* Jupyter Notebook / VS Code

Note :
```

Task 7 : Mini Practice Project 2 , Model Tuning, Cross-Validation & Testing Model
Task 7 : Mini Practice Project 3 , Grid Search CV & Rendomized Search CV
Task 7 : Mini Practice Project 4 , Ensembel Learning, Stacking,  Bagging,Boosting
Task 7 : Mini Practice Project 5, Unsupervised ML Algorithms

```

# 🎯 Learning Outcomes

After completing Week 5, I should be able to:

* Implement KNN from scratch.
* Explain how distance-based classification works.
* Train and visualize Decision Trees.
* Identify Decision Tree overfitting.
* Train Random Forest models.
* Compare Random Forest with a single Decision Tree.
* Interpret feature importance.
* Implement K-Means from scratch.
* Understand centroids and cluster assignment.
* Use the Elbow Method to select K.
* Apply DBSCAN clustering.
* Identify DBSCAN noise points.
* Compare K-Means and DBSCAN.
* Perform K-Fold Cross-Validation.
* Interpret mean and standard deviation of validation scores.
* Perform feature scaling before distance-based algorithms.
* Build and interpret a complete clustering project.

---
 
**Syed Mehdi Shah**

BS Computer Science Student
Interested in **Data Science, Machine Learning, Deep Learning & Artificial Intelligence**

---

⭐ This repository documents is my Internship  **Week 5 Machine Learning** practice and progress.
 