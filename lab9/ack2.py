import pygame
import random
from enum import Enum

pygame.init()

W, H = 1200, 800
FPS = 60

screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)
clock = pygame.time.Clock()
done = False
bg = (0, 0, 0)

paddleW = 150
paddleH = 25
paddleSpeed = 20
paddle = pygame.Rect(W // 2 - paddleW // 2, H - paddleH - 30, paddleW, paddleH)
initial_paddleW = paddleW

ballRadius = 20
ballSpeed = 6
ball_rect = int(ballRadius * 2 ** 0.5)
ball = pygame.Rect(random.randrange(ball_rect, W - ball_rect), H // 2, ball_rect, ball_rect)
dx, dy = 1, -1

game_score = 0
game_score_fonts = pygame.font.SysFont('comicsansms', 40)
game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (0, 0, 0))
game_score_rect = game_score_text.get_rect()
game_score_rect.center = (210, 20)

collision_sound = pygame.mixer.Sound('catch.mp3')

def detect_collision(dx, dy, ball, rect):
    if dx > 0:
        delta_x = ball.right - rect.left
    else:
        delta_x = rect.right - ball.left
    if dy > 0:
        delta_y = ball.bottom - rect.top
    else:
        delta_y = rect.bottom - ball.top

    if abs(delta_x - delta_y) < 10:
        dx, dy = -dx, -dy
    if delta_x > delta_y:
        dy = -dy
    elif delta_y > delta_x:
        dx = -dx
    return dx, dy

block_list = [pygame.Rect(10 + 120 * i, 50 + 70 * j, 100, 50) for i in range(10) for j in range(4)]
color_list = [(random.randrange(0, 255), random.randrange(0, 255),  random.randrange(0, 255)) for i in range(10) for j in range(4)]

unbreakable_bricks = [random.choice(block_list) for _ in range(5)]

losefont = pygame.font.SysFont('comicsansms', 40)
losetext = losefont.render('Game Over', True, (255, 255, 255))
losetextRect = losetext.get_rect()
losetextRect.center = (W // 2, H // 2)

winfont = pygame.font.SysFont('comicsansms', 40)
wintext = winfont.render('You win yay', True, (0, 0, 0))
wintextRect = wintext.get_rect()
wintextRect.center = (W // 2, H // 2)

class GameState(Enum):
    MAIN_MENU = 0
    PLAYING = 1
    PAUSED = 2
    SETTINGS = 3

# Initial game state
game_state = GameState.MAIN_MENU

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                if game_state == GameState.PLAYING:
                    game_state = GameState.PAUSED
                elif game_state == GameState.PAUSED:
                    game_state = GameState.PLAYING
            elif event.key == pygame.K_s:
                if game_state == GameState.MAIN_MENU or game_state == GameState.PAUSED:
                    game_state = GameState.SETTINGS
            elif event.key == pygame.K_RETURN:
                if game_state == GameState.MAIN_MENU:
                    game_state = GameState.PLAYING
                elif game_state == GameState.SETTINGS:
                    game_state = GameState.MAIN_MENU

    screen.fill(bg)

    if game_state == GameState.MAIN_MENU:
        # Display main menu
        menu_font = pygame.font.SysFont('comicsansms', 50)
        menu_text = menu_font.render('Press ENTER to start, Press S to access settings', True, (255, 255, 255))
        menu_textRect = menu_text.get_rect()
        menu_textRect.center = (W // 2, H // 2)
        screen.blit(menu_text, menu_textRect)
    elif game_state == GameState.PLAYING:
        for i, block in enumerate(block_list):
            if block in unbreakable_bricks:
                pygame.draw.rect(screen, (255, 255, 255), block)  
            else:
                pygame.draw.rect(screen, color_list[i], block) 
        
        pygame.draw.rect(screen, pygame.Color(255, 255, 255), paddle)
        pygame.draw.circle(screen, pygame.Color(255, 0, 0), ball.center, ballRadius)

        ballSpeed += 0.005
        ball.x += ballSpeed * dx
        ball.y += ballSpeed * dy

        
        if ball.centerx < ballRadius or ball.centerx > W - ballRadius:
            dx = -dx
        if ball.centery < ballRadius + 50: 
            dy = -dy

       
        if ball.colliderect(paddle) and dy > 0:
            dx, dy = detect_collision(dx, dy, ball, paddle)
            paddleW -= 5
            paddle.width = max(paddleW, 10)
       
        for block in block_list[:]:  
            if block.colliderect(ball):
                if block not in unbreakable_bricks:
                    block_list.remove(block)
                    color_list.pop(0) 
                    dx, dy = detect_collision(dx, dy, ball, block)
                    game_score += 1
                    collision_sound.play()
                else:
                    dx, dy = detect_collision(dx, dy, ball, block)
        
        game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (255, 255, 255))
        screen.blit(game_score_text, game_score_rect)
        
        if ball.bottom > H:
            screen.fill((0, 0, 0))
            screen.blit(losetext, losetextRect)
        elif not len(block_list):
            screen.fill((255, 255, 255))
            screen.blit(wintext, wintextRect)

        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and paddle.left > 0:
            paddle.left -= paddleSpeed
        if key[pygame.K_RIGHT] and paddle.right < W:
            paddle.right += paddleSpeed

    elif game_state == GameState.PAUSED:
        pause_font = pygame.font.SysFont('comicsansms', 50)
        pause_text = pause_font.render('Game Paused. Press ESC to resume', True, (255, 255, 255))
        pause_textRect = pause_text.get_rect()
        pause_textRect.center = (W // 2, H // 2)
        screen.blit(pause_text, pause_textRect)
    elif game_state == GameState.SETTINGS:
        settings_font = pygame.font.SysFont('comicsansms', 50)
        settings_text = settings_font.render('Settings Menu. Press ENTER to go back', True, (255, 255, 255))
        settings_textRect = settings_text.get_rect()
        settings_textRect.center = (W // 2, H // 2)
        screen.blit(settings_text, settings_textRect)
        
        settings_text_speed = settings_font.render(f'Paddle Speed: {paddleSpeed}', True, (255, 255, 255))
        settings_textRect_speed = settings_text_speed.get_rect()
        settings_textRect_speed.center = (W // 2, H // 2 + 50)
        screen.blit(settings_text_speed, settings_textRect_speed)

    pygame.display.flip()
    clock.tick(FPS) 
