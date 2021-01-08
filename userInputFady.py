import pygame
import sys


class DashBoardUserInput:
    def __init__(self):
        self.bg = pygame.image.load("Data/BG.png")
        self.width, self.height = self.bg.get_size()
        self.screen = pygame.display.set_mode((self.width, self.height))  # screen to render thing into
        self.battery = pygame.image.load("Data/Battery.png")
        self.big_arrow = pygame.image.load("Data/Big_Arrow.png")
        self.small_arrow = pygame.image.load("Data/Small_Arrow.png")
        self.brakes = pygame.image.load("Data/Brakes.png")
        self.engine = pygame.image.load("Data/Engine.png")
        self.flasher = pygame.image.load("Data/Flasher.png")
        self.signal_right = pygame.image.load("Data/RightArrow.png")
        self.signal_left = pygame.image.load("Data/LeftArrow.png")
        self.seat_belt = pygame.image.load("Data/SeatBelt.png")
        self.font = pygame.font.Font('freesansbold.ttf', 20)
        self.mouse = pygame.mouse.get_pos()  # print this when you need to find the mouse position on screen
        self.battery_flag = False
        self.brakes_flag = False
        self.engine_flag = False
        self.flasher_flag = False
        self.signal_left_flag = False
        self.signal_right_flag = False
        self.seat_belt_flag = False
        self.acceleration = 0
        self.big_arrow_angle = 126
        self.small_arrow_angle = 0
        self.cw = False
        self.cs = False

    def __check_for_events(self):
        self.mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            self.__set_flags(event)

    def __set_flags(self, event):
        """
        Change all the required flags to be used in the render function
        :param event:
        :return:
        """
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                self.cw = True
                self.cs = False
            if event.key == pygame.K_s:
                self.cw = False
                self.cs = True
        elif event.type == pygame.KEYUP:
            self.cw = False
            self.cs = False

    @staticmethod
    def __rotate(im, an):
        nm = pygame.transform.rotate(im, an)
        rect = nm.get_rect()
        rect.center = 600, 508
        return nm, rect

    def __render(self):
        """
        renders needed images based on the input
        :return:
        """
        self.screen.fill((254, 254, 254))
        self.screen.blit(self.bg, (0, 0))
        rect = self.big_arrow.get_rect()
        rect.center = 600, 508
        t1 = self.font.render(str(self.big_arrow_angle), True, (0, 0, 0))
        t2 = self.font.render(str(self.acceleration), True, (0, 0, 0))
        t1r = t1.get_rect()
        t1r.center = 200, 10
        t2r = t2.get_rect()
        t2r.center = 200, 30
        self.screen.blit(t1, t1r)
        self.screen.blit(t2, t2r)
        a = 0
        if self.cw and 126 >= self.big_arrow_angle >= -126:
            self.acceleration -= 0.2
            a = self.acceleration
        elif self.cs and 126 >= self.big_arrow_angle >= -126:
            self.acceleration += 0.2
            a = self.acceleration
        elif 126 >= self.big_arrow_angle >= -126:
            if a > 0:
                self.acceleration = - 1
            else:
                self.acceleration = + 1
        elif self.big_arrow_angle == 126:
            self.acceleration = 0
        self.big_arrow_angle += self.acceleration
        if self.big_arrow_angle > 126:
            self.big_arrow_angle = 126
        elif self.big_arrow_angle < -126:
            self.big_arrow_angle = -126

        x, y = self.__rotate(self.big_arrow, self.big_arrow_angle)
        self.screen.blit(x, y)

    def __check_for_warning(self):
        """
        MY JOB LEAVE IT ALONE
        :return:
        """
        pass

    def start(self):
        while True:
            self.__check_for_events()
            self.__render()
            self.__check_for_warning()
            pygame.display.flip()
