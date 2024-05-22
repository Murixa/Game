import pygame, controls
from gun import Gun
from pygame.sprite import Group
from statistic import Statistic
from score import Score


def run():
    pygame.init()
    screen = pygame.display.set_mode((650, 700))
    pygame.display.set_caption("Космический воин")
    bg_color = (0, 0, 0)
    gun = Gun(screen)
    bullets = Group()
    nlos = Group()
    controls.create_army(screen, nlos)
    statistic = Statistic()
    scores = Score(screen, statistic)

    while True:
        #запуск основных циклов
        controls.events(screen, gun, bullets)
        if statistic.run_game:
            gun.update_gun()
            controls.update(bg_color, screen, statistic, scores, gun, nlos, bullets)
            controls.update_bullets(screen, statistic, scores, nlos, bullets)
            controls.update_nlos(statistic, screen, scores, gun, nlos, bullets)


run()
