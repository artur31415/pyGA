import pygame
from random import *
from food import Food

from vehicle import Vehicle

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


vehicles = []
foods = []

poison_nutrition = -1
food_nutrition = 0.1

init_pop_count = 50
init_food_count = 10

food_spawn_rate = 0.1
################################################################################################
#                                           FUNCTIONS
################################################################################################
def init_environment():
    for i in range(init_pop_count):
        vehicles.append(Vehicle((randint(0, width), randint(0, height)), None))

    for i in range(init_food_count):
        foods.append(Food((randint(0, width), randint(0, height)), poison_nutrition))
        foods.append(Food((randint(0, width), randint(0, height)), food_nutrition))

################################################################################################
#                                           MAIN LOOP
################################################################################################

init_environment()
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