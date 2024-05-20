## Exercice 1 

def solution (N):
    # Par défaut la solution est 0 car tout les entiers sont divible par 1
    answer = 0
    x = 1
    power_2 = 1
    # Tant qu'on ne dépasse pas N
    while (power_2 < N):
        # On calcule la puissance de 2 actuelle
        power_2 = 2**x
        # Si on tombe pile sur N on renvoit x
        if(power_2 == N): return x
        # Si la puissance de 2 divise N on met à jour "answer"
        if((N % power_2) == 0) : answer = x
        # Incrémentation
        x = x+1
    # On retourne "answer"
    return answer