import mysql.connector

connection = mysql.connector.connect(host="localhost", database="addressbook", user="root", password="")

try:
    cursor = connection.cursor()
    cursor.execute("select * from group_list")
    fprint = [row for row in cursor.fetchall()]
    print(fprint)
finally:
    connection.close()
