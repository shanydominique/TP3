from random import shuffle, random


class Joueur:
    """
    Cette classe permet de représenter un joueur.

    La classe joueur possède une variable de classe:
    - TAILLE_CHEVALET : le nombre de jetons maximum qu'un joueur peut avoir.

    Un joueur a 3 attributs:
    - nom (str, public): représente le nom du joueur doit être non vide.
    - __points (entier, privé): représente le nombre de points que le joueur détient.
    - __chevalet (list, privé): représente le chevalet (l'ensemble des jetons du joueur) du joueur.
            Cette liste devrait être en tout temps de taille Joueur.TAILLE_CHEVALET. À chaque position du chevalier on peut avoir un jeton ou pas.
            Une position libre devra contenir None. Autrement elle devrait avoir un objet Jeton à cette position.
    """
    TAILLE_CHEVALET = 7

    def __init__(self, nom):
        """
        Initialise un objet joueur avec le nom passé en argument.
        Le nombre de points d'un joueur devra être 0 à l'initialisation, et le chevalet devra être vide.
        Rappel: Un chevalet vide veut dire une liste contenant que des None.
        :param nom: Le nom du joueur.
        :return: Ne retourne rien.
        :exception: Levez une exception si le nom est une chaine vide.
        """
        self.nom = nom
        self.__chevalet= [None, None, None, None, None, None]
        self.__points = 0

        assert (nom == "" or " "), "Chaine vide..."
    @property
    def nb_a_tirer(self):
        """
        Méthode permet de trouver le nombre de places vides dans le chevalet.
        Rappel: Un chevalet vide veut dire une liste contenant que des None.
        :return: (int) Le nombre de places vides dans le chevalet.
        """
        # À compléter
        nombres_de_places_vides= 0
        for element in self.__chevalet:
            if element == None:
                nombres_de_places_vides += 1
        return nombres_de_places_vides

    @property
    def points(self):
        """
        Méthode permettant d'obtenir le nombre de points du joueur.
        :return: (int) Le nombre de points du joueur.
        """

        return self.nombres_de_points_du_joueur


    @staticmethod
    def position_est_valide(pos):
        """
        Méthode permettant de vérifier si une position sur un chevalet est valide ou pas.
        Valide veut dire que la position est entre 0 et Joueur.TAILLE_CHEVALET (Joueur.TAILLE_CHEVALET étant exclus)
        :param pos: (int) la position à valider
        :return: True si position valide, False sinon
        """
        # À compléter
        # Mettre votre code ici
        return 0 <= pos < Joueur.TAILLE_CHEVALET

    def position_est_vide(self, pos):
        """
        Étant donnée une position sur le chevalet, cette méthode permet de voir
        si la position est vide ou pas.
        Rappel: Une position vide ne contient pas de jeton, juste None.
        :param pos: (int) position à vérifier.
        :return: True si la position est vide et False sinon.
        :exception: Levez une exception avec assert si la position n'est pas valide. Pensez à réutiliser Joueur.position_est_valide.
        """
        assert (not self.position_est_valide(pos)), "Position invalide..."
        if pos == None:
            return True
        else:
            return False

    def ajouter_jeton(self, jeton, pos=None):
        """
        Étant donnés un jeton et une position sur le chevalet, cette méthode permet d'ajouter le jeton
        au chevalet si la position mentionnée est vide.
        Si la position est vide (i.e. pos est égal à None), le jeton est mis à la première position libre du chevalet en partant de la gauche.
        Rappel: Une position vide ne contient pas de jeton, juste None.
        :param jeton: (Jeton) Jeton à placer sur le chevalet.
        :param pos: (int, optionnel) Position où ajouter le jeton.
        :return: Ne retourne rien.
        :exception: Levez une exception avec assert si la position est spécifiée mais n'est pas valide ou si elle n'est pas vide pour y déposer un jeton. Pensez à réutiliser Joueur.position_est_valide et position_est_vide.
        """
        assert (not self.position_est_valide(pos)), "Position invalide..."
        if self.position_est_vide(pos):
            for i in Joueur.__chevalet:
                if self.position_est_vide(i):
                    Joueur.__chevalet = i
                    break


    def retirer_jeton(self, pos):
        """
        Cette méthode permet de retirer un jeton du chevalet: c'est comme simuler un joueur qui prend un jeton de son chevalet. Donc retirer veut dire mettre la position à None et retourner le jeton qui était présent à cet emplacement.
        :param pos: Position du jeton à retirer.
        :return: Le jeton retiré.
        :exception: Levez une exception avec assert si la position spécifiée n'est pas valide ou si elle est vide. Pensez à réutiliser Joueur.position_est_valide et position_est_vide.
        """
        # À compléter
        # Mettre votre code ici
        assert (not self.position_est_valide(pos)), "La position n'est pas valide."
        assert (self.position_est_vide(pos)), "La position est vide."
        jeton_retire = self.__chevalet[pos]
        self.__chevalet[pos] = None
        return jeton_retire

    def obtenir_jeton(self, pos):
        """
        Cette méthode permet d'obtenir un jeton du chevalet: c'est comme si le joueur voulait voir un jeton de son chevalet. Donc obtenir un jeton à une position revient juste à retourner le jeton à la position indiquée.
        :param pos: Position du jeton.
        :return: Le jeton à la position d'intérêt.
        :exception: Levez une exception avec assert si la position spécifiée n'est pas valide ou si elle est vide. Pensez à réutiliser Joueur.position_est_valide et position_est_vide.
        """
        # À compléter
        # Mettre votre code ici
        return self.__chevalet[pos]

    def ajouter_points(self, points):
        """
        Cette méthode permet d'ajouter des points à un joueur
        :param p: (int) points à ajouter.
        :return: Ne retourne rien.
        """
        self.__points += points


    def melanger_jetons(self):
        """
        Cette méthode permet de mélanger au hasard le chevalet du joueur, c'est-à-dire mélanger les positions des éléments dans la liste représentant le chevalet.
        Pensez à utiliser la fonction shuffle du module random.
        :return: Ne retourne rien.
        """
        random.shuffle(self.__chevalet)

    def __str__(self):
        """ *** Vous n'avez pas à coder cette méthode ***
        Formatage du joueur. Cette méthode est appelée lorsque vous faites str(v) où v est un joueur.
        :return: str représentant le joueur.
        """
        s = "{}\n".format(self.nom)
        s += "Score: {}\n".format(self.points)
        s += "            " + "".join(["{:<3s}".format(str(x)) if x else '  ' for x in self.__chevalet])
        s += "\nChevalet: \_" + "__".join([chr(0x2080 + i + 1) for i in range(self.TAILLE_CHEVALET)]) + '_/\n'
        return s
