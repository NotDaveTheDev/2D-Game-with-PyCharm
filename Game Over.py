import pygame # Indispensable
from sys import exit # Quitter le jeu sans renvoyer un message d'erreur

pygame.init() #Active le module, indispensable également
screen = pygame.display.set_mode((800,400)) # Affiche et définit la taille de la fenêtre du jeu (donner en px les tailles en argument (largeur x hauteur))
pygame.display.set_caption('Runner') #donne un titre au jeu (donner le titre en argument)
Clock = pygame.time.Clock() # Crée une variable qui sert à définir les FPS
game_active = True # Crée une variable d'état de jeu, celle-ci nous permettra de le modifier à l'aide de structures conditionelles

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
        if game_active: # Crée les nouvelles conditions selon lesquelles le jeu s'exécute (celles-ci s'éexécutent si le jeu est "actif")
            if event.type == pygame.MOUSEBUTTONDOWN and player_rectangle.bottom == 300: # Crée les conditions de la détection d'un clic
                    player_gravity = -20
            if event.type == pygame.KEYDOWN and player_rectangle.bottom == 300: # Vérifie si une touche est enfoncée lors du cycle d'événements
                if event.key == pygame.K_SPACE: #Vérifie si la touche espace est enfoncée lors du cycle d'événements
                    player_gravity =-20
        else: # crée les nouvelles conditions de comportement du jeu si celui-ci est "over" ; ici, on ne fait que relancer le jeu en appuyant sur espace
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True # Relance le jeu en appuyant sur espace (ligne du dessus)
                snail_rectangle.left = 800 # réinitialise la position de l'escargot

    if game_active: # indique les événements qui se produisent lorsque l'état de jeu est en mode "actif"
        screen.blit(sky_surface,(0,0)) # blit sert à attacher la surface régulière à la surface d'affichage pour la rendre visible (indiquer en premier argument l'image que l'on souhaite afficher et ses coordonnées en deuxième (largeur x hauteur))
        screen.blit(ground_surface,(0,300))
        screen.blit(snail_surface,snail_rectangle)
        screen.blit(player_surface,player_rectangle)
        pygame.draw.rect(screen,'#DBF3FA',score_rectangle) # Paramètre les caractéristiques du rectangle (indiquer en argument la taille, la couleur (plain, hexa ou RGB, etc.)
        pygame.draw.rect(screen, '#DBF3FA', score_rectangle,2) # Paramètre les caractéristiques du rectangle (indiquer en argument la taille, la couleur (plain, hexa ou RGB, etc.) ; ici, une bordure est demandée
        screen.blit(score_surface,score_rectangle)
        pygame.draw.rect(screen, '#DBF3FA',title_rectangle) # Paramètre les caractéristiques du rectangle (indiquer en argument la taille, la couleur (plain, hexa ou RGB, etc.)
        pygame.draw.rect(screen, '#DBF3FA', title_rectangle,2) # Paramètre les caractéristiques du rectangle (indiquer en argument la taille, la couleur (plain, hexa ou RGB, etc.) ; ici, une bordure est demandée
        screen.blit(title_surface,title_rectangle)
        player_gravity += 1
        player_rectangle.y += player_gravity
        if player_rectangle.bottom >= 300: player_rectangle.bottom = 300
        screen.blit(player_surface,player_rectangle)
        if snail_rectangle.colliderect(player_rectangle): # Indique les conditions de défaite/sortie de jeu
            game_active = False #Change l'état en False, état qui nous permet de proposer de nouvelles conditions de jeu et de créer un nouvel état de jeu

    snail_rectangle.x -= 5 # Anime le rectangle de l'escargot en fonction du point que l'on indique
    if snail_rectangle.right <= 0 : snail_rectangle.right = 800 # Fait "revenir" l'escargot à droite passé une certaine coordonnée

    pygame.display.update() # Indique à Pygame qu'il doit rafraîchir l'affichage
    Clock.tick(60) # Indique à Pygame la fréquence de rafraîchissement (indiquer la fréquence en argument)