import pygame
from pygame.locals import *

class Personnage:
    def __init__(self, nom, dessin):
        self.nom = nom
        self.dessin = dessin
        self.personne = pygame.image.load(self.dessin)

    def dessiner(self, ecran, taille, position):
        rect = self.personne.get_rect()
        rect.y = position[0] * taille
        rect.x = position[1] * taille
        ecran.blit(self.personne, rect)

class Professeur(Personnage):
    def __init__(self, nom, dessin, question):
        super().__init__(nom, dessin)
        self.question = question

    def dessiner(self, ecran, taille):
        position = self.question.position
        super().dessiner(ecran, taille, position)

class Directeur(Personnage):
    def __init__(self, nom, dessin, bareme):
        super().__init__(nom, dessin)
        self.bareme = bareme

    def dessiner(self, ecran, taille):
        position = [9,15]
        super().dessiner(ecran, taille, position)

# La classe Ecolier décrit l'acteur du jeu qui se déplace pour sortir
class Ecolier(Personnage):
    def __init__(self, nom, dessin):
        super().__init__(nom, dessin)
        self.score_total = 0

    def modifier_nb_points(self, reponse_juste):
        if reponse_juste:
            self.score_total += 3
        else:
            self.score_total -= 4
        titre = "Score : " + str(self.score_total) + " points"
        pygame.display.set_caption(titre)

    def capture_touche(self):
        attend_touche = True
        while attend_touche:
            for action in pygame.event.get():
                if action.type == pygame.QUIT:
                    return [0, 0]  # Code pour la fin du jeu
                if action.type == pygame.KEYDOWN:  # Une touche est appuyée
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