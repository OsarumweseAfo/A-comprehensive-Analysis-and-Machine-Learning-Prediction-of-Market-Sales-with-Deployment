# Project Overview

Title: 
A comprehensive Analysis and Machine Learning Analysis Prediction of Market Sales with Deployment.

Objective:
In the world of business today, accurate forcasting of sales is very important to fully maximising prining strategies, inventory and the overall performance of a business. This project aims to analyze market sales trend and develop machine learning predictive model that can estimate future sales based on unit pricing, quantity, cutomer type and product line.

---

## Scope
Data Collection and Preprocessing:

* Handling missing values, removing duplicates, ensure correct data types,creating our target variable and encoding categorical variables.
  
* Visaulize trends and relationship among variables to have a clear picture of the data set and understand factors influencing market sales
  
* Build and compare multiple regression models(e.g Linear Regression, Ridge Regression, Elastic net, Decesion Tree Regressor, Gradient Boosting Regressor and Random Tree Regressor) to predict market sales.
  
* Create an interactive web application using streamlit to deploy the best performing model, allowing users to input features values and obtain market  sales predictions.

---

## Data Description
The Dataset used in this project provides a comprehensive overview of supermarket transactions, tracking details such as product categories, unit prices, quantities sold, and gross income. It also includes customer demographics, such as  gender and membership type.

## Key Variables and their Description

* Customer Type: Indicates if the customer is a "Member" or "Normal.". This variable Specifies whether the customer is a "Member" or "Normal", highlighting the distinction between different customer categories.
  
* Unit Price: The cost of a single unit of the product.
  
* Quantity: The number of units purchased in a single transaction.
  
* Tax (5%): The tax amount, calculated as 5% of the pre-tax total.
  
* City: Represents the location of the branch where the transaction took place.
  
* Product Line: Categorizes the product based on its type, such as Fashion accessories, Food and beverages, Electronic accessories, Sports and travel, Home and lifestlye and  Health and Beauty.
  
* Gender: Categorizes customer's gender.
  
* Total Sales: The final amount generated from a transaction; unit price multiplied by quantity plus 5% tax. This represents the total revenue from a single purchase.

  ---
  # Methodology
  1. Data Cleaning and Imputation: This project begins by checking for duplicates, missing values and removing estra spaces from the headers
     
  2. Exploratory Data Analysis(EDA): Various plots like Histogram,Box plot, Bar Plot,Pie chart, Line Chart and Heatmap are used to understand the distribution of market sales and relationship among various predictable variables.
   
  3. Feature Engineering:
     * Creating new variables (Total Sales) to improve model performance.
     * Encoded all categorical variables such as Gender, City, Customer Type and Product using one-hot encoding to prepare the data for regression.
       
  4. Model Redeployment: Several  machine learning models including Random Tree Regressor( Our Primary Model) are  explored and trained too predict market sales.

  5. Hyperparameter Tuning: Ussed techniques like GridSearchCV to optimize model parameters.
     
  6. Deployment: The final model is deployed using Streamlit, enabling end users to input various sales indicators and obtain real-time market sales predictions.
