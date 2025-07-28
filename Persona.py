from dataclasses import dataclass

# Paso1. Definimos la estructura de datos
@dataclass
class Persona:
    nombre: str
    apellido: str
    edad: int
    direccion: str
    telefono: str
    correo: str

# Paso2. Función para registrar una persona (NO imprime, solo retorna)
def registrar_persona() -> Persona:
    print("\n.:Formulario de registro:.")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    edad = int(input("Edad: "))
    direccion = input("Dirección: ")
    telefono = input("Teléfono: ")
    correo = input("Correo electrónico: ")

    return Persona(nombre, apellido, edad, direccion, telefono, correo)

# 3. Lista para guardar personas
personas_registradas = []

# 4. Pedir cuántas personas se van a registrar
cantidad = int(input("¿Cuántas personas desea registrar? "))

# 5. Registrar N personas
for i in range(cantidad):# Ciclo for para registrar N personas
    print(f"\n--- Registro {i + 1} de {cantidad} ---")
    persona = registrar_persona()
    personas_registradas.append(persona)

# 6. Mostrar los datos registrados al final
print("\n\n.:INFORMACIÓN REGISTRADA:.")
for i, persona in enumerate(personas_registradas, start=1):#Ciclo for para mostrar los datos
    print(f"\nRegistro #{i}")
    print(f"Nombre: {persona.nombre}")
    print(f"Apellido: {persona.apellido}")
    print(f"Edad: {persona.edad}")
    print(f"Dirección: {persona.direccion}")
    print(f"Teléfono: {persona.telefono}")
    print(f"Correo electrónico: {persona.correo}")
print("\n\n.:LISTA COMPLETA DE OBJETOS REGISTRADOS:.")
print(personas_registradas)

# Fin del código
