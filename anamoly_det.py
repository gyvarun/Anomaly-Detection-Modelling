import streamlit as st
import pickle
from datetime import datetime, time
import numpy as np

# Load the pre-trained model and scaler (if any)
with open(r'C:\Users\91916\GUVI_DS\classification_model_anamoly.pkl', 'rb') as g:
    model_2 = pickle.load(g)

def preprocess_inputs(Temperature, Location, date_input, time_input, date_seconds):
    # Extract year, month, day from date input
    date_year = date_input.year
    date_month = date_input.month
    date_day = date_input.day
    
    # Extract hour, minute, second from time input
    date_hour = time_input.hour
    date_minute = time_input.minute


    # Combine all inputs into a single array
    inputs = np.array([Temperature, Location, date_year, date_month, date_day, date_hour, date_minute, date_seconds]).reshape(1, -1)
    return inputs

# Configure Streamlit Interface
st.set_page_config(page_title='Anamoly Detection', 
                   layout="centered")

st.title(":red[INDUSTRIAL EQUIPMENT ANAMOLY PREDICTION]")

Location_values = ['SensorA', 'SensorB']
Location_dict = {'SensorA' : 1, 'SensorB' : 2}

# User inputs
Temperature = st.number_input(label = '**Temperature**', value=25.0)
Location = st.selectbox(label='**Location**', options=Location_values)
date_input = st.date_input(label = '**Date**', value=datetime.now())
time_input = st.time_input(label = '**Time(HHMM)**',  value=time(0,0), step = 60)
date_seconds = st.number_input(label = '**Seconds**', min_value=0, max_value=59, value=0)

# Preprocess inputs
inputs = preprocess_inputs(Temperature, Location_dict[Location], date_input, time_input, date_seconds)

# Predict button
if st.button(":red[**Predict**]"):
    try:
        # Make prediction
        prediction = model_2.predict(inputs)
        
        # Display prediction
        st.write(f"**Prediction: {prediction[0]}**")

        if prediction[0] == 1:
            st.write(':red[**Anamoly Detected**]')
        else:
            st.write(':green[**No Anamoly**]')

    except Exception as e:
        st.error(f"Error: {str(e)}")





