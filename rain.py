# coding=utf-8
import pygame
import sys
from pygame.locals import *


pygame.init()
pygame.mixer.init()

bg_size = width, height = 683, 383



def main():
    
    screen = pygame.display.set_mode(bg_size)
    pygame.display.set_caption("Rian")
    background = pygame.image.load("images/1.jpg").convert()
    pygame.mixer.music.load("sounds/1.mp3")
    pygame.mixer.music.set_volume(0.2)

    pygame.mixer.music.play(-1)
    fullscreen = False
    
    while True:
        # 按f键切换窗口与全屏
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_f:
                    fullscreen  = not fullscreen
                    if fullscreen:
                        background = pygame.image.load("images/f1.jpg").convert()
                        screen = pygame.display.set_mode(bg_size, FULLSCREEN, 0)
                    else:
                        background = pygame.image.load("images/1.jpg").convert()
                        screen = pygame.display.set_mode(bg_size)                 
        screen.blit(background, (0, 0))
        pygame.display.update()
        
if __name__ == "__main__":
    main()
