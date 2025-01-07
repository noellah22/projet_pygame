import pygame
from pygame.locals import *
import random
import time
from questions import *
from graphique import *
from personnages import *


pygame.init()

# Charger et redimensionner les images
image_av = pygame.transform.scale(pygame.image.load("classroom.png"), (150, 190))
image_chimie = pygame.transform.scale(pygame.image.load("classroom.png"), (150, 150))
image_geo = pygame.transform.scale(pygame.image.load("classroom.png"), (150,149))
image_allemand = pygame.transform.scale(pygame.image.load("classroom.png"), (267,148))
image_histoire = pygame.transform.scale(pygame.image.load("classroom.png"), (190,150))

# Créer les personnages
ecolier = Ecolier("Élève", "ecolier3.jpeg")
professeur_chimie = Professeur("Prof de chimie", "prof-2.png", question_chimie)
professeur_geo = Professeur("Prof de geo", "prof-2.png", question_geo)
professeur_aaaa = Professeur("Prof de aaa", "prof-2.png", question_aaaa)
professeur_bbbb = Professeur("Prof de bbb", "prof-2.png", question_bbbb)
professeur_cccc = Professeur("Prof de ccc", "prof-2.png", question_cccc)
les_profs = [professeur_chimie, professeur_geo, professeur_aaaa, professeur_bbbb, professeur_cccc]
directeur = Directeur("Monsieur le Directeur", "directeur.jpg", 8)

parcours = Parcours()
ecran = pygame.display.set_mode((parcours.longueur_fenetre, parcours.largeur_fenetre))
direction = [0, 0]

pygame.display.set_caption("Utilisez les flèches pour vous déplacer.")
parcours.dessiner_tout(ecran, direction, ecolier, directeur, les_profs)

# Positions des images
pos_av = (5, 203)
pos_chimie = (244, 204)
pos_geo =(485, 207)
pos_allemand =(367, 5)
pos_histoire =(85, 5)

pygame.display.flip()

en_cours = True
while en_cours:
    # Capturer les événements
    direction = ecolier.capture_touche()

    # Effacer l'écran avant de redessiner
    ecran.fill((0, 0, 0))  # Noir pour le fond

    # Redessiner le parcours et les éléments
    parcours.dessiner_tout(ecran, direction, ecolier, directeur, les_profs)

    # Dessiner les images supplémentaires
    ecran.blit(image_av, pos_av)
    ecran.blit(image_chimie, pos_chimie)
    ecran.blit(image_geo, pos_geo)
    ecran.blit(image_allemand, pos_allemand)
    ecran.blit(image_histoire, pos_histoire)

    # Mettre à jour la position des personnages
    parcours.changer_position(ecran, direction, ecolier, les_profs)

    # Rafraîchir l'écran
    pygame.display.flip()

    # Vérifier la condition d'arrêt
    if direction == [0, 0]:
        en_cours = False

pygame.quit()
