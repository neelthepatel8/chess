import pygame
from pygame.locals import *
from sys import exit

pygame.init()

screen = pygame.display.set_mode((640, 520))

image = pygame.image.load('assets/pieces/bishop_black.svg').convert_alpha()
image_rect = image.get_rect(center = (640//2, 520//2))

moving = False

while True:

    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()
            exit()

        elif event.type == MOUSEBUTTONDOWN:
            if image_rect.collidepoint(event.pos):
                moving = True

        elif event.type == MOUSEBUTTONUP:
            moving = False

        elif event.type == MOUSEMOTION and moving:
            image_rect.move_ip(event.rel)

    screen.fill('WHITE')
    screen.blit(image, image_rect)
    pygame.display.update()