"""
12/11/2019
premiere version de l'import general
deve : Mahli
concu initialement pour l'architecture general c'est fonction est une fonction
de gestion des ressources fichiers, qui ne prend que tres peux sur le cpu et le
gpu.
Elle a pour but d'eviter et de cibler les problemes qui pourraient-etre liés a
tel ou tel import.
"""
def Fpx1211importGeneral():
    try:
        import sys
        metaD = "succes"
    except ImportError:
            print("Impossible de charger le module sys")
    try:
        import random
        metaD = "succes"
    except ImportError:
            print("Impossible de charger le module random")
            metaD = "fail"
    try:
        import math
        metaD = "succes"
    except ImportError:
            print("Impossible de charger le module math")
            metaD = "fail"
    try:
        import os
        metaD = "succes"
    except ImportError:
            print("Impossible de charger le module os")
            metaD = "fail"
    try:
        import getopt
        metaD = "succes"
    except ImportError:  
            print("Impossible de charger le module getopt")
            metaD = "fail"
    try:          
        import pygame
        metaD = "succes"
    except ImportError:
            print("Impossible de charger le module pygame")
            metaD = "fail"
    try:          
        import numpy as np
        metaD = "succes"
    except ImportError:
            print("Impossible de charger le module numpy")
            metaD = "fail"
    try:          
        import simpleaudio as sa
        metaD = "succes"
    except ImportError:
            print("Impossible de charger le module simpleaudio")
            metaD = "fail"
    return metaD
"""
17/01/2020
premiere version de variablesStatic
deve : Mahli
concu initialement pour l'architecture general c'est fonction est une fonction
de gestion des ressources statique , qui ne prend que tres peux sur le cpu et le
gpu.
Elle a pour but d'englober des variables qui serront utiliser par tous les deves.
"""
def Fpx1701variablesStatics():
    pi = np.pi
    return pi
"""
12/11/2019
premiere version de createWindow
deve : Mahli
concu initialement pour l'architecture grapique d'un niveau d'abstraction bas.
c'est fonction est une fonction de type graphique.
Pour l'instant ne permet de creer que 2 types de fenetres.
Elle a pour but d'avoir une meilleur gestion de la creation de fenetres.
notes:dans de futures versions il serra possible d'y isserrer des images dans le titres.
"""
def Gpx1211createWindow(typeW,H,L,titl):
    if typeW == "F"or "f":
        Wind =pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        metaD = [("fullscreen" , "title="+str(titl))]
    else:
        Wind =pygame.display.set_mode((L,H))
        metaD = [(str(L) , "x" , str(H) , "title="+str(titl))]
    pygame.dysplay.set_caption(str(titl))
    return Wind,metaD
"""
Saundoefekuto
"""
class Phiggs:
    def __init__(self):
        return 0
    def pi():
        return 3.14
    pi = staticmethod(pi)
