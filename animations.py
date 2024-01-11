```python
import pygame
from pygame.locals import *

class Animation:
    def __init__(self, images, speed):
        self.images = images
        self.speed = speed
        self.current = 0
        self.time = 0

    def update(self, dt):
        self.time += dt
        if self.time >= self.speed:
            self.time = 0
            self.current = (self.current + 1) % len(self.images)

    def draw(self, screen, pos):
        screen.blit(self.images[self.current], pos)

def load_images(*files):
    return [pygame.image.load(f) for f in files]

def animate_bot_avatar():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()

    bot_avatar_images = load_images('bot_avatar1.png', 'bot_avatar2.png', 'bot_avatar3.png')
    bot_avatar_animation = Animation(bot_avatar_images, 0.1)

    running = True
    while running:
        dt = clock.tick(60) / 1000
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        bot_avatar_animation.update(dt)

        screen.fill((255, 255, 255))
        bot_avatar_animation.draw(screen, (400, 300))
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    animate_bot_avatar()
```