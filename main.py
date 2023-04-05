#PenQuins

import sys
sys.path.append('/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages')
import pygame

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the window caption
pygame.display.set_caption("PenQuins")

#Create PenQuin Class
class lemming:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
        self.direction = "right"

    def move(self):
        if self.direction == "right":
            self.x += self.speed
        else:
            self.x -= self.speed

    def check_collision(self, other_object):
        # Check for collision with other objects in the game
        pass

#Create Obstacle Class
class Obstacle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def check_collision(self, other_object):
        # Check for collision with other objects in the game
        pass

#Create Game Class
class Game:
    def __init__(self):
        self.lemmings = []
        self.obstacles = []
        self.score = 0

    def spawn_lemming(self):
        # Spawn a new Lemming in the game world
        pass

    def assign_task(self, lemming):
        # Assign a task to a Lemming
        pass

    def check_collisions(self):
        # Check for collisions between Lemmings and obstacles
        pass

# Load the Lemming and obstacle images
lemming_image = pygame.image.load("lemming.png")
obstacle_image = pygame.image.load("obstacle.png")

# Add keyboard controls to move the Lemmings
keys = pygame.key.get_pressed()
if keys[pygame.K_LEFT]:
    lemming.direction = "left"
elif keys[pygame.K_RIGHT]:
    lemming.direction = "right"

# Draw the Lemmings and obstacles on the screen
screen.blit(lemming_image, (lemming.x, lemming.y))
screen.blit(obstacle_image, (obstacle.x, obstacle.y))


# Run the game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Draw the game elements
    pygame.display.update()


