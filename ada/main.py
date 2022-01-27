from algo1 import *
#from backtracking import *
from greedy import *
""" Backtracking

#Ejercicio 1
monedas = Array(5, 0)
monedas[0] = 1
monedas[1] = 2
monedas[2] = 10
monedas[3] = 8
monedas[4] = 6

print(darCambio(14, monedas))

monedas = Array(5, 0)
monedas[0] = 1
monedas[1] = 3
monedas[2] = 7
monedas[3] = 11
monedas[4] = 12

print(darCambio(20, monedas))


#Ejercicio 2
latas = Array(3, 0)
latas[0] = 7
latas[1] = 13
latas[2] = 2

print(mochila(34, latas))

#Ejercicio 3
sub = Array(10, 0)
sub[0] = 5
sub[1] = 1
sub[2] = 2
sub[3] = 3
sub[4] = 100
sub[5] = 20
sub[6] = 17
sub[7] = 8
sub[8] = 19
sub[9] = 21

print(subsecuenciaCreciente(sub))

#Ejercicio 4
X = Array(7)
X[0] = 8
X[1] = 6
X[2] = 7
X[3] = 5
X[4] = 3
X[5] = 10
X[6] = 9

print(subconjuntoSuma(X, 15))
"""


""" Greedy

#Ejercico 5

tareas = Array(9, tarea())


tareas[0] = tarea(1, 3, 1)
tareas[1] = tarea(2, 5, 2)
tareas[2] = tarea(4, 7, 3)
tareas[3] = tarea(1, 8, 4)
tareas[4] = tarea(5, 9, 5)
tareas[5] = tarea(8, 10, 6)
tareas[6] = tarea(9, 11, 7)
tareas[7] = tarea(11, 14, 8)
tareas[8] = tarea(13, 16, 9)

orgtar = adminActividades(tareas, 0, 17)

for i in range(len(orgtar)):
    print(f"t-{orgtar[i].id}", end=' ')
print('')


#Ejercicio 6

t = Array(6)
t[0] = 5
t[1] = 8
t[2] = 1
t[3] = 4
t[4] = 7
t[5] = 8

print(buscaPares(t))
"""

#ejercio 7

m = Array(3, lata())

m[0] = lata(9, 18, 1)
m[1] = lata(2, 4, 2)
m[2] = lata(3, 5, 3)

temp = mochila(152, m)

for i in range(len(temp)):
    print(f"lata {temp[i].id}: {temp[i].qtty}")

