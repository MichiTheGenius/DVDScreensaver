import pygame
from image import Image
from settings import *


class Main():
    def __init__(self) -> None:
        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode(
            (WIDTH, HEIGHT))
        pygame.display.set_caption('DVD screensaver')

        self.dvd_logo = Image(100, 100)

    def mainloop(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen.fill(WHITE)

            self.dvd_logo.update(self.screen)

            if self.dvd_logo.get_x() >= WIDTH - self.dvd_logo.get_image_width() or self.dvd_logo.get_x() <= 0:
                current_velocity_x = self.dvd_logo.get_velocity_x()
                self.dvd_logo.set_velocity_x(current_velocity_x * -1)

            if self.dvd_logo.get_y() >= HEIGHT - self.dvd_logo.get_image_height() or self.dvd_logo.get_y() <= 0:
                current_velocity_y = self.dvd_logo.get_velocity_y()
                self.dvd_logo.set_velocity_y(current_velocity_y * -1)

            pygame.display.update()

            self.clock.tick(FPS)

        pygame.quit()
        quit()


if __name__ == '__main__':
    m = Main()
    m.mainloop()
