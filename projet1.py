import pygame
from pygame.locals import *
import random
import time
from questions import *
from graphique import *
from personnages import *


pygame.init()

ecolier = Ecolier("Élève", "ecolier.png")
professeur_chimie = Professeur("Prof de chimie", "profs.png", question_chimie)
professeur_geo = Professeur("Prof de geo", "profs.png", question_geo)
professeur_aaaa = Professeur("Prof de aaa", "profs.png",question_aaaa)
professeur_bbbb = Professeur("Prof de bbb", "profs.png", question_bbbb)
professeur_cccc = Professeur("Prof de ccc", "profs.png", question_cccc)
les_profs = [professeur_chimie, professeur_geo, professeur_aaaa, professeur_bbbb, professeur_cccc]
directeur = Directeur("Monsieur le Directeur", "directeur.png", 8 )

parcours = Parcours()
ecran = pygame.display.set_mode((parcours.longueur_fenetre, parcours.largeur_fenetre))
direction = [0, 0]

pygame.display.set_caption("Utilisez les flèches pour vous déplacer.")
parcours.dessiner_tout(ecran, direction, ecolier, directeur, les_profs)

pygame.display.flip()

en_cours = True
while en_cours:
    direction = ecolier.capture_touche()
    parcours.changer_position(ecran, direction, ecolier, les_profs)
    parcours.dessiner_tout(ecran, direction, ecolier, directeur, les_profs)
    if direction == [0, 0]:
        en_cours = False
pygame.quit()
