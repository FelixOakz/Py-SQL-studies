import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='timemachine'
)
cursor = conn.cursor()

cursor.execute(
    'drop table '
)