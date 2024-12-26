
class Question:
    def __init__(self, titre, question, reponse1, reponse2, reponse3, reponse_juste, position):
        self.titre = titre
        self.question = question
        self.reponse1 = reponse1
        self.reponse2 = reponse2
        self.reponse3 = reponse3
        if 1 <= reponse_juste <= 3:
            self.reponse_juste = reponse_juste
        else:
            self.reponse_juste = 0
        self.position = position

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

# Instancier les questions
questions_profs = [question_geo, question_chimie, question_aaaa, question_bbbb, question_cccc]