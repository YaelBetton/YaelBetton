from labyrinthe import Labyrinthe
from TAD import Pile,File
from random import randint
laby = Labyrinthe(10,10)
laby.creer()
coordPM = str(randint(0,10))+ '_' +str(randint(0,10))#A completer (randint) !
coordf = '0_1'
stockage = ['0_1']
deja_visite = []


def recherche(coord):
    """Essaye tous les chemins jusqu'à ce que Pac Man trouve Blinky, il enregistre dans deja_visite les coordonnees ou il est deja passe,
        il enregistre dans stockage les coordonnes du bon chemin
        recherche('0_1') = 0_0
                           1_0
                           2_0
                           1_1
                           True
    """
    deja_visite.append(coord)
    tour = 0
    while coord != coordPM:
        x = autre_choix(coord) 
        if x != None:
            stockage.append(coord)
            deja_visite.append(coord)
            coord = x
            tour += 1
            print(coord)
        else :
            deja_visite.append(coord)
            z = stockage.pop()
            coord = z
            
    return True
    
def possibilite(coordoneeF):
    """ Trouve la/les possibilitées que une coordonnées as pour avancer d'une case vers une autre
        possibilite('0_1') = ['0_2', '0_0', '1_1']"""
    poss = []
    if laby.lire_graphe()[coordoneeF]['N'] != None:
        if stockage[-1] != laby.lire_graphe()[coordoneeF]['N']:
            poss.append(laby.lire_graphe()[coordoneeF]['N'])
    if laby.lire_graphe()[coordoneeF]['S'] != None:
        if stockage[-1] != laby.lire_graphe()[coordoneeF]['S']:
            poss.append(laby.lire_graphe()[coordoneeF]['S'])
    if laby.lire_graphe()[coordoneeF]['E'] != None:
        if stockage[-1] != laby.lire_graphe()[coordoneeF]['E']:
            poss.append(laby.lire_graphe()[coordoneeF]['E'])
    if laby.lire_graphe()[coordoneeF]['O'] != None:
        if stockage[-1] != laby.lire_graphe()[coordoneeF]['O']:
            poss.append(laby.lire_graphe()[coordoneeF]['O'])
    return poss


def autre_choix(coord):
    """ Cette fonction renvoie les autres possbilités de la case demandé
        autre_choix('0_1') = '1_1'
    """
    p = possibilite(coord)
    for v in p:
        if v not in deja_visite:
            return v
    return None

        
        
def PM_trouve(coord):
    """ Affiche le chemin de Blinky pour trouver Pac Man est vérifie si il l'a trouvé ou non
        PM_trouve('0_1') = 0_2
                           0_3
                           1_2
                           1_1
                           Trouvé
    """
    if recherche(coord) == True:
        print('Trouvé')
    else:
        print('Pas trouvé')





