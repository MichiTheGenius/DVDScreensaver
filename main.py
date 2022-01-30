import pygame
from rect import Rect


clock = pygame.time.Clock()
width, height = 800, 600

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Michaels Window')

x,y = 400,300

rect_width = 60

my_rect = Rect(x,y,rect_width, rect_width, (255,0,0))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0,0,0))
    my_rect.on_press()
    my_rect.draw(screen)
    pygame.display.update()

    clock.tick(60)


pygame.quit()
quit()
