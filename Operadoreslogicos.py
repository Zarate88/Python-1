# Variables de ejemplo
a = 5
b = 3

# OPERADORES DE COMPARACIÓN
print(a == b)   # ¿a es igual a b?
print(a != b)   # ¿a es diferente de b?
print(a > b)    # ¿a es mayor que b?
print(a < b)    # ¿a es menor que b?
print(a >= b)   # ¿a es mayor o igual que b?
print(a <= b)   # ¿a es menor o igual que b?

# OPERADORES LÓGICOS
print("Operadores lógicos:")

# AND lógico
print(True and True)
print(True and False)
print(False and True)
print(False and False)
print(3 > 2 and 2 < 3)
print(5 == 2 and 2 < 3)

# OR lógico
print(True or True)
print(True or False)
print(False or True)
print(False or False)
print(3 > 2 or 2 < 3)
print(5 == 2 or 2 < 3)

# NOT lógico
print(not True)
print(not False)
print(not (3 > 2))
print(not (5 == 2))

# OPERADORES UNARIOS
print(+b)    # Signo positivo
print(-b)    # Negación

# Simulación de incremento y decremento
b += 1       # equivalente a ++b
print(b)

b -= 1       # equivalente a --b
print(b)

# Simulación de post-incremento
temp = b
b += 1
print(temp)  # muestra el valor antes de incrementar

# Simulación de post-decremento
temp = b
b -= 1
print(temp)  # muestra el valor antes de decrementar

print("Valor final de b:", b)
