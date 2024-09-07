import pygame
import sys
import random
import main
import numpy
import winner
import time

color = ['black', 'pink', 'orange', 'yellow', 'grey', 'purple']


# 碰撞检测
def collision(walls, tk_rect):
    for wall in walls:
        if tk_rect.colliderect(pygame.Rect(wall)):
            return True
    return False


# 坦克出生
def tank_born(walls):
    while True:
        f = 0
        born = []
        '''red'''
        tank_x = random.randint(50, 1100)
        tank_y = random.randint(100, 500)
        tank_rect = (tank_x, tank_y, 27, 41)
        a_rect = pygame.Rect(tank_rect)
        for wall in walls:
            if a_rect.colliderect(pygame.Rect(wall)):
                f = 1
        if f == 1:
            continue
        born.append((tank_x, tank_y))
        '''green'''
        f = 0
        tank_x = random.randint(50, 1100)
        tank_y = random.randint(100, 500)
        tank_rect = (tank_x, tank_y, 27, 41)
        b_rect = pygame.Rect(tank_rect)
        for wall in walls:
            if b_rect.colliderect(pygame.Rect(wall)) or b_rect.colliderect(a_rect):
                f = 1
        if f == 1:
            continue
        born.append((tank_x, tank_y))
        '''blue'''
        f = 0
        tank_x = random.randint(50, 1100)
        tank_y = random.randint(100, 500)
        tank_rect = (tank_x, tank_y, 27, 41)
        c_rect = pygame.Rect(tank_rect)
        for wall in walls:
            if c_rect.colliderect(pygame.Rect(wall)) or c_rect.colliderect(a_rect) or c_rect.colliderect(b_rect):
                f = 1
        if f == 1:
            continue
        born.append((tank_x, tank_y))
        break
    print(born)
    return born


def map(wall, win):
    # 地图生成
    pygame.draw.rect(win, 'white', (0, 57, 1200, 538))
    t = 50
    j_x = 150
    j_y = 200
    q_x = 900
    q_y = 100
    k_x = 400
    k_y = 700
    while t > 0:
        t -= 1
        if j_x > 1000 or j_x < 150:
            j_x = 250
        if j_y > 500 or j_y < 100:
            j_y = 300
        if q_x > 1000 or q_x < 150:
            q_x = 650
        if q_y > 500 or q_y < 100:
            q_y = 200
        if k_x > 1000 or k_x < 150:
            k_x = 550
        if k_y > 500 or k_y < 100:
            k_y = 400
        j = (j_x, j_y, 50, 50)
        q = (q_x, q_y, 50, 50)
        k = (k_x, k_y, 50, 50)
        wall.append(j)
        wall.append(q)
        wall.append(k)
        s = random.randint(0, 3)
        if s == 0:
            j_y -= 50
        elif s == 1:
            j_x += 50
        elif s == 2:
            j_y += 50
        elif s == 3:
            j_x -= 50
        s = random.randint(0, 3)
        if s == 0:
            q_y -= 50
        elif s == 1:
            q_x += 50
        elif s == 2:
            q_y += 50
        elif s == 3:
            q_x -= 50
        s = random.randint(0, 3)
        if s == 0:
            k_y -= 50
        elif s == 1:
            k_x += 50
        elif s == 2:
            k_y += 50
        elif s == 3:
            k_x -= 50

    return wall


class game_start:
    def __init__(self, win, red_tank, green_tank, blue_tank):
        self.win = win
        self.red_tank = red_tank
        self.green_tank = green_tank
        self.blue_tank = blue_tank

    def run(self):
        # bgm
        bgm6 = pygame.mixer.Sound('sounds/gogogo_01.wav')
        bgm7 = pygame.mixer.Sound('sounds/fly.mp3')
        bgm9 = pygame.mixer.Sound('sounds/thatsgood/先辈啊啊啊啊.mp3')
        bgm10 = pygame.mixer.Sound('sounds/thatsgood/成龙duang.wav')
        bgm11 = pygame.mixer.Sound('sounds/thatsgood/先辈哼.mp3')
        bgm12 = pygame.mixer.Sound('sounds/钢管.mp3')
        bgm13 = pygame.mixer.Sound('sounds/吔_01.wav')
        bgm6.play()
        bgm7.play(-1)

        self.win.fill('white')
        r_again = self.red_tank
        g_again = self.green_tank
        b_again = self.blue_tank

        # 图标
        red_image = pygame.image.load('images/red.png')
        green_image = pygame.image.load('images/green.png')
        blue_image = pygame.image.load('images/blue.png')
        red_shoot = pygame.image.load('images/red_s.png')
        green_shoot = pygame.image.load('images/green_s.png')
        blue_shoot = pygame.image.load('images/blue_s.png')
        die_tank = pygame.image.load('images/icon.png')
        die_tank = pygame.transform.scale(die_tank, (41, 41))
        red_image = pygame.transform.scale(red_image, (27, 41))
        green_image = pygame.transform.scale(green_image, (27, 41))
        blue_image = pygame.transform.scale(blue_image, (27, 41))

        # 分数
        r_mark = g_mark = b_mark = 0
        r_font = pygame.font.SysFont(None, 50)
        g_font = pygame.font.SysFont(None, 50)
        b_font = pygame.font.SysFont(None, 50)
        r_image = r_font.render(f'{r_mark}', True,
                                'red', 'white')
        g_image = g_font.render(f'{g_mark}', True,
                                'green', 'white')
        b_image = b_font.render(f'{b_mark}', True,
                                'blue', 'white')
        if self.red_tank:
            self.win.blit(red_image, (200, 620))
            self.win.blit(r_image, (250, 630))
        if self.green_tank:
            self.win.blit(green_image, (550, 620))
            self.win.blit(g_image, (600, 630))
        if self.blue_tank:
            self.win.blit(blue_image, (910, 620))
            self.win.blit(b_image, (960, 630))

        # 边界墙
        l1 = (0, 600, 1200, 2)
        l2 = (0, 55, 1200, 2)
        l3 = (0, 0, 2, 680)
        l4 = (1200, 0, 2, 680)

        # 返回
        back_text = "home"
        back_rect = pygame.Rect(10, 10, 200, 50)
        back_font = pygame.font.Font(None, 60)
        back_text = back_font.render(back_text, True, 'black', 'grey')
        self.win.blit(back_text, back_rect)

        # 地图刷新
        new_color = color[random.randint(0, 5)]
        walls = [l1, l2, l3, l4]
        wall = map(walls, self.win)
        wall = list(set(wall))
        wall_hp = [3]*len(wall)
        print(wall)
        for w in wall:
            pygame.draw.rect(self.win, new_color, w)
        map_text = "New map"
        map_rect = pygame.Rect(980, 10, 200, 50)
        map_font = pygame.font.Font(None, 60)
        map_text = map_font.render(map_text, True, 'black', 'grey')
        self.win.blit(map_text, map_rect)

        # 坦克出生
        tank_hp = [5]*3
        rtank = pygame.image.load('images/red.png')
        gtank = pygame.image.load('images/green.png')
        btank = pygame.image.load('images/blue.png')
        tb = tank_born(wall)
        r_rect = rtank.get_rect(center=tb[0])
        g_rect = gtank.get_rect(center=tb[1])
        b_rect = btank.get_rect(center=tb[2])
        if self.red_tank:
            self.win.blit(rtank, r_rect)
        if self.green_tank:
            self.win.blit(gtank, g_rect)
        if self.blue_tank:
            self.win.blit(btank, b_rect)

        # 速度
        speed = 2
        rot_speed = 4
        bullet_speed = 6

        # 初始角度
        rtank_angle = 0
        gtank_angle = 0
        btank_angle = 0
        rotated_red = pygame.transform.rotate(rtank, rtank_angle)
        rrotated_rect = rotated_red.get_rect(center=r_rect.center)
        rotated_green = pygame.transform.rotate(gtank, gtank_angle)
        grotated_rect = rotated_green.get_rect(center=g_rect.center)
        rotated_blue = pygame.transform.rotate(btank, btank_angle)
        brotated_rect = rotated_blue.get_rect(center=b_rect.center)

        # 子弹
        r_cd = g_cd = b_cd = 0
        r_bt = []
        g_bt = []
        b_bt = []
        red_bullet = pygame.image.load('images/roundr.png')
        green_bullet = pygame.image.load('images/roundg.png')
        blue_bullet = pygame.image.load('images/roundb.png')

        while True:
            # winner
            if self.red_tank + self.green_tank + self.blue_tank == 1:
                bgm7.stop()
                time.sleep(3.3)
                if self.red_tank:
                    winner.the_winner(self.win, rtank, red_shoot, r_again, g_again, b_again).run()
                elif self.green_tank:
                    winner.the_winner(self.win, gtank, green_shoot, r_again, g_again, b_again).run()
                elif self.blue_tank:
                    winner.the_winner(self.win, btank, blue_shoot, r_again, g_again, b_again).run()
                break
            elif len(wall) == 4:
                bgm7.stop()
                time.sleep(3.3)
                m = max(r_mark, g_mark, b_mark)
                if m == r_mark:
                    winner.the_winner(self.win, rtank, red_shoot, r_again, g_again, b_again).run()
                elif m == g_mark:
                    winner.the_winner(self.win, gtank, green_shoot, r_again, g_again, b_again).run()
                elif m == b_mark:
                    winner.the_winner(self.win, btank, blue_shoot, r_again, g_again, b_again).run()
                break

            f_r_shoot = f_g_shoot = f_b_shoot = 0
            r_cd += 1
            g_cd += 1
            b_cd += 1

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if back_rect.collidepoint(event.pos):
                        bgm7.stop()
                        main.main()
                    elif map_rect.collidepoint(event.pos):
                        new_color = color[random.randint(0, 5)]
                        walls = [l1, l2, l3, l4]

                        wall = map(walls, self.win)
                        wall = list(set(wall))
                        wall_hp = [3] * len(wall)
                        tank_hp = [5] * 3
                        print(wall)
                        tb = tank_born(wall)
                        r_rect = rtank.get_rect(center=tb[0])
                        g_rect = gtank.get_rect(center=tb[1])
                        b_rect = btank.get_rect(center=tb[2])
                        if self.red_tank:
                            self.win.blit(rtank, r_rect)
                        if self.green_tank:
                            self.win.blit(gtank, g_rect)
                        if self.blue_tank:
                            self.win.blit(btank, b_rect)

            # 永远都别想出去
            for w in wall:
                pygame.draw.rect(self.win, new_color, w)
            pygame.draw.rect(self.win, 'black', l1)
            pygame.draw.rect(self.win, 'black', l2)
            pygame.draw.rect(self.win, 'black', l3)
            pygame.draw.rect(self.win, 'black', l4)
            if l1 not in wall:
                wall.append(l1)
                wall_hp.append(999)
            if l2 not in wall:
                wall.append(l2)
                wall_hp.append(999)
            if l3 not in wall:
                wall.append(l3)
                wall_hp.append(999)
            if l4 not in wall:
                wall.append(l4)
                wall_hp.append(3)

            # 击杀
            if tank_hp[0] == 0:
                bgm9.play()
                self.red_tank = 0
                pygame.draw.rect(self.win, 'white', rrotated_rect)
                self.win.blit(die_tank, rrotated_rect)
                r_rect = pygame.Rect((0, 0, 0, 0))
                self.win.blit(die_tank, (193, 620))
                tank_hp[0] -= 1
                g_mark += 20
                b_mark += 20
            if tank_hp[1] == 0:
                bgm9.play()
                self.green_tank = 0
                pygame.draw.rect(self.win, 'white', grotated_rect)
                self.win.blit(die_tank, grotated_rect)
                g_rect = pygame.Rect((0, 0, 0, 0))
                self.win.blit(die_tank, (543, 620))
                tank_hp[1] -= 1
                r_mark += 20
                b_mark += 20
            if tank_hp[2] == 0:
                bgm9.play()
                self.blue_tank = 0
                pygame.draw.rect(self.win, 'white', brotated_rect)
                self.win.blit(die_tank, brotated_rect)
                b_rect = pygame.Rect((0, 0, 0, 0))
                self.win.blit(die_tank, (903, 620))
                tank_hp[2] -= 1
                g_mark += 20
                r_mark += 20

            # 分数刷新
            r_image = r_font.render(f'{r_mark}', True,
                                    'red', 'white')
            g_image = g_font.render(f'{g_mark}', True,
                                    'green', 'white')
            b_image = b_font.render(f'{b_mark}', True,
                                    'blue', 'white')
            if self.red_tank:
                self.win.blit(r_image, (250, 630))
            if self.green_tank:
                self.win.blit(g_image, (600, 630))
            if self.blue_tank:
                self.win.blit(b_image, (960, 630))

            keys = pygame.key.get_pressed()
            # red
            if self.red_tank:
                '''清除'''
                pygame.draw.rect(self.win, 'white', r_rect)
                pygame.draw.rect(self.win, 'white', rrotated_rect)
                for i in r_bt:
                    pygame.draw.rect(self.win, 'white', i[0])
                '''移动'''
                if keys[pygame.K_a]:
                    rtank_angle += rot_speed
                if keys[pygame.K_d]:
                    rtank_angle -= rot_speed
                if rtank_angle == 360 or rtank_angle == -360:
                    rtank_angle = 0
                if keys[pygame.K_s]:
                    r_rect.y += speed * numpy.cos(numpy.radians(rtank_angle))
                    r_rect.x += speed * numpy.sin(numpy.radians(rtank_angle))
                    if collision(wall, r_rect) or r_rect.colliderect(g_rect) or r_rect.colliderect(b_rect):
                        r_rect.y -= speed * numpy.cos(numpy.radians(rtank_angle))
                        r_rect.x -= speed * numpy.sin(numpy.radians(rtank_angle))
                if keys[pygame.K_w]:
                    r_rect.y -= speed * numpy.cos(numpy.radians(rtank_angle))
                    r_rect.x -= speed * numpy.sin(numpy.radians(rtank_angle))
                    if collision(wall, r_rect) or r_rect.colliderect(g_rect) or r_rect.colliderect(b_rect):
                        r_rect.y += speed * numpy.cos(numpy.radians(rtank_angle))
                        r_rect.x += speed * numpy.sin(numpy.radians(rtank_angle))
                '''发射'''
                if keys[pygame.K_q] and r_cd > 25:
                    bgm13.play()
                    r_cd = 0
                    f_r_shoot = 1
                rotated_red = pygame.transform.rotate(rtank, rtank_angle)
                rrotated_rect = rotated_red.get_rect(center=r_rect.center)
                if r_cd < 8:
                    rotated_red = pygame.transform.rotate(red_shoot, rtank_angle)
                    rrotated_rect = rotated_red.get_rect(center=r_rect.center)
                if f_r_shoot:
                    r_bt_shoot = pygame.transform.rotate(red_bullet, rtank_angle)
                    r_bt_rect = r_bt_shoot.get_rect(center=r_rect.center)
                    r_bt.append((r_bt_rect, rtank_angle))
                for i in r_bt:
                    f_hit = 0
                    for w in range(len(wall)):
                        if i[0].colliderect(pygame.Rect(wall[w])):
                            blow = w
                            f_hit = 1
                    i[0].y -= bullet_speed * numpy.cos(numpy.radians(i[1]))
                    i[0].x -= bullet_speed * numpy.sin(numpy.radians(i[1]))
                    self.win.blit(red_bullet, i[0])
                    if f_hit:
                        bgm10.play()
                        wall_hp[blow] -= 1
                        r_bt.remove(i)
                        pygame.draw.rect(self.win, 'white', i[0])
                        if wall_hp[blow] == 0:
                            bgm12.play()
                            pygame.draw.rect(self.win, 'white', pygame.Rect(wall[blow]))
                            r_mark += 1
                            wall_hp.remove(wall_hp[blow])
                            wall.remove(wall[blow])
                    if i[0].colliderect(g_rect):
                        bgm11.play()
                        pygame.draw.rect(self.win, 'white', i[0])
                        tank_hp[1] -= 1
                        try:
                            r_bt.remove(i)
                        except:
                            pass
                    if i[0].colliderect(b_rect):
                        bgm11.play()
                        pygame.draw.rect(self.win, 'white', i[0])
                        tank_hp[2] -= 1
                        try:
                            r_bt.remove(i)
                        except:
                            pass
                '''重绘'''
                self.win.blit(rotated_red, rrotated_rect)

            # green
            if self.green_tank:
                '''清除'''
                pygame.draw.rect(self.win, 'white', g_rect)
                pygame.draw.rect(self.win, 'white', grotated_rect)
                for j in g_bt:
                    pygame.draw.rect(self.win, 'white', j[0])
                '''移动'''
                if keys[pygame.K_j]:
                    gtank_angle += rot_speed
                if keys[pygame.K_l]:
                    gtank_angle -= rot_speed
                if gtank_angle == 360 or gtank_angle == -360:
                    gtank_angle = 0
                if keys[pygame.K_k]:
                    g_rect.y += speed * numpy.cos(numpy.radians(gtank_angle))
                    g_rect.x += speed * numpy.sin(numpy.radians(gtank_angle))
                    if collision(wall, g_rect) or r_rect.colliderect(g_rect) or g_rect.colliderect(b_rect):
                        g_rect.y -= speed * numpy.cos(numpy.radians(gtank_angle))
                        g_rect.x -= speed * numpy.sin(numpy.radians(gtank_angle))
                if keys[pygame.K_i]:
                    g_rect.y -= speed * numpy.cos(numpy.radians(gtank_angle))
                    g_rect.x -= speed * numpy.sin(numpy.radians(gtank_angle))
                    if collision(wall, g_rect) or r_rect.colliderect(g_rect) or g_rect.colliderect(b_rect):
                        g_rect.y += speed * numpy.cos(numpy.radians(gtank_angle))
                        g_rect.x += speed * numpy.sin(numpy.radians(gtank_angle))
                '''发射'''
                if keys[pygame.K_u] and g_cd > 25:
                    bgm13.play()
                    g_cd = 0
                    f_g_shoot = 1
                rotated_green = pygame.transform.rotate(gtank, gtank_angle)
                grotated_rect = rotated_green.get_rect(center=g_rect.center)
                if g_cd < 8:
                    rotated_green = pygame.transform.rotate(green_shoot, gtank_angle)
                    grotated_rect = rotated_green.get_rect(center=g_rect.center)
                if f_g_shoot:
                    g_bt_shoot = pygame.transform.rotate(green_bullet, gtank_angle)
                    g_bt_rect = g_bt_shoot.get_rect(center=g_rect.center)
                    g_bt.append((g_bt_rect, gtank_angle))
                for j in g_bt:
                    f_hit = 0
                    for w in range(len(wall)):
                        if j[0].colliderect(pygame.Rect(wall[w])):
                            blow = w
                            f_hit = 1
                    j[0].y -= bullet_speed * numpy.cos(numpy.radians(j[1]))
                    j[0].x -= bullet_speed * numpy.sin(numpy.radians(j[1]))
                    self.win.blit(green_bullet, j[0])
                    if f_hit:
                        bgm10.play()
                        wall_hp[blow] -= 1
                        g_bt.remove(j)
                        pygame.draw.rect(self.win, 'white', j[0])
                        if wall_hp[blow] == 0:
                            bgm12.play()
                            pygame.draw.rect(self.win, 'white', pygame.Rect(wall[blow]))
                            g_mark += 1
                            wall_hp.remove(wall_hp[blow])
                            wall.remove(wall[blow])
                    if j[0].colliderect(r_rect):
                        bgm11.play()
                        pygame.draw.rect(self.win, 'white', j[0])
                        tank_hp[0] -= 1
                        try:
                            g_bt.remove(j)
                        except:
                            pass
                    if j[0].colliderect(b_rect):
                        bgm11.play()
                        pygame.draw.rect(self.win, 'white', j[0])
                        tank_hp[2] -= 1
                        try:
                            g_bt.remove(j)
                        except:
                            pass
                '''重绘'''
                self.win.blit(rotated_green, grotated_rect)

            # blue
            if self.blue_tank:
                '''清除'''
                pygame.draw.rect(self.win, 'white', b_rect)
                pygame.draw.rect(self.win, 'white', brotated_rect)
                for k in b_bt:
                    pygame.draw.rect(self.win, 'white', k[0])
                '''移动'''
                if keys[pygame.K_LEFT]:
                    btank_angle += rot_speed
                if keys[pygame.K_RIGHT]:
                    btank_angle -= rot_speed
                if btank_angle == 360 or btank_angle == -360:
                    btank_angle = 0
                if keys[pygame.K_DOWN]:
                    b_rect.y += speed*numpy.cos(numpy.radians(btank_angle))
                    b_rect.x += speed*numpy.sin(numpy.radians(btank_angle))
                    if collision(wall, b_rect) or r_rect.colliderect(b_rect) or g_rect.colliderect(b_rect):
                        b_rect.y -= speed * numpy.cos(numpy.radians(btank_angle))
                        b_rect.x -= speed * numpy.sin(numpy.radians(btank_angle))
                if keys[pygame.K_UP]:
                    b_rect.y -= speed*numpy.cos(numpy.radians(btank_angle))
                    b_rect.x -= speed*numpy.sin(numpy.radians(btank_angle))
                    if collision(wall, b_rect) or r_rect.colliderect(b_rect) or g_rect.colliderect(b_rect):
                        b_rect.y += speed * numpy.cos(numpy.radians(btank_angle))
                        b_rect.x += speed * numpy.sin(numpy.radians(btank_angle))
                '''发射'''
                if keys[pygame.K_m] and b_cd > 25:
                    bgm13.play()
                    b_cd = 0
                    f_b_shoot = 1
                rotated_blue = pygame.transform.rotate(btank, btank_angle)
                brotated_rect = rotated_blue.get_rect(center=b_rect.center)
                if b_cd < 8:
                    rotated_blue = pygame.transform.rotate(blue_shoot, btank_angle)
                    brotated_rect = rotated_blue.get_rect(center=b_rect.center)
                if f_b_shoot:
                    b_bt_shoot = pygame.transform.rotate(blue_bullet, btank_angle)
                    b_bt_rect = b_bt_shoot.get_rect(center=b_rect.center)
                    b_bt.append((b_bt_rect, btank_angle))
                for k in b_bt:
                    f_hit = 0
                    for w in range(len(wall)):
                        if k[0].colliderect(pygame.Rect(wall[w])):
                            blow = w
                            f_hit = 1
                    k[0].y -= bullet_speed * numpy.cos(numpy.radians(k[1]))
                    k[0].x -= bullet_speed * numpy.sin(numpy.radians(k[1]))
                    self.win.blit(blue_bullet, k[0])
                    if f_hit:
                        bgm10.play()
                        wall_hp[blow] -= 1
                        b_bt.remove(k)
                        pygame.draw.rect(self.win, 'white', k[0])
                        if wall_hp[blow] == 0:
                            bgm12.play()
                            pygame.draw.rect(self.win, 'white', pygame.Rect(wall[blow]))
                            b_mark += 1
                            wall_hp.remove(wall_hp[blow])
                            wall.remove(wall[blow])
                    if k[0].colliderect(r_rect):
                        bgm11.play()
                        pygame.draw.rect(self.win, 'white', k[0])
                        tank_hp[0] -= 1
                        try:
                            b_bt.remove(k)
                        except:
                            pass
                    if k[0].colliderect(g_rect):
                        bgm11.play()
                        pygame.draw.rect(self.win, 'white', k[0])
                        tank_hp[1] -= 1
                        try:
                            b_bt.remove(k)
                        except:
                            pass
                '''重绘'''
                self.win.blit(rotated_blue, brotated_rect)

            pygame.display.flip()
            pygame.time.Clock().tick(60)
