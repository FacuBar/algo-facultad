class RedBlackTree:
    root = None

class RedBlackNode:
    parent = None
    leftnode = None
    rightnode = None 
    key = None 
    value = None 
    color = None 

"""insert(RBTree, RBNode): Inserta nuevo nodo en el arbol"""
def insert(B, node):
    p = None		#parent de cn
    cn = B.root		#current_node
    #Se busca el lugar de insersion comprobando que este no esté ocup.
    while cn:
        p = cn

        if node.key < cn.key:
            cn = cn.leftnode
        elif node.key > cn.key:
            cn = cn.rightnode
        else:
            return B

    node.parent = p
    
    if not p:
        B.root = node 
    elif node.key < p.key:
        p.leftnode = node
    else:
        p.rightnode = node
    
    node.color = True
    fixup(B, node)
    
    return B
#Repara las violaciones a los axiomas RBT producidos por la insersion
def fixup(B, node):
    #Si el padre del nodo insertado es rojo, hay propiedades que no se cumplen
    while is_nill(node.parent):
        if node.parent == node.parent.parent.leftnode: 
            uncl = node.parent.parent.rightnode
            if is_nill(uncl):
                node.parent.color = False
                uncl.color = False
                node.parent.parent.color = True
                node = node.parent.parent
            else:
                if node == node.parent.rightnode:
                    node = node.parent
                    rotateLeft(B, node)
                node.parent.color = False
                node.parent.parent.color = True
                rotateRight(B, node.parent.parent)

        else:
            uncl = node.parent.parent.leftnode
            if is_nill(uncl):
                node.parent.color = False
                uncl.color = False
                node.parent.parent.color = True
                node = node.parent.parent
            else:
                if node == node.parent.leftnode:
                    node = node.parent
                    rotateRight(B, node)
                node.parent.color = False
                node.parent.parent.color = True
                rotateLeft(B, node.parent.parent)			

    B.root.color = False

"""-delete()- elimina d_node del arbol"""
def delete(B, d_node):
    tmp = d_node
    tmp_orig_color = tmp.color

    if not d_node.leftnode:
        x = d_node.rightnode
        #Si el padre de x no está completo, se completa con nodos NIL
        if not x:
            x = c_nil(d_node)
            d_node.rightnode = x
            if not d_node.leftnode:
                d_node.leftnode = x

        rb_transplant(B, d_node, d_node.rightnode)

    elif not d_node.rightnode:
        x = d_node.leftnode
        #Si el padre de x no está completo, se completa con nodos NIL
        if not x:
            x = c_nil(d_node)
            d_node.leftnode = x
            if not d_node.rightnode:
                d_node.rightnode = x

        rb_transplant(B, d_node, d_node.leftnode)

    else:
        tmp = fetch_min(d_node.rightnode)
        tmp_orig_color = tmp.color
        x = tmp.rightnode
        #Si el padre de x no está completo, se completa con nodos NIL
        if not x:
            x = c_nil(tmp)
            tmp.rightnode = x
            if not tmp.leftnode:
                tmp.leftnode = x

        if tmp.parent == d_node:
            x.parent = tmp

        else:
            rb_transplant(B, tmp, tmp.rightnode)
            tmp.rightnode = d_node.rightnode
            tmp.rightnode.parent = tmp 

        rb_transplant(B, d_node, tmp)
        tmp.leftnode = d_node.leftnode
        tmp.leftnode.parent = tmp
        tmp.color = d_node.color
    #Si el color eliminado es negro, hay que reajustar altura negra.
    if not tmp_orig_color:
        rb_delete_fixup(B,x)

    return B
#v toma el lugar de u
def rb_transplant(T, u, v):
    if not u.parent:
        T.root = v
    elif u == u.parent.leftnode:
        u.parent.leftnode = v 
    else:
        u.parent.rightnode = v

    if v:
        v.parent = u.parent
#se rebalancea la altura negra.
def rb_delete_fixup(T, x):
    #Se ejecuta mientras x no sea rojo-negro o raiz.
    while x != T.root and not x.color:
        if x == x.parent.leftnode:
            sib = x.parent.rightnode
            #Se completa sib con Nil
            if not sib.rightnode:
                sib.rightnode = c_nil(sib)
            if not sib.leftnode:
                sib.leftnode = c_nil(sib)

            if sib.color:
                sib.color = False
                sib.parent.color = True
                rotateLeft(T, x.parent)
                sib = x.parent.rightnode

            if not sib.leftnode.color and not sib.rightnode.color:
                sib.color = True
                x = x.parent
            else:
                if not sib.rightnode.color:
                    sib.leftnode.color = False
                    sib.color = True
                    rotateRight(T, sib)
                    sib = x.parent.rightnode
                
                sib.color = x.parent.color
                x.parent.color = False
                sib.rightnode.color = False
                rotateLeft(T, x.parent)
                x = T.root

        else:
            sib = x.parent.leftnode
            #Se completa sib con Nil
            if not sib.rightnode:
                sib.rightnode = c_nil(sib)
            if not sib.leftnode:
                sib.leftnode = c_nil(sib)

            if sib.color:
                sib.color = False
                sib.parent.color = True
                rotateRight(T, x.parent)
                sib = x.parent.leftnode
            
            if not sib.leftnode.color and not sib.rightnode.color:
                sib.color = True
                x = x.parent
            else:
                if not sib.leftnode.color:
                    sib.rightnode.color = False
                    sib.color = True
                    rotateLeft(T, sib)
                    sib = x.parent.leftnode
                
                sib.color = x.parent.color
                x.parent.color = False
                sib.leftnode.color = False
                rotateRight(T, x.parent)
                x = T.root
    x.color = False


"""--Utilities--"""
#Determina si un nodo es hoja o no
def is_leaf(node):
    #solo ocurre cuando rightnode y leftnode son None
    if node.rightnode == node.leftnode:
        return True
    else: 
        return False

#Imprime arbol
def printTree(node, level=0):
    if node != None and node.value != None:
        printTree(node.leftnode, level + 1)
        print(' ' * 4 * level + '->', node.value, color(node))
        printTree(node.rightnode, level + 1)

#Balancea un subarbol ladeado hacía la derecha
def rotateLeft(B, node):
    rplc_node = node.rightnode
    node.rightnode = rplc_node.leftnode

    if rplc_node.leftnode:
        rplc_node.leftnode.parent = node

    rplc_node.parent = node.parent

    if node.parent == None:
        B.root = rplc_node
    elif node == node.parent.leftnode:
        node.parent.leftnode = rplc_node
    else:
        node.parent.rightnode = rplc_node

    rplc_node.leftnode = node
    node.parent = rplc_node

    return rplc_node

#Balancea un subarbol ladeado hacía la izquierda
def rotateRight(B, node):
    rplc_node = node.leftnode
    node.leftnode = rplc_node.rightnode

    if rplc_node.rightnode:
        rplc_node.rightnode.parent = node

    rplc_node.parent = node.parent

    if node.parent == None:
        B.root = rplc_node
    elif node == node.parent.leftnode:
        node.parent.leftnode = rplc_node
    else:
        node.parent.rightnode = rplc_node

    rplc_node.rightnode = node
    node.parent = rplc_node

    return rplc_node

#Devuelve str que indica el color de un rbnode
def color(node):
    if node.color:
        return 'red'
    else:
        return 'black'

#Permite considerar los nodos None como si fueran Black
def is_nill(node):
    if node:
        return node.color
    return False

def fetch_min(node):
    cn = node
    while cn.leftnode:
        cn = cn.leftnode
    return cn

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
        return node

    if key > node.key:
        temp = Access(node.rightnode, key)
        if temp: return temp
    else: 
        temp = Access(node.leftnode, key)
        if temp: return temp

def c_nil(node):
    if node.key == None:
        return None
    
    nw = RedBlackNode()
    nw.parent = node
    return nw