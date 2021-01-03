import pygame
import sys
import pandas as pd


class DashBoardFileInput:
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
        self.mouse = pygame.mouse.get_pos()  # print this when you need to find the mouse position on screen
        self.battery_flag = False
        self.brakes_flag = False
        self.engine_flag = False
        self.flasher_flag = False
        self.signal_left_flag = False
        self.signal_right_flag = False
        self.seat_belt_flag = False
        self.big_arrow_angle = 0
        self.small_arrow_angle = 0
        self.data = pd.read_csv("FILENAMEHERE")  # put the file in the Data directory and access it here

    def __check_for_events(self):
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
        pass

    def __render(self):
        """
        renders needed images based on the input
        :return:
        """
        pass

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
