# Heart Disease Prediction Project

## Overview

This project aims to predict whether a person has heart disease or not using Logistic Regression. It is built using Pandas, NumPy, Scikit-Learn, and Streamlit. The application allows users to input relevant health parameters, and it provides a prediction based on the trained model.

## Technologies Used

- [Pandas](https://pandas.pydata.org/): For data manipulation and analysis.
- [NumPy](https://numpy.org/): For numerical operations.
- [Scikit-Learn](https://scikit-learn.org/): For machine learning modeling.
- [Streamlit](https://streamlit.io/): For creating an interactive web application.

## Dataset

The model is trained on the [Heart Disease Dataset on Kaggle](https://www.kaggle.com/datasets/johnsmith88/heart-disease-dataset), which contains various health parameters and binary labels indicating the presence or absence of heart disease.

## Model

The prediction model is based on Logistic Regression, a commonly used algorithm for binary classification problems.

## Deployment

The application is deployed using Streamlit, providing an easy-to-use and accessible interface for users.

## Usage

1. Make sure you have the required libraries installed:

    ```bash
    pip install pandas numpy scikit-learn streamlit
    ```

2. Run the application:

    ```bash
    streamlit run streamlit_app.py
    ```

3. Open your web browser and go to the provided URL to use the Heart Disease Prediction system.

## Example

User inputs health parameters:

- Age: 45
- Gender: Male
- Blood Pressure: 130
- Cholesterol Level: 240
- ... (Other relevant features)

The system predicts whether the user is at risk of heart disease or not.
| HomePage | Result |
| --------------------------------------- | --------------------------------------- |
| ![Heart Disease Prediction](https://github.com/aryangusain/heart-disease-prediction/assets/97178343/18819daf-f287-44f3-94b8-0fcc6e9de804) | ![Heart Disease Prediction](https://github.com/aryangusain/heart-disease-prediction/assets/97178343/876e7bb6-82ff-4877-8351-757d9f4f86b8) |

**Explore the live application [here](https://heart-disease-prediction-cywbntmtb2m78qrsz4x27y.streamlit.app/).**

Feel free to use the application and gain insights into potential heart disease risks.
