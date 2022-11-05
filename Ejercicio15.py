# 15. Se requiere implementar un grafo para almacenar las siete maravillas arquitectónicas modernas
# y naturales del mundo, para lo cual se deben tener en cuenta las siguientes actividades:
# a. de cada una de las maravillas se conoce su nombre, país de ubicación (puede ser más de
# uno en las naturales) y tipo (natural o arquitectónica);
# b. cada una debe estar relacionada con las otras seis de su tipo, para lo que se debe almacenar
# la distancia que las separa;
# c. hallar el árbol de expansión mínimo de cada tipo de las maravillas;
# d. determinar si existen países que dispongan de maravillas arquitectónicas y naturales;
# e. determinar si algún país tiene más de una maravilla del mismo tipo;
# f. deberá utilizar un grafo no dirigido.

from grafo import Grafo

class Datos_Maravillas:

    def __init__(self, nombre, pais, tipo):
        self.nombre=nombre 
        self.pais=pais
        self.tipo=tipo
   
    def __str__(self):
        return f'{self.nombre}'

dic_maravillas=[
    {'nombre':'Gran Muralla China','pais':'China','tipo':'arquitectónica'},
    {'nombre':'Petra','pais':'Jordania','tipo':'arquitectónica'},
    {'nombre':'Coliseo Romano','pais':'Italia','tipo':'arquitectónica'},
    {'nombre':'Chichen Itza','pais':'Mexico','tipo':'arquitectónica'},
    {'nombre':'Machu Pichu','pais':'Perú','tipo':'arquitectónica'},
    {'nombre':'Cristo Redentor','pais':'Brasil','tipo':'arquitectónica'},
    {'nombre':'Taj Mahal','pais':'India','tipo':'arquitectónica'},

    {'nombre':'Rio Subterraneo de Puerto Princesa','pais':'Filipinas','tipo':'natural'},
    {'nombre':'Montaña de la Mesa','pais':'Sudafrica','tipo':'natural'},
    {'nombre':'Cataratas del Iguazú','pais':'Argentina/Brasil','tipo':'natural'},
    {'nombre':'Amazonia','pais':'Bolivia/Brasil/Colombia/Ecuador/Guayana Francesa/Guyana/Perú/Surinam/Venezuela','tipo':'natural'},
    {'nombre':'Bahia de Ha Long','pais':'Vietnam','tipo':'natural'},
    {'nombre':'Isla Jeju','pais':'Corea del Sur','tipo':'natural'},
    {'nombre':'Parque Nacional de Komodo','pais':'Indonesia','tipo':'natural'}
]

g_maravillas= Grafo(False)

for m in dic_maravillas:
    g_maravillas.insertar_vertice(Datos_Maravillas(m['nombre'].title(),
                                                m['pais'].title().split('/'),
                                                m['tipo']),'nombre')
# g_maravillas.barrido_vertice()
# print()

# b. cada una debe estar relacionada con las otras seis de su tipo, para lo que se debe almacenar
# la distancia que las separa;
g_maravillas.asignar_arista_maravillas()
print()
# g_maravillas.barrido_amplitud('Amazonia')
# print()
# g_maravillas.barrido_amplitud('Petra')

# # c. hallar el árbol de expansión mínimo de cada tipo de las maravillas;
arbol_nat, arbol_arq = g_maravillas.kruskal_class()
arbol_min = arbol_arq[0].split('-')
peso_total = 0
for nodo in arbol_min:
    nodo = nodo.split(';')
    peso_total += int(nodo[2])
print(f"El minimo camino para poder recorrer todas las maravillas arquitectonicas es {peso_total} kms")
print()
arbol_min = arbol_nat[0].split('-')
peso_total = 0
for nodo in arbol_min:
    nodo = nodo.split(';')
    peso_total += int(nodo[2])
print(f"El minimo camino para poder recorrer todas las maravillas naturales es {peso_total} kms")
print()

# d. determinar si existen países que dispongan de maravillas arquitectónicas y naturales;
paises=g_maravillas.paises_con_nat_arq()
print('Paises con maravillas naturales y arquitectónicas')
for pais in paises:
    if (paises[pais]['arq']==True) and  (paises[pais]['nat']==True):
        print(pais)
print()

# e. determinar si algún país tiene más de una maravilla del mismo tipo;
paises_n,paises_a=g_maravillas.pais_mas_de_una()
print('Pais con mas de una maravilla natural:')
for pais in paises_n:
    if paises_n[pais]['control']==True:
        print(pais)   
print()
print('Pais con mas de una maravilla arquitectónica:')
for pais in paises_a:
    if paises_a[pais]['control']==True:
        print(pais)
print()           