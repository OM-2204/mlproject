# Student Performance Predictor

> A machine learning project to analyze and predict student academic performance based on demographic and socioeconomic factors.

![Python](https://img.shields.io/badge/Python-3.8-blue) ![ML](https://img.shields.io/badge/Machine%20Learning-Scikit--learn-orange) ![Status](https://img.shields.io/badge/Status-Active-green)

---

## 🎯 Problem Statement

Educational institutions often lack robust data-driven mechanisms to identify and analyze the factors influencing student academic performance. 

The objective of this project is to develop a predictive machine learning model that estimates student performance based on demographic and socioeconomic attributes. By leveraging these insights, the system aims to support early identification of at-risk students and enable informed, data-driven interventions to improve academic outcomes.

---

## Overview

This project explores how demographic and socioeconomic factors such as gender, ethnicity, parental education, lunch type, and test preparation influence a student's academic performance in Math, Reading, and Writing.

The dataset contains **1,000 student records** across **8 features** and serves as the foundation for both exploratory data analysis (EDA) and predictive modeling.

---

## Dataset Description

| Column | Description | Values |
|--------|-------------|--------|
| `gender` | Sex of the student | Male / Female |
| `race/ethnicity` | Ethnicity group of the student | Group A, B, C, D, E |
| `parental level of education` | Highest education level attained by parents | High School, Some College, Associate's Degree, Bachelor's Degree, Master's Degree |
| `lunch` | Type of lunch before the test | Standard / Free or Reduced |
| `test preparation course` | Whether the student completed the prep course | Completed / None |
| `math score` | Score in the mathematics test | 0 – 100 |
| `reading score` | Score in the reading test | 0 – 100 |
| `writing score` | Score in the writing test | 0 – 100 |

---

## Project Workflow

1. **Data Loading** — Import and inspect the raw dataset
2. **Exploratory Data Analysis (EDA)** — Understand distributions, correlations, and outliers
3. **Data Preprocessing** — Encode categorical variables, handle missing values, scale features
4. **Model Building** — Train and evaluate machine learning models
5. **Insights & Conclusions** — Draw actionable insights from the results

---

## Tech Stack

- **Language:** Python 3.8
- **Libraries:** Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn, catboost, xgboost, flask ,dill
- **Environment:** Jupyter Notebook

---

## Model Results

Multiple regression models were trained and evaluated using the **R² Score** metric.

| Rank | Model | R² Score |
|------|-------|----------|
| 1 | Ridge Regression ⭐ | 0.8806 |
| 2 | Linear Regression | 0.8803 |
| 3 | CatBoosting Regressor | 0.8516 |
| 4 | AdaBoost Regressor | 0.8511 |
| 5 | Random Forest Regressor | 0.8504 |
| 6 | XGB Regressor | 0.8278 |
| 7 | Lasso | 0.8253 |
| 8 | K-Neighbors Regressor | 0.7838 |
| 9 | Decision Tree | 0.7433 |

> **Best Model: Ridge Regression** with an R² Score of **0.8806**, meaning the model explains ~88% of the variance in student scores.

---

## Key Insights

- Students who completed the test preparation course scored significantly higher.
- Lunch type (proxy for socioeconomic status) strongly impacts performance.
- Reading and writing scores are highly correlated.
- Parental education level positively influences student outcomes.

---

## Future Improvements

- Deploy using Docker & Kubernetes  
- Add real-time student performance tracking  
- Improve model with deep learning  
- Integrate database for large-scale data storage  

---

## How to Run
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
pip install -r requirements.txt
jupyter notebook
```


