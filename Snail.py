import pygame #Indispensable
from sys import exit #Quitter le jeu sans renvoyer un message d'erreur
pygame.init() #Active le module, indispensable également
screen = pygame.display.set_mode((800,400)) #Affiche et définit la taille de la fenêtre du jeu (donner en px les tailles en argument (largeur x hauteur))
pygame.display.set_caption('Runner') #donne un titre au jeu (donner le titre en argument)
Clock = pygame.time.Clock() #Crée une variable qui sert à définir les FPS
test_font = pygame.font.Font('Font/Pixeltype.ttf', 50) #Crée une police (indiquer en argument le type et la taille)
sky_surface = pygame.image.load('Graphics/Sky.png') # Sert à importer l'image contenue dans un dossier (indiquer le chemin de données en argument sans oublier l'extension du fichier)
ground_surface = pygame.image.load('Graphics/Ground.png') # Sert à importer l'image copntenue dans un dossier (indiquer le chemin de données en argument sans oublier l'extension du fichier)
text_surface = test_font.render('My game', False, 'Black') # Sert à paramétrer le texte affiché à l'écran (indiquer en argument le texte lui-même, l'antialiasing, la couleur du texte)
snail_surface = pygame.image.load('graphics/snail/snail1.png')
while True: # (ligne actuelles = 5 suivantes) Empêche la fenêtre du jeu de se fermer lorsque le code s'exécute ; permet au joueur de quitter en cliquant sur la croix
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(sky_surface,(0,0)) # blit sert à attacher la surface régulière à la surface d'affichage pour la rendre visible (indiquer en premier argument l'image que l'on souhaite afficher et ses coordonnées en deuxième (largeur x hauteur))
    screen.blit(ground_surface,(0,300))
    screen.blit(text_surface,(350,50))
    screen.blit(snail_surface,(600,250))
    pygame.display.update() # Indique à Pygame qu'il doit rafraîchir l'affichage
    Clock.tick(60) # Indique à Pygame la fréquence de rafraîchissement (indiquer la fréquence en argument)
