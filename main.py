import pygame
from pygame.locals import *
import random

# Initialisatie van het spel
pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Cookie Monster!")
clock = pygame.time.Clock()

# Kleuren
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Cookie Monster instellingen
cookie_monster_image = pygame.image.load("monster.png")
cookie_monster_rect = cookie_monster_image.get_rect()
cookie_monster_rect.center = (width // 2, height - 100)
cookie_monster_speed = 5
cookie_monster_lives = 3

# Koekje instellingen
cookie_image = pygame.image.load('cookie.png')
cookie_rect = cookie_image.get_rect()
cookie_rect.center = (random.randint(50, width - 50), -100)
cookie_speed = 3

cookies = []

# Score
score = 0
font = pygame.font.Font(None, 36)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        cookie_monster_rect.x -= cookie_monster_speed
    if keys[pygame.K_RIGHT]:
        cookie_monster_rect.x += cookie_monster_speed

    # Nieuwe cookies toevoegen
    if len(cookies) < 3:
        new_cookie_rect = cookie_image.get_rect()
        new_cookie_rect.x = random.randint(50, width - 50)
        new_cookie_rect.y = -100
        cookies.append(new_cookie_rect)

    # Beweging van de cookies
    for cookie in cookies:
      cookie.y += cookie_speed

      # Koekje gevangen
    for cookie_rect in cookies:
        if cookie_rect.colliderect(cookie_monster_rect):
            score += 1
            cookies.remove(cookie_rect)
            new_cookie_rect = cookie_image.get_rect()
            new_cookie_rect.x = random.randint(50, width - 50)
            new_cookie_rect.y = -100
            cookies.append(new_cookie_rect)


    # Koekje gemist
    if cookie.y > height:
      cookies.remove(cookie)
      cookie_monster_lives -= 1
      new_cookie_rect = cookie_image.get_rect()
      new_cookie_rect.x = random.randint(50, width - 50)
      new_cookie_rect.y = -100
      cookies.append(new_cookie_rect)
        
    # Game over
    if cookie_monster_lives == 0:
        running = False
    Cookie_surface = pygame.image.load('cookie.png')
    Cookie_surface = pygame.transform.scale(Cookie_surface,(100,80))
    Monster_surface = pygame.image.load('monster.png')
    Monster_surface = pygame.transform.scale(Monster_surface,(200,180))
    # Achtergrond en tekenen van sprites
    screen.fill('LIGHTBLUE')
    screen.blit(Cookie_surface,(0,0))
    screen.blit(Monster_surface,(0,0))
    #screen.blit(cookie_image, cookie_rect)

    # Score en levens weergeven
    score_text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(score_text, (10, 10))
    lives_text = font.render("Lives: " + str(cookie_monster_lives), True, WHITE)
    screen.blit(lives_text, (width - 120, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
