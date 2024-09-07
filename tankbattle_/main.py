
import pygame
import sys
import game_ready

color = ['black', 'red', 'pink', 'orange', 'yellow', 'green', 'grey', 'blue', 'purple']


def main():

    # 主窗口
    pygame.init()
    win = pygame.display.set_mode((1200, 680))
    win_rect = win.get_rect()
    pygame.display.set_caption('坦克大战')
    win.fill('white')
    txt_font = pygame.font.SysFont(None, 180)

    # 坦克图标
    red_image = pygame.image.load('images/red.png')
    green_image = pygame.image.load('images/green.png')
    blue_image = pygame.image.load('images/blue.png')
    red_image = pygame.transform.scale(red_image, (120, 150))
    green_image = pygame.transform.scale(green_image, (120, 150))
    blue_image = pygame.transform.scale(blue_image, (120, 150))

    # 按钮
    l_text = "Game Start"
    l_rect = pygame.Rect(500, 520, 200, 50)
    l_font = pygame.font.Font(None, 100)
    l_text = l_font.render(l_text, True, 'black', 'grey')
    l_rect = l_text.get_rect(center=l_rect.center)

    # bgm
    bgm0 = pygame.mixer.Sound('sounds/thatsgood/BoyNextDoor1.mp3')
    bgm1 = pygame.mixer.Sound('sounds/开头鬼畜.wav')
    bgm1.play(-1)

    i = t = 0
    # 主循环
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # 点击按钮
            if event.type == pygame.MOUSEBUTTONDOWN:
                if l_rect.collidepoint(event.pos):
                    bgm1.stop()
                    bgm0.play()
                    game_ready.play(win).run()

        # 彩虹标题
        t += 1
        if t % 3 == 0:
            t = 0
            i += 1
        if i == 9:
            i = 0
        txt_image = txt_font.render('Tank battle', True,
                                    f'{color[i]}', 'white')
        # 绘制
        win.blit(txt_image, (250, 60))
        win.blit(red_image, (140, 250))
        win.blit(green_image, (540, 250))
        win.blit(blue_image, (940, 250))
        win.blit(l_text, l_rect)

        pygame.display.flip()
        pygame.time.Clock().tick(60)


if __name__ == '__main__':
    main()
