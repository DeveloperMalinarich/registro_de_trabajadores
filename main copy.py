

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

    if resultado:
        print("El trabajador ya existe, seleccione una opcion: ")        
        menu_existe(documento)
    else:
        menu_noexiste()


#defino la funcion si el DNI es existente
def menu_existe (documento):

    #realizo un bucle While
    while True:

        #solicito al usuario que ingrese la opcion deseada
        opcion = int(input("Seleccion la opcion deseada y presione ENTER:"
                           "\n1. Consultar sus datos"
                           "\n2. Salir del programa\n"))

        if opcion == 1:
            #realizar la consulta a la tabla trabajadores 
            cursor.execute("SELECT * FROM trabajadores WHERE dni = ?", (documento,))
            resultado = cursor.fetchall() #recuperar los datos obtenidos de la consulta y almacenarlos en la variable "resultado"
            print (resultado) #imprimir los datos guardados en la variable "resultado"
            print("Muchas gracias por consultar el registro de trabajadores") #despedida del usuario
            print("Hasta la proxima!")
            break                       
        
        elif opcion == 2: #si la opcion es 2
            #despedida del usuario
            print("Muchas gracias por consultar el registro de trabajadores") 
            print("Hasta la proxima!")
            break

        else: #mensaje si no elije ninguna opcion correcta
            print("Opcion no valida, Presione enter")


        
    
def menu_noexiste(): #defino la funcion si no existe "menu_noexiste"
    print("El usuario ingresado no existe.")
    while True:  #defino un bucle while
        
        #Pido seleccion al usuario
        opcion = int(input("Seleccion la opcion deseada y presione ENTER:"
                                    "\n1. Agregar usuario."
                                    "\n2. Salir del programa.\n"))   
        
            
        def agregar_usuario():
            #defino variables para los datos a ingresar
            nombre = input("ingrese el nombre: ") 
            apellido = input("ingrese el apellido: ")
            dni = input("ingrese el DNI: ")
            mail = input("ingrese el mail: ")
            telefono = int(input("ingrese el telefono: "))
            area = input("ingrese el area: ")

            #defino esta variable donde se almacenan los datos que seran cargados en la base
            todos_datos = (None,nombre, apellido, dni, mail, telefono, area)             

            #ejecuto la busqueda para insertar los datos almacenados en la variable "todos_datos"
            cursor.execute("INSERT INTO trabajadores VALUES(?,?,?,?,?,?,?)", todos_datos) 
            conn.commit()                
            print("Se agregaron los datos ingresados correctamente."
                "\nPresione ENTER para comenzar nuevamente") #se imprime mensaje de exito
            input()
            saludo_inicial()


        if opcion == 1:
            agregar_usuario()

        elif opcion == 2: #si la opcion es 2
            print("Muchas gracias por consultar el registro de trabajadores") #despedida del usuario
            print(input("Hasta la proxima, presiona Enter para salir!"))
            break
            

        else: #mensaje si no elije ninguna opcion correcta
            print(input("Opcion no valida, vuelve a intentarlo."
                        "\nPresioná Enter"))
            
            
saludo_inicial()