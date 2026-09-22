import random

import pygame

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float)-> None:
        super().__init__(x,y,radius)

    def draw(self, screen):
        pygame.draw.circle(screen,'white',self.position,self.radius,LINE_WIDTH)

    def update(self, dt):
        self.position+=self.velocity*dt

    def split(self):
        self.kill()
        if self.radius<=ASTEROID_MIN_RADIUS:
            return
        log_event('asteroid_split')
        angle = random.uniform(20,50)
        asteroid1=self.velocity.rotate(angle)
        asteroid2=self.velocity.rotate(-angle)
        new_radius=self.radius-ASTEROID_MIN_RADIUS
        new_asteroid1=Asteroid(self.position[0],self.position[1],new_radius)
        new_asteroid2=Asteroid(self.position[0],self.position[1],new_radius)

        new_asteroid1.velocity=asteroid1*1.2
        new_asteroid2.velocity=asteroid2*1.2
