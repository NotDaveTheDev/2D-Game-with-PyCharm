import pygame # Indispensable
from sys import exit # Quitter le jeu sans renvoyer un message d'erreur

pygame.init() #Active le module, indispensable également
screen = pygame.display.set_mode((800,400)) # Affiche et définit la taille de la fenêtre du jeu (donner en px les tailles en argument (largeur x hauteur))
pygame.display.set_caption('Runner') #donne un titre au jeu (donner le titre en argument)
Clock = pygame.time.Clock() # Crée une variable qui sert à définir les FPS

test_font = pygame.font.Font('Font/Pixeltype.ttf', 50) # Crée une police (indiquer en argument le type et la taille)

sky_surface = pygame.image.load('Graphics/sky.png').convert_alpha() # Sert à importer l'image contenue dans un dossier (indiquer le chemin de données en argument sans oublier l'extension du fichier)
ground_surface = pygame.image.load('Graphics/ground.png').convert_alpha() # Sert à importer l'image copntenue dans un dossier (indiquer le chemin de données en argument sans oublier l'extension du fichier)

title_surface = test_font.render('Runner game', False, (64,64,64)).convert_alpha() # Sert à paramétrer le texte du titre affiché à l'écran (indiquer en argument le texte lui-même, l'antialiasing, la couleur du texte (en RGB, hexa ou plain)
title_rectangle = title_surface.get_rect(center = (400,20)) # Place la surface de texte dans un rectangle

score_surface = test_font.render('Score', False, (64,64,64)).convert_alpha() # Sert à paramétrer le texte du titre affiché à l'écran (indiquer en argument le texte lui-même, l'antialiasing, la couleur du texte (en RGB, hexa ou plain)
score_rectangle = score_surface.get_rect(center = (400,80)) # Place la surface de texte dans un rectangle

snail_surface = pygame.image.load('Graphics/Snail/snail1.png').convert_alpha()
snail_rectangle = snail_surface.get_rect(bottomright = (600,300)) # Donne les coordonnées du rectangle de l'escargot

player_surface = pygame.image.load('Graphics/Player/player_walk_1.png').convert_alpha() # Importation de l'image du joueur + conversion
player_rectangle = player_surface.get_rect(midbottom = (80,300)) # Considère une surface et la place dans un rectangle (indiquer en argument le point de rectangle de référence + coordonnées)
player_gravity = 0
while True: # (ligne actuelles = 5 suivantes) Empêche la fenêtre du jeu de se fermer lorsque le code s'exécute ; permet au joueur de quitter en cliquant sur la croix
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEMOTION: # Crée les conditions de la détection de la position de la souris
            print(event.pos) # Renvoie les coordonnées de celle-ci
            if player_rectangle.collidepoint(event.pos):# Crée une nouvelle condition : si un des points du rectangle du joueur touche la souris (event.pos)
                print ('collision') # On renvoie la détection de collision
        if event.type == pygame.MOUSEBUTTONDOWN: # Crée les conditions de la détection d'un clic
            print ('mouse down') # Renvoie l'information
        if event.type == pygame.MOUSEBUTTONUP: # Crée les conditions de la détection d'un relâchement de clic
            print ('mouse up') # Renvoie l'information
        if event.type == pygame.KEYDOWN: # Vérifie si une touche est enfoncée lors du cycle d'événements
            if event.key == pygame.K_SPACE: #Vérifie si la touche espace est enfoncée lors du cycle d'événements
                print('Key down') # Renvoie l'information
        if event.type == pygame.KEYUP: # Vérifie si une touche est relâchée lors du cycle d'événements
            print('Key up') # Renvoie l'information


    screen.blit(sky_surface,(0,0)) # blit sert à attacher la surface régulière à la surface d'affichage pour la rendre visible (indiquer en premier argument l'image que l'on souhaite afficher et ses coordonnées en deuxième (largeur x hauteur))
    screen.blit(ground_surface,(0,300))
    screen.blit(snail_surface,snail_rectangle)
    player_gravity += 1
    player_rectangle.y += player_gravity
    screen.blit(player_surface,player_rectangle)
    pygame.draw.rect(screen,'#DBF3FA',score_rectangle) # Paramètre les caractéristiques du rectangle (indiquer en argument la taille, la couleur (plain, hexa ou RGB, etc.)
    pygame.draw.rect(screen, '#DBF3FA', score_rectangle,2) # Paramètre les caractéristiques du rectangle (indiquer en argument la taille, la couleur (plain, hexa ou RGB, etc.) ; ici, une bordure est demandée
    screen.blit(score_surface,score_rectangle)
    pygame.draw.rect(screen, '#DBF3FA',title_rectangle) # Paramètre les caractéristiques du rectangle (indiquer en argument la taille, la couleur (plain, hexa ou RGB, etc.)
    pygame.draw.rect(screen, '#DBF3FA', title_rectangle,2) # Paramètre les caractéristiques du rectangle (indiquer en argument la taille, la couleur (plain, hexa ou RGB, etc.) ; ici, une bordure est demandée
    screen.blit(title_surface,title_rectangle)

    keys = pygame.key.get_pressed() #Renvoie l'information indiquant quelle(s) touche(s) est/sont pressées
    if keys[pygame.K_SPACE]: # Renvoie un message si la touche Space est enfoncée
        print('jump')

    snail_rectangle.x -= 5 # Anime le rectangle de l'escargot en fonction du point que l'on indique
    if snail_rectangle.right <= 0 : snail_rectangle.right = 800 # Fait "revenir" l'escargot à droite passé une certaine coordonnée

    if player_rectangle.colliderect(snail_rectangle):
        print('collision')

    mouse_position = pygame.mouse.get_pos() # Active la souris et suit sa position
    if player_rectangle.collidepoint(mouse_position): # Sert à détecter les collisions entre la souris et un point du rectangle du joueur
        print(pygame.mouse.get_pressed()) # Sert à détecter les clics de souris effectués sur le personnage du joueur

    pygame.display.update() # Indique à Pygame qu'il doit rafraîchir l'affichage
    Clock.tick(60) # Indique à Pygame la fréquence de rafraîchissement (indiquer la fréquence en argument)