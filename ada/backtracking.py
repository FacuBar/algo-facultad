from mergesort import mergeSort
from algo1 import *

"""--Ejercicio 1"""
def darCambio(cambio, monedas):
    #La minima cantidad de monedas estará compuesta en la mayoría
    #de veces por monedas del mayor costo posible.
    mergeSort(monedas, inverse = True)
    t = temp()
    _darCambio(cambio, monedas, t)
    return t.t
#i es equivalente a la cantidad de monedas necesarias
def _darCambio(cambio, monedas, min, i = 1):
    if cambio < 0 or len(monedas) == 0:
        return None
    #Se llega a una solución
    if cambio == 0:
        return True

    for m in range(len(monedas)):
        cambio -= monedas[m]
        #Si se llega a un estado válido ...
        if cambio >= 0:
            #y la solución parcial no es prometedora ...
            if min.t != None:
                if i >= min.t:
                    #backtrack
                    cambio += monedas[m]
                    continue
            t = _darCambio(cambio, monedas, min, i = i + 1)
            if t: 
                if min.t == None:
                    min.t = i
                else:
                    if i < min.t:
                        min.t = i
        cambio += monedas[m]
        
    return False
"""--Ejercicio 1"""


"""--Ejercicio 2"""
def mochila(max, latas):
    tmp = Array(len(latas), 0)
    for i in range(len(latas)):
        tmp[i] = 0
    
    ans = temp()

    _mochila(max, latas, tmp, ans)
    return ans.t

def _mochila(max, latas, temp, ans):
    if max < 0 or len(latas) == 0:
        return None
    #Se llega a una solución ...
    if minPossible(max, temp, latas):
        #Se comprueba que sea la mejor hasta el momento//actualizar
        if ans.t == None:
            ar = Array(len(temp), 0)
            ans.t = ar
            copyAr(ans.t, temp)
        else:
            if weight(latas, ans.t) < weight(latas, temp):
                copyAr(ans.t, temp)
                
        return True

    for l in range(len(latas)):
        temp[l] += 1
        #estado válido
        if weight(latas, temp) <= max:
            _mochila(max, latas, temp, ans)
        #Backtrack
        temp[l] -= 1

    return False
#Se que no se pueda sumar otra lata a la mochila
def minPossible(v, temp, latas):
    v = v - weight(latas, temp)
    for i in range(len(latas)):
        if (v - latas[i]) > 0:
            return False
    
    return True
#Calcula el peso total de la mochila
def weight(latas, valores):
    total = 0

    for i in range(len(latas)):
        total += latas[i] * valores[i]

    return total
"""--Ejercicio 2"""


"""--Ejercicio 3"""
def subsecuenciaCreciente(nros):
    tmp = Array(len(nros), 0)
    t = temp()

    _sub(nros, t, tmp)
    #resize array
    ans = Array(lenShittyArray(t.t), 0)
    for i in range(len(ans)):
        ans[i] = t.t[i]

    return ans

def _sub(nros, max, temp, i = 0):
    if len(nros) == 0:
        return None
    #Solución//Se mantiene la mejor solución al momento
    if validSeq(temp, nros, i):
        if max.t == None:
            ar = Array(len(temp), 0)
            max.t = ar
            copyAr(max.t, temp)
            
        else:
            if lenShittyArray(temp) > lenShittyArray(max.t):
                copyAr(max.t, temp)
        return True

    for j in range(i, len(nros)):
        addShittyArray(temp, nros[j]) 
        if isAscending(temp):
            #Se llama dede el último elemento creciente encontrado.
            _sub(nros, max, temp, i = j+1)
        #backtrack
        delShittyArray(temp, nros[j])

    return False
#Se comprueba que ar sea efectivamente una solución al problema
def validSeq(ar, nros, i):
    if lenShittyArray(ar) == None or lenShittyArray(ar) == 0:
        return False

    temp = ar[lenShittyArray(ar) - 1]

    for l in range(i, len(nros)):
        if nros[l] > temp:
            return False

    return True
#shittyArray -> evitar resize constante de arrays
def lenShittyArray(ar):
    l = 0

    for i in range(len(ar)):
        if ar[i] == None or i == len(ar)-1:
            return l
        l += 1

    return None

def addShittyArray(ar, n):
    for i in range(len(ar)):
        if ar[i] == None:
            ar[i] = n
            return

def delShittyArray(ar, n):
    for i in range(len(ar)-1, -1, -1):
        if ar[i] == n:
            ar[i] = None
            return
#solución parcial valida
def isAscending(ar):
    for i in range(1, len(ar)):
        if ar[i] == None:
            break

        if ar[i-1] >= ar[i]:
            return False
    return True
"""--Ejercicio 3"""


"""--Ejercicio 4"""
def subconjuntoSuma(nros, v, i = 0):
    if len(nros) == 0 or v < 0:
        return None
    #Solución
    if v == 0:
        return True

    for j in range(i, len(nros)):
        v -= nros[i]
        if v >= 0:
            #Se llama dede el último elemento agregado.
            tmp = subconjuntoSuma(nros, v, i = j + 1)
            if tmp:
                return True
        #backtrack
        v += nros[i]

    return False
"""--Ejercicio 4"""


"""--Utilities"""
#Posibilitar paso por referencia
class temp:
    t = None
#Copia un array en otro
def copyAr(copy, ori):
    for i in range(len(ori)):
        copy[i] = ori[i]
    return
#shittyArray -> evitar resize constante de arrays
def lenShittyArray(ar):
    l = 0

    for i in range(len(ar)):
        if ar[i] == None or i == len(ar)-1:
            return l
        l += 1

    return None

def addShittyArray(ar, n):
    for i in range(len(ar)):
        if ar[i] == None:
            ar[i] = n
            return

def delShittyArray(ar, n):
    for i in range(len(ar)-1, -1, -1):
        if ar[i] == n:
            ar[i] = None
            return
"""--Utilities"""