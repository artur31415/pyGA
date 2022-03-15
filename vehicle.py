import pygame
from utils import *
from random import *


class Vehicle:

  acceleration = (0, 0)
  velocity = (0, 0)
  position = (0, 0)

  dna = []

  r = 10
  maxforce = 0.5
  maxspeed = 3

  mutationRate = 0.1
  
  
  health = 1

  alive_tick = 0

  def __init__(self, _position, _dna):
    maxAtracRepul = 3
    self.position = _position
    self.velocity = (randint(-1, 1), randint(-1, 1))

    self.velocity = setMag(self.velocity, self.maxspeed)

    if _dna != None:
      self.dna = []
      
      for i in range(len(_dna)):
        dna_gene = _dna[i]
        if randint(0, 1) < self.mutationRate:
            new_gene = 0
            if i < 2:
                # Adjust steering force weights
                new_gene = _dna[i] + randFloat(-1, 1)
            else:
                # Adjust perception radius
                new_gene = _dna[i] + randFloat(-1, 1)
            self.dna.append(new_gene)
          
          # Copy DNA
        self.dna.append(dna_gene)
    else:
        
        # DNA
        # 0: Attraction/Repulsion to food
        # 1: Attraction/Repulsion to poison
        # 2: Radius to sense food
        # 3: Radius to sense poison
        
        self.dna = [randFloat(-maxAtracRepul, maxAtracRepul), randFloat(-maxAtracRepul, maxAtracRepul), randFloat(5, 100), randFloat(5, 100)]
    

  # Method to update location
  def update(self):
    # Update velocity
    self.velocity = vec_add(self.velocity, self.acceleration)
    # Limit speed
    self.velocity = clamp(self.velocity, self.maxspeed)
    self.position = vec_add(self.position, self.velocity)
    # Reset acceleration to 0 each cycle
    self.acceleration = (0, 0)

    # Slowly die unless you eat
    self.health -= 0.002

    self.alive_tick += 1

  # Return true if health is less than zero
  def dead(self):
    return (self.health <= 0)

  # Small chance of returning a new child vehicle
  def birth(self): 
  
    rnd = random()

    if (rnd < 0.002):
      # Same location, same DNA
      return Vehicle((self.position[0], self.position[1]), self.dna)
    
    return None
  
  # Check against array of food or poison
  # index = 0 for food, index = 1 for poison
  def eat(self, food_list):
    # What's the closest?
    closest = None
    closestD = -1
    food_gene_index = 0

    #WHY?
    remaining_foods = [food_list[0]]

    # Look at everything
    for i in range(len(food_list) - 1, 0, -1):
      # Calculate distance
      d = vec_dist(food_list[i].position, self.position)
      

      if food_list[i].nutrition < 0:
        food_gene_index = 1

      # If it's within perception radius and closer than pervious
      if d < self.dna[2 + food_gene_index] and d < closestD or closestD == -1:
        closestD = d
        # Save it
        closest = food_list[i]

      # If we're withing 5 pixels, eat it!
      if d < self.r:
        # Add or subtract from health based on kind of food
        self.health += food_list[i].nutrition
        #food_list.pop(i)
      else:
        remaining_foods.append(food_list[i])
        

    # If something was close
    if closest != None:
      # Seek
      seek = self.seek(closest.position)
      # Weight according to DNA
      seek = vec_scalar_mult(seek, self.dna[food_gene_index])
      # Limit
      seek = clamp(seek, self.maxforce)
      self.applyForce(seek)
    
    return remaining_foods
    

  # Add force to acceleration
  def applyForce(self, force):
    self.acceleration = vec_add(self.acceleration, force)
  
  # A method that calculates a steering force towards a target
  # STEER = DESIRED MINUS VELOCITY
  def seek(self, target):
    desired = vec_sub(target, self.position) # A vector pointing from the location to the target
    d = mag(desired)

    # Scale to maximum speed
    desired = clamp(desired, self.maxspeed)

    # Steering = Desired minus velocity
    steer = vec_sub(desired, self.velocity)

    # Not limiting here
    # steer.limit(self.maxforce)

    return steer
  

  def draw(self, DISPLAY): 
    # Color based on health
    green = (0, 255, 0)
    red = (255, 0, 0)
    col = lerpColor(red, green, self.health, 0.0, 1.0)

    # Draw a circle rotated in the direction of velocity
    theta = math.atan2(self.velocity[1], self.velocity[0])# + math.pi / 2
    heading_pos = (self.r * math.cos(theta), self.r * math.sin(theta))
    heading_pos = vec_add(heading_pos, self.position)

    pygame.draw.circle(DISPLAY, col, self.position, self.r)
    pygame.draw.line(DISPLAY, (255, 255, 255), self.position, heading_pos, 3)
  

  # A force to keep it on screen
  def boundaries(self, screen_w, screen_h):
    # tolerable distance
    d = self.r / 2
    desired = None

    if self.position[0] < d:
        desired = (self.maxspeed, self.velocity[1])
    elif self.position[0] > screen_w - d:
        desired = (-self.maxspeed, self.velocity[1])

    if self.position[1] < d:
        desired = (self.velocity[0], self.maxspeed)
    elif self.position[1] > screen_h - d:
        desired = (self.velocity[0], -self.maxspeed)

    if desired != None:
      #desired = clamp(desired, self.maxspeed)
      steer = vec_sub(desired, self.velocity)
      #steer = clamp(steer, self.maxforce)
      self.applyForce(steer)
 