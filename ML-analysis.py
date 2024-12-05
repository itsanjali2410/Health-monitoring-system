from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def train_model(data):
    data["is_abnormal"] = data["heart_rate"].apply(lambda x: 1 if x < 60 or x > 100 else 0)
    X = data[["heart_rate", "blood_pressure", "spO2", "temperature"]]
    y = data["is_abnormal"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    print(f"Accuracy: {accuracy_score(y_test, predictions):.2f}")
    return model

data = load_data()
cleaned_data = preprocess_data(data)
model = train_model(cleaned_data)
