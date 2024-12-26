import pygame
from pygame.locals import *
import random
import time
from datetime import timedelta
from questions import *

# La classe Parcours décrit un chemin à emprunter. 0 indique le couloir sur lequel on peut passer.
# 1 indique un emplacement où il y a un bâtiment (là où l'on peut pas passer)
# 2 indique un emplacement d'une porte où il y a un professeur
# 3 indique la sortie
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
                        [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3]
                    ]
        # Dimensions de la fenêtre et couleurs
        self.taille_cellule = 40
        self.nb_lignes = len(self.couloir)
        self.nb_colonnes = len(self.couloir[0])
        self.longueur_fenetre = self.nb_colonnes * self.taille_cellule
        self.largeur_fenetre = self.nb_lignes * self.taille_cellule
        # Position de départ dans le couloir (càd en haut à gauche)
        self.position =  [0, 0]
        #self.prec_position = [0, 0]

    # Dessine un carreau de dimensions taille_cellule (ex : 40x40)
    def dessiner_carreau(self, ecran, x, y, couleur):
        pygame.draw.rect(ecran, couleur,
                         (y * self.taille_cellule, x * self.taille_cellule, self.taille_cellule, self.taille_cellule))

    # Dessine les plans vus de dessus du batiment en fonction de la direction empruntée par l'écolier
    def dessiner_tout(self, ecran, direction, ecolier):
        carreau_blanc = (255, 255, 255)
        carreau_noir = (0, 0, 0)
        carreau_rouge = (255, 0, 0)
        carreau_bleu = (0, 0, 255)
        carreau_vert = (0, 255, 0)
        for i in range(self.nb_lignes):
            for j in range(self.nb_colonnes):
                if self.couloir[i][j] == 1:
                    couleur = carreau_noir
                elif self.couloir[i][j] == 0:
                    couleur = carreau_blanc # les portes pour rentrer dans les salles
                elif self.couloir[i][j] == 3:
                    couleur = carreau_vert # la porte de sortie
                else :
                    couleur = carreau_bleu
                self.dessiner_carreau(ecran, i, j, couleur)
        # La position de l'écolier est marquée en rouge
        self.dessiner_carreau(ecran, self.position[0], self.position[1], carreau_rouge)
        # Dessine l'écolier en image
        ecolier.dessiner(ecran, self.taille_cellule, self.position)
        #professeur_chimie.dessiner(ecran, self.taille_cellule, self.position)
        pygame.display.flip()

    def verifier_reponse(self):
        attend_touche  = True
        while attend_touche:
            for action in pygame.event.get():
                if action.type == pygame.QUIT:
                    return 0 # Si on ferme la fenêtre alors le programme s'arrête
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

    def question_reponse(self, ecran, x, y):
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
            font = pygame.font.Font(None, 25)
            couleur_texte = (0, 0, 0)
            couleur_rectangle = (200, 200, 200)
            dimensions_rectangle = (100, 100, 400, 200)
            texte_0 = font.render(question, True, couleur_texte)
            texte_1 = font.render(reponse1, True, couleur_texte)
            texte_2 = font.render(reponse2, True, couleur_texte)
            texte_3 = font.render(reponse3, True, couleur_texte)
            #ecran2 = pygame.display.set_mode((200, 200))
            pygame.draw.rect(ecran, couleur_rectangle, dimensions_rectangle)
            ecran.blit(texte_0, (120, 120))
            ecran.blit(texte_1, (120, 150))
            ecran.blit(texte_2, (120, 170))
            ecran.blit(texte_3, (120, 190))
            #ecolier.dessiner(ecran, self.taille_cellule, self.position)
            pygame.display.flip()
            reponse = self.verifier_reponse()
            return(reponse_juste == reponse)

    def dialogue_directeur(self, ecran, score_total):
        couleur_texte = (0, 0, 0)
        fonte = pygame.font.Font(None, 25)
        texte_1 = fonte.render("Directeur : ", True, couleur_texte)
        if score_total >= 8:
            self.afficher_reussite(ecran, fonte, texte_1)
        else:
            self.afficher_echec(ecran, fonte, texte_1)

    def afficher_reussite(self, ecran, fonte, texte_1):
        couleur_texte = (0, 255, 0)
        couleur_texte_quitter = (0, 0, 0)
        couleur_rectangle = (200, 200, 200)
        texte_2 = fonte.render("BRAVO ! Vous avez réussi.", True, couleur_texte)
        texte_quitter = fonte.render("Appuyez sur une touche pour quitter le jeu.", True, couleur_texte_quitter)
        dimensions_rectangle = (100, 100, 400, 200)
        pygame.draw.rect(ecran, couleur_rectangle, dimensions_rectangle)
        ecran.blit(texte_1, (120, 120))
        ecran.blit(texte_2, (120, 150))
        ecran.blit(texte_quitter, (120, 190))
        pygame.display.flip()
        attend_touche = True
        while attend_touche:
            for action in pygame.event.get():
                if action.type == pygame.KEYDOWN:  # Une touche est appuyée
                    exit()

    def afficher_echec(self, ecran, fonte, texte_1):
        couleur_texte = (255, 0, 0)
        couleur_texte_4 = (0, 0, 0)
        couleur_rectangle = (200, 200, 200)
        texte_2 = fonte.render("Vous n'avez pas les compétences pour m'affronter.", True, couleur_texte)
        texte_3 = fonte.render("Revenez plus tard.", True, couleur_texte)
        texte_4 = fonte.render("Appuyez sur une touche pour continuer.", True, couleur_texte_4)
        dimensions_rectangle = (100, 100, 450, 200)
        pygame.draw.rect(ecran, couleur_rectangle, dimensions_rectangle)
        ecran.blit(texte_1, (120, 120))
        ecran.blit(texte_2, (120, 150))
        ecran.blit(texte_3, (120, 170))
        ecran.blit(texte_4, (120, 210))
        pygame.display.flip()
        attend_touche = True
        while attend_touche:
            for action in pygame.event.get():
                if action.type == pygame.KEYDOWN:  # Une touche est appuyée
                    attend_touche = False

    # Déplacement de l'écolier
    def changer_position(self, ecran, direction, ecolier):
        #self.prec_position = self.position
        x = self.position[0] + direction[0]
        y = self.position[1] + direction[1]
        # Vérifie que l'on sorte pas du couloir
        if x >= 0 and x < self.nb_lignes and y >= 0 and y < self.nb_colonnes:
            if self.couloir[x][y] == 0 or self.couloir[x][y] == 2:
                self.position[0] = x
                self.position[1] = y
                # vérifier si on rentre ou on sort d'une porte
                #ecolier.dessiner(ecran, self.taille_cellule, self.position)
                pygame.display.flip()
                if self.couloir[x][y] == 2:
                    reponse_juste = self.question_reponse(ecran, x, y)
                    ecolier.modifier_nb_points (reponse_juste)
            elif self.couloir[x][y] == 3:
                self.dialogue_directeur(ecran, ecolier.score_total)







