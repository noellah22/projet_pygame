import pygame
from pygame.locals import *
import random
import time
from questions import *
from graphique import *
from personnages import *

pygame.init()
ecolier = Ecolier("Élève", "ecolier3.jpeg")
professeur_chimie = Professeur("Prof de chimie", "directeur.png", questions_profs[1])
parcours = Parcours()
ecran = pygame.display.set_mode((parcours.longueur_fenetre, parcours.largeur_fenetre))
pygame.display.set_caption("Utilisez les flèches pour vous déplacer.")
direction = [0, 0]
parcours.dessiner_tout(ecran, direction, ecolier)
professeur_chimie.dessiner(ecran, 40)
pygame.display.flip()
en_cours = True
while en_cours:
    direction = ecolier.capture_touche()
    parcours.changer_position(ecran, direction, ecolier)
    parcours.dessiner_tout(ecran, direction, ecolier)
    if direction == [0, 0]:
        en_cours = False
    #clock.tick(30)
pygame.quit()
