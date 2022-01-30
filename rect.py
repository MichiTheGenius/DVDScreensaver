import pygame

class Rect():
    def __init__(self, x, y, w, h, color):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color
        self.rectangle = pygame.Rect(self.x, self.y, self.w, self.h)

    def move_x(self, speed):
        self.x += speed

    def move_y(self, speed):
        self.y += speed

    def draw(self, screen):
        pygame.draw.rect(screen, (self.color), self.rectangle)

    def on_press(self):
        if self.is_clicked():
            print('it still works!')

    def is_clicked(self):
        mouse_pos = pygame.mouse.get_pos()
        return self.rectangle.collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0]


