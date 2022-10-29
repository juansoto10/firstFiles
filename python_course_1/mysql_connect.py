import mysql.connector 
from mysql.connector import Error

print('Resultado de MySQL connector:\n')

try:
    mi_conexion = mysql.connector.connect(
        host='192.168.0.9', 
        port=3306,
        user='root', 
        password='zacarias', 
        db='valkaublog')
    
    cur = mi_conexion.cursor()
    cur.execute('SELECT login, email FROM users')

    for name, last_name in cur.fetchall():
        print(name, last_name)

    if mi_conexion.is_connected():
        print('\nConexión exitosa perrrrroo')
        
    mi_conexion.close()
    
except Error as ex:
    print(ex)
