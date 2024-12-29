import cv2
import mysql.connector
import json

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

cap = cv2.VideoCapture(0)
if __name__ == "__main__":
    a = int(input("etykieta >>>"))
    while True:
        ret, frame = cap.read()
        cv2.imshow('NiggaCam', frame)
        if cv2.waitKey(1) & 0xFF == ord('a'):
            features = przetworz_obraz(frame)
            conn = polacz_z_baza()
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS obrazy (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    cechy TEXT,
                    etykieta INT
                )
            ''')
            cechy_json = json.dumps(features.tolist())
            sql = "INSERT INTO obrazy (cechy, etykieta) VALUES (%s, %s)"
            cursor.execute(sql, (cechy_json, a))
            conn.commit()
            cursor.close()
            print("done")
