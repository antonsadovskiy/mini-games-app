import pygame
from random import randrange as rnd
from difficulty import *


class Arkanoid:
    def __init__(self):
        self.fps = 60
        self.clock = pygame.time.Clock()
        self.WIDTH = 800
        self.HEIGHT = 600
        self.SCREEN = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.block_list = [pygame.Rect(10 + 72 * i, 10 + 30 * j, 60, 20) for i in range(11) for j in range(9)]
        self.color_list = [(rnd(30, 256), rnd(30, 256), rnd(30, 256)) for i in range(11) for j in range(9)]
        self.fps = 60

        # paddle settings
        self.paddleW = 100
        self.paddleH = 10
        self.paddleSpeed = 20
        self.paddle = pygame.Rect(self.WIDTH // 2 - self.paddleW // 2, self.HEIGHT - self.paddleH - 10, self.paddleW,
                                  self.paddleH)

        # ball settings
        self.ballRadius = 7
        # self.ballSpeed = 10
        self.ballRect = int(self.ballRadius * 2 ** 0.5)
        self.ball = pygame.Rect(rnd(self.ballRect, self.WIDTH - self.ballRect), self.HEIGHT // 2, self.ballRect,
                                self.ballRect)
        self.dx = 1
        self.dy = -1

        pygame.init()

    def detect_collision(self, dx, dy, ball, rect):
        if dx > 0:
            delta_x = ball.right - rect.left
        else:
            delta_x = rect.right - ball.left
        if dy > 0:
            delta_y = ball.bottom - rect.top
        else:
            delta_y = rect.bottom - ball.top

        if abs(delta_x - delta_y) < 10:
            dx, dy = -dx, -dy
        elif delta_x > delta_y:
            dy = -dy
        elif delta_y > delta_x:
            dx = -dx
        return dx, dy

    def get_font(self, size):
        return pygame.font.Font("assets/vag-world-bold.ttf", size)

    def lose(self):
        MENU_TEXT = self.get_font(50).render("YOU LOST!", True, "red")
        MENU_RECT = MENU_TEXT.get_rect(center=(400, 390))
        self.SCREEN.blit(MENU_TEXT, MENU_RECT)
        pygame.display.update()

    def play(self, ball_speed):
        while True:
            img = pygame.image.load('assets/Background.png').convert()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
            self.SCREEN.blit(img, (0, 0))

            # ini sound of ball hit
            sound1 = pygame.mixer.Sound('assets/ball_hit_block.wav')
            # sound2 = pygame.mixer.Sound('assets/ball_hit_paddle.wav')
            # drawing blocks
            [pygame.draw.rect(self.SCREEN, self.color_list[color], block) for color, block in
             enumerate(self.block_list)]
            pygame.draw.rect(self.SCREEN, pygame.Color('darkorange'), self.paddle)
            pygame.draw.circle(self.SCREEN, pygame.Color('white'), self.ball.center, self.ballRadius)

            # ball movement
            self.ball.x += ball_speed * self.dx
            self.ball.y += ball_speed * self.dy

            # collision left right
            if self.ball.centerx < self.ballRadius or self.ball.centerx > self.WIDTH - self.ballRadius:
                self.dx = -self.dx
            # collision top
            if self.ball.centery < self.ballRadius:
                self.dy = -self.dy

            if self.ball.centery > self.HEIGHT + 20:
                self.lose()

            # collision paddle
            if self.ball.colliderect(self.paddle) and self.dy > 0:
                sound1.play()
                self.dx, self.dy = self.detect_collision(self.dx, self.dy, self.ball, self.paddle)

            # collision blocks
            hit_index = self.ball.collidelist(self.block_list)
            if hit_index != -1:
                sound1.play()
                hit_rect = self.block_list.pop(hit_index)
                hit_color = self.color_list.pop(hit_index)
                self.dx, self.dy = self.detect_collision(self.dx, self.dy, self.ball, hit_rect)

            # control
            key = pygame.key.get_pressed()
            if key[pygame.K_LEFT] and self.paddle.left > 0:
                self.paddle.left -= self.paddleSpeed
            if key[pygame.K_RIGHT] and self.paddle.right < self.WIDTH:
                self.paddle.right += self.paddleSpeed

            pygame.display.flip()
            self.clock.tick(self.fps)


game2 = Arkanoid()
