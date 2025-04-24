import sys

import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import (
    ASTEROID_KINDS,
    ASTEROID_MAX_RADIUS,
    ASTEROID_MIN_RADIUS,
    ASTEROID_SPAWN_RATE,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
)
from player import Player
from shot import Shot


def main() -> None:
    print("Starting Asteroids!")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    # Game Loop
    while True:
        # Check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # Update Game state
        for item in updatable:
            item.update(dt)
        for asteroid in asteroids:
            if asteroid.colliding(player):
                print("Game over!")
                sys.exit(0)
        for asteroid in asteroids:
            for shot in shots:
                if shot.colliding(asteroid):
                    asteroid.split()
                    shot.kill()

        # Draw screen
        screen.fill(color=(0, 0, 0))
        for item in drawable:
            item.draw(screen)
        dt = clock.tick(60) / 1000
        pygame.display.flip()


if __name__ == "__main__":
    main()
