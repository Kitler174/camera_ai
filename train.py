import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np
import mysql.connector
import json
import joblib

def polacz_z_baza():
    conn = mysql.connector.connect(
        host="localhost",
        user="root", 
        password="Maba@@22", 
        database="dane_obrazu",
        charset="utf8mb4",
        collation="utf8mb4_general_ci"
    )
    return conn


conn = polacz_z_baza()
cursor = conn.cursor()
cursor.execute("SELECT * FROM obrazy ORDER BY etykieta")
fetchall = cursor.fetchall()
obrazy = []
etykiety = []

for i in fetchall:
    obrazy.append(np.array(json.loads(i[1])))
    etykiety.append(i[2])

obrazy = np.array(obrazy)
etykiety = np.array(etykiety)
X_train, X_test, y_train, y_test = train_test_split(obrazy, etykiety, test_size=0.2, random_state=42)
model = xgb.XGBClassifier(learning_rate=0.1)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f'Dokładność modelu: {accuracy * 100:.2f}%')
joblib.dump(model, 'model_xgboost.pkl')

