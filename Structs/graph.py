from linkedlist import *
from algo1 import *

class graphNode:
    value = None
    nextNode = None
    visited = False

    parent = None
    color = 'white'
    d = 0
    f = 0

class tim:
    v = 0

"""Funcion que dadas 2 listas V(vertices) A(aristas) crea un grafo
(repr por lista de adyacencia).
-Para grafos no dirijidos recomendable usar complete.
-Para grafos dirijidos representacion con complete = False"""
def createGraph(V, A, complete = True):
    Graph = Array(length(V), graphNode())
    
    allocVertices(V, Graph)

    allocEdges(A, Graph, complete)

    return Graph
#Inserta los vertices en el array del grafo
def allocVertices(V, G):
    cn = V.head
    i = 0

    while cn:
        G[i] = graphNode()
        G[i].value = cn.value
        i += 1
        cn = cn.nextNode

    return
#Completa listas de adyacencia -complete -> no dirigido; incomplete -> si/no dirigido-
def allocEdges(A, G, complete):
    glen = len(G)
    cn = A.head

    while cn:
        flag = False

        for i in range(glen):
            if G[i].value == cn.value:
                #Se inserta un nodo al Grafo(lista de adyacencia).
                nwn = graphNode()
                nwn.nextNode = G[i].nextNode
                nwn.value = cn.nextNode.value
                G[i].nextNode = nwn
                #Evitar recorrer todo el arreglo de no ser necesario
                if flag or not complete:
                    break
                else:
                    flag = True
            #Si se quiere la representacion completa
            #Se indica la adyacencia en ambos nodos conectados por la arista
            if complete and G[i].value == cn.nextNode.value:
                #Se inserta un nodo al Grafo(lista de adyacencia).
                nwn = graphNode()
                nwn.nextNode = G[i].nextNode
                nwn.value = cn.value
                G[i].nextNode = nwn
                #Evitar recorrer todo el arreglo de no ser necesario
                if flag:
                    break
                else:
                    flag = True

        cn = cn.nextNode.nextNode

    return   

"""existPath() verifica que exista un camino entre v1 y v2"""
#Uso de wrapper para poder resetear valores al finalizar ejecucion.
def existPath(G,v1,v2):
    temp = _existPath(G, v1, v2)
    unsetVisited(G)
    return temp

def _existPath(G, v1, v2):
    #Se busca el nodo correspondiente a v1 en el array
    for i in range(len(G)):
        if G[i].value == v1:
            G[i].visited = True
            #Se recorre la lista de adyacencia relacionada al nodo de v1
            cn = G[i].nextNode
            while cn:
                #Si dentro de sus relaciones se encuentra v2 ...
                if cn.value == v2:
                    return True
                #si no lo hace ...
                for j in range(len(G)):
                    if G[j].value == cn.value:
                        #y no se ha hecho anteriormente ...
                        if G[j].visited == False:
                            #se reliza el mismo procedimiento con todos los nodos relacionados a v1
                            temp = _existPath(G, G[j].value, v2)
                            if temp == True: 
                                return True
                cn = cn.nextNode
    return False
#Se resetea visited para evitar inconvenientes en futuras ejecuciones.
def unsetVisited(G):
    for i in range(len(G)):
        G[i].visited = False
    
    
"""isConnected(): verifica que un Grafo sea conexo"""
#Lazy impl.
def isConnected(G):
    for i in range(len(G)-1):
        for j in range(i+1,len(G)):
            temp = existPath(G, G[i].value, G[j].value)
            if temp == False:
                return False
    return True

"""isTree() determina si el grafo es un arbol"""
#Solo se toma como parametro valido a Grafos con lista de ady completa
#Todo grafo conexo para el que |A|=|V|-1 es un arbol.
def isTree(G):
    A = EdgesQtty(G)
    V = len(G) 
    if isConnected(G) and A == (V-1):
        return True
    return False

def EdgesQtty(G):
    t = 0
    for i in range(len(G)):
        t += (_lenlist(G[i]) - 1)

    return t/2

"""countConnections(G) cuenta la cantidad de componenetes conexas dentro de G"""
def countConnections(G):
    #Se recorre el grafo con DFS para poder utilizar el teorema del parentesis
    dfs(G)    
    #Se empieza asumiendo que todos los nodos son raices de diferentes arboles.
    roots = LinkedList()
    for i in range(len(G)):
        add(roots, G[i])

    for i in range(len(G)):
        cn = roots.head

        while cn:
            #Si el parentesis de G[i] abarca más que una de las presuntas raices ...
            if va(G[i]) > va(cn.value):
                #Y el parentesis de G[i] encierra a la presunta raiz ...
                if G[i].d < cn.value.d and G[i].f > cn.value.f:
                    #La presunta raiz es hijo de G[i] por lo que no es raiz.
                    delete(roots, cn.value)
            cn = cn.nextNode
    #La cantidad de componentes conexas será igual a la cantidad de árboles
    #generados en un bosque por DFS
    return length(roots)
#Calcula la extensión de los parentesis de un nodo v.
def va(v):
    return abs(v.f - v.d)
    
def dfs(G):
    for i in range(len(G)):
        G[i].color = 'white'
        G[i].parent = None

    time = tim()
    for i in range(len(G)):
        if G[i].color == 'white':
            dfsVisit(G, G[i], time)

def dfsVisit(G, u, time):
    time.v += 1 
    u.d = time.v
    u.color = 'gray'

    cn = u.nextNode

    while cn:
        for i in range(len(G)):
            if cn.value == G[i].value:
                if G[i].color == 'white':
                    G[i].parent = u
                    
                    dfsVisit(G, G[i], time) 
        cn = cn.nextNode
    
    u.color = 'black'
    time.v += 1
    u.f = time.v

"""converToTree(G,v) convierte el grafo G en un árbol
con raiz v, la representación de dicho árbol está en
listas de adyacencia"""
def convertToTree(G, v):
    #Es necesario que G sea conexa ...
    if not isConnected(G):
        return None
    #y que v exista en G
    exist = False
    for i in range(len(G)):
        if G[i].value == v:
            exist = True
    if not exist:
        return None
    #Se recorre con BFS para generar el árbol
    bfs(G, v)
    
    #Se crean las listas generadoras
    V = LinkedList()
    A = LinkedList()
    for i in range(len(G)):
        add_toend(V, G[i].value)
        if G[i].parent:
            add_toend(A, G[i].parent.value)
            add_toend(A, G[i].value)
    #Se devuelve una lista de adyacencia reducida para
    #facilitar la visualización
    T = createGraph(V, A, False)
    return T

def bfs(G, v):
    for i in range(len(G)):
        if G[i].value == v:
            temp = i
        G[i].color = 'white'
        G[i].parent = None
    
    G[temp].color = 'gray'
    Q = LinkedList()
    enqueue(Q, G[temp])

    while Q.head:
        u = dequeue(Q)
        cn = u.value.nextNode
        while cn:
            for i in range(len(G)):
                if cn.value == G[i].value and G[i].color == 'white':
                    G[i].color = 'gray'
                    G[i].parent = u.value
                    enqueue(Q, G[i])
            cn = cn.nextNode
        u.color = 'black'
                    
#prim(G) genera un arbol abarcador de costo minimo utilizando el alg de Prim.
#G es un array de longitud 2 en el que se almacenan 2 objetos:
#un array con todos los vértices, una matriz de adyacencia que usa el primer
#array como indice posicional.
def prim(G):
    A = LinkedList()
    V = LinkedList()
    #Se agrega el primer vertice de G al árbol abarcador
    add(V, G[0][0])
    #Mientras el árbol abarcador no cubra todos los vértices del grafo ...
    while length(V) != len(G[0]):
        #Se parte desde el último vértice cubierto
        i = V.head.value
        min = min_v = 0
        #Arista de costo minimo entre V y G[0] - V
        while min == 0:
            for j in range(len(G[0])):
                if search(V, G[0][j]):
                    continue
                if G[1][i][j] < min_v or min_v == 0:
                    min_v = G[1][i][j]
                    min = j
            j = min
            i = i.nextNode
        #Se agrega la arista de menor costo al árbol abarcador
        add_toend(A, i)
        add_toend(A, j)
        #Se agrega el vértice encontrado como vértice del árbol.
        add(V, j)
    
    Tree = createGraph(V, A)
    return Tree



"""-Utilities-"""
#Imprime Grafo en su repr lista de adyacencia.
def printgraph(G):
    for i in range(len(G)):
        node = G[i]
        _printlist(node)
def _printlist(node):
	current_node = node

	if not current_node:
		print("None")
		return
		
	while current_node:
		if current_node.nextNode:
			print(current_node.value,"->", end = " ")
		else: 
			print(current_node.value)
		current_node = current_node.nextNode

def _lenlist(node):
    cn = node
    i = 0
    while  cn:
        i += 1
        cn = cn.nextNode
    return i

#Se agrega elemento a la cola 
def enqueue(Q, element):
	add(Q, element)
#Se elimina el primer elemento insertado
def dequeue(Q):
	if Q.head == None: 
		return None
	else:
		index = length(Q)-1
		element = access(Q, index)
		#Caso especial: colas de un solo elemento
		if length(Q) == 1:
			Q.head = None
			return element

		current_node = Q.head
		#Se avanza hasta el penúltimo nodo y se desvincula el último.
		for i in range(index-1):
			current_node = current_node.nextNode
		current_node.nextNode = None

		return element