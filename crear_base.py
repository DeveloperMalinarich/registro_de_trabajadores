import  sqlite3 #importo la libreria
conn = sqlite3.connect('registrotrabajadores.db') #creo una conexion con la base (y creo la base)
cursor = conn.cursor() #creo un cursor en la variable "cursor"

cursor.execute ("""CREATE TABLE trabajadores (
          ID_trabajador INTEGER PRIMARY KEY AUTOINCREMENT,
          nombre TEXT NOT NULL,
          apellido TEXT NOT NULL,
          dni INTEGER UNIQUE NOT NULL,
          telefono INTEGER NOT NULL,                
          mail TEXT NOT NULL,
          area TEXT NOT NULL
                )""")


conn.commit
conn.close
