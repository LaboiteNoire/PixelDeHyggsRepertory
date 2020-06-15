"""
26/01/2020
premiere version de Tekisuto litteralement texte.
deve : Mahli,Cloe
concu initialement pour l'architecture general c'est fonction est une fonction
de gestion des ressources fichiers ttf, qui ne prend que tres peux sur le cpu et le
gpu.
Elle a pour but d'afficher du texte progressivement a l'aide d'un fichier ttf.
"""
def Fpx2601Tekisuto(string,name,integrated,scale):
    text = ''
    for i in range(len(string)):
        text += string[i]
        choose_font = pygame.font.Font(str(name)+".ttf",scale)
        text_surface = choose_font.render(text, True, (0,0,0))
        Wind.blit(text_surface,(0,0+integrated))
        pygame.display.flip()
        pygame.time.wait(100)
"""
26/01/2020
premiere version de TekisutoArial version de sa fonction mere en arial.
deve : Mahli,Cloe
concu initialement pour l'architecture, qui ne prend que tres peux sur le cpu et le
gpu.
Elle a pour but d'afficher du texte progressivement a l'aide d'un fichier ttf.
"""
def Fpx2601TekisutoArial(string,integrated,scale):
    text = ''
    for i in range(len(string)):
        text += string[i]
        arial_font = pygame.font.Font("GeneralsRessources/arial.ttf",scale)
        text_surface = arial_font.render(text, True, (0,0,0))
        Wind.blit(text_surface,(0,0+integrated))
        pygame.display.flip()
        pygame.time.wait(100)
