import pygame
import random
def get_random_position():
    x = random.randint(0, GAME_WIDTH - SQUARE_SIZE)
    y = random.randint(0, GAME_HEIGHT - SQUARE_SIZE)
    return x, y

# Draw the square at a random position
def draw_square(window, x, y):
    pygame.draw.rect(window, SQUARE_COLOR, (x, y, SQUARE_SIZE, SQUARE_SIZE))