from algo1 import *

def mergeSort(arr, inverse = False):
    divide(arr, 0, len(arr) - 1, inverse)

def divide(arr, start, tail, inverse):
    if start < tail:
        med = (start + tail)//2

        divide(arr, start, med, inverse)
        divide(arr, med + 1, tail, inverse)

        merge(arr, start, med, tail, inverse)

def merge(arr, start, med, tail, inverse):
    l1, l2 = (med-start+1), (tail-med)
    left = Array(l1, 0)
    right = Array(l2, 0)

    for i in range(l1):
        left[i] = arr[start + i]
    for j in range(l2):
        right[j] = arr[med + 1 + j]

    i = j = 0
    k = start
    while i < l1 and j < l2:
        if inverse:
            comp = left[i] >= right[j]
        else:
            comp = left[i] <= right[j]
        
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