import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',passwd='Nandini@123',database="Application")
mycursor=mydb.cursor()
mycursor.execute('insert Resumemain values (\'Nandini Parekh\', \'30/April/2002\', \'Indian\', \'AKIS\', \'Computer Science\', 1500, 2380, \'female\', 97.4, 1)')
mydb.commit()

