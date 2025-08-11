name = "DIEGO FERNANDO ZARATE PINEDA"
surname = "SENA"

# Imprimir el valor de la cadena
print(name)

# Longitud de la cadena
print(len(name))

# Convertir a mayúsculas
print(name.upper())

# Convertir a minúsculas
print(name.lower())

# Imprimir el carácter en la posición 2
print(name[2])

# Buscar la posición de la subcadena "ZARATE"
print(name.find("ZARATE"))  # Devuelve -1 si no lo encuentra

# Imprimir subcadena desde el índice 0 hasta el 5 (excluye el 5)
print(name[0:5])

# Concatenar cadenas
print(name + " " + surname)

# Longitud de la cadena
print("Longitud de la cadena:", len(name))

# Verificar si una subcadena está contenida en otra
print("diego" in "HOLA JAVA")  # False
print("HOLA" in "HOLA JAVA")   # True

# Comparar cadenas
print("HOLA JAVA" == "HOLA JAVA")  # True

# Eliminar espacios al inicio y al final
print("   hola me llamo diego zarate   ".strip())

# Reemplazar "diego" por "fernando"
print("hola me llamo diego zarate".replace("diego", "fernando"))
