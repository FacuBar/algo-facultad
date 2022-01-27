from algo1 import *
#Todas las operaciones son no sensitivas -Ej9

#Ejercicio1
def existChar(s, c):
    c = toUpper(c)

    for i in range(len(s)):
        if toUpper(s[i]) == c:
            return True

    return False

#Ejercicio2
def isPalindrome(s):
    len_s =  len(s)

    for i in range(len_s):
        j = len_s - i

        if toUpper(s[i]) != toUpper(s[j]):
            return False

    return True

#Ejercicio3
def mostRepeatedChar(s):
    max = 0
    counter = Array(26, 0)

    for i in range(len(s)):
        #Indice del caracter dentro del array contador
        temp = ord(toUpper(s[i])) - ord('A')
        counter[temp] += 1
        #Si se encuentra un nuevo caracter más repetido
        if counter[temp] > counter[max]:
            #Se guarda su indice dentro del array contador
            max = temp
    
    return chr(max + ord('A'))

#Ejercicio 4
def getBiggestIslandLen(s):
    temp = 0
    max = 0
    len_s = len(s)

    for i in range(len_s - 1):
        if toUpper(s[i]) == toUpper(s[i+1]):
            temp += 1
    
        else:
            if temp > max:
                max = temp
            temp = 0
            #Evitar recorrer toda la string de no ser nec.
            if max > (len_s - i):
                break
        
    return max

#Ejercicio 5 
#Que 2 palabras sean anagramas significa que ambas palabras son permutaciones
#de un mismo conjunto de caracteres.
#Se va a comprobar que las 2 palabras sean permutaciones de un mismo conjunto.
def isAnagram(s1, s2):
    if len(s1) != len(s2):
        return False
    counter = Array(26, 0)
    #Se contabilizan los caracteres de s1
    for i in len(s1):
        counter[ord(toUpper(s1[i])) - ord('A')] += 1
    #Se comprueba que los caracteres presentes en s1 sean iguales a los de s2
    for i in len(s2):
        temp = ord(toUpper(s2[i])) - ord('A')
        counter[temp] -= 1
        #Si el conjunto de caracteres no coincide, no son anagramas.
        if counter[temp] < 0:
            return False
    
    return True

#Ejercicio 6
#Para que los parentesis estén balanceados se debe verificar lo siguiente:
#(1)La cantidad de parentesis deben ser iguales
#(2)Los parentesis deben estar ordenados(deben encapsular correctm)
def verifyBalancedParentheses(s):
    balance = 0

    for i in range(len(s)):
        if s[i] == '(':
            balance += 1
        elif s[i] == ')':
            balance -= 1
        #Con esto se verifica (2)
        if balance < 0:
            return False
    #Con esto se verifica (1)
    if balance != 0:
        return False

    return True

#Ejercicio7
def reduceLen(s):
    new_s = String('')
    last = None
    pair = False
    #útil para casos especiales por trabajar con pares de elem
    if len(s) % 2 == 0:
        pair = True

    for i in range(0, len(s), 2):
        #Si en el útlimo ciclo se encontraron pares repetidos ...
        if last == None:
            #Caso especial último chr.
            if not pair and i == len(s) - 1:
                new_s = concat(new_s, String(s[i]))
                break
            #Si no hay par de chr repetidos ...
            if toUpper(s[i]) != toUpper(s[i+1]):
                #Se agrega el primer elemento del par a la string
                new_s = concat(new_s, String(s[i]))
                #Se guarda el último elemento del par para el prox. ciclo
                last = s[i+1]
            #Si hay par de elementos repetidos se eliminan
            else:
                #Y se marca que se encontró par para el prox ciclo
                last = None
        #Si no... Se trabaja con el último elemento del par anterior.
        else:
            #Caso especial último chr.
            if not pair and i == len(s) - 1:
                if toUpper(s[i]) != toUpper(last):
                    new_s = concat(new_s, String(last))
                    new_s = concat(new_s, String(s[i]))
            #Si el anterior y el primer chr del nuevo par no coinciden ...
            if toUpper(s[i]) != toUpper(last):
                #Se agrega el chr anterior a la str
                new_s = concat(new_s, String(last))
                #Y se compara el nuevo par
                if toUpper(s[i]) != toUpper(s[i+1]):
                    new_s = concat(new_s, String(s[i]))
                    last = s[i+1]
                else:
                    last = None
            #Si coinciden, se eliminan y se guarda el chr para el proximo ciclo
            else:
                last = s[i+1]
    
    return new_s

#Ejercicio8
#Se checkea que los caracteres de s1 se encuentren ordenados
#dentro de s2, no necesariamente consecutivamente.
def isContained(s1, s2):
    if len(s2) > len(s1):
        return False
    
    l_s2 = len(s2)
    j = 0

    for i in range(len(s1)):
        if toUpper(s1[i]) == toUpper(s2[j]):
            j += 1
            
        if j == l_s2:
            return True

    return False

#Ejercico9
#substr() : AHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH
#Podría utilizarse un RabinKarp para las comparaciones de cada 'isla' #Lazy
def isPatternContained(s1, s2, c):
    #Se obtienen todas las islas de s1
    s1 = fetchIsles(s1, c)
    j = i = 0

    while i < len(s2):
        isle = s1[j]
        #Si toda isla de s1, está ordenada en s2, se cumple lo pedido
        if isle == None:
            return True

        if i + len(isle) > len(s2):
            break

        temp = substr(s2, i, i + len(isle))

        if strcmp(isle, temp):
            j += 1
            i += len(isle)
            continue

        i += 1

    if s1[j] == None:
        return True
    return False
#Se separan las subcadenas cuyos caracteres debes ser contiguos
def fetchIsles(s1, c):
    isles = Array(len(s1), String(''))
    
    last_isle = 0
    j=0 
    for i in range(len(s1)):
        if s1[i] == c:
            isles[j] = substr(s1, last_isle, i)
            last_isle = i+1
            j += 1

        elif i == len(s1) - 1:
            isles[j] = substr(s1, last_isle, i+1)

    return isles


"""-Utilities-"""
def toUpper(c):
    if ord(c) > 91:
        c = chr(ord(c) - 32)
    return c