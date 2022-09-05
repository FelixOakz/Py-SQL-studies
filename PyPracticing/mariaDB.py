import mysql.connector

try:
    connection = mysql.connector.connect(host ='localhost',
                                         user = 'root',
                                         passwd = 'timemachine',
                                         database = 'pythonx')
    cursor = connection.cursor()



    cursor.execute('insert into user values(4533,'
                   'roger',
                   'rogerinho@yahoo.com',
                   'PRO');
    ')

    connection.commit()
    connection.close()
except error:
    print('error')