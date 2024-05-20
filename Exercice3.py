## Exercice 3

def solution(A, B):
    # String à retourner 
    string = ""
    # Tant que l'on a pas utilisé toutes les lettres
    while ((A != 0) or (B!= 0)):
        # N'est pas censé arrivé mais utile pour les tests
        if((A < 0) or (B < 0)): return "Impossible"
        # Si il reste plus de "a" à placer
        if(A > B): 
            # Si les deux dernières lettres sont des "a" -> place un b
            if(string[-2:] == "aa"): 
                string = string + "b"
                B = B-1
            # Sinon -> place un a
            else: 
                string = string + "a"
                A = A-1
        # Sinon (B >= A)
        else: 
            # Si les deux dernières lettres sont des "b" -> place un a
            if(string[-2:] == "bb"): 
                string = string + "a"
                A = A-1
            # Sinon -> place un b
            else: 
                string = string + "b"
                B = B-1
    # Retourne la string créé
    return string