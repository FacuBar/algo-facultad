from  linkedlist import LinkedList, add_toend

class AVLTree:
    root = None

class AVLNode:
    parent = None
    leftnode = None
    rightnode = None
    key = None
    value = None
    balanceFactor = None
    height = None

"""access(): busca un nodo por key"""
#Wrapper
def access(B, key):
    if not B.root:
        return None
    return Access(B.root, key)
#Se busca el nodo cuya key coincida con el parametro.
def Access(node, key):
    if not node: 
        return None
    elif node.key == key:
        return node.value

    if key > node.key:
        temp = Access(node.rightnode, key)
        if temp: return temp
    else: 
        temp = Access(node.leftnode, key)
        if temp: return temp

"""search(): busca elemento en arbol y devuelve la key correspondiente """
#Wrapper
def search(B, element):
    if not B.root:
        return None
    return Search(B.root, element)
#Se busca el nodo cuyo elemento coincida con el parametro.
def Search(node, element):
    if not node:
        return None
    elif node.value == element:
            return node.key

    temp = Search(node.leftnode, element)
    if temp: return temp
    temp = Search(node.rightnode, element)
    if temp: return temp

"""insert(): Inserta nuevo nodo en el arbol"""
#Wrapper       
def insert(B, element, key):
    new_node = AVLNode()
    new_node.value = element
    new_node.key = key
    new_node.balanceFactor = 0
    new_node.height = 0
    #Si el arbol est'a vacio, se inserta el nuevo nodo como ra'iz
    if not B.root:
        B.root = new_node
        return key 
    #Se llama a la funci'on recursiva de la que esta es wrapper.
    t_new_node = Insert(B.root, new_node)
    if t_new_node: 
        #se actualizan bf y h y si es necesario, se rebalancea
        update_bf(B, t_new_node)
        return t_new_node.key
    return False
#Se inserta el nuevo nodo en el arbol
def Insert(current_node, new_node):
    if new_node.key < current_node.key:
        if not current_node.leftnode:
            current_node.leftnode = new_node
            new_node.parent = current_node
            return new_node
        else:
            return Insert(current_node.leftnode, new_node)
    
    elif new_node.key > current_node.key:
        if not current_node.rightnode:
            current_node.rightnode = new_node
            new_node.parent = current_node
            return new_node
        else:
            return Insert(current_node.rightnode, new_node)
    #Ya existe la llave a utilizar para el nuevo nodo, no se inserta.
    else: 
        return None

"""delete(): elimina un nodo value sea element, devuelve la key de dicho nodo"""
#Wrapper
def delete(B, element):
    if B.root.value == element:
        node_rplc = fetch_rplc(B.root)

        node_rplc.parent = None
        node_rplc.rightnode = B.root.rightnode
        node_rplc.leftnode = B.root.leftnode

        B.root = node_rplc
        cll_upbf_leaves(B, B.root)
        return B.root.key

    temp = Delete(B.root, element)
    if temp:
        #actualizacion de bf y h, rebalanceo si necesario
        cll_upbf_leaves(B, temp.parent)
        return temp.key
    return False

def Delete(node, element):
    if not node: 
        return None
    #caso nodos hoja
    if is_leaf(node) and node.value == element:
        node_p = node.parent
        if node_p.leftnode == node:
            node_p.leftnode = None
        else:
            node_p.rightnode = None
        return node
    #Resto de casos
    elif not is_leaf(node) and node.value == element:
        node_rplc = fetch_rplc(node)
        node_rplc.parent = node.parent
        node_rplc.key = node.key

        if node.parent.leftnode == node:
            node.parent.leftnode = node_rplc
        else:
            node.parent.rightnode = node_rplc

        node_rplc.leftnode = node.leftnode
        node_rplc.rightnode = node.rightnode

        if node_rplc.leftnode:
            node_rplc.leftnode.parent = node_rplc
        if node_rplc.rightnode:
            node_rplc.rightnode.parent = node_rplc

        return node
    #Si valores no coinciden, llamada recurs.
    else:
        temp = Delete(node.leftnode, element)
        if temp: return temp
        temp = Delete(node.rightnode, element)
        if temp: return temp
#se busca un nodo que cumpla con la condicion de ser el mayor de los menores o viceversa.
def fetch_rplc(node):
    if node.leftnode:
        current_node = node.leftnode
        while True:
            if current_node.rightnode:
                current_node = current_node.rightnode
            else: 
                break

    else:
        current_node = node.rightnode
        while True:
            if current_node.leftnode:
                current_node = current_node.leftnode
            else:
                break

    if node.leftnode == current_node or node.rightnode == current_node:
        if current_node.parent.leftnode == current_node:
            current_node.parent.leftnode = current_node.leftnode
        else:
            current_node.parent.rightnode = current_node.rightnode

    else:	
        if current_node.parent.leftnode == current_node:
            current_node.parent.leftnode = current_node.rightnode
        else:
            current_node.parent.rightnode = current_node.leftnode

    return current_node

"""Se recorre el arbol in order"""
#Wrapper
def traverseInOrder(B):
    #arbol vacio
    if not B.root:
        return None
    else: 
        L = LinkedList()
        node = B.root
        inorder(node, L)
    #se devuelve una lista.
    return L
#Se agregan nodos a la lista con el valor del respectivo nodo del arbol.
#Siguiendo el ord'en: izquierda - raiz - derecha.
def inorder(node, l):
    #caso base
    if node == None:
        return
    else:
        #por cada (sub)arbol se anexa primero el lado izquierdo, luego la raiz, f. lado derecho 
        inorder(node.leftnode, l)
        add_toend(l, node.value)
        inorder(node.rightnode, l)


"""funciones de utilidad"""
#determina si un nodo es hoja o no
def is_leaf(node):
    #solo ocurre cuando rightnode y leftnode son None
    if node.rightnode == node.leftnode:
        return True
    else: 
        return False

def printTree(node, level=0):
    if node != None:
        printTree(node.leftnode, level + 1)
        print(' ' * 4 * level, '->', node.value, ',', node.balanceFactor)
        printTree(node.rightnode, level + 1)


""" AVL specific functions """
#Balancea un subarbol ladeado hacía la derecha
def rotateLeft(B, node):
    rplc_node = node.rightnode
    node.rightnode = rplc_node.leftnode
    #se resetan los valores de h. y bf de los nodos involucrados
    #cuyo h o bf sea > 1
    rset_bf(rplc_node)
    rset_bf(node)

    if rplc_node.leftnode:
        rplc_node.leftnode.parent = node

    if node.parent:
        if node.parent.rightnode == node:
            node.parent.rightnode = rplc_node
        else: 
            node.parent.leftnode = rplc_node
    else:
        B.root = rplc_node

    rplc_node.parent = node.parent
    node.parent = rplc_node
    rplc_node.leftnode = node	

    return rplc_node

#Balancea un subarbol ladeado hacía la izquierda
def rotateRight(B, node):
    rplc_node = node.leftnode
    node.leftnode = rplc_node.rightnode

    rset_bf(rplc_node)
    rset_bf(node)

    if rplc_node.rightnode:
        rplc_node.rightnode.parent = node

    if node.parent:
        if node.parent.rightnode == node:
            node.parent.rightnode = rplc_node
        else:
            node.parent.leftnode = rplc_node
    else:
        B.root = rplc_node

    rplc_node.parent = node.parent
    node.parent = rplc_node
    rplc_node.rightnode = node

    return rplc_node

#calcula altura y bf de los nodos  entre node y B.root
def update_bf(B, node):
    if node:
        if node.leftnode and node.rightnode:
            if node.leftnode.height > node.rightnode.height:
                node.height = node.leftnode.height + 1
            else:
                node.height = node.rightnode.height + 1

            node.balanceFactor = node.leftnode.height - node.rightnode.height

        elif node.leftnode:
            node.height = node.leftnode.height + 1

            node.balanceFactor = node.height

        elif node.rightnode:
            node.height = node.rightnode.height + 1

            node.balanceFactor = -node.height
        else:
            node.height = 0
            node.balanceFactor = 0
            
        #si el subarbol está desbalanceado se balancea con reBalance(), caso contrario se avanza hacia root.
        if node.balanceFactor < -1 or node.balanceFactor > 1:
            reBalance(B, node)
        else:
            update_bf(B, node.parent)

    return B


def reBalance(B, node):
    #temp = futura raiz del subarbol sobre el que se trabaja
    if node.balanceFactor < 0:
        temp = node.rightnode
        #caso especial en el que la rotacion no balancea
        if node.rightnode.balanceFactor > 0:
            temp = node.rightnode.leftnode
            rotateRight(B, node.rightnode)
            rotateLeft(B, node)
        else:
            rotateLeft(B, node)

    elif node.balanceFactor > 0:
        temp = node.leftnode
        #caso especial en el que la rotacion no balancea
        if node.leftnode.balanceFactor < 0:
            temp = node.leftnode.rightnode
            rotateLeft(B, node.leftnode)
            rotateRight(B, node)
        else:
            rotateRight(B, node)
    #Se actualizan bf y h despues del balanceo
    cll_upbf_leaves(B, temp)
    return B

#desde nodo temp de la operacion anterior se avanza a las raices y se actualiza bf y h
def cll_upbf_leaves(B, node):
    if is_leaf(node):
        update_bf(B, node)
        return

    if node.rightnode:
        cll_upbf_leaves(B, node.rightnode)
    else:
        cll_upbf_leaves(B, node.leftnode)


def rset_bf(node):
    node.height = 0
    node.balanceFactor = 0