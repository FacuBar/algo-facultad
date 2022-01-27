from algo1 import * 
from mergesort import mergeSort


"""--Ejercicio 12 """
def darCambio(cambio, monedas):
    ans =  Array(len(monedas), Array(cambio+1, 0))

    mergeSort(monedas)

    for i in range(len(monedas)):
        for j in range(cambio+1):
            _cambio(i, monedas, j, ans)

    return ans[len(monedas)-1][cambio]


def _cambio(i, monedas, cambio, D):
    if i == 0:
        D[0][cambio] = cambio
        return cambio
    elif cambio == 0:
        D[i][0] = 0
        return 0

    else:
        if monedas[i] <= cambio:
            k = cambio // monedas[i]
            resto = cambio - k*monedas[i]
            
            if resto == 0:
                D[i][cambio] = k
            else:
                temp = k + D[i-1][resto]

                if temp <= D[i-1][cambio]:
                    D[i][cambio] = temp
                else:
                    D[i][cambio] = D[i-1][cambio]
        else:
            D[i][cambio] = D[i-1][cambio]
        
        return D[i][cambio]
"""--Ejercicio 12 """


"""--Ejercicio 13 """
def sumsTo(ar, k):
    ans =  Array(len(ar), Array(k+1, 0))

    for i in range(len(ar)):
        for j in range(k+1):
            #Ya que se busca saber si existe una solución
            #y no la solución optima; una vez descubierta
            #se detiene la ejeución
            temp = _sumsTo(i, ar, j, ans)
            if temp: return True
            
    return False


def _sumsTo(i, ar, k, D):
    if i == 0:
        if ar[i] == k or k == 0:
            D[0][k] = 1
        else:
            D[0][k] = 0

    else:
        if ar[i] > k:
            D[i][k] = D[i-1][k]
        elif ar[i] < k:
            temp = k - ar[i]
            if D[i-1][temp] == 1:
                D[i][k] = 1
            else:
                D[i][k] = D[i-1][k]
        else:
            D[i][k] = 1

    if k  == len(D[0])-1:

        if D[i][k] == 1:
            return True
"""--Ejercicio 13 """


"""--Ejercicio 15 """
#Extraido de Cormen con pequeña modificación
#(ya no se hace uso de  2 tablas)
#devuelve un array que contiene la LCS
def LCS(st1, st2):
    ans = Array(len(st1)+1, Array(len(st2)+1, 0))

    for i in range(len(st1)+1):
        for j in range(len(st2)+1):
            if i == 0 or j == 0:
                ans[i][j] = 0
            else:
                if st1[i-1] == st2[j-1]:
                    ans[i][j] = ans[i-1][j-1] + 1
                
                elif ans[i-1][j] >= ans[i][j-1]:
                    
                    ans[i][j] = ans[i-1][j]
                else:
                    ans[i][j] = ans[i][j-1]
    
    sub = Array(ans[len(st1)][len(st2)], 'c')
    getLCS(ans, st1, len(st1), len(st2), sub)
    
    return sub

def getLCS(ans, st, i, j, sub):
    if i == 0 or j == 0:
        return
    if ans[i][j] == ans[i-1][j-1]+1:
        getLCS(ans, st, i-1, j-1, sub)
        add(sub, st[i-1])
    elif ans[i][j] == ans[i-1][j]:
        getLCS(ans, st, i-1, j, sub)
    else:
        getLCS(ans, st, i, j-1, sub)

def add(ar, c):
    for i in range(len(ar)):
        if ar[i] == None:
            ar[i] = c
            break
"""--Ejercicio 15 """
