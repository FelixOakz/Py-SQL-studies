import mysql.connector

myDB = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'timemachine',
    database = 'pythonx')

myCur = myDB.cursor()

cur.execute('INSERT INTO user VALUES(1516,'
            'victoria',
            'vic@gmail.com',
            'PRO')')

myDB.commit()

cur.execute('SELECT * FROM user')
result = cur.fetchall()
for i in result:
    print(i)

myDB.close()