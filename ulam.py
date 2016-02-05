from math import sqrt
from PIL import Image


class GenerateurSpirale:
    def __init__(self, longueur, fichier, premier):
        # Longueur d'un côté de la spirale
        self.longueur = longueur
        # On suit la position courante lors de l'écriture de la spirale
        self.point_en_cours = [0,0]
        # Le nombre en cours, qui est égal à l'index en cours + 1
        self.c = 1
        # On initialise une liste de booléens qui nous indique quels nombres sont/ne sont pas premiers.
        # La liste est initialisée à Vrai pour toutes les valeurs sauf pour premier[0].
        self.premier = premier
        # On créé l'image
        # (0,0) = coin supérieur gauche
        self.im = Image.new("1", (longueur, longueur), "black")
        # Données qu'on va "mettre" dans l'image
        # Initialisées à blanc (1). Les nombres premiers vont être mis en noir (0).
        self.data = [1] * (longueur*longueur)
        self.fichier = fichier

    def CoordonneesADataNumber(self, x, y):
        return x+self.longueur*y

    # On bouge le pixel courant à gauche
    # On colorie le pixel courant
    def gauche(self):
        self.c += 1
        self.point_en_cours[0] -= 1
        if self.premier[self.c-1]:
            self.data[self.CoordonneesADataNumber(self.point_en_cours[0], self.point_en_cours[1])] = 0

    # On bouge le pixel courant à droite
    # On colorie le pixel courant
    def droite(self):
        self.c += 1
        self.point_en_cours[0] += 1
        if self.premier[self.c-1]:
            self.data[self.CoordonneesADataNumber(self.point_en_cours[0], self.point_en_cours[1])] = 0

    # On bouge le pixel courant en haut
    # On colorie le pixel courant
    def haut(self):
        self.c += 1
        self.point_en_cours[1] -= 1
        if self.premier[self.c-1]:
            self.data[self.CoordonneesADataNumber(self.point_en_cours[0], self.point_en_cours[1])] = 0

    # On bouge le pixel courant en bas
    # On colorie le pixel courant
    def bas(self):
        self.c += 1
        self.point_en_cours[1] += 1
        if self.premier[self.c-1]:
            self.data[self.CoordonneesADataNumber(self.point_en_cours[0], self.point_en_cours[1])] = 0

    def pair(self, k):
        self.gauche()
        for _ in range(1, k+1):
            self.bas()
        for _ in range(1, k+1):
            self.droite()

    def impair(self, k):
        self.droite()
        for _ in range(1, k+1):
            self.haut()
        for _ in range(1, k+1):
            self.gauche()

    def ColorisationImage(self):
        self.point_en_cours[0] = int((self.longueur-1)/2)
        self.point_en_cours[1] = int(self.longueur/2)

        # k augmente au fur et à mesure qu'on tourne. Il compte le nombre de pixel qu'il nous reste à aller
        k = 1
        while k < self.longueur:
            if self.c % 2 == 0:
                self.pair(k)
            else:
                self.impair(k)
            k += 1

        self.im.putdata(self.data)
        #self.im.show()

        try:
            self.im.save(self.fichier)
        except IOError:
            print("IOError\n")


# Méthode 1 : on initialise la liste des premiers avec la méthode Crible d'Ératosthène
def InitialisePremiers_CribleEratosthene(longueur):
    premier = [True] * (longueur*longueur)
    premier[0] = False
    for i in range(2,longueur*longueur+1):
        # Si on trouve un nouveau nombre premier, on met tous ses multiples à False
        if premier[i-1]:
            multiple = 2*i
            while multiple <= longueur*longueur:
                premier[multiple-1] = False
                multiple += i
    return premier

# Méthode 2
def InitialisePremiers_methode2(longueur, start=1):
    top = start + longueur*longueur + 1
    premier1 = [False,False,True] + [True,False]*(top//2)

    for x in range(3, 1 + int(sqrt(top))):
        if not premier1[x]: continue
        for i in range(x*x, top, x*2):
            premier1[i] = False
    return premier1


# On affiche la spirale
def cell(n, x, y, start=1):
    d, y, x = 0, y - n//2, x - (n - 1)//2
    l = 2*max(abs(x), abs(y))
    d = (l*3 + x + y) if y >= x else (l - x - y)
    return (l - 1)**2 + d + start - 1


def show_spiral(longueur, premier, symbol="- ", start=0, space=None):
    cell_str = lambda x: f(x) if premier[x] else space
    f = lambda _: symbol # how to show prime cells

    if space == None: space = ' '*len(symbol)

    if not len(symbol): # print numbers instead
        max_str = len(str(longueur*longueur + start - 1))
        if space == None: space = '.'*max_str + ' '
        f = lambda x: ('%' + str(max_str) + 'd ')%x

    for y in range(longueur):
        print(''.join(cell_str(v) for v in [cell(longueur, x, y, start) for x in range(longueur)]))
    print()