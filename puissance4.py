import numpy as np

compteur_ligne = 6
compteur_colonne = 7

def creation_planche():
    planche = np.zeros((compteur_ligne,compteur_colonne))
    return planche

def affichage_piece(planche, ligne, colonne, piece):
    planche[ligne][colonne] = piece

def location_valide(planche, colonne):
    return planche[compteur_ligne-1][colonne] == 0

def prochaine_ligne(planche, colonne):
    for l in range(compteur_ligne):
        if planche[l][colonne] == 0:
            return l

def sens_planche(planche):
    print(np.flip(planche, 0))

def gagner(planche, piece):
    # Vérification horizontale
    for c in range(compteur_colonne-3):
        for l in range(compteur_ligne):
            if planche[l][c] == piece and planche[l][c+1] == piece and planche[l][c+2] == piece and planche[l][c+3] == piece:
                return True

    # Vérification verticale
    for c in range(compteur_colonne):
        for l in range(compteur_ligne-3):
            if planche[l][c] == piece and planche[l+1][c] == piece and planche[l+2][c] == piece and planche[l+3][c] == piece:
                return True

    # Vérification diagonale croissante
    for c in range(compteur_colonne-3):
        for l in range(compteur_ligne-3):
            if planche[l][c] == piece and planche[l+1][c+1] == piece and planche[l+2][c+2] == piece and planche[l+3][c+3] == piece:
                return True

    # Vérification diagonale décroissante
    for c in range(compteur_colonne-3):
        for l in range(3, compteur_ligne):
            if planche[l][c] == piece and planche[l-1][c+1] == piece and planche[l-2][c+2] == piece and planche[l-3][c+3] == piece:
                return True

planche = creation_planche()
sens_planche(planche)
fin = False
tour = 0

while not fin:
    # Appel Joueur 1
    if tour == 0:
        colonne = int(input("Joueur 1 sélection (0-6):"))
        if location_valide(planche, colonne):
            ligne = prochaine_ligne(planche, colonne)
            affichage_piece(planche, ligne, colonne, 1)

            if gagner(planche, 1):
                sens_planche(planche)
                print("Le joueur 1 a gagné !")
                fin = True
                break

    # Appel Joueur 2
    else:
        colonne = int(input("Joueur 2 sélection (0-6):"))
        if location_valide(planche, colonne):
            ligne = prochaine_ligne(planche, colonne)
            affichage_piece(planche, ligne, colonne, 2)

            if gagner(planche, 2):
                sens_planche(planche)
                print("Le joueur 2 a gagné !")
                fin = True
                break

    sens_planche(planche)

    tour += 1
    tour = tour % 2