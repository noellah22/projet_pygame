import pygame
from pygame.locals import *
import random

# le but du jeu est de s'évader de l'école

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

class EnnemiDirecteur(pygame.sprite.Sprite): # les ennemis sont les profs
    def __init__(self, x, y):
       super().__init__()
       self.image = pygame.image.load("directeur.jpeg").convert_alpha()
       self.rect = self.image.get_rect()
       self.rect.x = x
       self.rect.y = y
       self.speed = 2
    def update(self):
       self.rect.y += self.speed
       if self.rect.top > HAUTEUR:
           self.kill()


crayons = []
nombre = random.randint(1, 100)
ennemis = []


pygame.init()
LARGEUR = 600
HAUTEUR = 600
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
clock = pygame.time.Clock()
perso = Personnage()
liste_des_sprites = pygame.sprite.LayeredUpdates()
liste_des_sprites.add(perso)
running = True
pygame.key.set_repeat(40, 30)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           running = False
        if event.type == KEYDOWN:
           if event.key == K_a:
               perso.bouger_gauche()
           if event.key == K_d:
               perso.bouger_droite()
           if event.key == K_SPACE:
               nouveau_crayon = Crayon(crayon.rect.x + 10, crayon.rect.y - 10)
               crayon.append(nouveau_crayon)
               liste_des_sprites.add(nouveau_crayon)
    for crayon in crayons:
        crayon.update()
        for ennemi in ennemis:
            if ennemi.rect.colliderect(crayon.rect):
                ennemis.remove(ennemi)
                crayons.remove(crayon)
                ennemi.kill()
                crayon.kill()
    fenetre.fill((0,0,0))
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