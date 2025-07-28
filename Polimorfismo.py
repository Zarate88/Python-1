# Clase padre o superclase
class Animal:
    def hacer_sonido(self):
        # Método que será sobrescrito por las clases hijas
        pass  # No se implementa aquí (actúa como una interfaz)

# Clases hijas que implementan el mismo método pero con comportamientos distintos
class Perro(Animal):
    def hacer_sonido(self):
        print("Guau guau")

class Gato(Animal):
    def hacer_sonido(self):
        print("Miau miau")

class Vaca(Animal):
    def hacer_sonido(self):
        print("Muuu")

# ---------- Polimorfismo en acción ----------

# Creamos una lista de objetos de distintas clases
animales = [Perro(), Gato(), Vaca()]

# Recorremos la lista y llamamos al mismo método 'hacer_sonido'
# Aunque son objetos de diferentes clases, todos responden al mismo método
for animal in animales:
    animal.hacer_sonido()
