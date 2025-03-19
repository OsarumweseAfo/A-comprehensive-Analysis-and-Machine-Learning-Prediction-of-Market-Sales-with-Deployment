import streamlit as st
import pickle
import numpy as np

# Load the saved Random Forest model
with open('rf_model.pkl', 'rb') as f:
    rf_model = pickle.load(f)

# Title
st.title('Market Sales Prediction App')
st.write('Provide the required inputs to Predict Market Sales')

# User Inputs
unit_price = st.number_input("Unit Price", min_value=10.08, value=99.96)
quantity = st.number_input("Quantity", min_value=1.0, value=10.0)

customer_type = st.selectbox("Customer Type", ["Member", "Normal"])
customer_type_val = 1 if customer_type == "Member" else 0

product_line = st.selectbox(
    "Product Line",
    ["Electronic accessories", "Fashion accessories", "Food and beverages", 
     "Health and beauty", "Home and lifestyle", "Sports and travel"]
)
product_line_val = {
    "Electronic accessories": 1,
    "Fashion accessories": 2,
    "Food and beverages": 3,
    "Health and beauty": 4,
    "Home and lifestyle": 5,
    "Sports and travel": 6
}[product_line]

# Prepare input features
input_features = np.array([[unit_price, quantity,customer_type_val, product_line_val]])

# Make Prediction
if st.button("Predict Market Sales"):
    prediction = rf_model.predict(input_features)
    st.write(f"Predicted Market Sales: ${prediction[0]:,.2f}")