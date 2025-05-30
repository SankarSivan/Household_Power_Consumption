import streamlit as st
import pandas as pd
import joblib
import os
import glob
import pickle

# Page configuration
st.set_page_config(page_title="Power Consumption Predictor", page_icon="⚡", layout="centered")

# Title
st.title("⚡ Household Energy Usage Prediction App")
st.markdown("Enter the input parameters to predict **Global Active Power (kW)**.")

# Load model
model_path = "Ops_rf_model.pkl"

if not os.path.exists(model_path):
    st.error("Model file not found! Please ensure 'Ops_rf_model.pkl' is in the same folder as this script.")
    st.stop()

model = joblib.load(model_path)

# Show expected features for debugging
st.write("Model expects features:", model.feature_names_in_)

# --- Sidebar Inputs ---
st.sidebar.header("🧮 Input Features")

hour = st.sidebar.slider("Hour of Day", 0, 23, 12)
weekday = st.sidebar.selectbox(
    "Weekday",
    options=[0, 1, 2, 3, 4, 5, 6],
    format_func=lambda x: ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"][x]
)
voltage = st.sidebar.slider("Voltage (V)", 220.0, 250.0, 235.0)
global_intensity = st.sidebar.slider("Global Intensity (A)", 0.0, 50.0, 10.0)
total_sub_metering = st.sidebar.slider("Total Sub Metering", 0.0, 80.0, 10.0)  # Adjust max as needed

# --- Create DataFrame ---
input_data = pd.DataFrame({
    "hour": [hour],
    "weekday": [weekday],
    "Voltage": [voltage],
    "Global_intensity": [global_intensity],
    "Total_sub_metering": [total_sub_metering]
})

# --- Prediction ---
if st.button("🔍 Predict Global Active Power"):
    prediction = model.predict(input_data)[0]
    st.success(f"✅ Predicted Global Active Power: **{prediction:.3f} kW**")

# --- Footer ---
st.markdown("---")
st.markdown(
    "<small>Developed by Sankar | Powered by Streamlit & Scikit-learn</small>", 
    unsafe_allow_html=True
)

# --- End of the app ---