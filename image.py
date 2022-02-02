import pygame

class Image():
    def __init__(self, x, y):
        self.image = pygame.image.load('dvd.png')
        self.image_width = self.image.get_width() / 8
        self.image_height = self.image.get_height() / 8
        self.image = pygame.transform.scale(self.image, (self.image_width, self.image_height))
        self.x = x
        self.y = y 
        self.speed_x = 2
        self.speed_y = 2
        print(self.image)

    def move(self):
        self.x += self.speed_x 
        self.y += self.speed_y

    def get_image_width(self):
        return self.image_width

    def get_image_height(self):
        return self.image_height

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
        screen.blit(self.image, (self.x, self.y))
    
    def update(self, screen):
        self.draw(screen)
        self.move()