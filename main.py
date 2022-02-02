import pygame
from image import Image


clock = pygame.time.Clock()
width, height = 800, 600

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('DVD screensaver')


dvd_logo = Image(0,0)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255,255,255))

    dvd_logo.update(screen)

    if dvd_logo.get_x() >= width - dvd_logo.get_image_width() or dvd_logo.get_x() <=0:
        current_speed_x = dvd_logo.get_speed_x()
        dvd_logo.set_speed_x(current_speed_x * -1)
    
    if dvd_logo.get_y() >= height - dvd_logo.get_image_height() or dvd_logo.get_y() <=0:
        current_speed_y = dvd_logo.get_speed_y()
        dvd_logo.set_speed_y(current_speed_y * -1)
    

    pygame.display.update()

    clock.tick(60)


pygame.quit()
quit()
