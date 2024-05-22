import pygame

class Nlo(pygame.sprite.Sprite):
    #один враг
    def __init__(self, screen):
        #начальная позиция
        super(Nlo, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/pixil-frame-1.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def draw(self):
        #отрисовка
        self.screen.blit(self.image, self.rect)

    def update(self):
        #движение
        self.y += 0.04
        self.rect.y = self.y