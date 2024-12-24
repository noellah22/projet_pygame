import pygame
from pygame.locals import *
import random
import time
from datetime import timedelta
from questions import *

# La classe Parcours décrit un chemin à emprunter. 0 indique le couloir sur lequel on peut passer.
# 1 indique un emplacement où il y a un bâtiment (là où l'on peut pas passer)
class Parcours:
    def __init__(self):
        self.couloir = [
                        [0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1],
                        [0, 0, 1, 1, 1, 1, 1, 0, 0, 2, 1, 1, 1, 1, 1, 1],
                        [0, 0, 1, 1, 1, 1, 2, 0, 0, 1, 1, 1, 1, 1, 1, 1],
                        [0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 2, 1, 1],
                        [1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1],
                        [1, 1, 1, 2, 0, 0, 1, 1, 1, 2, 0, 0, 1, 1, 1, 1],
                        [1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1],
                        [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                    ]
        # Dimensions de la fenêtre et couleurs
        self.taille_cellule = 40
        self.nb_lignes = len(self.couloir)
        self.nb_colonnes = len(self.couloir[0])
        self.longueur_fenetre = self.nb_colonnes * self.taille_cellule
        self.largeur_fenetre = self.nb_lignes * self.taille_cellule
        # Position de départ dans le couloir (càd en haut à gauche)
        self.position =  [0, 0]
        self.prec_position = [0, 0]

    # Dessine um carreau de dimensions taille_cellule (ex : 40x40)
    def dessiner_carreau(self, ecran, x, y, couleur):
        pygame.draw.rect(ecran, couleur,
                         (y * self.taille_cellule, x * self.taille_cellule, self.taille_cellule, self.taille_cellule))

    # Dessine les plans vus de dessus du batiment en fonction de la direction empruntée par l'écolier
    def dessiner_tout(self, ecran, direction, ecolier):
        carreau_blanc = (255, 255, 255)
        carreau_noir = (0, 0, 0)
        carreau_rouge = (255, 0, 0)
        carreau_bleu = (0, 0, 255)
        for i in range(self.nb_lignes):
            for j in range(self.nb_colonnes):
                if self.couloir[i][j] == 1:
                    couleur = carreau_noir
                elif self.couloir[i][j] == 0:
                    couleur = carreau_blanc # les portes pour rentrer dans les salles
                else :
                    couleur = carreau_bleu
                self.dessiner_carreau(ecran, i, j, couleur)
        # La position de l'écolier est marquée en rouge
        self.dessiner_carreau(ecran, self.position[0], self.position[1], carreau_rouge)
        # Dessine l'écolier en image
        ecolier.dessiner(ecran, self.taille_cellule, self.position)
        pygame.display.flip()

    def verifier_reponse(self):
        attend_touche  = True
        while attend_touche:
            for action in pygame.event.get():
                if action.type == pygame.QUIT:
                    return 0 # pas de réponse. fenêtre fermée
                if action.type == pygame.KEYDOWN: # Une touche est appuyée
                    touche = action.key
                    if touche == K_a:
                        return 1
                    if touche == K_b:
                        return 2
                    if touche == K_c:
                        return 3
                    if touche == K_ESCAPE:
                        return 0

    def poser_question(self, ecran, x, y):
        if self.couloir[x][y] == 2:
            for q in questions_profs:
                if q.position[0] == x and q.position[1] == y:
                    question = q.question
                    reponse1 = "a) " + q.reponse1
                    reponse2 = "b) " + q.reponse2
                    reponse3 = "c) " + q.reponse3
                    reponse_juste = q.reponse_juste
            self.position[0] = x
            self.position[1] = y
            font = pygame.font.Font(None, 20)
            text1 = font.render(question, True, (255,0,0))
            text2 = font.render(reponse1, True, (255,0,0))
            text3 = font.render(reponse2, True, (255,0,0))
            text4 = font.render(reponse3, True, (255,0,0))
            #ecran2 = pygame.display.set_mode((200, 200))
            pygame.draw.rect(ecran, (200,200,200), (100, 100, 300, 200))
            ecran.blit(text1, (120, 120))
            ecran.blit(text2, (120, 150))
            ecran.blit(text3, (120, 170))
            ecran.blit(text4, (120, 190))
            #ecolier.dessiner(ecran, self.taille_cellule, self.position)
            pygame.display.flip()
            reponse = self.verifier_reponse()
            if reponse == reponse_juste:
                print ("Bravo")
            else:
                print ("Essaie encore")
            return(reponse)

    # Déplacement de l'écolier
    def changer_position(self, ecran, direction):
        self.prec_position = self.position
        x = self.position[0] + direction[0]
        y = self.position[1] + direction[1]
        print ("Position demandée", x, y)
        # Vérifie que l'on sorte pas du couloir
        if x >= 0 and x < self.nb_lignes and y >= 0 and y < self.nb_colonnes:
            if self.couloir[x][y] == 0 or self.couloir[x][y] == 2:
                self.position[0] = x
                self.position[1] = y
                # vérifier si on rentre ou on sort d'une porte
                #ecolier.dessiner(ecran, self.taille_cellule, self.position)
                pygame.display.flip()
                if self.couloir[x][y] == 2:
                    self.poser_question(ecran, x, y)

def capture_touche():
        attend_touche  = True
        while attend_touche:
            for action in pygame.event.get():
                if action.type == pygame.QUIT:
                    return [0, 0] # Code pour la fin du jeu
                if action.type == pygame.KEYDOWN: # Une touche est appuyée
                    touche = action.key
                    if touche == K_DOWN:
                        return [1, 0]
                    if touche == K_UP:
                        return [-1, 0]
                    if touche == K_LEFT:
                        return [0, -1]
                    if touche == K_RIGHT:
                        return [0, 1]
                    if touche == K_ESCAPE:
                        return [0, 0]

# La classe Ecolier décrit l'acteur du jeu qui se déplace pour sortir
class Ecolier:
    def __init__(self, nom, dessin):
        self.nom = nom
        self.dessin = dessin
        self.personne = pygame.image.load(self.dessin)

    def dessiner(self, ecran, taille, position):
        rect = self.personne.get_rect()
        rect.y = position[0] * taille
        rect.x = position[1] * taille
        ecran.blit(self.personne, rect)

pygame.init()
ecolier = Ecolier("Elève", "ecolier3.jpeg")
parcours = Parcours()
ecran = pygame.display.set_mode((parcours.longueur_fenetre, parcours.largeur_fenetre))
pygame.display.set_caption("Ecole")
direction = [0, 0]
parcours.dessiner_tout(ecran, direction, ecolier)
pygame.display.flip()

en_cours = True
while en_cours:
    direction = capture_touche()
    parcours.changer_position(ecran, direction)
    parcours.dessiner_tout(ecran, direction, ecolier)
    if direction == [0, 0]:
        en_cours = False
    #clock.tick(30)

pygame.quit()
