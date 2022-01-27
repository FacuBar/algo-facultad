from algo1 import *
from linkedlist import *
from mergesort import mergeSort

"""--Ejercicio 5"""
class tarea:
    def __init__(self, inic=None, fin=None, id=None):
        self.inic = inic
        self.fin = fin
        self.id = id

def adminActividades(tareas, inicio, fin):
    if len(tareas) == 0 or fin < inicio:
        return None
    #Respuesta
    ans = Array(len(tareas), tarea())

    while len(tareas) != 0 and not isAns(tareas, inicio):
        tareas = delInv(tareas, inicio, fin)
        temp = select(tareas)
        addShittyArray(ans, temp)
        inicio = temp.fin
    #Transición de shittyarray a array
    temp = Array(lenShittyArray(ans), tarea())
    for i in range(len(temp)):
        temp[i] = ans[i]
    ans = temp

    return ans
#Devuelve la tarea que empieza primero
def select(tareas):
    min = tareas[0]
    for i in range(len(tareas)):
        if tareas[i].fin < min.fin:
            min = tareas[i]

    return min
#Comprueba que dentro de tareas no quede ninguna tarea
#que pueda sumarse a la solución
def isAns(tareas, inicio):
    for i in range(len(tareas)):
        if tareas[i].inic >= inicio:
            return False

    return True
#Elimina aquellas tareas que no cumplan con los parametros deseados
def delInv(tareas, inicio, fin):
    for i in range(len(tareas)):
        if tareas[i].inic < inicio or tareas[i].fin > fin:
            tareas[i] = None

    newAr = Array(lenShittyArray(tareas), tarea())
    j = 0
    for i in range(len(tareas)):
        if tareas[i] != None:
            newAr[j] = tareas[i]
            j += 1

    return newAr
"""--Ejercicio 5"""


"""--Ejercicio 6"""
#El mejor resultado posible se va a obtener sumando
#los elementos opuestos en un array ordenado
def buscaPares(vector):
    if len(vector) % 2 != 0:
        return None

    mergeSort(vector)
    max = 0

    for i in range(len(vector)//2):
        temp = vector[i] + vector[len(vector)-1 - i]
        if temp > max:
            max = temp

    return max
"""--Ejercicio 6"""


"""--Ejercicio 7"""
class lata:
    def __init__(self, weight=None, benef=None, id=None):
        self.weight = weight
        self.benef = benef
        self.id = id
        if weight != None:
            self.ef = benef/weight
        self.qtty = 0

def mochila(max, latas):
    if len(latas) == 0:
        return None

    mergeSort_latas(latas)

    ans = Array(len(latas), lata())

    while len(latas) != 0:
        latas = delInv_latas(latas, max)
        temp = select_latas(latas, max)
        if temp:
            addShittyArray(ans, temp)
            max -= temp.weight*temp.qtty
    #Convierte shittyarray en array
    temp = Array(lenShittyArray(ans), lata())
    for i in range(len(temp)):
        temp[i] = ans[i]
    ans = temp

    return ans
#Devuelve la cantidad de una lata 
#que maximice la eficiencia (beneficio/peso)
def select_latas(latas, max):
    if len(latas) == 0:
        return None
    temp = max//latas[0].weight
    latas[0].qtty = temp

    return latas[0]
#Elimina las latas que no cumplan con los parametrosss requeridos
def delInv_latas(latas, max):
    for i in range(len(latas)):
        if latas[i].weight > max:
            latas[i] = None

    newAr = Array(lenShittyArray(latas), lata())
    j = 0
    for i in range(len(latas)):
        if latas[i] != None:
            newAr[j] = latas[i]
            j += 1

    return newAr
#Determina si la respuesta es definitiva 
#no hay ninguna lata que pueda incluirse en la soluc.
def isAnsLatas(max, ans, latas):
    max = max - weight(ans)
    for i in range(len(latas)):
        if (max - latas[i].weight) > 0:
            return False
    
    return True
#Calcula el peso total de las latas en la mochila
def weight(latas):
    total = 0
    for i in range(lenShittyArray(latas)):
        total += latas[i].weight * latas[i].qtty

    return total

#Ordena latas según eficiencia (ben/peso)
def mergeSort_latas(arr, inverse = True):
    divide_latas(arr, 0, len(arr) - 1, inverse)

def divide_latas(arr, start, tail, inverse):
    if start < tail:
        med = (start + tail)//2

        divide_latas(arr, start, med, inverse)
        divide_latas(arr, med + 1, tail, inverse)

        merge_latas(arr, start, med, tail, inverse)

def merge_latas(arr, start, med, tail, inverse):
    l1, l2 = (med-start+1), (tail-med)
    left = Array(l1, lata())
    right = Array(l2, lata())

    for i in range(l1):
        left[i] = arr[start + i]
    for j in range(l2):
        right[j] = arr[med + 1 + j]

    i = j = 0
    k = start
    while i < l1 and j < l2:
        if inverse:
            comp = left[i].ef >= right[j].ef
        else:
            comp = left[i].ef <= right[j].ef
        
        if comp:
                arr[k] = left[i]
                i += 1

        else:
            arr[k] = right[j]
            j += 1
        k += 1
    
    while i<l1:
        arr[k] = left[i]
        i += 1
        k += 1

    while j<l2:
        arr[k] = right[j]
        j+=1
        k+=1 
"""--Ejercicio 7"""


"""--Utilities"""
#ShittyArray -> evitar resize de arrays
def lenShittyArray(ar):
    l = 0

    for i in range(len(ar)):
        if ar[i] != None:
            l += 1
    
    return l

def addShittyArray(ar, n):
    for i in range(len(ar)):
        if ar[i] == None:
            ar[i] = n
            return
"""--Utilities"""