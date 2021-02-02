# import fileInput
import userInput
import pygame
import sys


class startingScreen:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((600, 200))
        self.font = pygame.font.Font('freesansbold.ttf', 20)
        self.mouse = pygame.mouse.get_pos()

    def render(self):
        main_text = self.font.render("Please choose which mode you want:", True, (0, 0, 0))
        user_text = self.font.render("User Driven", True, (0, 0, 0))
        file_text = self.font.render("File Driven", True, (0, 0, 0))
        main_text_rect = main_text.get_rect()
        main_text_rect.center = 300, 40
        user_text_rect = user_text.get_rect()
        user_text_rect.center = 120, 100
        file_text_rect = file_text.get_rect()
        file_text_rect.center = 500, 100
        self.screen.blit(main_text, main_text_rect)
        self.screen.blit(user_text, user_text_rect)
        self.screen.blit(file_text, file_text_rect)

    def start(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 110 > self.mouse[1] > 85:
                        if 180 > self.mouse[0] > 60:
                            return "USER"
                        elif 555 > self.mouse[0] > 445:
                            return "FILE"
            self.mouse = pygame.mouse.get_pos()
            self.screen.fill((245, 245, 245))
            self.render()
            pygame.display.flip()


s = startingScreen()
mode = s.start()
if mode == "USER":
    dash_board = userInput.DashBoardUserInput()
# else:
#     dash_board = fileInput.DashBoardFileInput()
dash_board.start()
