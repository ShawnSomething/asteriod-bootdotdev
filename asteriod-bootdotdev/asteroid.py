import pygame  # type: ignore
from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

    def update(self, dt):
        self.position += (self.velocity * dt) 
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        new_angle = random.uniform(20,50)
        split_x = self.velocity.rotate(new_angle)
        split_y = self.velocity.rotate(-new_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_asteroid_1 = Asteroid(self.position, split_x, new_radius)
        new_asteroid_2 = Asteroid(self.position, split_y, new_radius)

        new_asteroid_1.velocity = split_x * 1.2
        new_asteroid_2.velocity = split_y * 1.2
