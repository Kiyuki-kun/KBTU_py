import pygame
import random
import time

# Initialize pygame
pygame.init()

# Constants
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
FPS = 60

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Create screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Game")

# Clock for FPS
clock = pygame.time.Clock()

# Game variables
SPEED = 1
coins_collected = 0

# Classes
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("C:\D_Files\KBTU_coding\Python\PP2_2024-Serikbai-\Lab 8\_tsis8\enemy_car.png")
        self.image = pygame.transform.scale(self.image, (50, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        self.rect.move_ip(0, SPEED)
        if (self.rect.top > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("C:\D_Files\KBTU_coding\Python\PP2_2024-Serikbai-\Lab 8\_tsis8\main_car.png")
        self.image = pygame.transform.scale(self.image, (50, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[pygame.K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[pygame.K_RIGHT]:
                self.rect.move_ip(5, 0)


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("C:\D_Files\KBTU_coding\Python\PP2_2024-Serikbai-\Lab 8\_tsis8\coin.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(10, SCREEN_WIDTH - 10), random.randint(0, 100))

    def move(self):
        self.rect.move_ip(0, SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.top = 0
            self.rect.center = (random.randint(0, SCREEN_WIDTH - 10), random.randint(0, 100))
            
class SuperCoin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("C:\D_Files\KBTU_coding\Python\PP2_2024-Serikbai-\Lab 8\_tsis8\coin.png")
        self.image = pygame.transform.scale(self.image, (75, 75))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(10, SCREEN_WIDTH - 10), random.randint(0, 100))

    def move(self):
        self.rect.move_ip(0, SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.top = 0
            self.rect.center = (random.randint(0, SCREEN_WIDTH - 10), random.randint(0, 100))


# Setting up Sprites
P1 = Player()
E1 = Enemy()
C1 = Coin()
SC1 = SuperCoin()

# Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
coins = pygame.sprite.Group()
coins.add(C1)
all_sprites.add(C1)
supercoins = pygame.sprite.Group()

# Adding a new User event
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

# Initialize supercoin_timer to 5 seconds (10000 milliseconds)
supercoin_timer = 10000

# Game Loop
while True:
    # Cycles through all events occuring
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 1

        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Increment the SuperCoin timer
    supercoin_timer -= clock.get_time()

    # Create a new SuperCoin instance after 10 seconds
    if supercoin_timer <= 0:
        SC1 = SuperCoin()
        all_sprites.add(SC1)
        coins.add(SC1)
        supercoin_timer = 10000

    #collision with coin
    if pygame.sprite.spritecollide(P1, coins, False):
        for coin in pygame.sprite.spritecollide(P1, coins, False):
            if isinstance(coin, SuperCoin):
                # Display the ending screen
                screen.fill((0, 0, 0))
                font = pygame.font.Font(None, 72)
                text = font.render("Congratulations!", True, WHITE)
                screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2 - text.get_height() // 2))
                pygame.display.flip()
                time.sleep(2)
                pygame.quit()
                exit()
            else:
                coins_collected += 1
                SPEED += 1
                coin.rect.center = (random.randint(0, SCREEN_WIDTH - 10), random.randint(0, 100))

    #collision with enemy
    if pygame.sprite.spritecollide(P1, enemies, False):
        screen.fill((0, 0, 0))
        font = pygame.font.Font(None, 72)
        text = font.render("YOU DIED", True, WHITE)
        screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2 - text.get_height() // 2))
        pygame.display.flip()
        time.sleep(2)
        pygame.quit()
        exit()

    # Game logic
    screen.fill((128, 128, 128))
    P1.move()
    E1.move()
    C1.move()
    SC1.move()

    # Drawing game objects
    all_sprites.draw(screen)

    # Text
    font = pygame.font.Font(None, 36)
    text = font.render(f"Coins collected: {coins_collected}", True, WHITE)
    screen.blit(text, (0, 0))

    # Update
    pygame.display.flip()
    clock.tick(FPS)
