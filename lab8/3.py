import pygame
import sys
pygame.init()

WIDTH, HEIGHT = 800, 600

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Paint")
screen.fill(WHITE)

drawing_color = BLACK
eraser_color = WHITE
brush_size = 5
drawing_tool = "pencil"

def draw_shape(start_pos, end_pos):
    if drawing_tool == "rectangle":
        pygame.draw.rect(screen, drawing_color, (start_pos, (end_pos[0] - start_pos[0], end_pos[1] - start_pos[1])))
    elif drawing_tool == "circle":
        radius = max(abs(end_pos[0] - start_pos[0]), abs(end_pos[1] - start_pos[1])) // 2
        pygame.draw.circle(screen, drawing_color, (start_pos[0] + radius, start_pos[1] + radius), radius)
    else:
        pygame.draw.line(screen, drawing_color, start_pos, end_pos, brush_size)

def draw_color_options():
    color_options = [BLACK, RED, GREEN, BLUE, YELLOW]
    color_rects = []
    rect_width = 40
    rect_height = 40
    margin = 20
    y = HEIGHT - rect_height - margin

    for color in color_options:
        x = margin + (margin + rect_width) * color_options.index(color)
        pygame.draw.rect(screen, color, (x, y, rect_width, rect_height))
        color_rects.append( pygame.Rect(x, y, rect_width, rect_height))

    return color_rects

running = True
start_pos = None
color_rects = draw_color_options()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for rect in color_rects:
                    if rect.collidepoint(event.pos):
                        index = color_rects.index(rect)
                        drawing_color = [BLACK, RED, GREEN, BLUE, YELLOW][index]
                start_pos = event.pos
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                end_pos = event.pos
                if drawing_tool == "eraser":
                    pygame.draw.circle(screen, eraser_color, event.pos, brush_size)
                else:
                    draw_shape(start_pos, end_pos)
        elif event.type == pygame.MOUSEMOTION:
            if start_pos:
                if drawing_tool == "eraser":
                    pygame.draw.circle(screen, eraser_color, event.pos, brush_size)
                else:
                    draw_shape(start_pos, event.pos)
                start_pos = event.pos

    keys = pygame.key.get_pressed()
    if keys[pygame.K_r]:
        drawing_tool = "rectangle"
    elif keys[pygame.K_c]:
        drawing_tool = "circle"
    elif keys[pygame.K_e]:
        drawing_tool = "eraser"

    pygame.display.flip()
