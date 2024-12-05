import numpy as np
import pandas as pd
import time

def generate_sensor_data():
    heart_rate = np.random.randint(60, 100)
    blood_pressure = np.random.randint(110, 140)
    spO2 = np.random.uniform(95, 100)
    temperature = np.random.uniform(36.5, 37.5)
    return {"heart_rate": heart_rate, "blood_pressure": blood_pressure, "spO2": spO2, "temperature": temperature}

while True:
    data = generate_sensor_data()
    df = pd.DataFrame([data])
    df.to_csv("sensor_data.csv", mode='a', header=False, index=False)
    print(f"Data: {data}")
    time.sleep(5)
