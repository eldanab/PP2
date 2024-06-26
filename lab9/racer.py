import pygame
import sys
import random
import time
from pygame.locals import *

pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()

BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
COINS_COLLECTED = 0
TOTAL_WEIGHT_COLLECTED = 0  # Total weight of coins collected
COIN_WEIGHTS = [1, 2, 3]  # Different weights and images of coins
COIN_IMAGES = {
    1: "coin1.png",
    2: "coin2.png",
    3: "coin3.png"
}

font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

background = pygame.image.load("AnimatedStreet.png")

DISPLAYSURF = pygame.display.set_mode((400, 600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        global SCORE, SPEED
        self.rect.move_ip(0, SPEED)
        if self.rect.top > 600:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
            if SCORE % 10 == 0:  # Increase speed every 10 score
                SPEED += 0.5


# Class for coins
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.weight = random.choice(COIN_WEIGHTS)  # Randomly assign weight to the coin
        orig_image = pygame.image.load(COIN_IMAGES[self.weight])
        self.image = pygame.transform.scale(orig_image, (40, 40))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        self.rect.move_ip(0, SPEED)
        if self.rect.top > 600:
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)


P1 = Player()
E1 = Enemy()

enemies = pygame.sprite.Group()
coins = pygame.sprite.Group()  # Group for coins
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)

INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

# New User event for coin generation
CREATE_COIN = pygame.USEREVENT + 2
pygame.time.set_timer(CREATE_COIN, 3000)

MainGame = 0
Pause = 1

gamestate = MainGame

while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.5
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == CREATE_COIN:  # Handle coin creation event
            new_coin = Coin()
            coins.add(new_coin)
            all_sprites.add(new_coin)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if gamestate == MainGame:
                    gamestate = Pause
                else:
                    gamestate = MainGame

    DISPLAYSURF.blit(background, (0, 0))
    scores = font_small.render("Score: " + str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10, 10))  # Coin collection
    coins_collected_text = font_small.render(
        "Coins Collected: " + str(TOTAL_WEIGHT_COLLECTED), True, BLACK
    )
    DISPLAYSURF.blit(coins_collected_text, (200, 10))

    if gamestate == Pause:
        menu_font = pygame.font.SysFont('comicsansms', 20)
        menu_text = menu_font.render('Game Paused. Press SPACE to start', True, (0, 0, 0))
        menu_textRect = menu_text.get_rect()
        menu_textRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        DISPLAYSURF.blit(menu_text, menu_textRect)
    else:
        for entity in all_sprites:
            DISPLAYSURF.blit(entity.image, entity.rect)
            entity.move()

        coins_collected = pygame.sprite.spritecollide(P1, coins, True)
        for coin in coins_collected:
            COINS_COLLECTED += 1
            TOTAL_WEIGHT_COLLECTED += coin.weight

        if pygame.sprite.spritecollideany(P1, enemies):
            pygame.mixer.Sound("crash.wav").play()
            time.sleep(0.5)

            DISPLAYSURF.fill(RED)
            DISPLAYSURF.blit(game_over, (30, 250))

            pygame.display.update()
            for entity in all_sprites:
                entity.kill()
            time.sleep(2)
            pygame.quit()
            sys.exit()

    pygame.display.update()
    FramePerSec.tick(FPS)
