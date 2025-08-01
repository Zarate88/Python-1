#realizar un programa que simule un menu interactivos con las siguientes condiciones
#Agregar un dato uno a uno
#ver los datos almacenados  
#opcion para salir del programa
#___________________________________________
print("____________________________________________ ")

print("Bienvenido al programa de almacenamiento de datos")

print("____________________________________________ ")

# Creación de las variables y listas a utilizar
# Creamos una lista Vacia  la llamaremos datos 
datos = []     #lista para almacenar los datos 
# el menu debe ser interactivo debe realimentarse varias ocaciones
# se Implementaria un bucle while para que el menu se repita
# while palabra clave
#<condicion>: 
# codigo que se repite
while  True: # Bucle infinito para el menú interactivo
    print("\n --- MENÚ DE OPCIONES ---")#
    print("1. Agregar un dato UNO a uno")   
    print("2. Ver los datos almacenados")
    print("3. Salir del programa")
    opcion = int(input("Seleccione una opción (1, 2 o 3  ): "))
    #verificar si el usuario ingreso el usuario
    #verificar si el usuario ingreso 1 
    if opcion == 1:  # Opción para agregar un dato
        dato = input("Ingrese el dato que desea agregar: ")
        datos.append(dato)  # Agrega el dato a la lista
        print(f"Dato '{dato}' agregado exitosamente.")
    elif opcion == 2:  # Opción para ver los datos almacenados
        if datos:
            print("\nDatos almacenados:")
            for i, d in enumerate(datos, 1):
                print(f"{i}. {d}")
        else:
            print("No hay datos almacenados.")
    elif opcion == 3:  # Opción para salir del programa
        print("Saliendo del programa. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, seleccione 1, 2 o 3.")
 