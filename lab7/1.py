import pygame
from time import strftime

pygame.init()

w, h = 800, 800
screen = pygame.display.set_mode((w, h), pygame.RESIZABLE)
pygame.display.set_caption("Mickey Mouse Clock")

mickey = pygame.image.load("mickey.png")
left_hand = pygame.image.load("second.png")
right_hand = pygame.image.load("minute.png")

m_rect = mickey.get_rect(center=(w // 2, h // 2))
l_rect = left_hand.get_rect(center=m_rect.center)
r_rect = right_hand.get_rect(center=m_rect.center)

clock = pygame.time.Clock()

while True:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    screen.blit(mickey, m_rect)

    c_sec = int(strftime("%S"))
    c_min = int(strftime("%H"))

    angle_s = -(c_sec / 60) * 360 + 90
    r_second = pygame.transform.rotate(left_hand, angle_s)
    r_second_rect = r_second.get_rect(center=m_rect.center)
    screen.blit(r_second, r_second_rect)

    angle_m = -(c_min / 60.0) * 360 + 84
    r_minute = pygame.transform.rotate(right_hand, angle_m)
    r_minute_rect = r_minute.get_rect(center=m_rect.center)
    screen.blit(r_minute, r_minute_rect)

    pygame.display.flip()
    clock.tick(60)

