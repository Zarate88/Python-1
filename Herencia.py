# Clase Padre o Superclase
class Animal:
    def __init__(self, nombre, especie):
        self.nombre = nombre       # Atributo nombre
        self.especie = especie     # Atributo especie

    def presentarse(self):
        # Método que muestra el nombre y la especie del animal
        print(f"Soy {self.nombre} y soy un {self.especie}.")

    def sonido(self):
        # Método genérico para sonido (será sobreescrito por clases hijas)
        print("Este animal hace un sonido genérico.")

# Clase Hija que hereda de Animal
class Perro(Animal):
    def __init__(self, nombre, raza):
        # Usamos super() para llamar al constructor de la clase padre
        super().__init__(nombre, "perro")  # 'especie' se fija como "perro"
        self.raza = raza                   # Atributo específico de Perro

    def sonido(self):
        # Sobrescribimos el método sonido con uno específico para perros
        print("¡Guau guau!")

    def mostrar_raza(self):
        # Método propio de la clase Perro
        print(f"Soy un {self.raza}.")

# Clase Hija que hereda de Animal
class Gato(Animal):
    def __init__(self, nombre, color):
        super().__init__(nombre, "gato")
        self.color = color  # Atributo específico de Gato

    def sonido(self):
        print("¡Miau!")

    def mostrar_color(self):
        print(f"Mi color es {self.color}.")

# ---------- Uso de las clases ----------

# Crear un objeto de tipo Perro
mi_perro = Perro("Firulais", "Labrador")
mi_perro.presentarse()     # Heredado de Animal
mi_perro.sonido()          # Sobrescrito en Perro
mi_perro.mostrar_raza()    # Propio de Perro

print()  # Línea en blanco

# Crear un objeto de tipo Gato
mi_gato = Gato("Michi", "blanco")
mi_gato.presentarse()      # Heredado de Animal
mi_gato.sonido()           # Sobrescrito en Gato
mi_gato.mostrar_color()    # Propio de Gato
# Fin del código