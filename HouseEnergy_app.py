
import streamlit as st
import pandas as pd
import joblib
import os

# Page configuration
st.set_page_config(page_title="Power Consumption Predictor", page_icon="⚡", layout="centered")

# Title
st.title("⚡ Household Energy Usage Prediction App")
st.markdown("Enter the input parameters to predict **Global Active Power (kW)**.")

# Load model
model_path = "best_energy_model.pkl"

if not os.path.exists(model_path):
    st.error("Model file not found! Please ensure 'best_energy_model.pkl' is in the same folder as this script.")
    st.stop()

model = joblib.load(model_path)

# --- Sidebar Inputs ---
st.sidebar.header("🧮 Input Features")

hour = st.sidebar.slider("Hour of Day", 0, 23, 12)
weekday = st.sidebar.selectbox("Weekday", 
                               options=[0, 1, 2, 3, 4, 5, 6],
                               format_func=lambda x: ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"][x])
voltage = st.sidebar.slider("Voltage (V)", 220.0, 250.0, 235.0)
total_sub_metering = st.sidebar.slider("Total Sub Metering", 0.0, 100.0, 20.0)
daily_avg_power = st.sidebar.slider("Daily Avg Power (kW)", 0.0, 10.0, 2.0)

# --- Create DataFrame ---
input_data = pd.DataFrame({
    "hour": [hour],
    "weekday": [weekday],
    "Voltage": [voltage],
    "Total_sub_metering": [total_sub_metering],
    "daily_avg_power": [daily_avg_power]
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
