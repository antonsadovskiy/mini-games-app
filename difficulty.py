import sys
from button import Button
from Game2 import *
import pygame


class Difficulty:
    def __init__(self):
        self.SCREEN = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Mini-Games")

        self.ball_speed = 0
        self.BG = pygame.image.load("assets/menu-background.jpg")

    def get_font(self, size):
        return pygame.font.Font("assets/vag-world-bold.ttf", size)

    def run_menu(self):
        while True:
            self.SCREEN.blit(self.BG, (0, 0))

            MENU_MOUSE_POS = pygame.mouse.get_pos()

            MENU_TEXT = self.get_font(40).render("Select Difficulty", True, "#99cc66")
            MENU_RECT = MENU_TEXT.get_rect(center=(400, 90))

            GAME_EASY = Button(image=pygame.image.load("assets/game1.png"), pos=(400, 200),
                               text_input="EASY", font=self.get_font(50), base_color="#d7fcd4", hovering_color="Black")
            GAME_MEDIUM = Button(image=pygame.image.load("assets/game1.png"), pos=(400, 350),
                                 text_input="MEDIUM", font=self.get_font(50), base_color="#d7fcd4",
                                 hovering_color="Black")
            GAME_HARD = Button(image=pygame.image.load("assets/game1.png"), pos=(400, 500),
                               text_input="HARD", font=self.get_font(50), base_color="#d7fcd4",
                               hovering_color="Black")

            self.SCREEN.blit(MENU_TEXT, MENU_RECT)

            for button in [GAME_EASY, GAME_MEDIUM, GAME_HARD]:
                button.changeColor(MENU_MOUSE_POS)
                button.update(self.SCREEN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if GAME_EASY.checkForInput(MENU_MOUSE_POS):
                        ball_speed = 5
                        game2.play(ball_speed)
                    if GAME_MEDIUM.checkForInput(MENU_MOUSE_POS):
                        ball_speed = 7
                        game2.play(ball_speed)
                    if GAME_HARD.checkForInput(MENU_MOUSE_POS):
                        ball_speed = 10
                        game2.play(ball_speed)

            pygame.display.update()


setting = Difficulty()
if __name__ == "__main__":
    setting.run_menu()
