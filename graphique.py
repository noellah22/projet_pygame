import pygame
from pygame.locals import *
import random
import time
from datetime import timedelta

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
        self.position =  [0, 0] # Position de départ dans le couloir (càd en haut à gauche)

    # Afficher les instructions au début du jeu
    def afficher_consignes(self, ecran):
               couleur_texte = (0, 0, 0)
               couleur_rectangle = (200, 200, 200)
               fonte = pygame.font.Font(None, 25) # Fonte de taille 25, sans rectangle autour
               # Format des textes pour affichage
               texte_0 = fonte.render("Instructions : ", True, couleur_texte) # True rend le texte non-pixélisé (lissage)
               texte_1 = fonte.render("Utilisez les flèches pour vous déplacer.", True, couleur_texte)
               texte_2 = fonte.render("Allez voir vos professeurs pour obtenir des points.", True, couleur_texte)
               texte_3 = fonte.render("Si vous avez au moins 8 points, dirigez-vous vers la sortie.", True, couleur_texte)
               texte_4 = fonte.render("Votre scrore sera affiché en haut de la fenêtre", True, couleur_texte)
               texte_5 = fonte.render("Si vous ratez, retournez voir vos professeurs.", True, couleur_texte)
               texte_6 = fonte.render("Bonne chance !", True, couleur_texte)
               dimensions_rectangle = (70, 70, 520, 240)
               pygame.draw.rect(ecran, couleur_rectangle, dimensions_rectangle)
               # Afficher les textes
               ecran.blit(texte_0, (90, 100))
               ecran.blit(texte_1, (90, 150))
               ecran.blit(texte_2, (90, 170))
               ecran.blit(texte_3, (90, 190))
               ecran.blit(texte_4, (90, 210))
               ecran.blit(texte_5, (90, 230))
               ecran.blit(texte_6, (90, 270))
               pygame.display.flip() # Rafraîchir la fenêtre texte

    # Dessine un carreau de dimensions taille_cellule (ex : 40x40)
    def dessiner_carreau(self, ecran, x, y, couleur):
        pygame.draw.rect(ecran, couleur,
                         (y * self.taille_cellule, x * self.taille_cellule, self.taille_cellule, self.taille_cellule))

    # Afficher les images des profs et salles de classe
    def afficher_classes_profs(self, ecran, les_profs):
        # Positions des images des classes
        pos_av = (5, 203)
        pos_chimie = (244, 204)
        pos_geo = (485, 207)
        pos_allemand = (367, 5)
        pos_histoire = (85, 5)
        # Charger et redimensionner les images des classes
        image_av = pygame.transform.scale(pygame.image.load("classroom.png"), (150, 190))
        image_chimie = pygame.transform.scale(pygame.image.load("classroom.png"), (150, 150))
        image_geo = pygame.transform.scale(pygame.image.load("classroom.png"), (150, 149))
        image_allemand = pygame.transform.scale(pygame.image.load("classroom.png"), (267, 148))
        image_histoire = pygame.transform.scale(pygame.image.load("classroom.png"), (190, 150))
        # Dessiner les images supplémentaires des classes
        ecran.blit(image_av, pos_av)
        ecran.blit(image_chimie, pos_chimie)
        ecran.blit(image_geo, pos_geo)
        ecran.blit(image_allemand, pos_allemand)
        ecran.blit(image_histoire, pos_histoire)
        # Afficher les images des profs
        for prof in les_profs:
            prof.dessiner(ecran, self.taille_cellule)

    # Dessine la structure de l'école SANS les images
    def dessiner_structure(self, ecran, ecolier):
        carreau_blanc = (255, 255, 255)
        carreau_noir = (0, 0, 0)
        for i in range(self.nb_lignes): # Pour chaque ligne du tableau
            for j in range(self.nb_colonnes): # Pour chaque colonne de la ligne (ligne * colonne = carreaux)
                if self.couloir[i][j] == 1: # Salles de classes
                    couleur = carreau_noir
                elif self.couloir[i][j] == 0: # Couloirs où l'on se déplace
                    couleur = carreau_blanc
                elif self.couloir[i][j] == 3: # Position des profs, càd les portes des salles
                    couleur = carreau_blanc
                else : # La sortie, càd la position du directeur
                    couleur = carreau_blanc
                self.dessiner_carreau(ecran, i, j, couleur) # Dessine les carreaux selon la couleur
        ecolier.dessiner(ecran, self.taille_cellule, self.position) # Dessine l'écolier en image

    # Attend une réponse a, b ou c : elle renvoie un code (1, 2, 3) selon la réponse
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

    # On pose la question selon la position du prof
    def question_reponse(self, ecran, x, y, prof):
        if prof.question.position[0] == x and prof.question.position[1] == y:
            if prof.deja_visite:
                prof.affiche_deja_visite(ecran)
                return(0) # Pas de question
            else:
                question = prof.question.question
                reponse1 = "a) " + prof.question.reponse1
                reponse2 = "b) " + prof.question.reponse2
                reponse3 = "c) " + prof.question.reponse3
                prof.modifier_visite(True)
        self.position[0] = x
        self.position[1] = y
        font = pygame.font.Font(None, 25)
        couleur_texte = (0, 0, 0)
        couleur_rectangle = (200, 200, 200)
        dimensions_rectangle = (100, 100, 400, 200)
        # Pose la question dans le rectangle ci-dessus
        texte_0 = font.render(question, True, couleur_texte)
        texte_1 = font.render(reponse1, True, couleur_texte)
        texte_2 = font.render(reponse2, True, couleur_texte)
        texte_3 = font.render(reponse3, True, couleur_texte)
        pygame.draw.rect(ecran, couleur_rectangle, dimensions_rectangle)
        # Afficher les textes
        ecran.blit(texte_0, (120, 120))
        ecran.blit(texte_1, (120, 150))
        ecran.blit(texte_2, (120, 170))
        ecran.blit(texte_3, (120, 190))
        pygame.display.flip() # Rafraîchir le pop up des questions
        reponse = self.verifier_reponse() # réponse 1, 2 ou 3
        return(reponse) # Donne la réponse donnée

    # Fonction pour parler avec le directeur en fonction du score obtenu par l'écolier
    def dialogue_directeur(self, ecran, ecolier, les_profs):
        couleur_texte = (0, 0, 0)
        fonte = pygame.font.Font(None, 25)
        texte_1 = fonte.render("Directeur : ", True, couleur_texte)
        if ecolier.score_total >= 8: # En fonction du score/nombre de points on affiche échec ou réussite
            self.afficher_reussite(ecran, fonte, texte_1)
        else:
            self.afficher_echec(ecran, fonte, texte_1)
            for prof in les_profs:
                prof.modifier_visite(False)
            ecolier.init_score()
            ecolier.modifier_score(0)

    # Fonction qui va afficher si l'on réussit
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
        pygame.display.flip() # Rafraîchir le pop up de la réussite
        attend_touche = True
        while attend_touche: # On attend d'appuyer sur une touche pour quitter le programme
            for action in pygame.event.get():
                if action.type == pygame.KEYDOWN:  # Une touche est appuyée
                    exit()

    # Fonction qui va afficher si l'on échoue
    def afficher_echec(self, ecran, fonte, texte_1):
        couleur_texte = (255, 0, 0)
        couleur_texte_4 = (0, 0, 0)
        couleur_rectangle = (200, 200, 200)
        texte_2 = fonte.render("Vous n'avez pas les compétences pour sortir.", True, couleur_texte)
        texte_3 = fonte.render("Revenez plus tard.", True, couleur_texte)
        texte_4 = fonte.render("Appuyez sur une touche pour continuer.", True, couleur_texte_4)
        dimensions_rectangle = (100, 100, 450, 200)
        pygame.draw.rect(ecran, couleur_rectangle, dimensions_rectangle)
        ecran.blit(texte_1, (120, 120))
        ecran.blit(texte_2, (120, 150))
        ecran.blit(texte_3, (120, 170))
        ecran.blit(texte_4, (120, 210))
        pygame.display.flip() # Rafraîchir le pop up de l'échec
        attend_touche = True
        while attend_touche: # On attend d'appuyer sur une touche pour recommencer ou continuer
            for action in pygame.event.get():
                if action.type == pygame.KEYDOWN:  # Une touche est appuyée
                    attend_touche = False

    # Déplacement de l'écolier
    def changer_position(self, ecran, direction, ecolier, les_profs):
        x = self.position[0] + direction[0]
        y = self.position[1] + direction[1]
        # Vérifie que l'on sorte pas du couloir
        if x >= 0 and x < self.nb_lignes and y >= 0 and y < self.nb_colonnes:
            if self.couloir[x][y] == 0 : # Vérifier si on reste dans le couloir
                self.position[0] = x
                self.position[1] = y
            elif self.couloir[x][y] == 2: # Vérifier si on rentre ou on sort d'une porte
                for prof in les_profs:  # Parcours la liste des profs pour trouver la bonne question
                    if prof.question.position[0] == x and prof.question.position[1] == y:
                        reponse = self.question_reponse(ecran, x, y, prof) # Pose la question
                        if reponse != 0 : # Vérifie qu'une question a bien été posée
                            if reponse == prof.question.reponse_juste: # Modifier le score selon la réponse juste ou fausse
                                ecolier.modifier_score (3) # Réponse juste alors +3 points
                            else :
                                ecolier.modifier_score(-4) # Réponse fausse alors -4 points
            elif self.couloir[x][y] == 3: # Vérifie si on va chez le directeur(sortie)
                self.dialogue_directeur(ecran, ecolier, les_profs)
