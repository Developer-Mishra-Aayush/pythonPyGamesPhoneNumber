import pygame
x = pygame.init() #For Initialize PyGame

#Creating Window
gameWindow = pygame.display.set_mode((1200,600))
pygame.display.set_caption("Snake Game By Aayush")

#Creating Random variables
exit_game = False  # For Exit the Game set The variable as True
game_over = False # When He Dies Then set the Variables as True

#Creating a Game Loop
while exit_game!=True:
    # pass
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT :# Enables The X Button
            exit_game = True
        if event.type == pygame.KEYDOWN:# Detect that Keys are Presses or Not
            if event.key == pygame.K_RIGHT:
                print("You Pressed right Arrow Key")
pygame.quit()
quit()