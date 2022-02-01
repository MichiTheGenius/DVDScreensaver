import pygame

class Rect():
    def __init__(self, x, y, w, h, color):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color
        self.rectangle = pygame.Rect(self.x, self.y, self.w, self.h)
        self.speed_x = 5
        self.speed_y = 0

    def move(self):
        self.x += self.speed_x 
        self.y += self.speed_y

    def set_speed_x(self, speed_x):
        self.speed_x = speed_x

    def increase_x(self, value):
        self.speed_x += value

    def set_speed_y(self, speed_y):
        self.speed_y = speed_y

    def get_speed_x(self):
        return self.speed_x

    def get_speed_y(self):
        return self.speed_y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def draw(self, screen):
        pygame.draw.rect(screen, (self.color), self.rectangle)
    
    def update(self):
        self.rectangle = pygame.Rect(self.x, self.y, self.w, self.h)
        self.move()