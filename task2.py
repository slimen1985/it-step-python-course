import sqlite3

conn = sqlite3.connect("materials.db")
cursor = conn.cursor()


def avg_weight():
    cursor.execute("SELECT AVG(weight) FROM materials")
    avg = cursor.fetchone()[0]
    return avg


print(avg_weight())
conn.close()
