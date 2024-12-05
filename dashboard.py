import streamlit as st
import pandas as pd
import numpy as np

# Title of the Dashboard
st.title("Health Monitoring Dashboard")

# Subheader for Data Input
st.subheader("Enter Your Health Data")

# Sliders for Input Data
heart_rate = st.slider('Heart Rate (bpm)', min_value=60, max_value=180, value=75)
blood_pressure = st.slider('Blood Pressure (mmHg)', min_value=80, max_value=180, value=120)
spo2 = st.slider('SpO2 (%)', min_value=90, max_value=100, value=98)
temperature = st.slider('Temperature (°C)', min_value=35.0, max_value=40.0, value=37.0)

# Display Input Data
st.write(f"Heart Rate: {heart_rate} bpm")
st.write(f"Blood Pressure: {blood_pressure} mmHg")
st.write(f"SpO2: {spo2} %")
st.write(f"Temperature: {temperature} °C")

# Health Warnings and Messages
if heart_rate > 100:
    st.error("Warning: High heart rate!")
else:
    st.success("Heart rate is normal.")

if blood_pressure > 140:
    st.warning("Warning: High blood pressure!")
else:
    st.success("Blood pressure is normal.")

if spo2 < 95:
    st.warning("Warning: Low oxygen saturation!")
else:
    st.success("Oxygen saturation is normal.")

if temperature > 37.5:
    st.warning("Warning: High body temperature!")
else:
    st.success("Body temperature is normal.")

# Function to Generate Graphs
def generate_graphs():
    # Generate Sample Data
    data = pd.DataFrame({
        'Time': pd.date_range('2024-12-01', periods=24, freq='H'),
        'Heart Rate': np.random.randint(60, 100, 24),
        'Blood Pressure': np.random.randint(110, 130, 24),
        'SpO2': np.random.randint(95, 100, 24),
        'Temperature': np.random.uniform(36.0, 37.5, 24)
    })

    # Heart Rate Chart
    st.subheader("Heart Rate over Time")
    st.line_chart(data.set_index('Time')['Heart Rate'])

    # Blood Pressure Chart
    st.subheader("Blood Pressure over Time")
    st.line_chart(data.set_index('Time')['Blood Pressure'])

    # SpO2 Chart
    st.subheader("SpO2 over Time")
    st.line_chart(data.set_index('Time')['SpO2'])

    # Temperature Chart
    st.subheader("Temperature over Time")
    st.line_chart(data.set_index('Time')['Temperature'])

# Generate Graphs
generate_graphs()
