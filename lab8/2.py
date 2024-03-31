import pygame 
import random
pygame.init()

# Constants
W, H = 1200, 800
FPS = 60

# Initialize screen
screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)
clock = pygame.time.Clock()
done = False
bg = (0, 0, 0)

# Paddle settings
paddleW = 150
paddleH = 25
paddleSpeed = 20
paddle = pygame.Rect(W // 2 - paddleW // 2, H - paddleH - 30, paddleW, paddleH)
initial_paddleW = paddleW

# Ball settings
ballRadius = 20
ballSpeed = 6
ball_rect = int(ballRadius * 2 ** 0.5)
ball = pygame.Rect(random.randrange(ball_rect, W - ball_rect), H // 2, ball_rect, ball_rect)
dx, dy = 1, -1

# Game score
game_score = 0
game_score_fonts = pygame.font.SysFont('comicsansms', 40)
game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (0, 0, 0))
game_score_rect = game_score_text.get_rect()
game_score_rect.center = (210, 20)

# Catching sound
collision_sound = pygame.mixer.Sound('catch.mp3')

# Function to detect collision
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

# Block settings
block_list = [pygame.Rect(10 + 120 * i, 50 + 70 * j, 100, 50) for i in range(10) for j in range(4)]
color_list = [(random.randrange(0, 255), random.randrange(0, 255),  random.randrange(0, 255)) for i in range(10) for j in range(4)]

# List of unbreakable bricks
unbreakable_bricks = [random.choice(block_list) for _ in range(5)]

# Game over screen
losefont = pygame.font.SysFont('comicsansms', 40)
losetext = losefont.render('Game Over', True, (255, 255, 255))
losetextRect = losetext.get_rect()
losetextRect.center = (W // 2, H // 2)

# Win screen
winfont = pygame.font.SysFont('comicsansms', 40)
wintext = winfont.render('You win yay', True, (0, 0, 0))
wintextRect = wintext.get_rect()
wintextRect.center = (W // 2, H // 2)

# Main game loop
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(bg)
    
    # Drawing blocks
    for i, block in enumerate(block_list):
        if block in unbreakable_bricks:
            pygame.draw.rect(screen, (255, 255, 255), block)  # Unbreakable bricks in white
        else:
            pygame.draw.rect(screen, color_list[i], block)  # Regular bricks
    
    pygame.draw.rect(screen, pygame.Color(255, 255, 255), paddle)
    pygame.draw.circle(screen, pygame.Color(255, 0, 0), ball.center, ballRadius)

    # Ball movement
    ballSpeed += 0.005
    ball.x += ballSpeed * dx
    ball.y += ballSpeed * dy

    # Collision with screen boundaries
    if ball.centerx < ballRadius or ball.centerx > W - ballRadius:
        dx = -dx
    if ball.centery < ballRadius + 50: 
        dy = -dy

    # Collision with paddle
    if ball.colliderect(paddle) and dy > 0:
        dx, dy = detect_collision(dx, dy, ball, paddle)
        paddleW -= 5
        paddle.width = max(paddleW, 10)
    # Collision with blocks
    for block in block_list[:]:  # Iterate over a copy of block_list
        if block.colliderect(ball):
            if block not in unbreakable_bricks:
                block_list.remove(block)
                color_list.pop(0)  # Assuming color_list is modified correspondingly
                dx, dy = detect_collision(dx, dy, ball, block)
                game_score += 1
                collision_sound.play()
            else:
                dx, dy = detect_collision(dx, dy, ball, block)
        
    # Update game score
    game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (255, 255, 255))
    screen.blit(game_score_text, game_score_rect)
    
    # Win/lose screens
    if ball.bottom > H:
        screen.fill((0, 0, 0))
        screen.blit(losetext, losetextRect)
    elif not len(block_list):
        screen.fill((255, 255, 255))
        screen.blit(wintext, wintextRect)

    # Paddle control
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and paddle.left > 0:
        paddle.left -= paddleSpeed
    if key[pygame.K_RIGHT] and paddle.right < W:
        paddle.right += paddleSpeed

    pygame.display.flip()
    clock.tick(FPS) 
