import pygame
from pygame.locals import *

# Dimensions de la fenêtre
LARGEUR, HAUTEUR = 800, 600

# Couleurs
BLANC = (255, 255, 255)

# Initialiser Pygame
pygame.init()

# Fenêtre du jeu
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Évasion de l'école")

# Classe Personnage
class Personnage(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()  # Appel obligatoire
        self.image = pygame.image.load("perso.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 100))  # Personnage plus grand
        self.rect = self.image.get_rect()
        self.rect.center = (LARGEUR // 2, HAUTEUR - 70)
        self.vitesse = 8
        self.arme = None

    def bouger(self, touches):
        print(touches)
        if touches[K_RIGHT] and self.rect.right < LARGEUR:
            self.rect.x += self.vitesse
        if touches[K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.vitesse
        if touches[K_UP] and self.rect.top > 0:
            self.rect.y -= self.vitesse
        if touches[K_DOWN] and self.rect.bottom < HAUTEUR:
            self.rect.y += self.vitesse

    def attaquer(self, fenetre, armes_groupe):
        if self.arme:
            nouvelle_arme = self.arme(self.rect.centerx, self.rect.top)
            armes_groupe.add(nouvelle_arme)

class Armes(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.rect.x = x
        self.rect.y = y
        self.speed = 2

    def update(self):
        self.rect.y -= self.speed
        if self.rect.bottom < 0:
            self.kill()


class Crayon(Armes):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = pygame.image.load("crayon.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect(center=(x, y))

class Becher(Armes):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = pygame.image.load("becher.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect(center=(x, y))

# Classe Jeu
class Jeu:
    def __init__(self):
        self.fond = pygame.image.load("hall.png").convert()
        self.fond = pygame.transform.scale(self.fond, (LARGEUR, HAUTEUR))
        self.personnage = Personnage()
        self.armes = pygame.sprite.Group()

    def afficher_fond(self, fenetre):
        fenetre.blit(self.fond, (0, 0))

    def gerer_clavier(self, touches, fenetre):
        self.personnage.bouger(touches)
        if touches[K_SPACE]:
            self.personnage.attaquer(fenetre, self.armes)

# Boucle Principale
def main():
    jeu = Jeu()
    clock = pygame.time.Clock()
    running = True

    while running:
        touches = pygame.key.get_pressed()

        # Gérer les événements
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

            # Changer d'arme (exemple : Crayon ou Bécher)
            if event.type == KEYDOWN:
                if event.key == K_c:  # Sélectionner Crayon
                    jeu.personnage.arme = Crayon
                if event.key == K_b:  # Sélectionner Bécher
                    jeu.personnage.arme = Becher

        # Afficher le fond
        jeu.afficher_fond(fenetre)

        # Gérer le personnage
        jeu.personnage.bouger(touches)
        fenetre.blit(jeu.personnage.image, jeu.personnage.rect)

        # Gérer les attaques
        jeu.armes.update()
        jeu.armes.draw(fenetre)

        # Rafraîchir l'écran
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()
