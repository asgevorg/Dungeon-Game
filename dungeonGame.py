import pygame
import random
from pygame import mixer

"""
Created 29/12/2021
Release 30/12/2021
Creators CEO/TeamLead Gevorg Asatryan, Head Developer Davit Ghonyan, Developer Arman Manukyan, Designer Ashot Chakhoyan
Enjoy !!!!
"""
game_active = True
start_ticks = pygame.time.get_ticks()  # starter tick
pygame.init()
clock = pygame.time.Clock()
x_poss = 300
# music part
mixer.init()
mixer.music.load("src/musica.mp3")
mixer.music.play(3, 10)
mixer.music.set_volume(0.3)

time_rand = random.randrange(2, 7)
# white color
color = (255, 255, 255)
# light shade of the button
color_light = (170, 170, 170)

# dark shade of the button
color_dark = (100, 100, 100)

# defining a font
smallfont = pygame.font.SysFont('src/Pixeltype.ttf', 35)

# rendering a text written in
# this font
text = smallfont.render('Quit', True, color)
text_next_lev = smallfont.render('Nextlevel', True, color)

# quit button coordinates
but_quit_x = 50.0
but_quit_y = 450.0

# next level button coordinates
but_next_x = 330.0
but_next_y = 450.0

# button for restart
but_restart_x = 170.0
but_restart_y = 450.0

text_restart = smallfont.render('Restart', True, color)

INTRO = pygame.image.load("src/intro.png")

start = True  
level1 = False
menu_level2 = False

level2 = False
menu_level3 = False
level3 = False
menu_level4 = False
level4 = False
menu_level5 = False
level5 = False
menu_final = False
final_level = False

boss = False

window_width = 500
window_height = 500

score_surf = 0
score_weap = 0

window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("MyGame")


# background surface
sky_surface = pygame.image.load("src/castle.png")
sky_rect = sky_surface.get_rect(center=(0, 0))
sky_rect2 = sky_surface.get_rect(center=(895, -300))
sky_rect_lose = sky_surface.get_rect(center=(-395, -400))

# player surface
player_surface = pygame.image.load("src/character.png")
player_surface = pygame.transform.scale(player_surface, (65, 90))
player_rect = player_surface.get_rect(midbottom=(50, 430))
player_rect_lose = player_surface.get_rect(midbottom=(180, 398))
player_rect_start = player_surface.get_rect(midbottom=(250, 200))
player_gravity = 0

# enemy image and surface
enemy_surface = pygame.image.load("src/enemy.png")
enemy_surface = pygame.transform.scale(enemy_surface, (60, 70))  # chap
enemy_surface = pygame.transform.flip(enemy_surface, True, False)

enemy_surface2 = pygame.image.load("src/enemy.png")
enemy_surface2 = pygame.transform.scale(enemy_surface2, (80, 90))  # chap

enemy_surface4 = pygame.image.load("src/enemy.png")
enemy_surface4 = pygame.transform.scale(enemy_surface2, (100, 120))
enemy_surface4 = pygame.transform.flip(enemy_surface4, True, False)

# final enemy
enemy_surface5 = pygame.image.load("src/enemy.png")
enemy_surface5 = pygame.transform.scale(enemy_surface2, (90, 100))
enemy_surface5 = pygame.transform.flip(enemy_surface5, True, False)


enemy_surface2 = pygame.transform.flip(enemy_surface2, True, False)
menu_level1_background = pygame.image.load("src/skeletonking_BG.png")

# for flying enemy
enemyFlying = pygame.image.load("src/flyingSkeleton.png")
enemyFlying = pygame.transform.scale(enemyFlying, (40, 50))
enemyFlying = pygame.transform.rotate(enemyFlying, 90)

# final level enemy called final boss, it loads the image of boss
FinalBoss = pygame.image.load("src/FinalBoss.png")
FinalBoss = pygame.transform.scale(FinalBoss, (250, 180))


# running is the main engine of our game, if it's false our game will quit
running = True
barev = 1


# it is the part of shooting, the array below is the array of guns, after certain points you are able to shoot, after shooting one element or gun will be deleted from array
enemyWeap = []
weaponArr = []
collide1 = False
collideEnemyWeapon = False

but_help_x = 360.0
but_help_y = 440.0
help_text = smallfont.render("Help", True, color)
exit_text = smallfont.render("exit", True, color)
# for help screen
help_s = False
# for help screen's exit button
but_exit_x = 360.0
but_exit_y = 440.0

BLACK = (0, 0, 0)
BLUE = (199, 44, 65)

help_font = pygame.font.SysFont('src/Pixeltype.ttf', 23)
# main engine if it's false the game will quit
shootingSpeed = 100
rand = random.randrange(shootingSpeed)
# boss health
health_boss = 200
# color green
GREEN = (0, 128, 0)

# menu, this is the function to make menu screens


def menu(levelnum, background_tuple):
    global player_surface_lose, level2, level1, level3, level4, level5, menu_level2, menu_level3, menu_level4, menu_level5, game_active, running, player_surface, start, final_level, menu_final, player_rect
    player_rect = player_surface.get_rect(midbottom = (50, 430))
    player_surface_lose = pygame.transform.scale(player_surface, background_tuple)
    text_title = font_start.render("Dungeon Run", False, "White")
    text_rect = text_title.get_rect(center=(250, 50))
    text_title_level = font_start.render(
        "Level {}".format(levelnum), False, "White")
    text_rect_start = text_title_level.get_rect(center=(250, 240))
    window.blit(text_title_level, text_rect_start)
    window.blit(text_title, text_rect)
    # stores the (x,y) coordinates into
    # the variable as a tuple
    mouse = pygame.mouse.get_pos()
    # ev is shortened event word
    for ev in pygame.event.get():
        # this part tells if the quit button is pressed
        if ev.type == pygame.QUIT:
            running = False

        # checks if a mouse is clicked
        if ev.type == pygame.MOUSEBUTTONDOWN:

            # if the mouse is clicked on the
            # button the game is terminated
            if but_quit_x <= mouse[0] <= (but_quit_x + 80) and but_quit_y <= mouse[1] <= (but_quit_y+40):
                mixer.music.load("src/button_click.mp3")
                mixer.music.play()
                pygame.mixer.music.queue('src/main.mp3')
                running = False
            if but_next_x <= mouse[0] <= (but_next_x + 140) and but_next_y <= mouse[1] <= (but_next_y+40):
                mixer.music.load("src/main.mp3")
                mixer.music.play()
                pygame.mixer.music.queue('src/main.mp3')
                if levelnum == 2:
                    level1 = False
                    level2 = True
                    menu_level2 = False
                    game_active = True
                elif levelnum == 3:
                    level2 = False
                    level3 = True
                    menu_level3 = False
                elif levelnum == 4:
                    level3 = False
                    level4 = True
                    menu_level4 = False
                elif levelnum == 5:
                    level4 = False
                    level5 = True
                    menu_level5 = False
                elif levelnum == 6:
                    level5 = False
                    final_level = True
                    menu_final = False
            elif but_restart_x <= mouse[0] <= (but_restart_x + 100) and but_restart_y <= mouse[1] <= (but_restart_y+40):
                start = True
                menu_level2 = False
                menu_level3 = False
                menu_level4 = False
        # checks if any key is pressed
        if ev.type == pygame.KEYDOWN:
            # checks if that any key is space to start the game
            if ev.key == pygame.K_SPACE:
                # start the next level and quits the menu screen
                if levelnum == 2:
                    level1 = False
                    level2 = True
                    menu_level2 = False
                    game_active = True
                elif levelnum == 3:
                    level2 = False
                    level3 = True
                    menu_level3 = False
                elif levelnum == 4:
                    level3 = False
                    level4 = True
                    menu_level4 = False
                elif levelnum == 5:
                    level4 = False
                    level5 = True
                    menu_level5 = False
                elif levelnum == 6:
                    level5 = False
                    final_level = True
                    menu_final = False
            # for restarting the game
            elif ev.key == pygame.K_r:
                start = True
                menu_level2 = False
                menu_level3 = False
                menu_level4 = False

    # for restart button
    if but_restart_x <= mouse[0] <= (but_restart_x + 140) and but_restart_y <= mouse[1] <= (but_restart_y+40):
        # x,y positions, width,height
        pygame.draw.rect(window, color_light, [
                         but_restart_x, but_restart_y, 100, 40])

    else:
        pygame.draw.rect(window, color_dark, [
                         but_restart_x, but_restart_y, 100, 40])
    # if mouse is hovered on a button it
    # changes to lighter shade,
    # button for next level
    if but_next_x <= mouse[0] <= (but_next_x + 140) and but_next_y <= mouse[1] <= (but_next_y+40):
        # x,y positions, width,height
        pygame.draw.rect(window, color_light, [
                         but_next_x, but_next_y, 140, 40])

    else:
        pygame.draw.rect(window, color_dark, [but_next_x, but_next_y, 140, 40])

    # mouse point for quit
    if but_quit_x <= mouse[0] <= (but_quit_x + 80) and but_quit_y <= mouse[1] <= (but_quit_y+40):
        # x,y positions, width,height
        pygame.draw.rect(window, color_light, [but_quit_x, but_quit_y, 80, 40])

    else:
        pygame.draw.rect(window, color_dark, [but_quit_x, but_quit_y, 80, 40])
    # superimposing the text onto our button
    window.blit(text, (but_quit_x + 10, but_quit_y + 8))
    window.blit(text_next_lev, (but_next_x + 13, but_next_y + 8))
    window.blit(text_restart, (but_restart_x + 10, but_restart_y + 8))

# this is the class for enemy, this class creates an enemy whitch has speed coordinates, scale, and image
# this class also makes our enemy animation to look like it's moving


class Enemy():
    def __init__(self, x, y, image, weapSize):
        self.image = image
        self.x = x
        self.y = y
        self.image = image
        self.weapSize = weapSize
        # animation vavribale
        self.attack_animation = False
        # the array of animation images
        self.sprites = [pygame.transform.flip(pygame.transform.scale(pygame.image.load('src/enemy_moving/enemy1_.png'), (70, 90)), True, False),
                        pygame.transform.flip(pygame.transform.scale(pygame.image.load(
                            'src/enemy_moving/enemy2_.png'), (70, 90)), True, False),
                        pygame.transform.flip(pygame.transform.scale(pygame.image.load(
                            'src/enemy_moving/enemy4_.png'), (70, 90)), True, False),
                        pygame.transform.flip(pygame.transform.scale(pygame.image.load(
                            'src/enemy_moving/enemy5_.png'), (70, 90)), True, False),
                        pygame.transform.flip(pygame.transform.scale(pygame.image.load('src/enemy_moving/enemy6_.png'), (70, 90)), True, False)]
        self.current_sprite = 0
        image = self.sprites[self.current_sprite]

        self.enemy_rect = image.get_rect(midbottom=(70, 90))
        self.enemy_rect.topleft = [x, y]
    # it's the part for moving our enemy, and also it makes the animation variable true to turn it on if the enemy is moving

    def move(self, speed):
        self.enemy_rect.right -= speed
        self.attack_animation = True
    # it updates and creates the main animation

    def update(self, speed):
        if self.attack_animation == True:
            self.current_sprite += speed
            if int(self.current_sprite) >= len(self.sprites):
                self.current_sprite = 0
                self.attack_animation = False
        # gives the enemy image to animation image
        self.image = self.sprites[int(self.current_sprite)]


won_font = pygame.font.Font("src/Pixeltype.ttf", 200)
font_start = pygame.font.Font("src/Pixeltype.ttf", 42)
font = pygame.font.Font("src/Pixeltype.ttf", 32)
flipped = False
# our ground class, it makes the grounds and makes them look like they are moving


class Ground(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        self.surface = pygame.image.load(image)
        self.rect = self.surface.get_rect(midbottom=(x, y))

    def transform(self, width, height):
        self.surface = pygame.transform.scale(self.surface, (width, height))
# weapon class, makes the weapons to shoot the enemy's


class Weapon():
    def __init__(self, x, y, image, shotUp):
        self.x = x
        self.y = y
        self.image = image
        self.surface = pygame.image.load(image)
        self.rect = self.surface.get_rect(center=(x, y))
        self.shotUp = shotUp
    # makes the gun to move

    def move(self, speed):
        self.rect.x += speed

    def moveF(self, speed):
        self.rect.y += speed

    def moveUp(self, speed):
        self.rect.y -= speed

    def moveFinal(self, speed):
        self.rect.x -= speed

# the level function, it creates a certain level, the on eyou need

health = 50
win = False
def level(enemy1, speed, ground1, sky_rect, groundType, speedF, beamSpeed, enemy3Flying):
    global game_active, score_surf, collide, collide1, score_weap, flipped, collideEnemyWeapon, level3, rand, boss, final_level, health, win, but_restart_x, but_exit_y,color_dark, window
    mouse = pygame.mouse.get_pos()
    mixer.music.set_volume(0.1)
    collide2 = False
    collideWeapons = False
    if len(weaponArr) > 0:
        collide1 = weapon.rect.colliderect(enemy1.enemy_rect)
        if not (level1 or level2):
            collide2 = weapon.rect.colliderect(enemy3Flying.enemy_rect)
    if len(enemyWeap) > 0:
        collideEnemyWeapon = enemyWeap[0].rect.colliderect(player_rect)
    else:
        collideEnemyWeapon = False
    if len(enemyWeap) > 0 and len(weaponArr) > 0:
        collideWeapons = weaponArr[0].rect.colliderect(enemyWeap[0].rect)
    else:
        collideWeapons = False
    collide = player_rect.colliderect(enemy1.enemy_rect)
    if enemy3Flying.enemy_rect.left <= 0 and flipped == False:
        enemy3Flying.image = pygame.transform.flip(
            enemy3Flying.image, True, False)
        flipped = True
    elif flipped == True and enemy3Flying.enemy_rect.right >= 500:
        enemy3Flying.image = pygame.transform.flip(
            enemy3Flying.image, True, False)
        flipped = False
    if enemy1.enemy_rect.right <= 0:
        enemy1.enemy_rect.left = 514
    if len(enemyWeap) == 0 and game_active and rand >= 0 and rand <= 500 and (level3 or level4 or level5):
        weapF = Weapon(enemy3Flying.enemy_rect.x,
                       enemy3Flying.enemy_rect.y, "src/beam.png", None)
        weapF.surface = pygame.transform.rotate(weapF.surface, 90)
        weapF.surface = pygame.transform.scale(
            weapF.surface, (enemy3Flying.weapSize))
        enemyWeap.append(weapF)
    if game_active:
        if not boss:
            enemy1.move(speed)
        if flipped == True:
            enemy3Flying.move(-speedF)
        else:
            enemy3Flying.move(speedF)
        window.blit(sky_surface, sky_rect)
        window.blit(ground1.surface, ground1.rect)
        window.blit(player_surface, player_rect)
        window.blit(enemy1.image, enemy1.enemy_rect)
        window.blit(text_score, text_score_rect)
        if level3 or level4 or level5:
            window.blit(enemy3Flying.image, enemy3Flying.enemy_rect)
        if len(enemyWeap) > 0:
            window.blit(enemyWeap[0].surface, enemyWeap[0].rect)
            if final_level:
                enemyWeap[0].moveFinal(beamSpeed)
            else:
                enemyWeap[0].moveF(beamSpeed)
            if enemyWeap[0].rect.top >= 500:
                enemyWeap.pop()
        collideF = player_rect.colliderect(enemy3Flying.enemy_rect)
        collide = player_rect.colliderect(enemy1.enemy_rect)
        if len(weaponArr) > 0:
            for i in range(len(weaponArr)):
                window.blit(weaponArr[i].surface, weaponArr[i].rect)
                if weaponArr[ i].shotUp == True:
                    weaponArr[i].moveUp(10)
                else:
                    weaponArr[i].move(10)
                if weaponArr[i].rect.colliderect(enemy1.enemy_rect):
                    if final_level:
                        health -= 25
                        if health == 0:
                            game_active = False
                            win = True
                            print(win)
                    else:
                        score_surf += 20
                        enemy1.enemy_rect = enemy_surface.get_rect(midbottom=(600, 430))
                    weaponArr.pop(i)
                elif weaponArr[i].rect.left >= 500 or weaponArr[i].rect.bottom <= 0:
                    weaponArr.pop(i)
                    
        if collideWeapons and len(enemyWeap) > 0 and len(weaponArr) > 0:
            weaponArr.pop()
            enemyWeap.pop()
        if collide or collideF:
            score_surf = 0
            score_weap = 0
            game_active = False
            enemy1.enemy_rect = enemy_surface.get_rect(midbottom=(600, 430))
            enemy3Flying.enemy_rect = enemy3Flying.image.get_rect(
                midbottom=(600, 40))
            if len(enemyWeap) > 0:
                enemyWeap.pop()
        elif collideEnemyWeapon and len(enemyWeap) > 0:
            health = 100
            score_surf = 0
            score_weap = 0
            game_active = False
            enemy1.enemy_rect = enemy_surface.get_rect(midbottom=(600, 430))
            enemy3Flying.enemy_rect = enemy3Flying.image.get_rect(
                midbottom=(600, 40))
            enemyWeap.pop()
        elif collide1:
            score_surf += 5
            enemy1.enemy_rect = enemy_surface.get_rect(midbottom=(600, 430))
        elif collide2:
            score_surf += 5
            enemy3Flying.enemy_rect = enemyFlying.get_rect(
                midbottom=(2000, 40))
    else:
        health = 100
        if len(enemyWeap) > 0:
            enemyWeap.pop()
        if not final_level:
            player_rect.x = 50
            window.blit(sky_surface, sky_rect_lose)
            player_surface_lose = pygame.transform.scale(player_surface, (40, 70))
            window.blit(player_surface_lose, player_rect_lose)
            text_title = font.render("Press  Space  to  restart", False, "White")
            text_rect = text_title.get_rect(center=(250, 164))
            window.blit(text_title, text_rect)

def score(num, numWeap):
    global barev, score_surf, text_score, font, score_weap
    if barev % num == 0 and game_active:
        score_surf += 1
        text_score = font.render(
            "Score: " + str(score_surf) + " " + " weapon: " + str(score_weap), True, "White")
    if barev % numWeap == 0 and game_active:
        score_weap += 1

# final enemy


class Final_fog(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        self.attack_animation = False
        self.sprites = []
        self.sprites.append(pygame.transform.flip(pygame.transform.scale(
            pygame.image.load('src/boss_anim/boss_1.png'), (200, 200)), False, False))
        self.sprites.append(pygame.transform.flip(pygame.transform.scale(
            pygame.image.load('src/boss_anim/boss_2.png'), (200, 200)), False, False))
        self.sprites.append(pygame.transform.flip(pygame.transform.scale(
            pygame.image.load('src/boss_anim/boss_3.png'), (200, 200)), False, False))
        self.sprites.append(pygame.transform.flip(pygame.transform.scale(
            pygame.image.load('src/boss_anim/boss_4.png'), (200, 200)), False, False))
        self.sprites.append(pygame.transform.flip(pygame.transform.scale(
            pygame.image.load('src/boss_anim/boss_5.png'), (200, 200)), False, False))
        self.sprites.append(pygame.transform.flip(pygame.transform.scale(
            pygame.image.load('src/boss_anim/boss_6.png'), (200, 200)), False, False))
        self.sprites.append(pygame.transform.flip(pygame.transform.scale(
            pygame.image.load('src/boss_anim/boss_7.png'), (200, 200)), False, False))
        self.sprites.append(pygame.transform.flip(pygame.transform.scale(
            pygame.image.load('src/boss_anim/boss_8.png'), (200, 200)), False, False))
        self.sprites.append(pygame.transform.flip(pygame.transform.scale(
            pygame.image.load('src/boss_anim/boss_9.png'), (200, 200)), False, False))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.enemy_rect = self.image.get_rect()
        self.enemy_rect.topleft = [pos_x, pos_y]

    def attack(self):
        self.attack_animation = True

    def update(self, speed):
        if self.attack_animation == True:
            self.current_sprite += speed
            if int(self.current_sprite) >= len(self.sprites):
                self.current_sprite = 0
                self.attack_animation = False

        self.image = self.sprites[int(self.current_sprite)]


# text for score
text_score = font.render("Score: " + str(score_surf), True, "White")
text_score_rect = text_score.get_rect(center=(250, 44))
# ground objects
ground1 = Ground(150, 500, 'src/ground.png')
ground2 = Ground(500, 1180, 'src/floor2.png')
# trasnformes the ground
ground2.transform(700, 200)

# enemy objects
enemy1 = Enemy(450, 350, enemy_surface, 0)
enemy2 = Enemy(450, 350, enemy_surface2, 0)
enemy3 = Enemy(450, 350, enemy_surface2, 0)
enemy3Flying = Enemy(450, 40, enemyFlying, (20, 40))
enemy3Flying.enemy_rect = enemy3Flying.image.get_rect(midbottom=(600, 40))
enemy4Flying = Enemy(450, 40, enemyFlying, (40, 60))
enemy4Flying.enemy_rect = enemy4Flying.image.get_rect(midbottom=(600, 40))
enemy4 = Enemy(500, 350, enemy_surface4, 0)
enemy5 = Enemy(500, 350, enemy_surface5, 0)
enemy_final = Enemy(500, 350, FinalBoss, (765, 3764))
enemy6 = Enemy(-200, -200, enemy_surface5, (0, 0))
final_enemy_boss = Final_fog(300, 230)
enemy_small = Enemy(500, 350, enemy_surface5, 0)
# main loop
while running:
    if help_s:
        start = False
        window.blit(INTRO, (0, 0))
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if but_exit_x <= mouse[0] <= (but_exit_x + 140) and but_exit_y <= mouse[1] <= (but_exit_y+40):
                    mixer.music.load("src/button_click.mp3")
                    mixer.music.play()
                    pygame.mixer.music.queue('src/musica.mp3')

                    help_s = False
                    start = True
        if but_exit_x <= mouse[0] <= (but_exit_x + 80) and but_exit_y <= mouse[1] <= (but_exit_y+40):
            # x,y positions, width,height
            pygame.draw.rect(window, color_light, [
                             but_exit_x, but_exit_y, 80, 40])

        else:
            pygame.draw.rect(window, color_dark, [
                             but_exit_x, but_exit_y, 80, 40])
        window.blit(exit_text, (but_exit_x + 15, but_exit_y + 8))
    if len(weaponArr) > 0:
        collide1 = weaponArr[0].rect.colliderect(enemy1.enemy_rect)
    # this is the start screen
    if start:
        score_surf = 0
        window.blit(menu_level1_background, (-70, -10))
        player_surface_lose = pygame.transform.scale(player_surface, (40, 70))
        text_title = font_start.render("Dungeon Run", False, "White")
        text_rect = text_title.get_rect(center=(250, 50))
        text_title_level = font_start.render("Press Space To Begin Level 1", False, "White")
        text_rect_start = text_title_level.get_rect(center=(250, 400))
        window.blit(text_title_level, text_rect_start)
        window.blit(text_title, text_rect)
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_active = True
                    start = False
                    level1 = True
            # checks if a mouse is clicked
            if event.type == pygame.MOUSEBUTTONDOWN:
                if but_help_x <= mouse[0] <= (but_help_x + 80) and but_help_y <= mouse[1] <= (but_help_y+40):
                    mixer.music.load("src/button_click.mp3")
                    mixer.music.set_volume(1)
                    mixer.music.play()
                    pygame.mixer.music.queue('src/musica.mp3')
                    help_s = True

        if but_help_x <= mouse[0] <= (but_help_x + 140) and but_help_y <= mouse[1] <= (but_help_y+40):
            # x,y positions, width,height
            pygame.draw.rect(window, color_light, [
                             but_help_x, but_help_y, 100, 40])

        else:
            pygame.draw.rect(window, color_dark, [
                             but_help_x, but_help_y, 100, 40])
        window.blit(help_text, (but_help_x + 18, but_help_y + 8))
    else:
        if score_surf >= 10 and level1:
            menu_level2 = True
            level1 = False
        # level 2's menu screen
        if menu_level2:
            mixer.music.set_volume(0.3)
            window.blit(menu_level1_background, (-10, -10))
            menu(2, (40, 70))
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        menu_level2 = False
                        level2 = True

        # menu 3 level screen
        if menu_level3:
            mixer.music.set_volume(0.3)
            level2 = False
            window.blit(menu_level1_background, (-10, -10))
            menu(3, (40, 70))
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        level3 = True
                        menu_level3 = False
        # menu level 4's screen
        if menu_level4:
            mixer.music.set_volume(0.3)
            level3 = False
            if len(enemyWeap) > 0:
                enemyWeap.pop()
            level3 = False
            window.blit(menu_level1_background, (-10, -10))
            menu(4, (40, 70))
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        menu_level4 = False
                        level4 = True
        if menu_level5:
            mixer.music.set_volume(0.3)
            if len(enemyWeap) > 0:
                enemyWeap.pop()
            level4 = False
            window.blit(sky_surface, sky_rect2)
            menu(5, (70, 100))
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        level5 = True
                        menu_level5 = False
        if menu_final:
            mixer.music.set_volume(0.3)
            if len(enemyWeap) > 0:
                enemyWeap.pop()
            level5 = False
            window.blit(menu_level1_background, (-10, -10))
            menu(6, (70, 100))
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        menu_final = True
                        menu_level5 = False
        barev += 1
        if game_active and not menu_level2 and not menu_level3 and not menu_level4 and not menu_level5 and not start and not help_s:
            score(10, 200)
        # makes the player movable
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom == 430 and game_active:
                    player_gravity = -24
                    player_surface = pygame.image.load("src/characterJump.png")
                    player_surface = pygame.transform.scale(
                        player_surface, (60, 90))
                if event.key == pygame.K_RIGHT and player_rect.right <= 480 and game_active and not level1:
                    player_rect.x += 30
                    player_surface = pygame.image.load("src/characterMove.png")
                    player_surface = pygame.transform.scale(
                        player_surface, (60, 90))
                if event.key == pygame.K_LEFT and player_rect.left >= 20 and game_active and not level1:
                    player_rect.x -= 30
                    player_surface = pygame.image.load("src/characterMove.png")
                    player_surface = pygame.transform.scale(
                        player_surface, (60, 90))
                if event.key == pygame.K_DOWN and game_active and len(weaponArr) == 0 and score_weap > 0 and not level1:
                    weapon = Weapon(
                        player_rect.x, player_rect.y + 40, "src/Run5.png", False)
                    weaponArr.append(weapon)
                    score_weap -= 1
                if event.key == pygame.K_UP and game_active and len(weaponArr) == 0 and score_weap > 0 and not (level1 or level2):
                    weapon = Weapon(
                        player_rect.x, player_rect.y + 40, "src/Run5.png", True)
                    weapon.surface = pygame.transform.rotate(
                        weapon.surface, 90)
                    weaponArr.append(weapon)
                    score_weap -= 1
            if game_active == False:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if final_level:
                            start= Truefinal_level = False
                        game_active = True
        if ground1.rect.right >= 514:
            ground1.rect.x -= 1
            if ground1.rect.right == 514:
                ground1.rect = ground1.surface.get_rect(midbottom=(35, 500))

        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 430:
            player_rect.bottom = 430
            player_surface = pygame.image.load("src/character.png")
            player_surface = pygame.transform.scale(player_surface, (60, 90))
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT and player_rect.right <= 480 and game_active and not level1:
                    player_rect.x += 4
                    player_surface = pygame.image.load("src/characterMove.png")
                    player_surface = pygame.transform.scale(
                        player_surface, (60, 90))
                if event.key == pygame.K_LEFT and player_rect.left >= 20 and game_active and not level1:
                    player_rect.x -= 4
                    player_surface = pygame.image.load("src/characterMove.png")
                    player_surface = pygame.transform.scale(
                        player_surface, (60, 90))
        window.blit(player_surface, player_rect)

        # level 1
        if level1:
            level(enemy1, 6, ground1, (0, 0), "normal", 0, 0, enemy3Flying)
            enemy1.update(0.25)
        # level 2
        if level2:
            level(enemy2, 7, ground2, sky_rect2, "normal", 0, 0, enemy3Flying)
            enemy2.update(0.25)
            if score_surf >= 70:
                menu_level3 = True
                level2 = False
        # level 3
        if level3:
            rand = random.randrange(shootingSpeed)
            shootingSpeed = 1500
            shootingSpeed += 5
            level(enemy3, 8, ground2, (-200, -200),
                  "normal", 5, 8, enemy3Flying)
            enemy3.update(0.25)
            if score_surf >= 130:
                menu_level4 = True
                level3 = False
        # level 4
        if level4:
            rand = random.randrange(shootingSpeed)
            shootingSpeed = 1200
            shootingSpeed += 3
            level(enemy4, 9, ground2, (-500, -500),
                  "normal", 7, 9, enemy4Flying)
            enemy4.update(0.25)
            if score_surf >= 160:
                menu_level5 = True
                level4 = False
        if level5:
            rand = random.randrange(shootingSpeed)
            shootingSpeed = 1000
            shootingSpeed += 1
            level(enemy5, 10, ground2, (-800, -800),
                  "normal", 7, 8, enemy4Flying)
            enemy5.update(0.25)
            if score_surf >= 200:
                menu_final = True
                level5 = False
        if win:
            score_surf = 0
            weap = 0
            window.blit(menu_level1_background, (-10, -10))
            text_title = won_font.render("YOU WON", False, (255, 0, 255))
            text_rect = text_title.get_rect(center=(250, 250))
            window.blit(text_title, text_rect)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        health = 100
                        boss = False
                        final_level = False
                        win = False
                        start = True

        if final_level and game_active:
            final_enemy_boss.enemy_rect = final_enemy_boss.image.get_rect(midbottom=(400, 430))
            collideFinal = False
            seconds_t = False
            boss = True
            seconds = (pygame.time.get_ticks()-start_ticks) / \
                1000  # calculate how many seconds

            score_surf = 0
            # text_score_rect = [-200, -200]
            level(final_enemy_boss, 0, ground2,
                  (-300, -300), "normal", 0, 0, enemy4Flying)
            if len(enemyWeap) > 0:
                collideFinal = player_rect.colliderect(enemyWeap[0].rect)
                enemyWeap[0].moveFinal(10)
                if enemyWeap[0].rect.x <= 0:
                    enemyWeap.pop()
            if collideFinal:
                enemyWeap.pop()
                game_active = False
            if seconds > 1:
                random1 = random.randrange(350, 430)
                if len(enemyWeap) == 0:
                    finalweapon = Weapon(
                        final_enemy_boss.enemy_rect.right, random1, 'src/Boss_Sword.png', False)
                    finalweapon.surface = pygame.transform.scale(
                        finalweapon.surface, (120, 30))
                    enemyWeap.append(finalweapon)

                start_ticks = pygame.time.get_ticks()  # starter tick
            if health >= 100:
                pygame.draw.rect(window,GREEN,[50,20,400,30])
            elif health >= 75 and health < 100:
                pygame.draw.rect(window,(255, 255, 0),[50,20,300,30])
            elif health >= 50 and health < 75:
                pygame.draw.rect(window,(255, 100, 0),[50,20,200,30])
            elif health >= 25 and health < 50:
                pygame.draw.rect(window,(255, 40, 0),[50,20,100,30])
            
            final_enemy_boss.update(0.25)
            final_enemy_boss.attack()
        elif (game_active == False) and not start and not level1 and not level2 and not level3 and not level4 and not level5 and not menu_level2 and not help_s and not win and not health == 0:
            player_rect.x = 50
            window.blit(sky_surface, sky_rect_lose)
            player_surface_lose = pygame.transform.scale(
                player_surface, (40, 70))
            window.blit(player_surface_lose, player_rect_lose)
            text_title = font.render(
                "Press  Space  to  restart", False, "White")
            text_rect = text_title.get_rect(center=(250, 164))
            window.blit(text_title, text_rect)

    pygame.display.update()
    clock.tick(60)
