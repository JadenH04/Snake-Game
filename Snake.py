import pygame, sys, random, time
from pygame.math import Vector2
class SNAKE:
    def __init__(self):
        self.body = [Vector2(7, 10), Vector2(6, 10), Vector2(5, 10)]
        self.direction = (1,0)
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

def game_over():
    my_font = pygame.font.SysFont('times new roman', 30)
    game_over_surface = my_font.render('YOU DIED', True, (255,0,0))
    restart_text_surface = my_font.render('Press Y to restart, Press N to quit', True, (255,100,0))
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
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    snake.__init__
                    fruit.__init__
                    return True
                if event.key == pygame.K_n:
                    pygame.QUIT()
                    sys.exit()
pygame.init()
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
clock = pygame.time.Clock()

fruit = FRUIT()
snake = SNAKE()


SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150) #150 milliseconds
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
            if (
               snake.body[0][0] > 19 or snake.body[0][0] < 0 or snake.body[0][1] > 19 or snake.body[0][1] < 0 or (snake.body[0] in snake.body[1:])
            ):                
                if game_over():
                    snake = SNAKE()
                    fruit = FRUIT()
            
         #   for block in snake.body[1:]:
          #      if block == snake.body[0]:
           #         if game_over():
            #            snake = SNAKE()
             #           fruit = FRUIT()

                
        # Add input delay based off of screen update time or tickrate?
        if event.type == pygame.KEYDOWN:
            if event.key ==  pygame.K_UP and snake.direction != Vector2(0, 1):
                snake.direction = Vector2(0, -1)
            elif event.key == pygame.K_DOWN and snake.direction != Vector2(0, -1):
                snake.direction = Vector2(0, 1)
            elif event.key == pygame.K_LEFT and snake.direction != Vector2(1, 0):
                snake.direction = Vector2(-1, 0)
            elif event.key == pygame.K_RIGHT and snake.direction != Vector2(-1, 0):
                snake.direction = Vector2(1, 0)               

        
    screen.fill((175, 215, 70))
    fruit.draw_fruit()
    snake.draw_snake()
    pygame.display.update()
    clock.tick(30) 
