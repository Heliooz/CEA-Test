## Exercice 5

# Solution 1
# Version recursive fonctionnant sur le principe d'un parcours en profondeur -> 73%
# Erreur à la recursion quand la matrice est trop grande

from queue import Queue

# Définition d'une liste
a_parcourir = Queue()

def parcourir(A, x, y):
    # On récupère la couleur
    color = A[x][y]
    # Si la couleur est -1 on a déjà parcouru cette casse donc on retourne 0
    if(color == -1):
        return 0
    # On change la valeur de la case à -1
    A[x][y] = -1
    len_x = len(A) - 1
    len_y = len(A[0]) - 1
    # Pour les 4 cases adjacente on regarde si elle appartient au meme pays, si c'est le cas on les parcours récursivement 
    # Sinon on l'ajoute dans la queue des pays à parcourir
    if(y < len_y):
        if(A[x][y+1] == color):
            parcourir(A, x, y+1)
        elif(A[x][y+1] != -1) :
            a_parcourir.put((x, y+1))
    if(x < len_x):        
        if(A[x+1][y] == color):
            parcourir(A, x+1, y)
        elif (A[x+1][y] != -1): 
            a_parcourir.put((x+1, y))
    if(y > 0):
            if(A[x][y-1] == color):
                parcourir(A, x, y-1)
            elif (A[x][y-1] != -1):
                a_parcourir.put((x, y-1))
    if(x > 0):
            if(A[x-1][y] == color):
                parcourir(A, x-1, y)
            elif (A[x-1][y] != -1):
                a_parcourir.put((x-1, y))
    # Lorsque l'on a fini de parcourir le pays on renvoie 1
    return 1

def solution(A):
    a_parcourir = Queue()
    # On ajoute la première case à la liste des cases à parcourir
    a_parcourir.put((0, 0))
    # On initialise le décompte des pays
    decompte_pays = 0
    # Tant qu'il reste des cases à explorer
    while(not a_parcourir.empty()):
        # On récupère les index
        x, y = a_parcourir.get()
        # Si le pays n'est pas déjà exploré
        if(A[x] [y] != -1):
            # On parcours le pays 
            pays = parcourir(A, x, y)
            decompte_pays += pays
    return decompte_pays

# Solution 2 
# Version itterative du parcours en profondeur ci-dessus -> 80%

def check_around(A, x, y, len_x, len_y, color):
    new_cases = []
    # On met à jour la valeur de la case actuelle
    A[x][y] = -1
    # On regarde autour pour trouver des cases du pays
    if((y < len_y) and (A[x][y+1] == color)):
        new_cases.append((x, y+1))
    if((x < len_x) and (A[x+1][y] == color)):        
        new_cases.append((x+1, y))
    if((y > 0) and (A[x][y-1] == color)):
        new_cases.append((x, y-1))
    if((x > 0) and (A[x-1][y] == color)):
        new_cases.append((x-1, y))
    return new_cases

def explore_country(A, x, y, len_x, len_y):
    # On enregistre la couleur du pays
    color = A[x][y]
    # On initialise le pays
    country_size = 1
    # On explore à partir de la première case
    to_explore_country = check_around(A, x, y, len_x, len_y, color)
    # On explore tant que l'on a pas parcouru le pays entier
    while(len(to_explore_country) != 0):
        # On récupère la première case à explorer
        cur_x, cur_y = to_explore_country[0]
        # On la supprime de l'index
        to_explore_country.remove((cur_x, cur_y))
        # On ajoute 1 à la taille du pays
        country_size += 1
        # On regarde autour puis on ajoute les cases dans celles a explorer
        new_cases = check_around(A, cur_x, cur_y, len_x, len_y, color)
        to_explore_country.extend(new_cases)
    return country_size


def solution(A):
    # On initialise les compteurs et la taille du tableau
    country_count = 0
    cases_count = 0
    len_x = len(A) - 1
    len_y = len(A[0]) - 1
    # On parcours le tableau
    for cur_x in range(0, len_x+1):
        for cur_y in range(0, len_y+1):
            # Si la case n'a pas encore été explorée
            if(A[cur_x][cur_y] != -1):
                # On l'explore puis on ajoute 1 au nombre de pays
                country_size = explore_country(A, cur_x, cur_y, len_x, len_y)
                country_count += 1
                # On décompte le nombre de case parcouru pour le debug
                cases_count += country_size
    return country_count

# https://github.com/andrs/codility/blob/master/CountCountries.java
# Implémentation d'une solution existante pour comparaison -> 86%

def is_inbound(x, y):
    return (x >= 0) and (y >= 0)

def get_neighbours(A, x, y):
    neighbours =  [-1] * 3
    if(is_inbound(x-1, y-1)): neighbours[0] = A[x-1][y-1]
    if(is_inbound(x, y-1)): neighbours[1] = A[x][y-1]
    if(is_inbound(x-1, y)): neighbours[2] = A[x-1][y]
    return neighbours

def check_around(A, x, y):
    color = A[x][y]
    country = 0
    neighbours = get_neighbours(A, x, y)
    if((neighbours[0] != color) and (neighbours[1] == color) and (neighbours[2] == color)): country -= 1
    if((neighbours[1] != color) and (neighbours[2] != color)): country += 1

    return country

def solution(A):
    len_x = len(A)
    len_y = len(A[0])
    country_count = 0
    for x in range(0, len_x):
        for y in range(0, len_y):
            country = check_around(A, x, y)
            country_count += country
    return country_count