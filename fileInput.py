import pygame
import sys
import pandas as pd


class DashBoardFileInput:
    def __init__(self):
        self.i = 0 
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
        #self.brakes_flag = False
        self.engine_flag = False
        self.flasher_flag = False
        self.signal_left_flag = False
        self.signal_right_flag = False
        self.seat_belt_flag = False
        self.big_arrow_angle = 0
        self.small_arrow_angle = 0
        self.data = pd.read_excel('data.xlsx')  # put the file in the Data directory and access it here

    def __check_for_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        self.__set_flags()

    def __set_flags(self):
        """
        Change all the required flags to be used in the render function
        :return:
        """
        while self.i < 100:
            acc = self.data['Acceleration'][self.i]  #number not flag
            fuel = self.data['Fuel'][self.i] #number not flag
            self.battery_flag = self.data['Battery'][self.i]
            self.seat_belt_flag = self.data['Set Belt'][self.i]
            self.flasher_flag = self.data['Alart'][self.i]
            self.engine_flag = self.data['Engine'][self.i]
            self.signal_left_flag = self.data['Left'][self.i]
            self.signal_right_flag = self.data['Right'][self.i]
            
            
            

    def __render(self):
        """
        renders needed images based on the input
        :return:
        """
        if self.battery_flag:
                self.screen.blit(self.battery , (0,0))
            if self.seat_belt_flag:
                self.screen.blit(self.seat_belt, (0,0))
            if self.flasher_flag:
                self.screen.blit(self.flasher , (0,0))
            if self.engine_flag:
                self.screen.blit(self.engine, (0,0))
            if self.signal_left_flag:
                self.screen.blit( self.signal_left, (0,0))
            if self.signal_right_flag:
                self.screen.blit(self.signal_right , (0,0))
            self.i += 1
      
            
    def __check_for_warning(self):
        
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
