import streamlit as st
import pandas as pd
import numpy as np
import joblib

cond_model = joblib.load('Src/cond_model.pkl')
temp_model = joblib.load('Src/temp_model.pkl')
le_model = joblib.load('Src/label_encoder.pkl')

st.title("🌦️ Weather Prediction App")
st.header("Predict Weather!!")
st.write("We,ve made a weather predicting app which using Deep Learning/*")
st.sidebar.header("Write the inputs")


temp = st.sidebar.slider('Enter Today,s Temperature(C)',15.0, 40.0, 25.0)
tempmin = st.sidebar.slider('Enter Today,s Minimum Temperature(C)',10.0, 30.0, 17.0)
tempmax = st.sidebar.slider('Enter Today,s Maximum Temperature(C)',17.0, 40.0, 30.0)
feelslike = st.sidebar.slider('Enter The Feellike Temperature(C)',25.0, 45.0, 32.0)
feelslikemin = st.sidebar.slider('Enter The Feellike Min Temperature(C)',25.0, 45.0, 32.0)
feelslikemax = st.sidebar.slider('Enter The Feellike Max Temperature(C)',18.0, 55.0, 34.0)
dew = st.sidebar.slider('Enter The Dew',8.0, 28.0, 20.0)
precipprob = st.number_input('Enter Precipitation Probability(0-100)',0, 100, 66)
precipcover = st.sidebar.slider('Enter Precipitation Coverage',0, 100.0, 17)
cloudcover = st.sidebar.slider('Enter The CloudCover',0.0, 100.0,56.0)
humidity = st.sidebar.slider('Enter The Humidity',51.0, 98.0,82.0)
conditions = st.selectbox( 'Select The Weather Condition of Today', options=["Rain, Overcast", "Rain, Partially cloudy", "Partially cloudy","Clear"])

predict = st.button(label = "Predict tommorrows Weather")

if predict: 
    data = {
            'temp': temp,
            'tempmin' : tempmin,
            'tempmax': tempmax,
            'feelslike': feelslike,
            'feelslikemin': feelslikemin,
            'feelslikemax': feelslikemax,
            'dew' : dew,
            'precipprob':  precipprob,
            'precipcover': precipcover,
            'cloudcover': cloudcover,
            'humidity': humidity,
            'conditions': conditions
    }

    features =  pd.DataFrame(data, index=[0])
    return features

df = user_input_features
predictions = temp_model.predict(df)

df['Prediction'] = predictions
st.subheader("Predictions")
st.write(data)


# st.subheader

# uploaded_file = st.file_uploader("Upload a CSV file", type=['csv'])


# if uploaded_file:
#     df = pd.read_csv(uploaded_file)
#     st.write("Data Preview:", df.head())

#     df_cleaned, _ = clean_weather_data(df, label_encoders, fit_encoders=False)

#     features = df_cleaned[['temp', 'feelslike', 'dew','feelslikemax','feelslikemin', 'tempmin', 'tempmax','precipprob','cloudcover','precipcover', 'humidity','conditions']]  
#     p_feature = le_model(feature)          
#     predictions = temp_model.predict(p_features)

#     try:
#         predictions = label_encoder.inverse_transform(predictions)

#     df['Prediction'] = predictions
#     st.subheader("Predictions")
#     st.write(data)
