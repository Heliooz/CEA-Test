## Exercice 2

import math

def solution (S):
    if(len(S) == 0 or len(S)%2 == 0): return -1
    ## Nombre de lettres à verifier de chaque coté
    size = math.floor(len(S)/2)
    # Index droit
    right = len(S)-1
    # Index gauche et incrémentation
    for x in range(size):
        # On vérifie la symetrie sinon on renvoie -1
        if(S[x] != S[right-x]): return -1
    # Si on arrive au centre on renvoie le nombre de lettre 
    return size