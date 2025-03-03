import pygame
import math

# Initialize pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 650
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Multiplayer Game")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Fonts
font = pygame.font.Font(None, 50)

# Player setup
player1 = pygame.Rect(50, 150, 40, 40)  # Red player
player2 = pygame.Rect(500, 150, 40, 40) # Blue player
goal = pygame.Rect(280, 50, 40, 40)     # Moving green goal

# Speed
speed = 8
angle = 0  # Angle for circular movement

# Game loop
running = True
winner = None  # Track the winner

while running:
    pygame.time.delay(30)  # Controls game speed

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Key controls
    keys = pygame.key.get_pressed()

    # Player 1 (WASD)
    if keys[pygame.K_w]: player1.y -= speed
    if keys[pygame.K_s]: player1.y += speed
    if keys[pygame.K_a]: player1.x -= speed
    if keys[pygame.K_d]: player1.x += speed

    # Player 2 (Arrow Keys)
    if keys[pygame.K_UP]: player2.y -= speed
    if keys[pygame.K_DOWN]: player2.y += speed
    if keys[pygame.K_LEFT]: player2.x -= speed
    if keys[pygame.K_RIGHT]: player2.x += speed

    # Move the goal in a circular path
    angle += 0.03  # Speed of movement
    goal.x = 280 + int(80 * math.cos(angle))  # Move in X direction
    goal.y = 150 + int(80 * math.sin(angle))  # Move in Y direction

    # Check for winner
    if player1.colliderect(goal):
        winner = "Player 1 Wins!"
        running = False
    elif player2.colliderect(goal):
        winner = "Player 2 Wins!"
        running = False

    # Draw everything
    screen.fill(WHITE)
    pygame.draw.rect(screen, RED, player1)
    pygame.draw.rect(screen, BLUE, player2)
    pygame.draw.rect(screen, GREEN, goal)

    pygame.display.update()

# Show the winner message before quitting
if winner:
    screen.fill(WHITE)
    text = font.render(winner, True, BLACK)
    screen.blit(text, (WIDTH//2 - 150, HEIGHT//2 - 30))

pygame.quit()
