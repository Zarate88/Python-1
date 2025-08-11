# ==============================
# EJEMPLO DE TUPLA EN PYTHON
# ==============================

# Creamos una tupla con colores
colores = ("rojo", "verde", "azul")  # Tupla con 3 elementos

print(colores)  # Mostramos la tupla completa

# Acceder a elementos por índice
print(colores[0])  # Muestra "rojo"
print(colores[2])  # Muestra "azul"

# Las tuplas son inmutables, así que esto daría error:
# colores[1] = "amarillo"  # ❌ No se puede cambiar

# Podemos recorrer la tupla con un bucle for
for color in colores:  # 'color' toma cada valor de la tupla
    print("Mi color favorito es", color)

# Si queremos cambiar algo, debemos crear una nueva tupla
nueva_tupla = colores + ("amarillo",)  # Creamos una nueva tupla añadiendo "amarillo"
print(nueva_tupla)

# También podemos desempaquetar la tupla en variables
rojo, verde, azul = colores  # Asigna cada valor a una variable diferente
print("Rojo:", rojo)
print("Verde:", verde)
print("Azul:", azul)
