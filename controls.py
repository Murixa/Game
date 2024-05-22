import pygame, sys
from bullet import Bullet
from nlo import Nlo
import time

def events(screen, gun, bullets):
    # работа окна
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

            #движение WASD
        elif event.type == pygame.KEYDOWN:
            #право
            if event.key == pygame.K_d:
                gun.mright = True
            #лево
            elif event.key == pygame.K_a:
                gun.mleft = True
            #пуля
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, gun)
                bullets.add(new_bullet)

        elif event.type == pygame.KEYUP:
            #право
            if event.key == pygame.K_d:
                gun.mright = False
            # лево
            elif event.key == pygame.K_a:
                gun.mleft = False

def update(bg_color, screen, statistic, scores, gun, nlos, bullets):
    #обновление экрана
    screen.fill(bg_color)
    scores.show_score()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    gun.out()
    nlos.draw(screen)
    pygame.display.flip()

def update_bullets(screen, statistic, scores, nlos, bullets):
    #обновление пуль
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets, nlos, True, True)
    if collisions:
        #прибавление очков за одного врага
        for nlos in collisions.values():
            statistic.score += 10 * len(nlos)
        scores.image_score()
        check_high_score(statistic, scores)
        scores.image_hps()
    if len(nlos) == 0:
        bullets.empty()
        create_army(screen, nlos)


def gun_kill(statistic, screen, scores, gun, nlos, bullets):
    #попадание по кораблю
    if statistic.guns_left > 0:
        statistic.guns_left -= 1
        scores.image_hps()
        nlos.empty()
        bullets.empty()
        create_army(screen, nlos)
        gun.create_gun()
        time.sleep(0.5)
    else:
        statistic.run_game = False
        sys.exit()

def update_nlos(statistic, screen, scores, gun, nlos, bullets):
    #движение врагов
    nlos.update()
    if pygame.sprite.spritecollideany(gun, nlos):
        gun_kill(statistic, screen, scores, gun, nlos, bullets)
    nlos_check(statistic, screen, scores, gun, nlos, bullets)

def nlos_check(statistic, screen, scores, gun, nlos, bullets):
    #касание врагов противоположной стороны
    screen_rect = screen.get_rect()
    for nlo in nlos.sprites():
        if nlo.rect.bottom >= screen_rect.bottom:
            gun_kill(statistic, screen, scores, gun, nlos, bullets)
            break


def create_army(screen, nlos):
    #создание армии врагов
    nlo = Nlo(screen)
    nlo_width = nlo.rect.width
    nlo_height = nlo.rect.height
    # сколько влезает в экран
    number_nlo_x = int((650 - 2 * nlo_width) / nlo_width)
    number_nlo_y = int((700 - 300 - 2 * nlo_height) / nlo_height)

    for nlo_row_number in range(number_nlo_y):
        for nlo_number in range(number_nlo_x):
            nlo = Nlo(screen)
            nlo.x = nlo_width + nlo_width * nlo_number
            nlo.y = nlo_height + nlo_height * nlo_row_number
            nlo.rect.x = nlo.x
            nlo.rect.y = nlo.rect.height + nlo.rect.height * nlo_row_number
            nlos.add(nlo)

def check_high_score(statistic, scores):
    #проверка нового рекорда
    if statistic.score > statistic.high_score:
        statistic.high_score = statistic.score
        scores.image_high_score()
        with open('high_score.txt', 'w') as f:
            f.write(str(statistic.high_score))
