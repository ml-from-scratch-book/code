# Machine Learning From Scratch
![License](https://img.shields.io/badge/License-MIT-green?style=flat)

Companion code repository for [Machine Learning From Scratch](https://a.co/d/01WG6GFE).
<br>

<a href="https://a.co/d/01WG6GFE"><img height="480" alt="f" src="https://github.com/user-attachments/assets/f57946ec-b227-4fbd-86af-f0503b0f6f9d" />

<br>

[Machine Learning From Scratch](https://a.co/d/01WG6GFE) opens the "black box" behind `fit()` and `predict()`. Anyone with basic Python and high-school math can fully understand and build core ML algorithms from scratch via a 5-stage framework:

1. **Intuition**: Understand the plain-English human thinking behind the algorithm.
2. **Formalization**: Translate that intuition into accessible mathematical form.
3. **Implementation**: Put the math into clean, from-scratch code using NumPy.
4. **Test**: Validate your code on real data and compare it against industry-standard libraries.
5. **Tips**: Learn practical strengths, weaknesses, and real-world usage insights.

⭐️ If you find this repository and the book helpful, please consider giving this repo a star — thank you!

---

## Table of Contents
 
| Chapter | Content/Code |
|---------|------|
| Setup | [Overview](#setup) |
| Fundamentals of ML | [Overview](#fundamentals-of-ml) |
| Introduction to Data | [Overview](#introduction-to-data) |
| The Math You Actually Need for ML | [Overview](#the-math-you-actually-need-for-ml) |
| Data Preparation | [Overview](#data-preparation) <br/> [data_loader.py](data_loader.py) |
| Linear Regression | [01_linear_regression.ipynb](01_linear_regression.ipynb) |
| Logistic Regression | [02_logistic_regression.ipynb](02_logistic_regression.ipynb) |
| Regularization | [03_regularization.ipynb](03_regularization.ipynb) |
| K-Nearest Neighbors | [04_k_nearest_neighbors.ipynb](04_k_nearest_neighbors.ipynb) |
| Naïve Bayes | [05_naive_bayes.ipynb](05_naive_bayes.ipynb) |
| Decision Tree | [06_decision_tree.ipynb](06_decision_tree.ipynb) |
| Random Forest | [07_random_forest.ipynb](07_random_forest.ipynb) |
| Gradient Boosting | [08_gradient_boosting.ipynb](08_gradient_boosting.ipynb) |
| Extreme Gradient Boosting (XGBoost) | [09_xgboost.ipynb](09_xgboost.ipynb) |
| Neural Network | [10_neural_network.ipynb](10_neural_network.ipynb) |
| Making the Best out of Models | [Overview](#making-the-best-out-of-models) <br/> [11_model_optimization.ipynb](11_model_optimization.ipynb) |
| Conclusion | [Overview](#conclusion) |
 
---
## Chapter Overviews
 
### Setup
 
To run the code locally, clone the repo and install the dependencies:
 
```bash
git clone https://github.com/ml-from-scratch-book/code.git
cd code
pip install -r requirements.txt
```
Alternatively, every notebook can be opened directly in Google Colab with no local setup — go to [colab.research.google.com](https://colab.research.google.com) and import from GitHub.
 
---
 
### Fundamentals of ML
 
Introduces the core ideas and definitions behind machine learning — what an algorithm is, what a model is, and what role data plays in all of it. Uses relatable analogies to build a clear mental picture of what ML practitioners aim to accomplish and how they go about it.
 
---
 
### Introduction to Data
 
Explores what data actually looks like in practice: features, targets, data types, and common issues like missing values and class imbalance. Goes beyond toy datasets to explore when ML is actually the right tool over a rule-based approach.

---
 
### The Math You Actually Need for ML
 
An efficient dive into three mathematical pillars underlying most ML algorithms:
 
- **Manipulating Data (Linear Algebra Essentials)**: Vectors, matrices as ways to store data, matrix multiplication and other common operations as ways to manipulate it.
- **Understanding Data (Statistical Foundations)**: Distributions, mean/variance, probability, significance of sample size explained via practical examples.
- **Learning from Data (Optimization)**: Starting from the concept of a function and distance between two points to limits, objective functions, gradient descent, and how models actually "learn" by minimizing error.

---
 
### Data Preparation
 
Covers the practical work that happens before training: handling missing data, encoding categorical variables, feature scaling, train/test splitting, and avoiding data leakage. At this stage we prepare a script that loads, preprocesses and splits the data to be leveraged with algorithms. 

---

### Algorithms 🫀

The heart of the book — 10 core ML algorithms each built from scratch using the 5-stage framework:

Linear Regression · Logistic Regression · Regularization · K-Nearest Neighbors · Naïve Bayes · Decision Tree · Random Forest · Gradient Boosting · XGBoost · Neural Network
 
---

### Making the Best out of Models

Here, the reader learns how to approach a problem and if applicable, solve it with ML. In other words, how to put all the knowledge gained in this book into an iterative framework of ML project development comprised of 3 stages: 

- **Data**: Reinforces the idea of the importance of a clear problem statement, data quality, feature engineering and preventing data leakage.
- **Modeling**: Validation set, k-fold cross-validation, model selection and hyperparameter tuning with Optuna via Grid, Random and Bayesian search.
- **Evaluation**: Metrics for regression, binary and multiclass classification problems covered in detail with examples of why they matter.
---
 
### Conclusion

The reader takes a step back to look at the bigger picture of who they've become after this book and of different directions they can go from here. Most importantly they finish with the understanding that the mindset and practical skills they gained here goes a long way regardless of the exact path they follow.
