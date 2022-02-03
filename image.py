import pygame

class Image():
    def __init__(self, x, y):
        self.image = pygame.image.load('dvd.png')
        self.image_width = self.image.get_width() / 8
        self.image_height = self.image.get_height() / 8
        self.image = pygame.transform.scale(self.image, (self.image_width, self.image_height))
        self.x = x
        self.y = y 
        self.velocity_x = 1
        self.velocity_y = 1

    def move(self):
        self.x += self.velocity_x 
        self.y += self.velocity_y

    def get_image_width(self):
        return self.image_width

    def get_image_height(self):
        return self.image_height

    def set_velocity_x(self, velocity_x):
        self.velocity_x = velocity_x

    def increase_x(self, value):
        self.velocity_x += value

    def set_velocity_y(self, velocity_y):
        self.velocity_y = velocity_y

    def get_velocity_x(self):
        return self.velocity_x

    def get_velocity_y(self):
        return self.velocity_y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
    
    def update(self, screen):
        self.draw(screen)
        self.move()