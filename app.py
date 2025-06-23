import streamlit as st
import pandas as pd
import joblib

cond_model = joblib.load('Src/cond_model.pkl')
temp_model = joblib.load('Src/temp_model.pkl')

st.title("🌦️ Weather Prediction App")

uploaded_file = st.file_uploader("\Data\sylhet_weather.csv", type=['csv'])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("Data Preview:", df.head())

    features = df[['tempmax', 'tempmin', 'humidity', 'cloudcover',
              'temp', 'feelslike', 'dew', 'precip', 'precipprob', 'precipcover', 'preciptype', 'snow', 'snowdepth', 'windgust', 'windspeed',
              'winddir', 'sealevelpressure', 'visibility', 'solarradiation', 'solarenergy', 'uvindex',
              'moonphase', 'conditions','icon', 'categoryofweather']]  # example
    predictions = temp_model.predict(features)

    try:
        predictions = label_encoder.inverse_transform(predictions)
    except:
        pass

    df['Prediction'] = predictions
    st.subheader("Predictions")
    st.write(data)