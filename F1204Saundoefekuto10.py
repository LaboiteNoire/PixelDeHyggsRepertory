"""
24/01/2020
Derniere version de Saundoefekuto litteralement bruitage.
deve : Mahli,Cloe
concu initialement pour l'architecture general c'est fonction est une fonction
de gestion des ressources fichiers audio, qui ne prend que tres peux sur le cpu et le
gpu.
Elle a pour but d'eviter et de cibler les problemes qui pourraient-etre liés a
tel ou tel selection de son puis de le jouer en stereo avec le volume donné.
NB:ne prend en compte que les fichier .wav.
Il est recommander de n'utiliser cette fonction que pour les objets d'environnements.
Cette fonction ne fonctionne que si le mixer a été initialiser avec 2 channels.
"""
def Fpx2401Saundoefekuto(name,vX,vY):
    soundFx = pygame.mixer.Sound(str(name)+'.wav')
    channelFx = soundFx.play()
    if vX > 1:
        vX = 1
    else:
        vX = vX
    if vY > 1:
        vY = 1
    else:
        vY = vY
    try:
        channel.set_volume(vX, vY)
        MetaD = ["succes"]
    except AttributeError:
        MetaD = ["succes","attribut error"]
    return MetaD
"""
24/01/2020
premiere version de l'init audio.
deve : Mahli,Cloe
concu initialement pour l'architecture general c'est fonction est une fonction
de gestion des ressources fichiers audio, qui ne prend que tres peux sur le cpu et le
gpu.
Elle a pour but d'initialiser correctement le mixer pygame.
"""
def Fpx2401SaundoefekutoInit():
    pygame.mixer.init(frequency=44000, size=-16,channels=2, buffer=4096)
