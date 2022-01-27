class LinkedList:
    head = None

class Node:
    value = None
    nextNode = None
    prevNode = None
            
def add(list, element):
    new_node = Node()
    new_node.value = element
    
    list.head.prevNode = new_node
    new_node.nextNode = list.head

    list.head = new_node
    return
    
def search(list, element):
    if list.head == None:
        return None
    
    current_node = list.head
    while True:
        if current_node.value == element:
            return current_node
        # se llega al fin de la lista sin encontrar el elemento, se devuelve None
        if current_node.nextNode == None:
            return None
        current_node = current_node.nextNode

def insert(list, element, index):
    # index out of bounds, return None
    if index > length(list):
        return None

    if list.head == None:
        add(list, element)
        return 0

    new_node = Node()
    new_node.value = element
    
    current_node = list.head
    counter = 0
    while True:
        # si se desea insertar en la primer posic. se invoca add.
        if index == 0:
            add(list, element)
            return index
        elif index == counter:
        # se inserta el nuevo nodo enlazando como corresponde.
            current_node.prevNode.nextNode = new_node
            new_node.prevNode = current_node.prevNode
            new_node.nextNode = current_node
            return index
        counter += 1
        current_node = current_node.nextNode

def delete(list, element):
    if list.head == None:
        return None

    node = search(list, element)
    node.nextNode.prevNode = node.prevNode
    node.prevNode.nextNode = node.nextNode

def length(list):
    if list.head == None:
        return 0 

    current_node = list.head
    counter = 0
    
    while True:
        counter += 1
        current_node = current_node.nextNode
        if current_node == None:
            return counter

def access(list, index):
    if index >= length(list):
        return None

    current_node = list.head
    counter = 0
    while True:
        if counter == index:
            return current_node
        counter += 1
        current_node = current_node.nextNode

def update(list, element, index):
    node = access(list, index)
    if not node:
        return None

    node.value = element

def printlist(L, index = 0):

    list_len = length(L)

    if index == 0 or index >= list_len:
        index = list_len
    
    current_node = L.head
    for i in range(index):
        if current_node.nextNode:
            print(current_node.value,"->", end = " ")
        else: 
            print(current_node.value)
        current_node = current_node.nextNode

def add_toend(l, element):
    if l.head == None:
        add(l, element)
        return

    new_node = Node()
    new_node.value = element
    current_node = l.head 

    while current_node:
        if not current_node.nextNode: 
            current_node.nextNode = new_node
            new_node.prevNode = current_node
            return
        current_node = current_node.nextNode