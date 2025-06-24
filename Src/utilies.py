import pandas as pd
from sklearn.preprocessing import LabelEncoder

def clean_weather_data(df, label_encoders=None, fit_encoders=False):
    df = df.copy()

    df.fillna(method='ffill', inplace=True)

    obj_cols = df.select_dtypes(include='object').columns

    if fit_encoders:
        label_encoders = {}

    for col in obj_cols:
        if fit_encoders:
            le = LabelEncoder()
            df[col] = le.fit_transform(df[col].astype(str))
            label_encoders[col] = le
        else:
            if col in label_encoders:
                df[col] = label_encoders[col].transform(df[col].astype(str))
            else:
                df[col] = df[col].astype(str)  # Fallback

    return 
    