# Import necessary libraries
import pygame
import time
import random

# Initialize Pygame
pygame.init()

# Define colors
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Set the dimensions of the game window
dis_width = 800
dis_height = 600

# Create the game window
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake')

# Set up the clock for controlling the game's speed
clock = pygame.time.Clock()

# Define the size of the snake block and the snake's speed
snake_block_size = 20
snake_speed = 15

# Define the font styles for the score and messages
font_style = pygame.font.SysFont("arial", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# Define a function to display the score
def display_score(score):
    value = score_font.render("Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])

# Define a function to display the level
def display_level(score):
    level = score // 5 + 1
    value = score_font.render("Level:" + str(level), True, red)
    dis.blit(value, [0, 50])

# Define a function to draw the snake
def draw_snake(snake_block_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block_size, snake_block_size])

# Define a function to display messages
def display_message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])
# Define the main game loop
def game_loop():
    # Set up initial game state
    game_over = False
    game_close = False

    x1 = dis_width // 2
    y1 = dis_height // 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    snake_length = 1

    # Initialize snake speed
    snake_speed = 15

    # Green apple
    foodx1 = random.randrange(60, dis_width - snake_block_size * 2, snake_block_size)  
    foody1 = random.randrange(60, dis_height - snake_block_size * 2, snake_block_size)  

    # Yellow apple
    foodx2 = random.randrange(60, dis_width - snake_block_size * 2, snake_block_size)  
    foody2 = random.randrange(60, dis_height - snake_block_size * 2, snake_block_size)  

    # Time tracking for yellow fruit
    last_yellow_fruit_time = pygame.time.get_ticks()
    yellow_fruit_visible = False

    # Initialize level
    level = 1

    # Game loop
    while not game_over:
        while game_close == True:
            dis.fill(blue)
            display_message("You Lost! Press C-Continue or Q-Quit", red)
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
                game_close = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y1_change = -snake_block_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block_size
                    x1_change = 0
                elif event.key == pygame.K_LEFT:
                    x1_change = -snake_block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block_size
                    y1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        else:
            x1 += x1_change
            y1 += y1_change

        # Check for collision with green apple
        if x1 == foodx1 and y1 == foody1:
            foodx1 = random.randrange(0, dis_width - snake_block_size * 2, snake_block_size)  
            foody1 = random.randrange(0, dis_height - snake_block_size * 2, snake_block_size)  
            snake_length += 1
            display_level(level)

        # Check for collision with yellow apple
        if x1 == foodx2 and y1 == foody2:
            if yellow_fruit_visible:
                foodx2 = random.randrange(0, dis_width - snake_block_size * 2, snake_block_size)  
                foody2 = random.randrange(0, dis_height - snake_block_size * 2, snake_block_size)  
                snake_length += 2
                yellow_fruit_visible = False

        # Check for collision with snake
        for block in snake_list[:-1]:
            if x1 == block[0] and y1 == block[1]:
                game_close = True

        # Add the new snake block
        snake_list.append([x1, y1])

        # Remove the last block if the snake has grown
        if len(snake_list) > snake_length:
            del snake_list[0]

        # Draw the background
        dis.fill(blue)

        # Draw the green apple
        pygame.draw.rect(dis, green, [foodx1, foody1, snake_block_size, snake_block_size])

        # Draw the yellow apple if it's visible
        if yellow_fruit_visible:
            pygame.draw.rect(dis, yellow, [foodx2, foody2, snake_block_size, snake_block_size])

        # Draw the snake
        draw_snake(snake_block_size, snake_list)

        # Display the score and level
        display_level(snake_length -1)
        display_score(snake_length - 1)

        # Update the display
        pygame.display.update()

        # Control the game's speed
        clock.tick(snake_speed)

        # Check if it's time to spawn a yellow fruit
        if not yellow_fruit_visible and pygame.time.get_ticks() - last_yellow_fruit_time > 15000:
            last_yellow_fruit_time = pygame.time.get_ticks()
            foodx2 = random.randrange(0, dis_width - snake_block_size * 2, snake_block_size)  
            foody2 = random.randrange(0, dis_height - snake_block_size * 2, snake_block_size)  
            yellow_fruit_visible = True

    # Quit Pygame
    pygame.quit()
    quit()

# Start the game
game_loop()
