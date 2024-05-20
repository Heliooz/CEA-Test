## Exercice 4

import math

# https://www.geeksforgeeks.org/python-program-for-quicksort/

# Function to find the partition position
def partition(array, low, high):

    # choose the rightmost element as pivot
    pivot = array[high]

    # pointer for greater element
    i = low - 1

    # traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:

            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1

            # Swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])

    # Swap the pivot element with the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])

    # Return the position from where partition is done
    return i + 1

# function to perform quicksort


def quickSort(array, low, high):
    if low < high:

        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, low, high)

        # Recursive call on the left of pivot
        quickSort(array, low, pi - 1)

        # Recursive call on the right of pivot
        quickSort(array, pi + 1, high)


def solution(A):
    length = len(A)
    # Tri le tableau en ordre croissant
    quickSort(A, 0, length-1)
    # definir les indexs
    left_index = 0
    right_index = length - 1
    # definir la meilleure valeur
    best_value = math.inf
    # Vu que l'on tri notre liste on peut être sur que la solution sera un nombre négatif + un nombre positif ou 2 x le plus petit nombre (en valeur absolue)
    # On peut donc partir de l'exterieur vers l'interieur afin que nos 2 index se retrouvent sur la valeur absolue la plus faible
    # Tant que nos index ne se croisent pas 
    while(left_index <= right_index):
        # On calcule la valeur de la somme à nos index 
        current_value = abs(A[left_index] + A[right_index])
        # On remplace si elle est meilleure que notre valeur actuelle
        if(best_value > current_value): best_value = current_value
        # Si la valeur est 0, on peut directement retourner 
        if(best_value == 0): return best_value
        # On deplace l'index de la valeur absolue la plus elevé vers le centre
        if(abs(A[left_index]) > abs(A[right_index])): left_index += 1
        else: right_index -= 1
    return best_value