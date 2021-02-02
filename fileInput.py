'''
By: Mennatullah 
Last edit: 2/1/2021
'''
import pygame
import sys
import pandas as pd 

class DashBoardFileInput:
    def __init__(self): 
        '''
        Class initializer contains all properties of the dashboard 
        '''
        self.i = 0 
        self.bg = pygame.image.load("Data/BG.png") #Background image
        self.width, self.height = self.bg.get_size() #dimentions of the backgrounf image
        self.screen = pygame.display.set_mode((self.width, self.height))  # screen to render thing into
        self.battery = pygame.image.load("Data/Battery.png") #battery flag image
        self.big_arrow = pygame.image.load("Data/Big_Arrow.png") #Speed rotating arrow 
        self.small_arrow = pygame.image.load("Data/Small_Arrow.png") #Fuel rotating arrow
        #self.brakes = pygame.image.load("Data/Brakes.png") #Brakes alert image
        self.engine = pygame.image.load("Data/Engine.png") #Engine alert image
        self.flasher = pygame.image.load("Data/Flasher.png") #Flasher indicator image 
        self.signal_right = pygame.image.load("Data/RightArrow.png") #give a signal to move right
        self.signal_left = pygame.image.load("Data/LeftArrow.png") #give a signal to move left
        self.seat_belt = pygame.image.load("Data/SeatBelt.png") #seat belt alert image
        self.mouse = pygame.mouse.get_pos()  # print this when you need to find the mouse position on screen
        '''
        coming are flage for the images above
        '''
        self.battery_flag = False 
        #self.brakes_flag = False (I didn't put a flage for brakes)
        self.engine_flag = False
        self.flasher_flag = False
        self.signal_left_flag = False
        self.signal_right_flag = False
        self.seat_belt_flag = False
        self.big_arrow_angle = 0
        self.small_arrow_angle = 0
        self.data = pd.read_excel('Data/data.xlsx')  # put the file in the Data directory and access it here
        self.max_velocity = self.data['Velocity'].max() #getting max. value of velocity col as a length of the speed 
        self.data['angular'] = (self.data['Vecoity'] * 254) / self.max_velocity #Creating new col named angular 
      

    def __check_for_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        self.__set_flags()

    def __set_flags(self):
        """
        Change all the required flags to be used in the render function
        :return: It just put a name for evey col
        """
        while self.i <= 100:
            acc = self.data['Acceleration'][self.i]  #number not flag
            fuel = self.data['Fuel'][self.i] #number not flag
            velo = self.data['Velocity'][self.i] #number not flag Velocity = U + a*t 
            self.angular = self.data['angular'][self.i]
            angle = 127 - self.angular if self.angular < 127 else 127 + self.angular  #127 - angle --> Left other ---> Right
            self.battery_flag = self.data['Battery'][self.i] 
            self.seat_belt_flag = self.data['Set Belt'][self.i]
            self.flasher_flag = self.data['Alart'][self.i]
            self.engine_flag = self.data['Engine'][self.i]
            self.signal_left_flag = self.data['Left'][self.i]
            self.signal_right_flag = self.data['Right'][self.i]
            
            
            

    def __render(self):
        """
        renders needed images based on the input
        :return: Location for each col
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
        """
        MY JOB LEAVE IT ALONE
        :return: Ok! 
        """
        pass

    def start(self):
        '''
        Start executing the program
        '''
        while True:
            self.__check_for_events()
            self.__render()
            self.__check_for_warning()
            pygame.display.flip()
