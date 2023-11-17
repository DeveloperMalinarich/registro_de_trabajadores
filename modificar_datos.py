import  sqlite3 #importo la libreria SQLite3
conn = sqlite3.connect('registrotrabajadores.db') #creo la conexion a la db
cursor = conn.cursor() #creo el cursor

todos_trabajadores = [ #creo la variable donde almaceno los datos que voy ingresar
    (None,'Vanesa','Rincovich','32422029','vanesa@menandage.com','1156169165','videoconferencias')
]

cursor.executemany("INSERT INTO trabajadores VALUES (?,?,?,?,?,?,?)", todos_trabajadores) #ejecuto la sentencia

conn.commit()
conn.close()