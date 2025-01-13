import pygame
from pygame.locals import *
import random
import time
from questions import *
from graphique import *
from personnages import *

pygame.init()

# Créer les personnages
ecolier = Ecolier("Élève", "ecolier.png")
professeur_chimie = Professeur("Professeur de chimie", "profs.png", question_chimie)
professeur_geo = Professeur("Professeur de géographie", "profs.png", question_geo)
professeur_AV = Professeur("Professeur d'arts visuels", "profs.png",question_arts_visuels)
professeur_histoire = Professeur("Professeur d'histoire", "profs.png", question_histoire)
professeur_allemand = Professeur("Deutschlehrer", "profs.png", question_allemand)
les_profs = [professeur_chimie, professeur_geo, professeur_AV, professeur_histoire, professeur_allemand]
directeur = Directeur("Monsieur le Directeur", "directeur.png", 8 )

# Créer les couloirs incluant les images des salles
parcours = Parcours()
ecran = pygame.display.set_mode((parcours.longueur_fenetre, parcours.largeur_fenetre)) # Créer la fenêtre
pygame.display.set_caption("Score : " + str(ecolier.score_total) + " points") # Afficher le score initial

# Afficher le graphique
parcours.dessiner_structure(ecran, ecolier)
parcours.afficher_classes_profs(ecran, les_profs)
directeur.dessiner(ecran, parcours.taille_cellule)
parcours.afficher_consignes(ecran) # Afficher les consignes au départ dans un pop up

pygame.display.flip() # Éxécuter les affichages

en_cours = True # Pour commencer le jeu
while en_cours:
    direction = ecolier.capture_touche() # Capturer les événements et donne la direction du déplacement
    parcours.changer_position(ecran, direction, ecolier, les_profs, directeur) # Mettre à jour la position des personnages
    ecran.fill((0, 0, 0)) # Noir pour le fond et effacer l'écran avant de redessiner
    parcours.dessiner_structure(ecran, ecolier) # Redessiner le parcours et les éléments
    directeur.dessiner(ecran, parcours.taille_cellule)
    parcours.afficher_classes_profs(ecran, les_profs) # Dessiner les classes et les profs
    pygame.display.flip() # Rafraîchir l'écran

    # Vérifier la condition d'arrêt
    if direction == [0, 0]:
        en_cours = False

pygame.quit()
