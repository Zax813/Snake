import pygame
import time
import random

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Initialize the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake Game - PvP')

# Clock for controlling the game speed
clock = pygame.time.Clock()

# Snake block size and speed
BLOCK_SIZE = 20
SPEED = 15

# Font for text
define_font = pygame.font.SysFont("comicsansms", 35)

def display_message(msg, color):
    message = define_font.render(msg, True, color)
    screen.blit(message, [WIDTH / 4, HEIGHT / 2])

def draw_snake(block_size, snake_list, color):
    for block in snake_list:
        pygame.draw.rect(screen, color, [block[0], block[1], block_size, block_size])

def game_loop():
    game_over = False
    game_close = False

    # Player 1 initial position and controls
    x1 = WIDTH / 4
    y1 = HEIGHT / 2
    x1_change = 0
    y1_change = 0
    snake_list1 = []
    length_of_snake1 = 1

    # Player 2 initial position and controls
    x2 = 3 * WIDTH / 4
    y2 = HEIGHT / 2
    x2_change = 0
    y2_change = 0
    snake_list2 = []
    length_of_snake2 = 1

    # Food coordinates
    food_x = round(random.randrange(0, WIDTH - BLOCK_SIZE) / 20.0) * 20.0
    food_y = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / 20.0) * 20.0

    while not game_over:

        while game_close:
            screen.fill(BLACK)
            display_message("Game Over! Press Q-Quit or C-Play Again", RED)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                # Player 1 controls
                if event.key == pygame.K_LEFT:
                    x1_change = -BLOCK_SIZE
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = BLOCK_SIZE
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -BLOCK_SIZE
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = BLOCK_SIZE
                    x1_change = 0

                # Player 2 controls
                if event.key == pygame.K_a:
                    x2_change = -BLOCK_SIZE
                    y2_change = 0
                elif event.key == pygame.K_d:
                    x2_change = BLOCK_SIZE
                    y2_change = 0
                elif event.key == pygame.K_w:
                    y2_change = -BLOCK_SIZE
                    x2_change = 0
                elif event.key == pygame.K_s:
                    y2_change = BLOCK_SIZE
                    x2_change = 0

        # Check for collisions with walls
        if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0:
            game_close = True
        if x2 >= WIDTH or x2 < 0 or y2 >= HEIGHT or y2 < 0:
            game_close = True

        # Update positions
        x1 += x1_change
        y1 += y1_change
        x2 += x2_change
        y2 += y2_change

        screen.fill(BLACK)
        pygame.draw.rect(screen, BLUE, [food_x, food_y, BLOCK_SIZE, BLOCK_SIZE])

        # Update snake 1
        snake_head1 = []
        snake_head1.append(x1)
        snake_head1.append(y1)
        snake_list1.append(snake_head1)
        if len(snake_list1) > length_of_snake1:
            del snake_list1[0]

        # Update snake 2
        snake_head2 = []
        snake_head2.append(x2)
        snake_head2.append(y2)
        snake_list2.append(snake_head2)
        if len(snake_list2) > length_of_snake2:
            del snake_list2[0]

        # Check for collisions with self or opponent
        for block in snake_list1[:-1]:
            if block == snake_head1 or block == snake_head2:
                game_close = True
        for block in snake_list2[:-1]:
            if block == snake_head2 or block == snake_head1:
                game_close = True

        draw_snake(BLOCK_SIZE, snake_list1, GREEN)
        draw_snake(BLOCK_SIZE, snake_list2, YELLOW)
        pygame.display.update()

        # Check if food is eaten
        if x1 == food_x and y1 == food_y:
            food_x = round(random.randrange(0, WIDTH - BLOCK_SIZE) / 20.0) * 20.0
            food_y = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / 20.0) * 20.0
            length_of_snake1 += 1
        if x2 == food_x and y2 == food_y:
            food_x = round(random.randrange(0, WIDTH - BLOCK_SIZE) / 20.0) * 20.0
            food_y = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / 20.0) * 20.0
            length_of_snake2 += 1

        clock.tick(SPEED)

    pygame.quit()
    quit()

# Run the game
game_loop()
