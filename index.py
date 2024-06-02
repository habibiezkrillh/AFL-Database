import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password=''
)

c = conn.cursor()

c.execute('CREATE DATABASE IF NOT EXISTS mahasiswa_db')
c.execute('USE mahasiswa_db')

c.execute('''
CREATE TABLE IF NOT EXISTS mahasiswa (
    NIM VARCHAR(50) PRIMARY KEY,
    Nama VARCHAR(100),
    Nilai FLOAT,
    Grade VARCHAR(2)
)
''')

def determine_grade(nilai):
    if nilai >= 90:
        return 'A'
    elif nilai >= 85:
        return 'A-'
    elif nilai >= 80:
        return 'B+'
    elif nilai >= 75:
        return 'B'
    elif nilai >= 70:
        return 'B-'
    elif nilai >= 60:
        return 'C+'
    elif nilai >= 55:
        return 'C'
    elif nilai >= 45:
        return 'D'
    else:
        return 'E'

def before_insert_trigger(NIM, Nama, Nilai):
    grade = determine_grade(Nilai)
    print(f"NIM = {NIM}, Nama: {Nama}, Nilai: {Nilai}, Memperoleh Grade {grade}")
    return grade

mahasiswa = [
    ('0806022329001', 'Muh Habbibie Zikrillah', 85),
    ('0806022310006', 'A Alfian Tenggara Putra', 64),
    ('0806022310003', 'Calvin Richie Rumendong', 74.5),
    ('0806022310025', 'Javin Erasmus Clementino', 93.5),
    ('2023029', 'Excel', 15),
    ('0806022310099', 'John Morrison', 48)
]

for NIM, Nama, Nilai in mahasiswa:
    grade = before_insert_trigger(NIM, Nama, Nilai)
    c.execute('INSERT INTO mahasiswa (NIM, Nama, Nilai, Grade) VALUES (%s, %s, %s, %s)',
              (NIM, Nama, Nilai, grade))

conn.commit()
conn.close()
