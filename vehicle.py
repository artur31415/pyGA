from utils import *
from random import *


class Vehicle:

  acceleration = (0, 0)
  velocity = (0, 0)
  position = (0, 0)

  dna = []

  r = 3
  maxforce = 0.5
  maxspeed = 3

  mutationRate = 0.1
  
  
  health = 1

  def __init__(self, x, y, _dna):
    velocity = (randint(-1, 1), randint(-1, 1))

    velocity = setMag(self.velocity, self.maxspeed)

    if _dna != None:
      dna = []
      
      for i in range(len(_dna)):
        dna_gene = _dna[i]
        if randint(0, 1) < self.mutationRate:
            if i < 2:
                # Adjust steering force weights
                dna[i] = _dna[i] + randint(-2, 2) / 10.0
            else:
                # Adjust perception radius
                dna[i] = _dna[i] + randint(-100, 100) / 10.0
          
          # Copy DNA
        dna.append(dna_gene)
    else:
        maxAtracRepul = 3
        # DNA
        # 0: Attraction/Repulsion to food
        # 1: Attraction/Repulsion to poison
        # 2: Radius to sense food
        # 3: Radius to sense poison
        
        dna = [randFloat(-maxAtracRepul, maxAtracRepul), randFloat(-maxAtracRepul, maxAtracRepul), randFloat(5, 100), randFloat(5, 100)]
    

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

  # Return true if health is less than zero
  def dead(self):
    return (self.health < 0)

  # Small chance of returning a new child vehicle
  def birth(self): 
  
    rnd = random()

    if (rnd < 0.001):
      # Same location, same DNA
      return Vehicle(self.position[0], self.position[1], self.dna)
    
    return None
  
  # Check against array of food or poison
  # index = 0 for food, index = 1 for poison
  def eat(food_list, index):
    # What's the closest?
    closest = None
    closestD = -1

    # Look at everything
    for (int i = list.size() - 1 i >= 0 i--) 
    {
      # Calculate distance
      d = PVector.dist(list.get(i), self.position)

      # If it's within perception radius and closer than pervious
      if (d < self.dna[2 + index] && d < closestD || closestD == -1) 
      {
        closestD = d
        # Save it
        closest = list.get(i)

        # If we're withing 5 pixels, eat it!
        if (d < 5) 
        {
          list.remove(i)
          # Add or subtract from health based on kind of food
          self.health += nutrition[index]
        }
      }
    }

    # If something was close
    if (closest != None) 
    {
      # Seek
      PVector seek = self.seek(closest, index)
      # Weight according to DNA
      seek.mult(self.dna[index])
      # Limit
      seek.limit(self.maxforce)
      self.applyForce(seek)
    }
  }

  # Add force to acceleration
  def applyForce(PVector force) 
  {
    self.acceleration.add(force)
  }

  # A method that calculates a steering force towards a target
  # STEER = DESIRED MINUS VELOCITY
  PVector seek(PVector target, int index) 
  {
    PVector desired = PVector.sub(target, self.position) # A vector pointing from the location to the target
    d = desired.mag()

    # Scale to maximum speed
    desired.setMag(self.maxspeed)

    # Steering = Desired minus velocity
    PVector steer = PVector.sub(desired, self.velocity)

    # Not limiting here
    # steer.limit(self.maxforce)

    return steer
  }


  def display() 
  {  # Color based on health
    color green = color(0, 255, 0)
    color red = color(255, 0, 0)
    color col = lerpColor(red, green, self.health)

    # Draw a triangle rotated in the direction of velocity
    theta = self.velocity.heading() + PI / 2
    #Push()
    translate(self.position[0], self.position[1])
    rotate(theta)

    # Extra info
    # if (debug.checked()) 
    # {
    #   noFill()

    #   # Circle and line for food
    #   stroke(0, 255, 0, 100)
    #   ellipse(0, 0, self.dna[2] * 2)
    #   line(0, 0, 0, -self.dna[0] * 25)

    #   # Circle and line for poison
    #   stroke(255, 0, 0, 100)
    #   ellipse(0, 0, self.dna[3] * 2)
    #   line(0, 0, 0, -self.dna[1] * 25)
    # }

    # Draw the vehicle itself
    fill(col)
    stroke(col)
    beginShape()
    vertex(0, -self.r * 2)
    vertex(-self.r, self.r * 2)
    vertex(self.r, self.r * 2)
    endShape(CLOSE)
    #pop()
  }

  # A force to keep it on screen
  def boundaries() 
  {
    # tolerable distance
    int d = 10
    PVector desired = None

    if (self.position[0] < d) 
    {
      desired = new PVector(self.maxspeed, self.velocity[1])
    } 
    else if (self.position[0] > width - d) 
    {
      desired = new PVector(-self.maxspeed, self.velocity[1])
    }

    if (self.position[1] < d) 
    {
      desired = new PVector(self.velocity[0], self.maxspeed)
    } 
    else if (self.position[1] > height - d) 
    {
      desired = new PVector(self.velocity[0], -self.maxspeed)
    }

    if (desired != None) 
    {
      desired.setMag(self.maxspeed)
      PVector steer = PVector.sub(desired, self.velocity)
      steer.limit(self.maxforce)
      self.applyForce(steer)
    }
  }
}