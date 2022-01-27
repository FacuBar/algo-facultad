from algo1 import *

"""--Ejercicio 8"""
def busquedaBinaria(ar, x):
    t = _bSearch(ar, x, 0, len(ar)-1)
    if t: return True
    else: return False


def _bSearch(ar, x, i, j): 
    k = i + (j-i)//2

    if k == i or k == j:
        if ar[i] == x or ar[j] == x:
            return True
        else:
            return False

    if ar[k] < x:
        temp = _bSearch(ar, x, k+1, j)
    elif ar[k] > x:
        temp = _bSearch(ar, x, i, k-1)
    else: 
        return True

    if temp: return True
"""--Ejercicio 8"""


"""--Ejercicio 9"""
def busquedaKesimo(ar, k):
    if k > len(ar):
        return None

    return _bKesimo(ar, 0, len(ar)-1, k-1)


def _bKesimo(ar, st, end, k):
    if st >= end:
        if st == k:
            return ar[k]
        return None

    pivot = divide(ar, st, end)

    if k == pivot:
        return ar[k]
    elif k > pivot:
        temp = _bKesimo(ar, pivot+1, end, k)
    else:
        temp = _bKesimo(ar,st, pivot-1, k)

    if temp: return temp
    

def divide(ar, st, end):
    pivot = selectPivot(ar, st+1, end)
    index = i = st

    while i != pivot:
        if ar[i] <= ar[pivot]:
            ar[index], ar[i] = ar[i], ar[index]
            index += 1
        
        i += 1

    ar[index], ar[pivot] = ar[pivot], ar[index]
    return index

#Devuelve la mediana del arr [princ,med,final]
def selectPivot(ar, st, end):
    if end-st <= 1:
        return end

    med = (st + end)//2

    if (ar[st] > ar[end]) ^ (ar[st] > ar[med]):
        return st
    elif (ar[med] > ar[st]) ^ (ar[med] > ar[end]):
        return med
    else:
        return  end
"""--Ejercicio 9"""


"""--Ejercicio 11"""

"""--Ejercicio 11"""

