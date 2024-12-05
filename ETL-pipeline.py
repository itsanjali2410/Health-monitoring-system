import pandas as pd

def load_data(file_path="sensor_data.csv"):
    columns = ["heart_rate", "blood_pressure", "spO2", "temperature"]
    data = pd.read_csv(file_path, names=columns)
    return data

def preprocess_data(data):
    data = data.dropna()
    return data

if __name__ == "__main__":
    data = load_data()
    cleaned_data = preprocess_data(data)
    print(cleaned_data.head())
