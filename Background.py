import pygame #Indispensable
from sys import exit #Quitter le jeu sans renvoyer un message d'erreur
pygame.init() #Active le module, indispensable également
screen = pygame.display.set_mode((800,400)) #Affiche et définit la taille de la fenêtre du jeu (donner en px les tailles en argument (largeur x hauteur))
pygame.display.set_caption('Runner') #donne un titre au jeu (donner le titre en argument)
Clock = pygame.time.Clock() #Crée une variable qui sert à définir les FPS
sky_surface = pygame.image.load('Graphics/Sky.png') # Sert à importer l'image copntenue dans un dossier (indiquer le chemin de données en argument sans oublier l'extension du fichier)
ground_surface = pygame.image.load('Graphics/Ground.png') # Sert à importer l'image copntenue dans un dossier (indiquer le chemin de données en argument sans oublier l'extension du fichier)
while True: # (ligne actuelles = 5 suivantes) Empêche la fenêtre du jeu de se fermer lorsque le code s'exécute ; permet au joueur de quitter en cliquant sur la croix
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(sky_surface,(0,0)) #Sert à attacher la surface régulière à la surface d'affichage pour la rendre visible (indiquer en premier argument l'image que l'on souhaite afficher et ses coordonnées en deuxième (largeur x hauteur))
    screen.blit(ground_surface,(0,300))
    # Draw all elements
    #Update everything
    pygame.display.update() # Indique à Pygame qu'il doit rafraîchir l'affichage
    Clock.tick(60) # Indique à Pygame la fréquence de rafraîchissement (indiquer la fréquence en argument)