import pygame
pygame.init()

w, h = 800, 800
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("Red ball")
white = (255, 255, 255)
red = (255, 0, 0)

r = 25
x = w // 2
y = h // 2

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y = max(y - 20, r)
            elif event.key == pygame.K_DOWN:
                y = min(y + 20, h - r)
            elif event.key == pygame.K_RIGHT:
                x = min(x + 20, w - r)
            elif event.key == pygame.K_LEFT:
                x = max(x - 20, r)
    screen.fill(white)
    pygame.draw.circle(screen, red, (x, y), r)
    pygame.display.flip()