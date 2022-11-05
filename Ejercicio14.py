# 14. Implementar sobre un grafo no dirigido los algoritmos necesario para dar solución a las siguientes
# tareas:
# a. cada vértice representar un ambiente de una casa: cocina, comedor, cochera, quincho,
# baño 1, baño 2, habitación 1, habitación 2, sala de estar, terraza, patio;
# b. cargar al menos tres aristas a cada vértice, y a dos de estas cárguele cinco, el peso de la arista
# es la distancia entre los ambientes, se debe cargar en metros;
# c. obtener el árbol de expansión mínima y determine cuantos metros de cables se necesitan
# para conectar todos los ambientes;
# d. determinar cuál es el camino más corto desde la habitación 1 hasta la sala de estar para
# determinar cuántos metros de cable de red se necesitan para conectar el router con el
# Smart Tv.

from grafo import Grafo

casa=Grafo(False)

# a. cada vértice representar un ambiente de una casa: cocina, comedor, cochera, quincho,
# baño 1, baño 2, habitación 1, habitación 2, sala de estar, terraza, patio;
casa.insertar_vertice('cocina')
casa.insertar_vertice('comedor')
casa.insertar_vertice('cochera')
casa.insertar_vertice('quincho')
casa.insertar_vertice('baño1')
casa.insertar_vertice('baño2')
casa.insertar_vertice('habitacion1')
casa.insertar_vertice('habitacion2')
casa.insertar_vertice('saladeestar')
casa.insertar_vertice('terraza')
casa.insertar_vertice('patio')

# b. cargar al menos tres aristas a cada vértice, y a dos de estas cárguele cinco, el peso de la arista
# es la distancia entre los ambientes, se debe cargar en metros;
casa.insertar_arista('cocina','saladeestar',2)
casa.insertar_arista('cocina','baño1',4)
casa.insertar_arista('cocina','baño2',5)
casa.insertar_arista('cocina','comedor',7)
casa.insertar_arista('cocina','quincho',8)
casa.insertar_arista('comedor','patio',17)
casa.insertar_arista('comedor','terraza',13)
casa.insertar_arista('comedor','baño2',4)
casa.insertar_arista('comedor','habitacion1',15)
casa.insertar_arista('cochera','habitacion1',8)
casa.insertar_arista('cochera','patio',5)
casa.insertar_arista('cochera','quincho',21)
casa.insertar_arista('quincho', 'habitacion2',19)
casa.insertar_arista('habitacion2','habitacion1',1)
casa.insertar_arista('habitacion2','patio',3)
casa.insertar_arista('baño1','terraza',20)
casa.insertar_arista('baño1','saladeestar',14)
casa.insertar_arista('baño2','terraza',31)

# c. obtener el árbol de expansión mínima y determine cuantos metros de cables se necesitan
# para conectar todos los ambientes;
arbol_min = casa.kruskal()
arbol_min = arbol_min[0].split('-')
peso_total = 0
for nodo in arbol_min:
    nodo = nodo.split(';')
    peso_total += int(nodo[2])
    # print(f'{nodo[0]}-{nodo[1]}-{nodo[2]}')

print(f"Se necesitan {peso_total} metros de cable para conectar todos los ambientes")
print()

# d. determinar cuál es el camino más corto desde la habitación 1 hasta la sala de estar para
# determinar cuántos metros de cable de red se necesitan para conectar el router con el
# Smart Tv.
if casa.existe_paso('habitacion1','saladeestar'):
    tabla=casa.dijkstra('habitacion1')
    camino=casa.camino(tabla,'habitacion1','saladeestar')
    print('Camino mas corto de habtacion1 a sala de estar: ',camino['camino'])
    print('Se deberá disponer de',camino['costo'],'metros de cable para conectar el smart al router')
else:
    print('No hay camnio disponible')
print()
