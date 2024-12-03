import pygame, sys, random, time
from pygame.math import Vector2
class SNAKE:
    def __init__(self):
        self.body = [Vector2(7, 10), Vector2(6, 10), Vector2(5, 10)]
        self.direction = (1,0)
        self.direction_locked = False  # To prevent multiple direction changes in one frame
        self.score = 0
    def draw_snake(self):
        for block in self.body:
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
            pygame.draw.rect(screen, (183, 111, 122), block_rect)
    
    def move_snake(self):
        body_copy = self.body[:-1]
        body_copy.insert(0,body_copy[0] + self.direction)
        self.body = body_copy[:]
        self.direction_locked = False  # Unlock direction changes after movement
    
    def change_direction(self, new_direction):
        if not self.direction_locked and new_direction + self.direction != Vector2(0, 0):
            self.direction = new_direction
            self.direction_locked = True  # Lock direction changes until next move

class SNAKEOpp:
    def __init__(self):
        self.body = [Vector2(7, 1), Vector2(6, 1), Vector2(5, 1)]
        self.direction = (1,0)
        self.direction_locked = False
        self.blocked = False
        self.score = 0
    def draw_snake(self):
        for block in self.body:
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
            pygame.draw.rect(screen, (70, 130, 180), block_rect)
    
    def move_snake(self):
        self.body.insert(0, self.body[0] + self.direction)
        self.direction_locked = False

    def change_direction(self, new_direction):
        if not self.direction_locked and new_direction + self.direction != Vector2(0, 0):
            self.direction = new_direction
            self.direction_locked = True  # Lock direction changes until next move
    
class SNAKE1:
    def __init__(self):
        self.body = [Vector2(7, 18), Vector2(6, 18), Vector2(5, 18)]
        self.direction = (1,0)
        self.direction_locked = False
        self.blocked = False
        self.score = 0
    def draw_snake(self):
        for block in self.body:
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
            pygame.draw.rect(screen, (183, 111, 122), block_rect)
    
    def move_snake(self):
        self.body.insert(0, self.body[0] + self.direction)
        self.direction_locked = False

    def change_direction(self, new_direction):
        if not self.direction_locked and new_direction + self.direction != Vector2(0, 0):
            self.direction = new_direction
            self.direction_locked = True  # Lock direction changes until next move
class SNAKEImpact:
    def __init__(self, *body_positions, direction=(1, 0), color=(183, 111, 122)):
        if body_positions:
            self.body = [Vector2(pos) for pos in body_positions]
        else:
            # Default body positions if none are provided
            self.body = [Vector2(7, 18), Vector2(6, 18), Vector2(5, 18)]
        self.direction = Vector2(direction)
        self.direction_locked = False
        self.blocked = False
        self.color = color

    def draw_snake(self):
        for block in self.body:
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
            pygame.draw.rect(screen, self.color, block_rect)
    
    def move_snake(self):
        self.body.insert(0, self.body[0] + self.direction)
        self.direction_locked = False

    def change_direction(self, new_direction):
        if not self.direction_locked and new_direction + self.direction != Vector2(0, 0):
            self.direction = new_direction
            self.direction_locked = True  # Lock direction changes until next move

class FRUIT:
    def __init__(self):
        self.x = random.randint(0, cell_number - 1)        
        self.y = random.randint(0, cell_number - 1)
        self.pos = pygame.math.Vector2(self.x,self.y)
  
    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y*cell_size), cell_size, cell_size)
        pygame.draw.rect(screen, (126, 166, 114), fruit_rect)


pygame.init()
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
clock = pygame.time.Clock()

fruit = FRUIT()
snake = SNAKE()
snakeopp = SNAKEOpp()

def arrow_win():
    my_font = pygame.font.SysFont('times new roman', 30)
    game_over_surface = my_font.render('Red win!', True, (255,100,25))
    restart_text_surface = my_font.render('Press Y to restart, Press N to return to menu', True, (255,100,0))
    game_over_rect = game_over_surface.get_rect()
    restart_text_rect = restart_text_surface.get_rect()
    game_over_rect.midtop = (400, 400)
    restart_text_rect.midtop = (400, 700)
    screen.fill((0,0,0))
    screen.blit(game_over_surface, game_over_rect)
    screen.blit(restart_text_surface, restart_text_rect)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Check for the window close event
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    snake.__init__
                    snakeopp.__init__
                    return True
                if event.key == pygame.K_n:
                    main_menu()

def wasd_win():
    my_font = pygame.font.SysFont('times new roman', 30)
    game_over_surface = my_font.render('Blue win!', True, (255,100,25))
    restart_text_surface = my_font.render('Press Y to restart, Press N to return to menu', True, (255,100,0))
    game_over_rect = game_over_surface.get_rect()
    restart_text_rect = restart_text_surface.get_rect()
    game_over_rect.midtop = (400, 400)
    restart_text_rect.midtop = (400, 700)
    screen.fill((0,0,0))
    screen.blit(game_over_surface, game_over_rect)
    screen.blit(restart_text_surface, restart_text_rect)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Check for the window close event
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    snake.__init__
                    snakeopp.__init__
                    return True
                if event.key == pygame.K_n:
                    main_menu()

pygame.init()
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
clock = pygame.time.Clock()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150) #125 milliseconds for a screen update

def solo():
    fruit = FRUIT()
    snake = SNAKE()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == SCREEN_UPDATE:
                snake.move_snake()
            # Eat Fruit :)
                if snake.body[0] == fruit.pos:
                    fruit.__init__()
                    snake.body.append(snake.body[-1])
                    snake.score += 5
                # Game over :(
                if (snake.body[0][0] > 19 or snake.body[0][0] < 0 or snake.body[0][1] > 19 or snake.body[0][1] < 0 or (snake.body[0] in snake.body[1:])):                
                    game_over(snake)   
                    snake = SNAKE()
                    fruit = FRUIT()    
        # WITH input delay
            if event.type == pygame.KEYDOWN:
                if event.key ==  pygame.K_UP and snake.direction != Vector2(0, 1):
                    snake.change_direction(Vector2(0, -1))
                elif event.key == pygame.K_DOWN and snake.direction != Vector2(0, -1):
                    snake.change_direction(Vector2(0, 1))
                elif event.key == pygame.K_LEFT and snake.direction != Vector2(1, 0):
                    snake.change_direction(Vector2(-1, 0))
                elif event.key == pygame.K_RIGHT and snake.direction != Vector2(-1, 0):
                    snake.change_direction(Vector2(1, 0))  

        screen.fill((175, 215, 70))
        fruit.draw_fruit()
        snake.draw_snake()
        pygame.display.update()
        clock.tick(60) 

def game_over(snake):
    my_font = pygame.font.SysFont('times new roman', 30)
    game_over_surface = my_font.render('YOU DIED', True, (255,0,0))
    restart_text_surface = my_font.render('Press Y to restart, Press N for menu', True, (255,100,0))
    score_text_surface = my_font.render(f"Score: {str(snake.score)}", True, (0,0,255))
    game_over_rect = game_over_surface.get_rect()
    restart_text_rect = restart_text_surface.get_rect()
    score_text_rect = score_text_surface.get_rect()
    game_over_rect.midtop = (400, 400)
    score_text_rect.midtop = (400, 100)
    restart_text_rect.midtop = (400, 700)
    screen.fill((0,0,0))
    screen.blit(game_over_surface, game_over_rect)
    screen.blit(restart_text_surface, restart_text_rect)
    screen.blit(score_text_surface, score_text_rect)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Check for the window close event
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    snake.__init__
                    fruit.__init__
                    return True
                if event.key == pygame.K_n:
                    main_menu()

def OneOnOne():
    snakeopp = SNAKEOpp()
    snake = SNAKE1()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == SCREEN_UPDATE:
                snake.move_snake()
                snakeopp.move_snake()
                # Winner
                if (snake.body[0][0] > 19 or snake.body[0][0] < 0 or snake.body[0][1] > 19 or snake.body[0][1] < 0 or (snake.body[0] in snake.body[1:]) or (snake.body[0] in snakeopp.body[1:])):                
                    if wasd_win():
                        snake = SNAKE1()
                        snakeopp = SNAKEOpp()        
                elif (snakeopp.body[0][0] > 19 or snakeopp.body[0][0] < 0 or snakeopp.body[0][1] > 19 or snakeopp.body[0][1] < 0 or (snakeopp.body[0] in snakeopp.body[1:]) or (snakeopp.body[0] in snake.body[1:])):                
                    if arrow_win():
                        snake = SNAKE1()
                        snakeopp = SNAKEOpp()
        # Add input delay based off of screen update time or tickrate?
            if event.type == pygame.KEYDOWN:
                if event.key ==  pygame.K_UP and snake.direction != Vector2(0, 1):
                   snake.change_direction(Vector2(0, -1))
                elif event.key == pygame.K_DOWN and snake.direction != Vector2(0, -1):
                    snake.change_direction(Vector2(0, 1))
                elif event.key == pygame.K_LEFT and snake.direction != Vector2(1, 0):
                     snake.change_direction(Vector2(-1, 0))
                elif event.key == pygame.K_RIGHT and snake.direction != Vector2(-1, 0):
                    snake.change_direction(Vector2(1, 0))             
            if event.type == pygame.KEYDOWN:
                if event.key ==  pygame.K_w and snakeopp.direction != Vector2(0, 1):
                    snakeopp.change_direction(Vector2(0, -1))
                elif event.key == pygame.K_s and snakeopp.direction != Vector2(0, -1):
                    snakeopp.change_direction(Vector2(0, 1))
                elif event.key == pygame.K_a and snakeopp.direction != Vector2(1, 0):
                    snakeopp.change_direction(Vector2(-1, 0))
                elif event.key == pygame.K_d and snakeopp.direction != Vector2(-1, 0):
                    snakeopp.change_direction(Vector2(1, 0))  
        screen.fill((175, 215, 70))
        snakeopp.draw_snake()
        snake.draw_snake()
        pygame.display.update()
        clock.tick(60)  
def decayMode():
    snakeopp = SNAKEImpact((7, 1), (6, 1), (5, 1), color = (70, 130, 180))
    snake1 = SNAKEImpact((7, 18), (6, 18), (5, 18))
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == SCREEN_UPDATE:
                # Handle blocked status but don't change direction automatically
                for current_snake1 in [snake1, snakeopp]:
                    if len(current_snake1.body) > 0:  # Prevent moving empty snakes.
                        next_pos = current_snake1.body[0] + current_snake1.direction
                        
                        # Check if the snake is blocked
                        if (
                            next_pos in snake1.body or
                            next_pos in snakeopp.body or
                            next_pos.x < 0 or
                            next_pos.x >= cell_number or
                            next_pos.y < 0 or
                            next_pos.y >= cell_number
                        ):
                            # The snake is blocked, so it should not move
                            current_snake1.blocked = True
                            current_snake1.body.pop()
                        else:
                            # The snake is not blocked, so it can move
                            current_snake1.blocked = False
                        
                        # Only move if the snake isn't blocked
                        if not current_snake1.blocked:
                            current_snake1.move_snake()

            # Handle game over (no respawning)
            if len(snake1.body) == 0:
                if wasd_win():
                    snake1 = SNAKE1()
                    snakeopp = SNAKEOpp()
            if len(snakeopp.body) == 0:
                if arrow_win():
                    snake1 = SNAKE1()
                    snakeopp = SNAKEOpp()
                
                
            if event.type == pygame.KEYDOWN:
                # Snake 1 Controls
                if event.key == pygame.K_UP and snake1.direction != Vector2(0, 1):
                    # Check if the forward-facing position is clear before changing direction
                    next_pos = snake1.body[0] + Vector2(0, -1)
                    if next_pos not in snake1.body and next_pos not in snakeopp.body and next_pos.y >= 0:
                        snake1.direction = Vector2(0, -1)
                        snake1.blocked = False
                elif event.key == pygame.K_DOWN and snake.direction != Vector2(0, -1):
                    # Check if the forward-facing position is clear before changing direction
                    next_pos = snake1.body[0] + Vector2(0, 1)
                    if next_pos not in snake1.body and next_pos not in snakeopp.body and next_pos.y < cell_number:
                        snake1.direction = Vector2(0, 1)
                        snake1.blocked = False
                elif event.key == pygame.K_LEFT and snake1.direction != Vector2(1, 0):
                    # Check if the forward-facing position is clear before changing direction
                    next_pos = snake1.body[0] + Vector2(-1, 0)
                    if next_pos not in snake1.body and next_pos not in snakeopp.body and next_pos.x >= 0:
                        snake1.direction = Vector2(-1, 0)
                        snake1.blocked = False
                elif event.key == pygame.K_RIGHT and snake1.direction != Vector2(-1, 0):
                    # Check if the forward-facing position is clear before changing direction
                    next_pos = snake1.body[0] + Vector2(1, 0)
                    if next_pos not in snake1.body and next_pos not in snakeopp.body and next_pos.x < cell_number:
                        snake1.direction = Vector2(1, 0)
                        snake1.blocked = False

                # Snake 2 Controls
                if event.key == pygame.K_w and snakeopp.direction != Vector2(0, 1):
                    # Check if the forward-facing position is clear before changing direction
                    next_pos = snakeopp.body[0] + Vector2(0, -1)
                    if next_pos not in snakeopp.body and next_pos not in snake.body and next_pos.y >= 0:
                        snakeopp.direction = Vector2(0, -1)
                        snakeopp.blocked = False
                elif event.key == pygame.K_s and snakeopp.direction != Vector2(0, -1):
                    # Check if the forward-facing position is clear before changing direction
                    next_pos = snakeopp.body[0] + Vector2(0, 1)
                    if next_pos not in snakeopp.body and next_pos not in snake1.body and next_pos.y < cell_number:
                        snakeopp.direction = Vector2(0, 1)
                        snakeopp.blocked = False
                elif event.key == pygame.K_a and snakeopp.direction != Vector2(1, 0):
                    # Check if the forward-facing position is clear before changing direction
                    next_pos = snakeopp.body[0] + Vector2(-1, 0)
                    if next_pos not in snakeopp.body and next_pos not in snake1.body and next_pos.x >= 0:
                        snakeopp.direction = Vector2(-1, 0)
                        snakeopp.blocked = False
                elif event.key == pygame.K_d and snakeopp.direction != Vector2(-1, 0):
                    # Check if the forward-facing position is clear before changing direction
                    next_pos = snakeopp.body[0] + Vector2(1, 0)
                    if next_pos not in snakeopp.body and next_pos not in snake1.body and next_pos.x < cell_number:
                        snakeopp.direction = Vector2(1, 0)
                        snakeopp.blocked = False

        # Drawing all elements
        screen.fill((175, 215, 70))
        snake1.draw_snake()
        snakeopp.draw_snake()
        pygame.display.update()
        clock.tick(60)






def main_menu():
    while True:
        my_font = pygame.font.SysFont('times new roman', 30)
        menu_text_surface = my_font.render('Press 1 for solo, Press 2 for 1v1s, Press 3 for decay',  True, (125,125,40))
        option_text_surface = my_font.render('Main Menu', True, (100,100,0))
        enter_text_surface = my_font.render('Press 4 to quit', True, (0,0,255))
        menu_text_rect = menu_text_surface.get_rect()
        option_text_rect = option_text_surface.get_rect()
        enter_text_rect = enter_text_surface.get_rect()
        menu_text_rect.midtop = (400, 400)
        option_text_rect.midtop = (400, 100)
        enter_text_rect.midtop = (400, 700)
        screen.fill((175, 215, 70))
        screen.blit(menu_text_surface, menu_text_rect)
        screen.blit(option_text_surface, option_text_rect)
        screen.blit(enter_text_surface, enter_text_rect)
        pygame.display.update()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        solo()
                    if event.key == pygame.K_2:
                        OneOnOne()
                    if event.key == pygame.K_3:
                        decayMode()
                    if event.key == pygame.K_4:
                        pygame.quit()
                        sys.exit()

main_menu()
           
