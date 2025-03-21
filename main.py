#Shay VanLandschoot
#--DATE--#
# Pygame game template

import pygame
import sys
import config # Import the config module

def init_game ():

    pygame.init()
    screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT)) 
   
    
    pygame.display.set_caption(config.TITLE)
    return screen

def rec_draw(screen, color,tl,tr,ll,lr):
    pygame.draw.rect(screen, color, (tl,tr,ll,lr))


def handle_events (x1,y1):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return x1, y1, False
    keys=pygame.key.get_pressed()
    if keys[pygame.K_UP]and y1>0:
        y1 -=10
    if keys[pygame.K_DOWN]and y1<600:
        y1+=10
    if keys[pygame.K_LEFT]and x1>0:
        x1-=10
    if keys[pygame.K_RIGHT] and x1<800:
        x1+=10    

    return x1,y1, True

def main():
    
    screen = init_game()
    clock = pygame.time.Clock()

    y1=100
    x1=100


    running = True
    while running:
        x1,y1,running = handle_events(x1,y1)
        screen.fill(config.GRAY) # Use color from config

        # Add code to draw stuff (for example) below this comment

        rec_draw(screen, config.BLUE,x1,y1,x1,y1)







        pygame.display.flip()
        # Limit the frame rate to the specified frames per second (FPS)
        clock.tick(config.FPS)

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
