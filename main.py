import ulam
import time


def DemoNormalPrimes_CribleEratosthene(longueur, fichier):
    start_time1 = time.clock()
    primes = ulam.InitialisePremiers_CribleEratosthene(int(longueur))
    sp = ulam.GenerateurSpirale(int(longueur), fichier, primes)
    sp.ColorisationImage()
    print("Méthode 1 :", time.clock() - start_time1, "seconds")
    choix = input("Afficher la spirale ? (O/N) ")
    if choix == "O":
        ulam.show_spiral(longueur, primes, symbol="")


def DemoNormalPrimes_CribleAtkin(longueur, fichier):
    start_time2 = time.clock()
    primes = ulam.InitialisePremiers_methode2(longueur)
    sp = ulam.GenerateurSpirale(longueur, fichier, primes[1:])
    sp.ColorisationImage()
    print("Méthode 2 :", time.clock() - start_time2, "seconds")

    choix = input("Afficher la spirale ? (O/N) ")
    if choix == "O":
        ulam.show_spiral(longueur, primes[1:], symbol="")


def main():
    longueur = -1

    while longueur <= 0:
        longueur = int(input("Longueur côté spirale ? "))


    #Méthode 1
    DemoNormalPrimes_CribleEratosthene(longueur, "fichiermeth1.bmp")

    # Méthode 2
    DemoNormalPrimes_CribleAtkin(longueur, "fichiermeth2.bmp")

main()