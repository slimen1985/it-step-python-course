import sqlite3

conn = sqlite3.connect('materials.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS materials (
    id INTEGER PRIMARY KEY,
    weight TEXT,
    height TEXT,
    additional_features TEXT
)
""")

materials = [
    (1, "10 kg", "1.5 m", str([("wheels", 4), ("passengers", 5)])),
    (2, "20 kg", "2.0 m", str([("color", "red"), ("type", "Metal")])),
    (3, "5 kg", "0.5 m", str([("hardness", "hard"), ("density", "high")]))
]

cursor.executemany("""
INSERT INTO materials (id, weight, height, additional_features)
VALUES (?, ?, ?, ?)
""", materials)

conn.commit()
conn.close()
