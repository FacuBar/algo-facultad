from algo1 import Array
from math import floor
#-Modificable-#
SIZE = 1000
A = (5**(0.5)-1)/2

class dictionary:
    head = None

class dictionaryNode:
    value = None
    key = None
    nextNode = None
    prevNode = None

#-Modificable-#
def hash_function(k):
    return floor(SIZE * (k*A % 1))


def insert(D, k, v):
    i = hash_function(k)
    if not D.head:
        D.head = Array(SIZE, dictionaryNode())

    if D.head[i] == None:
        new_node = _new_node(k, v)

        D.head[i] = new_node
    else:
        new_node = _new_node(k, v)
        new_node.nextNode = D.head[i]
        new_node.nextNode.prevNode = new_node
     
        D.head[i] = new_node

    return D 

def _new_node(k, v):
    new_node = dictionaryNode()
    new_node.key = k
    new_node.value = v
    
    return new_node


def search(D,  k):
    if not D.head:
        return None

    i = hash_function(k)

    if D.head[i] == None:
        return None
    else:
        temp = _search(D.head[i], k)
        if temp: 
            return k
        return False
        
def _search(node, k):
    if node == None:
        return False

    if node.key == k:
        return node
    else:
        return _search(node.nextNode, k)


def delete(D, k):
    if not D.head:
        return False

    i = hash_function(k)

    node = _search(D.head[i], k)
    if node:
        if node.prevNode == None:
            D.head[i] = node.nextNode
        else:
            if node.nextNode:
                node.nextNode.prevNode = node.prevNode
            node.prevNode.nextNode = node.nextNode
            
        return k

    return False
