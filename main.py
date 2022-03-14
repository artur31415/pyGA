import pygame
from random import *

pygame.init()
pygame.font.init()

# seed random number generator
#seed(1)
################################################################################################
#                                           VARIABLES
################################################################################################
width = 700
height = 700

screen = pygame.display.set_mode([width, height])

myfont = pygame.font.SysFont('Comic Sans MS', 20)

running = True


ticks = 0

clock = pygame.time.Clock()

################################################################################################
#                                           FUNCTIONS
################################################################################################
def map(value, istart, istop, ostart, ostop):
    return ostart + (ostop - ostart) * ((value - istart) / (istop - istart))

################################################################################################
#                                           MAIN LOOP
################################################################################################

while running:

    ##################################################################
    # EVENTS
    ##################################################################
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                pass

    ##################################################################
    # STATE UPDATE
    ##################################################################


    ##################################################################
    # DRAW CODE
    ##################################################################

    
    # if is_complete:
    #     pygame.draw.rect(screen, (255, 255, 255), (20, 20, 500, 30))
    #     textsurface = myfont.render('A* FINISHED with ' + str(len(current_path)) + ' nodes!', False, (0, 0, 0))
    #     screen.blit(textsurface, (20, 20))


    screen.fill((255, 255, 255))
    ##################################################################
    # Flip the display
    ##################################################################
    pygame.display.flip()

    clock.tick(30)
    

# Done! Time to quit.
pygame.quit()