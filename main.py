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

poison_nutrition = -0.7
food_nutrition = 0.1

init_pop_count = 50
init_food_count = 10

food_spawn_rate = 0.2
poison_spawn_rate = 0.05
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

    for vehicle in vehicles:
        vehicle.eat(foods)
        
        # Check boundaries
        vehicle.boundaries(width, height)

        # Update
        vehicle.update()

        # If the vehicle has died, remove
        if vehicle.dead():
            vehicles.remove(vehicle)
        else:
            # Every vehicle has a chance of cloning itself
            child = vehicle.birth()

            if (child != None):
            
                vehicles.append(child)
        

    if random() < food_spawn_rate:
        foods.append(Food((randint(0, width), randint(0, height)), food_nutrition))

    if random() < poison_spawn_rate:
        foods.append(Food((randint(0, width), randint(0, height)), poison_nutrition))

    ##################################################################
    # DRAW CODE
    ##################################################################

    


    screen.fill((0, 0, 0))

    for vehicle in vehicles:
        vehicle.draw(screen)

    for food in foods:
        food.draw(screen)
    
    oldest_vehicle = None

    for vehicle in vehicles:
        if oldest_vehicle == None or vehicle.alive_tick > oldest_vehicle.alive_tick:
            oldest_vehicle = vehicle

    pygame.draw.circle(screen, (255, 255, 255), oldest_vehicle.position, 20, 2)
    #pygame.draw.rect(screen, (255, 255, 255), (20, 20, 500, 30))
    textsurface = myfont.render('pop = ' + str(len(vehicles)) + ' ; oldest is ' + str(oldest_vehicle.alive_tick) + ' ticks alive!', False, (255, 255, 255))
    screen.blit(textsurface, (20, 20))
    ##################################################################
    # Flip the display
    ##################################################################
    pygame.display.flip()

    clock.tick(20)
    

# Done! Time to quit.
pygame.quit()