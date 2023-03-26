import pygame
import random
pygame.init()

# Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (144, 238, 144)

#creating Window
SCREENWIDTH = 800
SCREENHEIGHT = 600
gameWindow = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))

# Creating Title
pygame.display.set_caption('Snake Game By Aayush')
pygame.display.update()
clock = pygame.time.Clock()
# Showing The Score In Screen
font = pygame.font.SysFont(None, 55)

def show(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])

def plot_snake(gameWindow, color, snk_list, snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])

def welcome():
    exit_game = False
    blue = (222, 237, 83)# 194 212 34
    while not exit_game:
        gameWindow.fill((80, 168, 76))
        show("Snake Game By Aayush Mishra",blue,100,210)
        show("Press Space Bar To Play",blue,160,270)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gameloop()
        pygame.display.update()
        clock.tick(60)
# Game Loop
def gameloop():
    # Creating Global variables
    exit_game = False  # For Exit the Game set The variable as True
    game_over = False  # When He Dies Then set the Variables as True

    snake_x = 200
    snake_y = 200
    snake_size = 20
    food_size = 12
    FPS = 30
    velocity_x = 0
    velocity_y = 0
    apple_x = random.randint(12, SCREENWIDTH)  # It Will Create a Random Number
    apple_y = random.randint(12, SCREENHEIGHT)  # It Will Create a Random Number
    score = 0
    snk_list = []
    snk_length = 1

    while exit_game!=True:
        if game_over :
            gameWindow.fill(white)
            show("Game over Please Enter to Continue",red, 100,250)

            for event in pygame.event.get():
                if event.type == pygame.QUIT :# Enables The X Button
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()

        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT :# Enables The X Button
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x=6
                        velocity_y=0
                    if event.key == pygame.K_LEFT:
                        velocity_x=-6
                        velocity_y = 0
                    if event.key == pygame.K_UP :
                        velocity_y=-6
                        velocity_x = 0
                    if event.key == pygame.K_DOWN :
                        velocity_y=+6
                        velocity_x = 0
                    if event.key == pygame.K_q:
                        score+=10
            snake_x+=velocity_x
            snake_y+=velocity_y
            if abs(snake_x - apple_x)<10 and abs(snake_y - apple_y)<10:
                score+=10
                apple_x = random.randint(0, SCREENWIDTH)  # It Will Create a Random Number
                apple_y = random.randint(0, SCREENHEIGHT)  # It Will Create a Random Numbers
                # snake_size+=10
                snk_length+=5
                print(score)
            gameWindow.fill(white)
            show("Score : " + str(score), red, 5, 5)
            head =[]
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_length:
                del snk_list[0]
            if head in snk_list[:-1]:
                game_over = True
            if snake_x<0 or snake_x>SCREENWIDTH or snake_y<0 or snake_y>SCREENHEIGHT:
                game_over = True
                # return/
                # print('Game Over')

            pygame.draw.rect(gameWindow,red,[apple_x, apple_y, food_size, food_size])
            plot_snake(gameWindow,black, snk_list,snake_size)
        pygame.display.update()
        clock.tick(FPS)
welcome()
gameloop()