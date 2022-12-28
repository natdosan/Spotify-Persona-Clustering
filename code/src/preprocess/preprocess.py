import pandas as pd
import numpy as np
import matplotlib
from sklearn.preprocessing import StandardScaler, MinMaxScaler

def load_dataset():
    charts = pd.read_csv('../../data/songs.csv')
    return charts

def return_tempo(tempo):
    if tempo < 60:
        return 0
    elif tempo < 90:
        return 1
    elif tempo < 110:
        return 2
    elif tempo < 120:
        return 3
    elif tempo < 160:
        return 4
    elif tempo < 180:
        return 5
    else:
        return 6

def clean_data(charts):
    charts = charts.assign(tempo_name = charts['tempo'].apply(return_tempo))
    charts = charts.assign(duration_min = charts['duration'] / 60000).drop(columns=['duration'])
    return charts

def get_features(charts):
    features_array = np.array(charts.columns)
    features = np.delete(features_array, [0, 1])
    return features

def feature_scale(charts):
    scaler = MinMaxScaler()
    scaler.fit(np.array(charts[['tempo', 'loudness', 'duration_min']]))
    charts[['tempo', 'loudness', 'duration_min']] = scaler.transform(np.array(charts[['tempo', 'loudness', 'duration_min']]))
    return charts

def main():
    charts = load_dataset()
    charts = clean_data(charts)
    print("\nFeatures: ", get_features(charts))
    charts = feature_scale(charts)
    return print(charts.head())

if __name__ == "__main__":
    main()