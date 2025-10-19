import random
import  pygame


pygame.init()

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption("snake XP")

FPS = 20
clock = pygame.time.Clock()

SNAKE_SIZE = 20
head_x = WINDOW_WIDTH // 2
head_y = WINDOW_HEIGHT //2 + 100

snake_dx = 0
snake_dy = 0



score = 0

GREEN = (0,255,0)
DARKGREEN = ( 10, 50, 10)
RED = ( 255 , 0 , 0)
DARKRED = ( 150, 0 , 0 )
WHITE = (255, 255, 255)
ELECTRIC_BLUE = (125, 249, 255)
ELECTRIC_PURPLE = (191,0,255)
HOT_PINK = (255,105,180)

font = pygame.font.SysFont('gabriola', 48)

title_text = font.render("Snake", True, GREEN, DARKGREEN)
title_rect = title_text.get_rect()
title_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT //2)

score_text = font.render("Score: " + str(score), GREEN, DARKRED)
score_rect = score_text.get_rect()
score_rect.topleft = (10,10)

game_over_text = font.render("GAMEOVER", True, RED, DARKGREEN)
game_over_rect = game_over_text.get_rect()
game_over_rect.center = (WINDOW_WIDTH//2 , WINDOW_HEIGHT//2)

continue_text = font.render("press any key to play again", True, RED, DARKGREEN)
continue_rect = continue_text.get_rect()
continue_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 64)

#Sound

#Images

border_apple_coord = (random.randint(0, WINDOW_WIDTH), random.randint(0, WINDOW_HEIGHT), SNAKE_SIZE,
                                   SNAKE_SIZE)
magic_apple_start_coord = (random.randint(0, WINDOW_WIDTH), random.randint(0, WINDOW_HEIGHT), SNAKE_SIZE,
                                   SNAKE_SIZE)

magic_apple_end_coord = (random.randint(0, WINDOW_WIDTH), random.randint(0, WINDOW_HEIGHT), SNAKE_SIZE,
                                 SNAKE_SIZE)

apple_coord = (500, 500, SNAKE_SIZE, SNAKE_SIZE)
apple_rect = pygame.draw.rect(display_surface,RED,apple_coord)

head_coord = (head_x, head_y, SNAKE_SIZE , SNAKE_SIZE)
head_rect = pygame.draw.rect(display_surface,GREEN,head_coord)

body_coords = []

#events
SPAWN_TELEPORT = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWN_TELEPORT,40000)
show_teleport = False
teleport_duration = 0

SPAWN_BORDER_BOUNCE = pygame.USEREVENT + 2
pygame.time.set_timer(SPAWN_BORDER_BOUNCE,30000)
show_border_bounce = False
border_bounce_duration = 0




class Snake(pygame.sprite.Sprite):
    """ Moves a snacke the screen"""

    def __init__(self):
        pygame.sprite.Sprite.__init__(self) # initializing sprite
        self.snake_dx = 0
        self.snake_dy = 0
        self.rect = pygame.draw.rect(display_surface,GREEN,head_coord)
        self.head_coord = (head_x, head_y, SNAKE_SIZE , SNAKE_SIZE)
        self.image = pygame.Surface([SNAKE_SIZE,SNAKE_SIZE])
        self.image.fill(GREEN)
        self.head_x = WINDOW_WIDTH // 2
        self.head_y = WINDOW_HEIGHT // 2 + 100
        self.body_coords = []
        self.outter_limits = False
        self.collision_protection = False

    def move_left(self):
        self.snake_dx = -1 * SNAKE_SIZE
        self.snake_dy = 0  # move down
    def move_right(self): # up key
        self.snake_dx = 1 * SNAKE_SIZE
        self.snake_dy = 0  # move up
    def move_up(self):
        self.snake_dx = 0
        self.snake_dy = -1 * SNAKE_SIZE  # move right
    def move_down(self):
        self.snake_dx = 0
        self.snake_dy = 1 * SNAKE_SIZE  # move left

    def move_forward(self):
        self.body_coords.insert(0, self.head_coord)
        self.body_coords.pop()
        self.rect.x += self.snake_dx
        self.rect.y += self.snake_dy
        self.head_coord = (self.rect.x, self.rect.y, SNAKE_SIZE, SNAKE_SIZE)

        #border limit
        if (self.rect.left < 0 or self.rect.right > WINDOW_HEIGHT or self.rect.top < 0 or self.rect.bottom > WINDOW_HEIGHT or self.head_coord in self.body_coords) and not self.collision_protection:
            self.outter_limits = True

        elif self.collision_protection and self.head_coord not in self.body_coords:

                if self.rect.left <= 1:
                    self.rect.move_ip(0,25)
                    self.move_right()

                if self.rect.right >= WINDOW_WIDTH:
                    self.rect.move_ip(0, -25)
                    self.move_left()

                if self.rect.top <= 0:
                    self.rect.move_ip(-25, 0)
                    self.move_down()

                if self.rect.bottom >= WINDOW_HEIGHT:
                    self.rect.move_ip(25, 0)
                    self.move_up()


    def reached_outter_limits(self):
        return self.outter_limits

    def grow_body(self):
        self.body_coords.append(self.head_coord)

    def teleport_body(self, portal_end):
        self.rect.x = portal_end[0]
        self.rect.y = portal_end[1]
        self.head_coord = (self.rect.x, self.rect.y, SNAKE_SIZE, SNAKE_SIZE)

    def collison_protection_on(self):
        self.collision_protection = True
    def collison_protection_off(self):
        self.collision_protection = False

    def draw_body(self):
        for body in self.body_coords:
            pygame.draw.rect(display_surface, DARKGREEN, body)

    def eat(self, target):
        rect = self.rect
        return rect.colliderect(target)
    def reset(self):
        self.outter_limits = False

        self.rect.x = WINDOW_WIDTH // 2
        self.rect.y = WINDOW_HEIGHT // 2 + 100
        self.head_coord = (self.rect.x, self.rect.y, SNAKE_SIZE, SNAKE_SIZE)
        self.body_coords = []

        self.snake_dx = 0
        self.snake_dy = 0
    #
    # def un_swat(self):
    #     self.spray = False

snake = Snake()
snake_sprite = pygame.sprite.GroupSingle(snake)




running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running= False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake.move_left()
            if event.key == pygame.K_RIGHT:
                snake.move_right()
            if event.key == pygame.K_UP:
                snake.move_up()
            if event.key == pygame.K_DOWN:
                snake.move_down()
        elif event.type == SPAWN_TELEPORT:
            duration = random.choice([15000,30000,45000])
            show_teleport = True
            teleport_duration = pygame.time.get_ticks() + duration
        elif event.type == SPAWN_BORDER_BOUNCE:
            duration_bb = random.choice([20000, 60000, 20000])
            show_border_bounce = True
            border_bounce_duration = pygame.time.get_ticks() + duration_bb

    snake.move_forward()


    # check for game over
    # if head_rect.left < 0 or head_rect.right > WINDOW_HEIGHT or head_rect.top < 0 or head_rect.bottom > WINDOW_HEIGHT or head_coord in body_coords:



    if snake.eat(apple_rect):
        score += 1
        apply_x = random.randint(0 , WINDOW_WIDTH - SNAKE_SIZE)
        apple_y = random.randint(0, WINDOW_HEIGHT - SNAKE_SIZE)
        apple_coord= (apply_x,apple_y, SNAKE_SIZE, SNAKE_SIZE)

        snake.grow_body()







    score_text = font.render("Score: "+str(score) , True, GREEN, DARKGREEN)








    display_surface.fill(WHITE)
    #Blit hud
    display_surface.blit(title_text, title_rect)
    display_surface.blit(score_text, score_rect)

    snake_sprite.update()
    snake_sprite.draw(display_surface)


    #blit assets
    snake.draw_body()
    head_rect = pygame.draw.rect(display_surface,GREEN, head_coord)
    apple_rect = pygame.draw.rect(display_surface,RED, apple_coord)

    if show_teleport and pygame.time.get_ticks() < teleport_duration:

        magic_apple_start_rect = pygame.draw.rect(display_surface,ELECTRIC_BLUE, magic_apple_start_coord)
        magic_apple_end_rect = pygame.draw.rect(display_surface,ELECTRIC_PURPLE, magic_apple_end_coord)
        pygame.display.flip()

        if snake.eat(magic_apple_start_rect):

            snake.teleport_body(magic_apple_end_coord)

    if show_teleport and pygame.time.get_ticks() >= teleport_duration:
        show_teleport = False

    if show_border_bounce and pygame.time.get_ticks() < border_bounce_duration:

        border_apple_rect = pygame.draw.rect(display_surface,HOT_PINK, border_apple_coord)
        pygame.display.flip()

        if snake.eat(border_apple_rect):
            snake.collison_protection_on()

    if show_border_bounce and pygame.time.get_ticks() >= border_bounce_duration:
        show_border_bounce = False
        snake.collison_protection_off()


    if snake.reached_outter_limits():
        display_surface.blit(game_over_text, game_over_rect)
        display_surface.blit(continue_text, continue_rect)
        pygame.display.update()

        is_paused = True
        while is_paused:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    score = 0
                    snake.reset()
                    is_paused = False

                if event.type == pygame.QUIT:
                    is_paused = False
                    running = False

    pygame.display.flip()
    clock.tick(FPS)


pygame.quit()