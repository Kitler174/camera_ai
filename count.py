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
    etykieta = int(input("etykieta>>>"))
    conn = polacz_z_baza()
    cursor = conn.cursor()
    sql = 'SELECT COUNT(*) FROM obrazy WHERE etykieta = %s'
    cursor.execute(sql, (etykieta,))
    wynik = cursor.fetchone()[0]
    cursor.close()
    print(wynik)
