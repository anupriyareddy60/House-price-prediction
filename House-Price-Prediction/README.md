# 🏠 House Price Prediction using Machine Learning

## 📌 Overview

This project is an end-to-end Machine Learning application that predicts house prices using the Ames Housing dataset. The project covers the complete machine learning workflow, including data preprocessing, exploratory data analysis, model training, hyperparameter tuning, and deployment using Streamlit.

The trained model allows users to enter house details through a web interface and receive an estimated house price instantly.

---

## 🚀 Features

- Data Cleaning and Preprocessing
- Exploratory Data Analysis (EDA)
- Feature Selection
- Multiple Regression Models
- Hyperparameter Tuning using GridSearchCV
- Streamlit Web Application
- Real-time House Price Prediction

---

## 📂 Dataset

**Dataset:** Ames Housing Dataset

The dataset contains residential house information such as:

- Overall Quality
- Living Area
- Garage Capacity
- Garage Area
- Basement Area
- Year Built
- Number of Bathrooms
- Number of Rooms
- Overall Condition
- Sale Price (Target)

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Joblib
- Streamlit
- Jupyter Notebook

---

## 🤖 Machine Learning Models

The following models were implemented and compared:

- Linear Regression
- Ridge Regression ✅
- Lasso Regression
- Elastic Net Regression

Hyperparameter tuning was performed using **GridSearchCV**.

---

## 🏆 Best Model

**Ridge Regression**

The Ridge Regression model produced the best overall performance for this project.

---

## 📊 Features Used in Deployment

The deployed application predicts house prices using the following features:

- Overall Quality
- Ground Living Area
- Garage Cars
- Garage Area
- Total Basement Area
- Year Built
- Full Bathrooms
- Total Rooms Above Ground
- First Floor Area
- Overall Condition

---

## 📁 Project Structure

```
House-Price-Prediction/
│
├── app.py
├── README.md
├── requirements.txt
├── house_price_prediction.ipynb
│
├── dataset/
│   ├── AmesHousing.csv
│   ├── cleaned_ames_housing.csv
│   └── processed_features.csv
│
└── models/
    ├── house_price_model_10features.pkl
    ├── ridge_model.pkl
    ├── lasso_model.pkl
    ├── elastic_model.pkl
    └── linear_model.pkl
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/your-username/House-Price-Prediction.git
```

Go to the project folder:

```bash
cd House-Price-Prediction
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

## 📈 Results

- Successfully trained multiple regression models.
- Compared model performance.
- Selected Ridge Regression as the best model.
- Built a working Streamlit application for real-time predictions.

---

## 🔮 Future Improvements

- Add Neighborhood (Location) as a feature.
- Improve the Streamlit user interface.
- Deploy the application online using Streamlit Community Cloud.
- Add charts and prediction confidence intervals.

If you found this project helpful, please consider giving it a ⭐ on GitHub.
