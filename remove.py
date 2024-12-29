import mysql.connector

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

if __name__ == "__main__":
    conn = polacz_z_baza()
    cursor = conn.cursor()
    cursor.execute('SELECT MAX(id) FROM obrazy')
    wynik = cursor.fetchone()
    ostatnie_id = wynik[0]
    cursor.execute('DELETE FROM obrazy WHERE id = %s', (ostatnie_id,))
    conn.commit()
    cursor.close()
    print("removed")