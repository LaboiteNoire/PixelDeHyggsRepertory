import pygame
"""
14/01/2019
2e version de loadImages
deve : Mahli, Eva
concu initialement pour l'architecture grapique d'un niveau d'abstraction bas.
c'est fonction est une fonction de type gestion des ressources fichiers,
car n'affiche rien.
Pour l'instant ne prend en charge que les .png car possedent une opacitée , elle
traduit neanmoins tout arguments en str.
Elle a pour but d'avoir une meilleur gestion et traduction que celle des
librairies pygames.
"""
def Fpx1400loadImages(acces,scale,rotate):
    try:
        img = pygame.image.load(str(str(acces)+".png"))
        if scale == 0 or scale == False or scale == "none":
            img = pygame.transform.rotozoom(img, rotate, 1)
            if rotate != 0:
                metaD = ["scale","none","rotate","succes"]
            else:
                metaD = ["scale","none","rotate","none"]
        else:
            img = pygame.transform.rotozoom(img, rotate, scale)
            if rotate != 0:
                metaD = ["scale","succes","rotate","succes"]
            else:
                metaD = ["scale","succes","rotate","none"]
    except pygame.error:
        img = "error"
        metaD = ["fail"]
        print("impossible de charger l'image png",str(acces))
    return img , metaD


"""
12/04/2020
Version finale de l'objet Tekusuchā signifiant litteralement texture.
deve:Mahli , Eva
L'objet Tekusuchā est un objet image.
Cet objet fait parti de la branche gpu.
"""
class Rph1204Tekusucha:
    def __init__(self,acc,sc,a,x,y):
        if type(sc) == list:
            self.acc , self.firstMetaD = Fpx1400loadImages(acc,sc,a)
            self.acc = pygame.transform.scale(self.acc,(sc[0],sc[1]))
            self.acc = pygame.transform.flip(self.acc,x,y)
            if x == True or y == True:
                self.secMetaD = ["flip","succes"]
            else:
                self.secMetaD = ["flip","none"]
        elif type(sc) == int:
            self.acc, self.firstMetaD = Fpx1400loadImages(acc,sc,a)
            self.acc = pygame.transform.flip(self.acc,x,y)
            if x == True or y == True:
                self.secMetaD = ["flip","succes"]
            else:
                self.secMetaD = ["flip","none"]
        self.MetaD = {"fisrt":self.firstMetaD,"sec":self.firstMetaD}
"""
14/01/2020
Version final de l'objet TekusuchāSprite signifiant litteralement texture de sprite.
deve:Mahli , Eva
L'objet Tekusuchā est un objet image plus avancé contenant des sprite et serra prochainement conbiner a la branche principal.
Cet objet fait parti de la branche gpu.
"""
class Fph1401TekusuchaSprite(pygame.sprite.Sprite):
    Class_Object_Index = 0
    def __init__(self,name,x,y,reso,spri):
        super(Fph1401TekusuchaSprite, self).__init__()
        self.images = []
        if len(self.images) == 0 and incr >= spri:
            self.images.append(pygame.image.load(str(name)+str(self.incr)+".png"))
            self.incr =+ 1
 
        self.index = 0
  
        self.image = self.images[self.index]
        
        self.rect = pygame.Rect(x, y, reso[0], reso[1])

        self.incr = 0
        Fph1401TekusuchaSprite.Class_Object_Index =+ 1
 
    def update(self):
        self.index += 1
 
        if self.index >= len(self.images):
            
            self.index = 0
        
        self.image = self.images[self.index]
    def postInistailization(self):
        if len(self.images) == 0 and incr >= spri:
            self.images.append(pygame.image.load(str(name)+str(self.incr)+".png"))
            self.incr =+ 1
        
        
        
    
