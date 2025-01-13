import pygame
from pygame.locals import *

# La classe Personnage inclue les professeurs, l'écolier et le directeur
class Personnage:
    def __init__(self, nom, dessin):
        self.nom = nom
        self.dessin = dessin
        self.personne = pygame.image.load(self.dessin)

    # Affiche l'image du personnage dans un carreau du parcours
    def dessiner(self, ecran, taille, position):
        rect = self.personne.get_rect()
        rect.y = position[0] * taille # La position du personnage
        rect.x = position[1] * taille # Ibid.
        ecran.blit(self.personne, rect) # Affiche le rectangle avec l'image dessus

# La classe Professeur hérite de la classe Personnage, on lui a rajouté une question
class Professeur(Personnage):
    def __init__(self, nom, dessin, question):
        super().__init__(nom, dessin)
        self.question = question # Associer avec une question
        self.personne = pygame.transform.scale_by(self.personne, 0.2) # Réduire la taille de l'image
        self.deja_visite = False

    # Afficher où se trouve le professeur en fonction de la position de sa question
    def dessiner(self, ecran, taille):
        position = self.question.position
        super().dessiner(ecran, taille, position)

    # Modifie l'attribut quand on visite un professeur
    def modifier_visite(self, visite):
        self.deja_visite = visite

    # Fonction qui affiche su l'on a déjà visité le professeur
    def affiche_deja_visite(self, ecran):
        couleur_texte = (0, 0, 0)
        couleur_rectangle = (200, 200, 200)
        fonte = pygame.font.Font(None, 25)
        texte = fonte.render("Vous avez déjà répondu à ma question.", True, couleur_texte)
        dimensions_rectangle = (100, 100, 400, 200)
        pygame.draw.rect(ecran, couleur_rectangle, dimensions_rectangle)
        ecran.blit(texte, (120, 150))
        pygame.display.flip() # Rafraîchir le pop up
        attend_touche = True
        while attend_touche: # On attend d'appuyer sur une touche pour quitter le programme
            for action in pygame.event.get():
                if action.type == pygame.KEYDOWN:
                    return

# La classe Directeur hérite de Personnage, on lui a rajouté un barème
class Directeur(Personnage):
    def __init__(self, nom, dessin, bareme):
        super().__init__(nom, dessin)
        self.bareme = bareme
        self.personne = pygame.transform.scale_by(self.personne, 0.072)

    def dessiner(self, ecran, taille):
        position = [9,15] # Position du directeur en bas à droite
        super().dessiner(ecran, taille, position)

# Ibid., on lui a rajouté un score
# La classe Ecolier décrit l'acteur du jeu qui se déplace pour sortir
class Ecolier(Personnage):
    def __init__(self, nom, dessin):
        super().__init__(nom, dessin)
        self.score_total = 0
        self.personne = pygame.transform.scale_by(self.personne, 0.23)

    # Modification du score de l'écolier
    def modifier_score(self, nb_points):
        self.score_total += nb_points
        titre = "Score : " + str(self.score_total) + " points"
        pygame.display.set_caption(titre)

    # Fonction qui initialisse le score pour pouvoir recommencer à 0 après l'échec
    def init_score(self):
        self.score_total = 0

    # Attend qu'on appuie sur une touche et retourne la direction choisie
    def capture_touche(self):
        attend_touche = True
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
                        return [0, 0] # Code pour la fin du jeu
