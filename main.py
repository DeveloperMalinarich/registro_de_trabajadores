import  sqlite3 #importo la libreria
conn = sqlite3.connect('registrotrabajadores.db') #creo una conexion con la base (y creo la base)
cursor = conn.cursor() #creo un cursor en la variable "cursor"

def saludo_inicial (): #defino funcion de saludo 
    
    # imprimo saludo inicial
    print("**Bienvenido al registro de trabajadores**") 
    print("En nuestra app podras buscar todos los registros"
          " de trabajadores existente en nuestra base, "
          "\nmodificar, eliminar registros existentes o bien agregar trabajadores inexistentes.")
    
    #solicito DNI al usuario
    documento = int(input("Ingrese su numero de DNI para comenzar: "))

    #ejecuto la consulta a la tabla trabajadores
    cursor.execute("SELECT *  FROM trabajadores WHERE dni = ?", (documento,))

    #recupera la primer fila de la query y la almacena en la variable "resultado"
    resultado = cursor.fetchone() 

    #si resultado es "True" (es decir que tiene algun valor)
    if resultado: 
        print("El trabajador ya existe, seleccione una opcion: ")
        
        def menu_existe ():
            while True:
                opcion = int(input("Seleccione una opción:" #solicito al usuario que ingrese la opcion deseada
                    "\n1. Consultar sus datos"
                    "\n2. Salir del programa\n"))
                
                if opcion == 1: #si la opcion es 1
                    cursor.execute("SELECT * FROM trabajadores WHERE dni = ?", (documento,)) #realizar la consulta a la tabla trabajadores
                    resultado = cursor.fetchall() #recuperar los datos obtenidos de la consulta y almacenarlos en la variable "resultado"
                    print (resultado) #imprimir los datos guardados en la variable "resultado"

                elif opcion == 2: #si la opcion es 2
                    print("Muchas gracias por consultar el registro de trabajadores") #despedida del usuario
                    print("Hasta la proxima!")
                    break

                else: #mensaje si no elije ninguna opcion correcta
                    print("Opcion no valida, intentalo otra vez")
                    menu_existe() #se reinicia el menu de usuario existente
    
    elif not resultado:#si el resultado esta vacio(no se encotro un usuario con ese DNI)
        print("El trabajador no existe, seleccione la opcion deseada:") #imprime las opciones
            
        def menu_noexiste(): #defino la funcion si no existe "menu_noexiste"
            while True:  #defino un bucle while
                
                #Pido seleccion al usuario
                opcion_noexiste = int(input("Seleccion la opcion deseada y presione ENTER:"
                                            "\n1. Agregar usuario."
                                            "\n2. Salir del programa.\n"))   
                
                #defino variables para los datos a ingresar
                nombre = input("ingrese el nombre: ") 
                apellido = input("ingrese el apellido: ")
                dni = input("ingrese el DNI: ")
                mail = input("ingrese el mail: ")
                telefono = int(input("ingrese el telefono: "))
                area = input("ingrese el area: ")

                #defino esta variable donde se almacenan los datos que seran cargados en la base
                todos_datos = (None,nombre, apellido, dni, mail, telefono, area) 
                    
                
                if opcion_noexiste == 1: #si la opcion elegida es 1
                    cursor.execute("INSERT INTO trabajadores VALUES(?,?,?,?,?,?,?)", todos_datos) #ejecuto la busqueda para insertar los datos almacenados en la variable "todos_datos"
                    conn.commit()                
                    print("Se agregaron los datos ingresados correctamente."
                        "\nPresione ENTER para comenzar nuevamente") #se imprime mensaje de exito 
                    saludo_inicial() #se llama a la funcion para comenzar nuevamente
                
                elif opcion_noexiste == 2: #si la opcion es 2
                    print("Muchas gracias por consultar el registro de trabajadores") #despedida del usuario
                    print("Hasta la proxima!")
                    break

                else: #mensaje si no elije ninguna opcion correcta
                    print("Opcion no valida, intentalo otra vez")
                    menu_existe() #se reinicia el menu de usuario existente
                    
   
saludo_inicial()