import pygame
from rect import Rect


clock = pygame.time.Clock()
width, height = 800, 600

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Michaels Window')

rect_width = 60
x,y = 400 - rect_width/2,300 - rect_width/2


my_rect = Rect(x,y,rect_width, rect_width, (255,0,0))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0,0,0))

    my_rect.update()

    if my_rect.get_x() >= width - rect_width or my_rect.get_x() <=0:
        temp_speed_x = my_rect.get_speed_x()
        my_rect.set_speed_x(temp_speed_x * -1)
    
    if my_rect.get_y() >= height - rect_width or my_rect.get_y() <=0:
        temp_speed_y = my_rect.get_speed_y() + 5
        my_rect.set_speed_y(temp_speed_y * -1)
    

    my_rect.draw(screen)
    pygame.display.update()

    clock.tick(60)


pygame.quit()
quit()
