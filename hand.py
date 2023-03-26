import pygame
import sys
import phonenumbers
from phonenumbers import timezone, geocoder, carrier

# timezone -->it Will Show the Time
# geocoder -->It will Show The region of The PhoneNumber
# carrier -->It will give the company name
# parse -->It will give the Details of the Phone Number

# conditions
# 1. we have To Enter the Phone Number as A string
# 2. +91
pygame.init()
# Global variables
WIDTH = 600
HEIGHT = 300
white = (255, 255, 255)
blue = (255, 0, 0)
balck = (0, 0, 0)
font = pygame.font.SysFont(None, 35)
# font = pygame.font.Font('freesansbold.ttf', 23)

p_number = input("Enter the Phone Number With + : ")
phone = phonenumbers.parse(p_number)
time = timezone.time_zones_for_number(phone)  # It will give the Time
carrier1 = carrier.name_for_number(phone, "en")  # It will give the Name of the Company in English
reg = geocoder.description_for_number(phone, "en")
nuWindow = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Trace Mobile Number By Aayush's")
pygame.display.update()
phone1 = str(phone)
time1 = str(time)
carrier2 = str(carrier1)
reg1 = str(reg)
# print(phone)
# nuWindow.fill(white)
# print(time)
# print(carrier1)
# print(reg)
print(phone1)


def show(text, color, x, y):
    # nuWindow.fill(white)
    screen_text = font.render(text, True, color)
    nuWindow.blit(screen_text, [x, y])


def welcome():
    # Creating Game Window

    nuWindow.fill(balck)
    exit_game = False
    blue = (222, 237, 83)  # 194 212 34
    while not exit_game:
        # show("Mobile Number Tracing",blue,100,210)
        # show("Press Space Bar To Play",blue,160,270)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
                quit()
            else:
                # gameloop()
                show(phone1, white, 5, 5)
                show("Comapany Name : " + carrier2, white, 5, 90)
                show("Region is : " + reg1, white, 5, 130)
                show("Time Zone" + time1, white, 5, 50)
                # show(time,blue,100,210)
                # show(carrier1,blue,100,210)
                # show(reg,blue,100,210)

        pygame.display.update()

    # pygame.display.update()
    # show(str(phone), blue, 5, 5)
    # show(str(time), blue, 5, 5)
    # show(str(carrier1), blue, 5, 5)
    # show(str(reg), blue, 5, 5)
    # pygame.display.update()


welcome()