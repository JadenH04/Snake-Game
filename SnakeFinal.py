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
        self.score = 0
    def draw_snake(self):
        for block in self.body:
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
            pygame.draw.rect(screen, (70, 130, 180), block_rect)
    
    def move_snake(self):
        
        ##body_copy = self.body[:-1]
        #body_copy.insert(0,body_copy[0] + self.direction)
        ##self.body = body_copy[:]
        ##self.direction_locked = False  # Unlock direction changes after movement
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
        self.score = 0
    def draw_snake(self):
        for block in self.body:
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
            pygame.draw.rect(screen, (183, 111, 122), block_rect)
    
    def move_snake(self):
        
        ##body_copy = self.body[:-1]
        #body_copy.insert(0,body_copy[0] + self.direction)
        ##self.body = body_copy[:]
        ##self.direction_locked = False  # Unlock direction changes after movement
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
    game_over_surface = my_font.render('Arrow Keys win!', True, (255,100,25))
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
    game_over_surface = my_font.render('WASD Keys win!', True, (255,100,25))
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

def game_over():
    my_font = pygame.font.SysFont('times new roman', 30)
    game_over_surface = my_font.render('YOU DIED', True, (255,100,25))
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
                    fruit.__init__
                    return True
                if event.key == pygame.K_n:
                    main_menu()

pygame.init()
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
clock = pygame.time.Clock()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 125) #125 milliseconds


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
                    if game_over():
                        snake = SNAKE()
                        fruit = FRUIT()          
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

        screen.fill((175, 215, 70))
        fruit.draw_fruit()
        snake.draw_snake()
        pygame.display.update()
        clock.tick(30) 

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
        clock.tick(30)  


def main_menu():
    while True:
        my_font = pygame.font.SysFont('times new roman', 30)
        menu_text_surface = my_font.render('Press 1 for solo, Press 2 for 1v1s', True, (125,125,40))
        option_text_surface = my_font.render('Main Menu', True, (100,100,0))
        enter_text_surface = my_font.render('Press 3 to quit', True, (0,0,255))
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
                        return True
                    if event.key == pygame.K_2:
                        OneOnOne()
                        return True
                    if event.key == pygame.K_3:
                        pygame.QUIT()

main_menu()
           
