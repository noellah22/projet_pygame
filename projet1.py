import pygame
from pygame.locals import *
import random
import time


# le but du jeu est de s'évader de l'école

class Personnage(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()  # Appel obligatoire
        self.image = pygame.image.load("perso.png").convert_alpha()
        self.image = pygame.transform.scale_by(self.image, 0.5)
        self.rect = self.image.get_rect()
        self.rect.x = LARGEUR / 2
        self.rect.y = HAUTEUR - 130
        self.vitesse = 8

    def bouger_droite(self):
        self.rect.x += self.vitesse

    def bouger_gauche(self):
        self.rect.x -= self.vitesse

    def reculer(self):
        self.rect.x -= self.vitesse

    def avancer(self):
        self.rect.x += self.vitesse


class EnnemiDirecteur(pygame.sprite.Sprite):  # les ennemis sont les profs
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("directeur.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 2

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > HAUTEUR:
            self.kill()


class ArmesCrayon(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("crayon.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 2

pygame.init()
LARGEUR = 600
HAUTEUR = 400
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
running = True
pygame.key.set_repeat(40, 30)

crayons = []
nombre = random.randint(1, 100)
ennemis = []

fond = pygame.image.load("background.png")
# Créer un nouveau sprite
fond = pygame.sprite.Sprite()
# Initialisation du sprite
pygame.sprite.Sprite.__init__(fond)
# Définir une image pour ce sprite
fond.image = pygame.image.load("background.png").convert()
# Permet à pygame de connaitre les dimensions de l’image
fond.rect = fond.image.get_rect()
# Coordonnées de l’image
fond.rect.x = 0
fond.rect.y = 0

pygame.init()
LARGEUR = 600
HAUTEUR = 600
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))


clock = pygame.time.Clock()
"""perso = Personnage()"""
liste_des_sprites = pygame.sprite.LayeredUpdates()
"""liste_des_sprites.add(perso)"""
pygame.key.set_repeat(40, 30)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_q:
                running = False
            elif event.key == K_a:
                perso.bouger_gauche()
            elif event.key == K_d:
                perso.bouger_droite()
            elif event.key == K_SPACE:
                pass
    for crayon in crayons:
        crayon.update()
        for ennemi in ennemis:
            if ennemi.rect.colliderect(crayon.rect):
                ennemis.remove(ennemi)
                crayons.remove(crayon)
                ennemi.kill()
                crayon.kill()

    fenetre.fill((0, 0, 0))
    liste_des_sprites.draw(fenetre)
    pygame.display.flip()
    clock.tick(60)  # Limite la boucle à 60 images par seconde

    nombre_aleatoire = random.randint(0, 100)
    if nombre_aleatoire == 0:
        position_x_aleatoire = random.randint(0, LARGEUR - 50)
        nouvel_ennemi = EnnemiDirecteur(position_x_aleatoire, -50)
        liste_des_sprites.add(nouvel_ennemi)
        ennemis.append(nouvel_ennemi)
    for ennemi in ennemis:
        ennemi.update()
pygame.quit()
