import pygame
import sys
import main
import game_start

color = ['black', 'red', 'pink', 'orange', 'yellow', 'green', 'grey', 'blue', 'purple']


class the_winner:
    def __init__(self, win, winner_tank, winner_tank_shoot, r_again, g_again, b_again):
        self.win = win
        self.winner_tank = winner_tank
        self.winner_tank_shoot = winner_tank_shoot
        self.r_again = r_again
        self.g_again = g_again
        self.b_again = b_again

    def run(self):
        # bgm
        bgm8 = pygame.mixer.Sound('sounds/sotired.mp3')
        bgm8.play(-1)

        self.win.fill('white')

        back_text = "home"
        back_rect = pygame.Rect(10, 10, 200, 50)
        back_font = pygame.font.Font(None, 60)
        back_text = back_font.render(back_text, True, 'black', 'grey')
        self.win.blit(back_text, back_rect)

        again_text = "again"
        again_rect = pygame.Rect(1080, 10, 200, 50)
        again_font = pygame.font.Font(None, 60)
        again_text = again_font.render(again_text, True, 'black', 'grey')
        self.win.blit(again_text, again_rect)

        txt_font = pygame.font.SysFont(None, 250)

        winner_tank_bullet = pygame.image.load('images/round.png')
        winner_tank_bullet = pygame.transform.scale(winner_tank_bullet, (45, 45))
        winner_tank = pygame.transform.scale(self.winner_tank, (162, 246))
        winner_tank_shoot = pygame.transform.scale(self.winner_tank_shoot, (162, 246))
        self.win.blit(winner_tank, (520, 180))
        t = i = s = f = 0
        bullet = []
        bullet_speed = 10
        while True:
            if f:
                bullet.append(pygame.Rect(578, 180, 45, 45))
            for k in bullet:
                pygame.draw.rect(self.win, 'white', k)
                k.y -= bullet_speed
                self.win.blit(winner_tank_bullet, k)

            f = 0
            s += 1
            if s % 3 == 1:
                self.win.blit(winner_tank_shoot, (520, 180))
                f = 1
            else:
                self.win.blit(winner_tank, (520, 180))

            t += 1
            if t % 3 == 0:
                t = 0
                i += 1
            if i == 9:
                i = 0
            txt_image = txt_font.render('Winner', True,
                                        f'{color[i]}', 'white')
            self.win.blit(txt_image, (300, 450))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if back_rect.collidepoint(event.pos):
                        bgm8.stop()
                        main.main()
                    if again_rect.collidepoint(event.pos):
                        bgm8.stop()
                        game_start.game_start(self.win, self.r_again, self.g_again, self.b_again).run()

            pygame.display.flip()
            pygame.time.Clock().tick(30)
