import sys
from button import Button
from Game1 import *
from difficulty import *


class Menu:
    def __init__(self):
        self.SCREEN = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Mini-Games")

        self.BG = pygame.image.load("assets/menu-background.jpg")

    def get_font(self, size):
        return pygame.font.Font("assets/vag-world-bold.ttf", size)

    def main_menu(self):
        while True:
            self.SCREEN.blit(self.BG, (0, 0))

            MENU_MOUSE_POS = pygame.mouse.get_pos()

            MENU_TEXT = self.get_font(40).render("MINI-GAMES", True, "#99cc66")
            MENU_RECT = MENU_TEXT.get_rect(center=(400, 90))

            GAME1 = Button(image=pygame.image.load("assets/game1.png"), pos=(400, 200),
                           text_input="2048", font=self.get_font(50), base_color="#d7fcd4", hovering_color="Black")
            GAME2 = Button(image=pygame.image.load("assets/game1.png"), pos=(400, 350),
                           text_input="Blocks Crasher", font=self.get_font(50), base_color="#d7fcd4",
                           hovering_color="Black")
            QUIT_BUTTON = Button(image=pygame.image.load("assets/game1.png"), pos=(400, 500),
                                 text_input="Quit", font=self.get_font(50), base_color="#d7fcd4",
                                 hovering_color="Black")

            self.SCREEN.blit(MENU_TEXT, MENU_RECT)

            for button in [GAME1, GAME2, QUIT_BUTTON]:
                button.changeColor(MENU_MOUSE_POS)
                button.update(self.SCREEN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if GAME1.checkForInput(MENU_MOUSE_POS):
                        game1.play()
                    if GAME2.checkForInput(MENU_MOUSE_POS):
                        setting.run_menu()
                    if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                        pygame.quit()
                        sys.exit()

            pygame.display.update()


start = Menu()
if __name__ == "__main__":
    start.main_menu()
