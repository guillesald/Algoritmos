from modulos.ListaDobleEnlazada import ListaDobleEnlazada  

# Crear una lista de ejemplo
lista_ejemplo = ListaDobleEnlazada()

# Agregar elementos a la lista
lista_ejemplo.agregar_al_inicio(5)
lista_ejemplo.agregar_al_final(10)
lista_ejemplo.agregar_al_final(3)
lista_ejemplo.agregar_al_final(8)

print("Lista inicial:", list(lista_ejemplo))

# Probar el método insertar
lista_ejemplo.insertar(20, 2)
print("Después de insertar 20 en la posición 2:", list(lista_ejemplo))

# Probar el método extraer
elemento_extraido = lista_ejemplo.extraer(2)
print("Elemento extraído:", elemento_extraido)
print("Después de extraer el elemento en la posición 2:", list(lista_ejemplo))

# Probar el método copiar
copia_lista = lista_ejemplo.copiar()
print("Copia de la lista:", list(copia_lista))

# Probar el método invertir
lista_ejemplo.invertir()
print("Después de invertir la lista:", list(lista_ejemplo))

# Probar el método ordenar
lista_ejemplo.ordenar()
print("Después de ordenar la lista:", list(lista_ejemplo))

# Probemos el método de concatenación con una nueva lista
otra_lista = ListaDobleEnlazada()
otra_lista.agregar_al_final(100)
otra_lista.agregar_al_final(50)

lista_ejemplo.concatenar(otra_lista)
print("Después de concatenar otra lista:", list(lista_ejemplo))