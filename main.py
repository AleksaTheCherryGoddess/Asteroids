import sys

import pygame

from asteroid import Asteroid
from asteroidField import AsteroidField
from constants import *
from logger import log_event, log_state
from player import Player


def main():
    pygame.init()

    clock=pygame.time.Clock()
    dt=0.0

    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

    asteroids = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    updatable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    player=Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)

    Asteroid.containers = (asteroids, drawable, updatable)
    AsteroidField.containers = (updatable)
    asteroidField = AsteroidField()

    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill('black')

        for object in updatable:
            object.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event('player_hit')
                print('Game over!')
                sys.exit()

        for object in drawable:
            object.draw(screen)



        pygame.display.flip()
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()
