from linkedlist import LinkedList, add_toend

class BinaryTree:
    root = None

class BinaryTreeNode:
    key = None
    value = None
    leftnode = None
    rightnode = None
    parent = None


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
    new_node = BinaryTreeNode()
    new_node.value = element
    new_node.key = key
    #Si el arbol est'a vacio, se inserta el nuevo nodo como ra'iz
    if not B.root:
        B.root = new_node
        return key 
    #Se llama a la funci'on recursiva de la que esta es wrapper.
    return Insert(B.root, new_node)
#Se inserta el nuevo nodo en el arbol
def Insert(current_node, new_node):
    if new_node.key < current_node.key:
        if not current_node.leftnode:
            current_node.leftnode = new_node
            new_node.parent = current_node
            return new_node.key
        else:
            return Insert(current_node.leftnode, new_node)
    
    elif new_node.key > current_node.key:

        if not current_node.rightnode:
            current_node.rightnode = new_node
            new_node.parent = current_node
            return new_node.key
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
        return B.root.key

    return Delete(B.root, element)

def Delete(node, element):
    if not node: 
        return None
    
    if is_leaf(node) and node.value == element:
        node_p = node.parent
        if node_p.leftnode == node:
            node_p.leftnode = None
        else:
            node_p.rightnode = None
        return node.key

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

        return node.key
    #Si valores no coinciden, llamada recurs.
    else:
        temp = Delete(node.leftnode, element)
        if temp: return temp
        temp = Delete(node.rightnode, element)
        if temp: return temp

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
        print(' ' * 4 * level + '->', node.value)
        printTree(node.rightnode, level + 1)