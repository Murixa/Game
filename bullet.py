import pygame

class Bullet(pygame.sprite.Sprite):

    def __init__(self, screen, gun):
        #создание
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 3, 12)
        self.color = 85, 170, 255
        self.speed = 3.5
        self.rect.centerx = gun.rect.centerx
        self.rect.top = gun.rect.top
        self.y = float(self.rect.y)

    def update(self):
        #перемещение вверх
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        #отрисовка
        pygame.draw.rect(self.screen, self.color, self.rect)