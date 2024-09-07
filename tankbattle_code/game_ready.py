import pygame
import sys
import main
import game_start

color = ['black', 'red', 'pink', 'orange', 'yellow', 'green', 'grey', 'blue', 'purple']


class play:
    def __init__(self, win):
        self.win = win

    def run(self):

        # bgm
        bgm2 = pygame.mixer.Sound('sounds/sanandreas.mp3')
        bgm3 = pygame.mixer.Sound('sounds/thatsgood/Ah_That_Is_Good.mp3')
        bgm4 = pygame.mixer.Sound('sounds/thatsgood/Sun_of_Beach.mp3')
        bgm5 = pygame.mixer.Sound('sounds/thatsgood/Fck_Coming.mp3')
        bgm2.play(-1)

        self.win.fill('white')
        # 坦克图标
        red_image = pygame.image.load('images/red.png')
        green_image = pygame.image.load('images/green.png')
        blue_image = pygame.image.load('images/blue.png')
        red_image = pygame.transform.scale(red_image, (120, 150))
        green_image = pygame.transform.scale(green_image, (120, 150))
        blue_image = pygame.transform.scale(blue_image, (120, 150))
        # 文字说明
        r_font = pygame.font.SysFont(None, 50)
        g_font = pygame.font.SysFont(None, 50)
        b_font = pygame.font.SysFont(None, 50)
        n_font = pygame.font.SysFont(None, 90)
        r_image = r_font.render('move:WASD   shoot:Q   press Q', True,
                                'black', 'white')
        g_image = g_font.render('move:IJKL   shoot:U   press U', True,
                                'black', 'white')
        b_image = b_font.render('move:direct   shoot:M   press M', True,
                                'black', 'white')
        n_image = n_font.render('                                   ', True,
                                        'black', 'white')
        # 返回
        back_text = "home"
        back_rect = pygame.Rect(10, 10, 200, 50)
        back_font = pygame.font.Font(None, 60)
        back_text = back_font.render(back_text, True, 'black', 'grey')

        # 绘制
        self.win.blit(r_image, (380, 100))
        self.win.blit(g_image, (380, 300))
        self.win.blit(b_image, (380, 500))
        self.win.blit(back_text, back_rect)
        pygame.display.flip()

        r_press = g_press = b_press = 0
        counter = i = 0
        none_fill = pygame.image.load('images/none.png')
        none_fill = pygame.transform.scale(none_fill, (120, 150))
        while True:
            s = r_press + g_press + b_press
            pygame.time.Clock().tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                # 返回
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if back_rect.collidepoint(event.pos):
                        bgm2.stop()
                        main.main()
                # 键盘
                elif event.type == pygame.KEYDOWN:
                    # 开始游戏
                    if event.key == pygame.K_SPACE and s >= 2:
                        bgm2.stop()
                        game_start.game_start(self.win, r_press, g_press, b_press).run()
                    # 选择坦克
                    if event.key == pygame.K_q:
                        if r_press == 0:

                            bgm3.play()
                            r_press = 1
                        else:
                            r_press = 0
                        print('q')
                    if event.key == pygame.K_u:
                        if g_press == 0:
                            bgm4.play()
                            g_press = 1
                        else:
                            g_press = 0
                        print('u')
                    if event.key == pygame.K_m:
                        if b_press == 0:
                            bgm5.play()
                            b_press = 1
                        else:
                            b_press = 0
                        print('m')
            # 绘制
            self.win.blit(red_image, (200, 30))
            self.win.blit(green_image, (200, 230))
            self.win.blit(blue_image, (200, 430))
            self.win.blit(n_image, (330, 590))

            # 选中时闪烁
            counter += 1
            if counter == 8:
                counter = 0
                if r_press:
                    self.win.blit(none_fill, (200, 30))
                if g_press:
                    self.win.blit(none_fill, (200, 230))
                if b_press:
                    self.win.blit(none_fill, (200, 430))
            i += 1
            if i == 9:
                i = 0
            start_font = pygame.font.SysFont(None, 85)
            start_image = start_font.render('press space to start', True,
                                            f'{color[i]}', 'white')
            if s >= 2:
                self.win.blit(start_image, (330, 590))

            pygame.display.flip()




