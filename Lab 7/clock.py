import pygame
import sys
from datetime import datetime

pygame.init()

window_size = (930, 930)
window = pygame.display.set_mode(window_size)
pygame.display.set_caption("Clock")

clock_img = pygame.image.load("C:\D_Files\KBTU_coding\Python\PP2_2024-Serikbai-\Lab 7\clock.png")
minute_hand_image = pygame.image.load("C:\D_Files\KBTU_coding\Python\PP2_2024-Serikbai-\Lab 7\minute_hand.png")
second_hand_image = pygame.image.load("C:\D_Files\KBTU_coding\Python\PP2_2024-Serikbai-\Lab 7\seconds_hand.png")

clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

def draw_clock():
    window.fill((255, 255, 255))

    window.blit(clock_img, (0, 0))

    current_time = datetime.now().time()
    hour = current_time.hour
    minute = current_time.minute
    second = current_time.second

    text_surface = font.render(f"{hour:02}:{minute:02}:{second:02}", True, (0, 0, 0))
    window.blit(text_surface, (150, 20))

    minute_angle = (minute * 360) / 60 - 90  
    minute_hand = pygame.transform.rotate(minute_hand_image, -minute_angle)
    minute_hand_rect = minute_hand.get_rect()
    minute_hand_rect.center = (465, 465)
    window.blit(minute_hand, minute_hand_rect)

    second_angle = (second * 360) / 60 - 90
    second_hand = pygame.transform.rotate(second_hand_image, -second_angle)
    second_hand_rect = second_hand.get_rect()
    second_hand_rect.center = (465, 465)
    window.blit(second_hand, second_hand_rect)

    pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    draw_clock()
    clock.tick(60)

pygame.quit()
sys.exit()