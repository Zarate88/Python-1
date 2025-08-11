# ==============================
# EJEMPLO DE LISTA EN PYTHON
# ==============================
#creamor una lista con varias frutas
frutas = ["manzana", "banana", "cereza",]#lista con tres elementos
print(frutas) #imprimir la lista completa 
#__________________________________
#Acceder a cada elemento de la lista por su posicion 
print(frutas[0]) #imprimir el primer elemento de la lista
print(frutas[1]) #imprimir el segundo elemento de la lista  

#__________________________________
#Modificar un elemento de la lista
frutas[1] = "naranja" #cambiar el segundo elemento de la lista
#cambiamos banana por naranja 
print(frutas) #imprimir la lista modificada
#__________________________________
#Agregar un elemento al final de la lista
frutas.append("uva") #agregar uva al final de la lista  
print(frutas) #imprimir la lista con el nuevo elemento
frutas.append("kiwi") #agregar kiwi al final de la lista  
print(frutas) #imprimir la lista con el nuevo elemento
#__________________________________
#Insertar un elemento en una posicion especifica
frutas.insert(1, "fresa") #insertar fresa en la posicion 1
print(frutas) #imprimir la lista con el nuevo elemento  
#__________________________________
#Eliminar un elemento de la lista por su valor
frutas.remove("cereza") #eliminar cereza de la lista        
print(frutas) #imprimir la lista sin cereza
#__________________________________
#Eliminar un elemento de la lista por su posicion   
del frutas[0] #eliminar el primer elemento de la lista
print(frutas) #imprimir la lista sin el primer elemento
#__________________________________
#Eliminar el ultimo elemento de la lista
frutas.pop() #eliminar el ultimo elemento de la lista   
print(frutas) #imprimir la lista sin el ultimo elemento
#__________________________________ 
#Recorrer la lista con un buclae for
for fruta in frutas: #para cada fruta en la lista frutas
    print("me gusta comer" ,fruta) #imprimir la fruta
