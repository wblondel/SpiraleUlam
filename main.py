# coding: utf8

# SpiraleUlam  Copyright (C) 2016    William Gerald Blondel
# william.blondel78@gmail.com
# Last modified 16th March 2016 1.06am

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


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