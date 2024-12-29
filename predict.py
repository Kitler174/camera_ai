import cv2
import mysql.connector
import joblib
import os
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

def przetworz_obraz(frame):
    frame_resized = cv2.resize(frame, (64, 64))
    frame_gray = cv2.cvtColor(frame_resized, cv2.COLOR_BGR2GRAY)
    features = frame_gray.flatten()
    return features

if __name__ == "__main__":
    model = joblib.load('model_xgboost.pkl')
    cap = cv2.VideoCapture(0)
    act = 0
    while True:
        ret, frame = cap.read()
        pred = model.predict(przetworz_obraz(frame).reshape(1, -1))
        if pred[0] == 0:
            if act==0:
                act = 1
                os.system("cls")
                print("Brak dłoni")
        else:
            if act==1:
                act = 0
                os.system("cls")
                print("dłoń")