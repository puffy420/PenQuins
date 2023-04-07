#PenQuins

import sys
sys.path.append('/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages')
import pygame
import random
import math
import time

# initialize Pygame
pygame.init()

# set up the window display
WIDTH, HEIGHT = 800, 600
display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ball Drop Game")

# set up colors
PINK = (255, 192, 203)
BLUE = (135, 206, 250)
WHITE = (255, 255, 255)

# set up fonts
FONT = pygame.font.SysFont("Arial", 30)

# set up variables
GRAVITY = 0.005
BALL_SIZE = 20
BALL_COUNT = 10
SCORE_PINK = 0
SCORE_BLUE = 0


# define Ball class
class Ball:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.velocity = 0
        self.scored = False
        self.drop_delay = random.uniform(0.1, 0.5)
        self.partner = None
        self.angular_velocity = 0

    def update(self):
        if self.drop_delay > 0:
            self.drop_delay -= GRAVITY
            return

        # update angular velocity if this ball is spinning with its partner
        if self.partner:
            self.angular_velocity = math.pi / 4

        self.velocity += GRAVITY
        self.y += self.velocity
        if self.y >= HEIGHT - BALL_SIZE:
            self.y = HEIGHT - BALL_SIZE
            self.velocity = 0

    def draw(self):
        # draw both this ball and its partner if it has one
        if self.partner:
            pygame.draw.circle(display, self.color, (int(self.x), int(self.y)), BALL_SIZE)
            pygame.draw.circle(display, self.partner.color, (int(self.partner.x), int(self.partner.y)), BALL_SIZE)
        else:
            pygame.draw.circle(display, self.color, (int(self.x), int(self.y)), BALL_SIZE)

    def bounce(self):
        self.velocity = -self.velocity

    def stop(self):
        self.velocity = 0

    def is_colliding(self, other):
        distance = math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
        return distance <= BALL_SIZE*2

    def score(self):
        if not self.scored:
            self.scored = True
            if self.color == PINK:
                global SCORE_PINK
                SCORE_PINK += 1
            else:
                global SCORE_BLUE
                SCORE_BLUE += 1

    def join(self, other):
        self.partner = other
        other.partner = self

    def spin(self):
        angle = math.atan2(self.partner.y - self.y, self.partner.x - self.x)
        dx = BALL_SIZE * math.cos(angle + self.angular_velocity) - BALL_SIZE * math.cos(angle)
        dy = BALL_SIZE * math.sin(angle + self.angular_velocity) - BALL_SIZE * math.sin(angle)
        self.x += dx
        self.y += dy
        self.partner.x -= dx
        self.partner.y -= dy

# game loop
running = True
while running:
    # reset the score
    SCORE_PINK = 0
    SCORE_BLUE = 0

    # create balls
    balls = []
    for i in range(BALL_COUNT):
        x = random.randint(BALL_SIZE, WIDTH - BALL_SIZE)
        y = random.randint(-HEIGHT, -BALL_SIZE)
        if i % 2 == 0:
            color = PINK
        else:
            color = BLUE
        ball = Ball(x, y, color)
        balls.append(ball)

    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # update balls
    for ball in balls:
        ball.update()
        if ball.y == HEIGHT - BALL_SIZE:
            ball.stop()
            ball.score()
        for other in balls:
            if ball != other and ball.is_colliding(other):
                if ball.color != other.color and not ball.partner and not other.partner:
                    ball.join(other)
                ball.bounce()
                other.bounce()
                if ball.partner:
                    ball.spin()

    # draw the screen
    display.fill(WHITE)
    for ball in balls:
        ball.draw()
    score_text = FONT.render(f"Score: Pink = {SCORE_PINK}, Blue = {SCORE_BLUE}", True, (0, 0, 0))
    display.blit(score_text, (10, 10))
    pygame.display.update()

# quit Pygame
pygame.quit()
