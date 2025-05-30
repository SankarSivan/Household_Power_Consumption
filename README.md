# Household Power Consumption Prediction

## Overview

This project focuses on predicting household power consumption using a dataset from the UCI Machine Learning Repository. The dataset contains measurements of electric power consumption in one household with a one-minute sampling rate over a period of almost 4 years.

The primary goal is to develop a predictive model for **Global Active Power (kW)** based on various input features.

## Table of Contents

- [Data Source](#data-source)
- [ETL Process](#etl-process)
- [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
- [Feature Engineering](#feature-engineering)
- [Modeling](#modeling)
- [Model Evaluation](#model-evaluation)
- [Streamlit Application](#streamlit-application)
- [Repository Structure](#repository-structure)
- [Dependencies](#dependencies)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Data Source

The dataset is sourced from the UCI Machine Learning Repository:

- [Individual household electric power consumption Dataset](https://archive.ics.uci.edu/dataset/235/individual+household+electric+power+consumption)

The dataset is fetched using the `ucimlrepo` library, as demonstrated in [Power_Consumption_ETL.ipynb](Power_Consumption_ETL.ipynb).

## Variables Table

| Variable Name          | Role     | Type         | Description                                     | Units | Missing Values |
|--------------------------|----------|--------------|-------------------------------------------------|-------|----------------|
| Date                     | Feature  | Date         | Date                                            |       | no             |
| Time                     | Feature  | Categorical  | Time                                            |       | no             |
| Global_active_power      | Feature  | Continuous   | Global active power                             |       | no             |
| Global_reactive_power    | Feature  | Continuous   | Global reactive power                           |       | no             |
| Voltage                  | Feature  | Continuous   | Voltage                                         |       | no             |
| Global_intensity         | Feature  | Continuous   | Global intensity                                |       | no             |
| Sub_metering_1           | Feature  | Continuous   | Sub-metering 1                                  |       | no             |
| Sub_metering_2           | Feature  | Continuous   | Sub-metering 2                                  |       | no             |
| Sub_metering_3           | Feature  | Continuous   | Sub-metering 3                                  |       | no             |

## Dataset Files
household_power_consumption.txt	                           126.8 MB

## ETL Process

The ETL (Extract, Transform, Load) process involves:

- **Extract:** Fetching the dataset from the UCI repository.
- **Transform:**
    - Converting data types (e.g., object to float).
    - Handling missing values (replacing '?' with NaN and dropping NaN values).
    - Converting 'Date' and 'Time' columns to appropriate datetime formats.
- **Load:** Combining features and targets into a single DataFrame.

Key steps are implemented in [Power_Consumption_ETL.ipynb](Power_Consumption_ETL.ipynb).

## Exploratory Data Analysis (EDA)

EDA is performed to understand the data distribution, identify patterns, and gain insights. Key steps include:

- Descriptive statistics (`df.describe()`).
- Checking for missing values (`df.isnull().sum()`).
- Plotting distributions of numeric columns using histograms (`sns.histplot`).
- Analyzing skewness of features and applying log transformations to reduce skewness.
- Visualizing correlations using heatmaps (`sns.heatmap`).
- Analyzing power consumption trends over time using line plots (`sns.lineplot`).

EDA is detailed in [Power_Consumption_ETL.ipynb](Power_Consumption_ETL.ipynb).

## Feature Engineering

Feature engineering involves creating new features from existing ones to improve model performance. Key steps include:

- Creating `DateTime` column by combining 'Date' and 'Time'.
- Extracting temporal features such as `hour`, `day`, `weekday`, `month`, and `year` from the `DateTime` column.
- Creating a `Total_sub_metering` feature by summing `Sub_metering_1`, `Sub_metering_2`, and `Sub_metering_3` ([Power_Consumption_ETL.ipynb](Power_Consumption_ETL.ipynb)).
- Generating rolling average features (`rolling_1h`, `rolling_3h`) to capture short-term trends.
- Calculating daily average power usage (`daily_avg_power`).

## Modeling

Several machine learning models are trained and evaluated to predict global active power:

- Linear Regression
- Random Forest Regressor
- Gradient Boosting Regressor

The models are trained using a subset of features, including "hour", "weekday", "Voltage", "Total_sub_metering", and "daily_avg_power".  The data is split into training and testing sets using `train_test_split` from `sklearn.model_selection`.

Model training and evaluation are performed in [Power_Consumption_ETL.ipynb](Power_Consumption_ETL.ipynb).

## Model Evaluation

Models are evaluated using the following metrics:

- Root Mean Squared Error (RMSE)
- Mean Absolute Error (MAE)
- R-squared (R^2)

The `evaluate_model` function in [Power_Consumption_ETL.ipynb](Power_Consumption_ETL.ipynb) calculates these metrics. Based on the evaluation, the Random Forest Regressor performs the best.

## Streamlit Application

A Streamlit application ([HouseEnergy_app.py](HouseEnergy_app.py)) is developed to provide a user interface for predicting power consumption. The application allows users to input features such as hour of day, weekday, and voltage, and receive a prediction of global active power.  The application loads a pre-trained model (`best_energy_model_00.pkl`) for making predictions.

