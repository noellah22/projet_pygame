# La classe Question décrit chacune des questions que chaque prof va poser
class Question:
    def __init__(self, titre, question, reponse1, reponse2, reponse3, reponse_juste, position):
        self.titre = titre
        # La question elle-même
        self.question = question
        # Les trois réponses proposées
        self.reponse1 = reponse1
        self.reponse2 = reponse2
        self.reponse3 = reponse3
        # Si la réponse est entre 1 et 3 (càd. a, b ou c)
        if 1 <= reponse_juste <= 3:
            self.reponse_juste = reponse_juste
        else:
            self.reponse_juste = 0 # Quand on ferme la fenetre sans répondre à la question
        self.position = position # Les coordonnées de la case où la question est posée

# Instanciation des 5 questions
question_geo = Question("Bonjour, je suis votre professeur de géographie. J'ai une question à vous poser.",
                        "Quel est le plus grand lac de Suisse ?",
                        "lac Léman","lac de Constance", "lac Majeur",
                        1, [7, 3])
question_chimie = Question("Bonjour, je suis votre professeur de chimie. J'ai une question à vous poser.",
                        "Quelle est la formule du méthane ?",
                        "H2O","CH4", "CHO4",
                        2, [2, 6])
question_aaaa = Question("Bonjour, je suis votre professeur de chimie. J'ai une question à vous poser.",
                        "Quelle est la formule du méthane ?",
                        "H2O","CH4", "CHO4",
                        2, [1, 9])
question_bbbb = Question("Bonjour, je suis votre professeur de chimie. J'ai une question à vous poser.",
                        "Quelle est la formule du méthane ?",
                        "H2O","CH4", "CHO4",
                        2, [5, 13])
question_cccc = Question("Bonjour, je suis votre professeur de chimie. J'ai une question à vous poser.",
                        "Quelle est la formule du méthane ?",
                        "H2O","CH4", "CHO4",
                        2, [7, 9])
