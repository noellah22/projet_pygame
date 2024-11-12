import pygame
from pygame.locals import *
import random

# le but du jeu est de sévader de l'école

class Personnage(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() #Appel obligatoire
        self.image = pygame.image.load("perso.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = LARGEUR/2
        self.rect.y = HAUTEUR-70
        self.vitesse = 8
    def bouger_droite(self):
        self.rect.x += self.vitesse
    def bouger_gauche(self):
        self.rect.x -= self.vitesse
    def reculer(self):
        self.rect.x -= self.vitesse
    def avancer(self):
        self.rect.x += self.vitesse

class Armes(pygame.sprite.Sprite):
    def __init__(self, x, y):
       super().__init__()
       self.image = pygame.image.load("crayon.png").convert_alpha()
       self.rect = self.image.get_rect()
       self.rect.x = x
       self.rect.y = y
       self.speed = 2

class Crayon(Armes): # contre prof de français
    def __init__(self, x, y):
       super().__init__()

class Compas(Armes): # contre prof de maths
    def __init__(self, x, y):
       super().__init__()

class Dictionnaire(Armes): # contre tous
    def __init__(self, x, y):
       super().__init__()

class Bécher(Armes): # contre prof de chimie
    def __init__(self, x, y):
       super().__init__()

class Ennemi(pygame.sprite.Sprite): # les ennemis sont les profs
    def __init__(self, x, y):
       super().__init__()
       self.image = pygame.image.load("ennemi1.png").convert_alpha()
       self.rect = self.image.get_rect()
       self.rect.x = x
       self.rect.y = y
       self.speed = 2
    def update(self):
       self.rect.y += self.speed
       if self.rect.top > HAUTEUR:
           self.kill()

class ProfMaths(Ennemi):
    def __init__(self, x, y):
       super().__init__()

class ProfChimie(Ennemi):
    def __init__(self, x, y):
        super().__init__()

class ProfSport(Ennemi):
    def __init__(self, x, y):
        super().__init__()

class ProfFrancais(Ennemi):
    def __init__(self, x, y):
        super().__init__()

class Directeur(Ennemi): # c'est le boss de fin du jeu
    def __init__(self, x, y):
        super().__init__()

class ProfAV(Ennemi):
    def __init__(self, x, y):
        super().__init__()

class ProfGeo(Ennemi):
    def __init__(self, x, y):
        super().__init__()

class ProfInfo(Ennemi):
    def __init__(self, x, y):
        super().__init__()
