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

def rec_draw(screen, color, top_l, top_r, low_l, low_r):
    pygame.draw.rect(screen, color,(top_l,top_r, low_l, low_r))


def handle_events ():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return x1, y1,x,y, False
    keys = pygame.key.get_pressed(y1,x1,x,y)
    if keys[pygame.K_UP]and y1>0:
        y1 -=10
    if keys[pygame.K_DOWN]and y1<600:
        y1+=10
    if keys[pygame.K_LEFT]and x1>0:
        x1-=10
    if keys[pygame.K_RIGHT] and x1<800:
        x1+=10    
    if keys[pygame.K_UP]and y>0:
        y -=10
    if keys[pygame.K_DOWN]and y<600:
        y+=10
    if keys[pygame.K_LEFT]and x>0:
        x-=10
    if keys[pygame.K_RIGHT] and x<800:
        x+=10    
    return True

def main():
    
    screen = init_game()
    clock = pygame.time.Clock()

    
    
    x1, y1=(420, 320)
    x, y=(400,300)
    
    running = True
    while running:
        y1, x1, x,y,running = handle_events(y1,x1,x,y)
        screen.fill(config.GRAY) # Use color from config
        
        # Add code to draw stuff (for example) below this comment

        rec_draw(screen, config.BLUE,x1, x, y1,y)







        pygame.display.flip()
        # Limit the frame rate to the specified frames per second (FPS)
        clock.tick(config.FPS)

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
