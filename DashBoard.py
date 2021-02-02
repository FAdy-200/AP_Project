import pygame
import sys
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile


class DashBoard:
    def __init__(self):
        pygame.init()
        self.index_in_DF = 0  # index of the row in the data of which we are in
        self.bg = pygame.image.load("Data/BG.png")  # Background image
        self.width, self.height = self.bg.get_size()  # dimensions of the background image
        self.screen = pygame.display.set_mode((self.width, self.height))  # screen to render thing into
        self.font = pygame.font.Font('freesansbold.ttf', 20)  # font to be used to render texts
        self.battery = pygame.image.load("Data/Battery.png")  # battery flag image
        self.big_arrow = pygame.image.load("Data/Big_Arrow.png")  # Speed rotating arrow
        self.small_arrow = pygame.image.load("Data/Small_Arrow.png")  # Fuel rotating arrow
        self.brakes = pygame.image.load("Data/Brakes.png")  # Brakes alert image
        self.engine = pygame.image.load("Data/Engine.png")  # Engine alert image
        self.flasher = pygame.image.load("Data/Flasher.png")  # Flasher indicator image
        self.signal_right = pygame.image.load("Data/RightArrow.png")  # give a signal to move right
        self.signal_left = pygame.image.load("Data/LeftArrow.png")  # give a signal to move left
        self.seat_belt = pygame.image.load("Data/SeatBelt.png")  # seat belt alert image
        self.mouse = pygame.mouse.get_pos()  # getting the mouse's position
        self.warning_sign = pygame.image.load("Data/Warning_Sign.png")  # loading the warning sign image
        # setting the place of the sign and it is flash interval
        self.warning_rect = self.warning_sign.get_rect()
        self.warning_rect.center = self.width // 2, 470
        self.warning_sign_flash = 10
        self.acceleration = []  # list to hold last 100 recorded acceleration
        self.current_Acceleration = 0
        self.big_arrow_angle = -125
        self.small_arrow_angle1 = -7
        self.small_arrow_angle2 = 37
        self.pivot_small_arrow1 = [318, 398]
        self.pivot_small_arrow2 = [431, 398]
        self.pivot_big_arrow1 = [150, 509]
        self.pivot_big_arrow2 = [600, 508]

        '''
        initializing flags
        '''
        self.battery_flag = False
        self.brakes_flag = False
        self.engine_flag = False
        self.flasher_flag = False
        self.signal_left_flag = False
        self.signal_right_flag = False
        self.seat_belt_flag = False
        self.data = None

    def __render_choosing_screen(self):
        """
        renders the text needed for the choosing screen in their right place
        :return:
        """
        main_text = self.font.render("Please choose which mode you want:", True, (0, 0, 0))
        user_text = self.font.render("User Driven", True, (0, 0, 0))
        file_text = self.font.render("File Driven", True, (0, 0, 0))
        main_text_rect = main_text.get_rect()
        main_text_rect.center = self.width // 2, self.height // 2
        user_text_rect = user_text.get_rect()
        user_text_rect.center = self.width // 2 - 100, self.height // 2 + 100
        file_text_rect = file_text.get_rect()
        file_text_rect.center = self.width // 2 + 100, self.height // 2 + 100
        self.screen.blit(main_text, main_text_rect)
        self.screen.blit(user_text, user_text_rect)
        self.screen.blit(file_text, file_text_rect)

    def __choosing_screen(self):
        """
        starting screen to choose which mode to operate in
        :return:
        """
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 480 > self.mouse[1] > 455:
                        if 335 > self.mouse[0] > 215:
                            return self.__user_Input  # data inputted by user
                        elif 535 > self.mouse[0] > 415:
                            return self.__file_Input  # data is taken from a file
            self.mouse = pygame.mouse.get_pos()
            self.screen.fill((245, 245, 245))
            self.__render_choosing_screen()
            pygame.display.flip()

    def __user_Input(self):
        """
        Starting the User input mode
        :return:
        """
        self.__set_Data_based_on_Input()

    def __init_file_input(self):
        """
        initializing the needed variables for the file input mode
        :return:
        """
        if self.data is None:
            self.data = pd.read_csv('Data/sensor_data.csv', low_memory=False)  # accessing the data
            self.max_velocity = self.data[
                'Velocity'].max()  # getting max. value of velocity col as a length of the speed
            self.data['angular'] = (self.data['Velocity'] * -254) / self.max_velocity  # Creating new col named angular

    def __file_Input(self):
        """
        starting the file input mode
        :return:
        """
        self.__init_file_input()
        self.__set_Data_based_on_File()

    def __set_Data_based_on_File(self):
        """
        changing the flags based on the data in the file
        :return:
        """
        if self.index_in_DF <= len(self.data):
            self.acceleration.append(self.data['Acceleration'][self.index_in_DF])  # number not flag
            self.small_arrow_angle2 = self.data['Fuel'][self.index_in_DF] * ((37 * 2) / 100) - 37  # number not flag
            self.angular_data = self.data['angular'][self.index_in_DF]
            self.big_arrow_angle = -127 - self.angular_data if self.angular_data < 127 else - 127 + self.angular_data  # 127 - angle --> Left other ---> Right
            self.battery_flag = self.data['Battery'][self.index_in_DF]
            self.seat_belt_flag = self.data['Set Belt'][self.index_in_DF]
            self.flasher_flag = self.data['Alart'][self.index_in_DF]
            self.engine_flag = self.data['Engine'][self.index_in_DF]
            self.signal_left_flag = self.data['Left'][self.index_in_DF]
            self.signal_right_flag = self.data['Right'][self.index_in_DF]

        self.index_in_DF += 1

    def __set_Data_based_on_Input(self):
        """
        Change all the required flags to be used in the render function
        :return:
        """
        self.brakes_flag = False
        self.signal_right_flag = False
        self.signal_left_flag = False
        self.engine_flag = False
        self.flasher_flag = False
        self.seat_belt_flag = False
        self.battery_flag = False
        self.big_arrow_angle -= 1

        ''' Take user input on keyboard and acting on it'''

        self.keys = pygame.key.get_pressed()
        if self.small_arrow_angle2 > -36:  # if w,up,s,down key pressed while small arrow angle <-36
            # then we can change the current acceleration which is constantly decreasing if car is moving with no gas
            if self.keys[pygame.K_w] or self.keys[pygame.K_UP]:
                if self.big_arrow_angle < 126:  # determined by small_arrow_angle2
                    self.current_Acceleration += 0.1
                else:
                    self.big_arrow_angle -= 1
                if self.small_arrow_angle2 > -37:
                    self.small_arrow_angle2 -= 0.2
            elif self.keys[pygame.K_s] or self.keys[pygame.K_DOWN]:
                if self.big_arrow_angle > -126:
                    self.current_Acceleration -= 0.2
                if self.current_Acceleration > 0:
                    self.current_Acceleration = 0
                else:
                    self.big_arrow_angle -= 1
                if self.small_arrow_angle2 > -37:
                    self.small_arrow_angle2 -= 0.2
            else:
                if self.big_arrow_angle > -126:
                    self.current_Acceleration = -1
        elif not self.small_arrow_angle2 > -36:
            self.big_arrow_angle -= 1
            if self.current_Acceleration > 0:
                self.current_Acceleration -= 0.1
            if self.current_Acceleration < 0:
                self.current_Acceleration += 0.1
        if self.keys[pygame.K_SPACE]:
            # if space key pressed hit braked by decreasing current acceleration and showing brakes flag
            self.brakes_flag = True
            self.big_arrow_angle -= 4
            if self.current_Acceleration > 0:
                self.current_Acceleration -= 2
            if self.current_Acceleration < 0:
                self.current_Acceleration += 2

        self.big_arrow_angle += self.current_Acceleration
        '''setting different flags to show up on screen when a button is pressed'''
        if self.keys[pygame.K_d] or self.keys[pygame.K_RIGHT]:  # d or right key pressed show signal right
            self.signal_right_flag = True
        if self.keys[pygame.K_a] or self.keys[pygame.K_LEFT]:  # a or left key pressed show signal left
            self.signal_left_flag = True
        if self.keys[pygame.K_1]:  # 1 pressed show engine
            self.engine_flag = True
        if self.keys[pygame.K_2]:  # 2 pressed show flasher
            self.flasher_flag = True
        if self.keys[pygame.K_3]:  # 3 pressed show seatbelt
            self.seat_belt_flag = True
        if self.keys[pygame.K_4]:  # 4 pressed show battery
            self.battery_flag = True
        if self.keys[pygame.K_5]:  # 5 pressed refuel
            self.small_arrow_angle2 = 37
        self.big_arrow_angle = min(max(self.big_arrow_angle, -126), 126)  # limiting big arrow angle between -126,126
        self.acceleration.append(self.current_Acceleration)

    @staticmethod
    def __rotate_surface(surface, angle, pivot):
        rotated_image = pygame.transform.rotozoom(surface, -angle, 1)  # Rotate the image.
        rect = rotated_image.get_rect(center=pivot)
        return rotated_image, rect  # Return the rotated image and shifted rect.

    def __rotate_arrows(self):
        """
        Rotating the arrows based on their angles
        :return:
        """
        self.rotated_small_arrow1, self.rect_small_arrow1 = self.__rotate_surface(self.small_arrow,
                                                                                  self.small_arrow_angle1,
                                                                                  self.pivot_small_arrow1)
        self.rotated_small_arrow2, self.rect_small_arrow2 = self.__rotate_surface(self.small_arrow,
                                                                                  self.small_arrow_angle2,
                                                                                  self.pivot_small_arrow2)
        self.rotated_big_arrow1, self.rect_big_arrow1 = self.__rotate_surface(self.big_arrow, self.big_arrow_angle,
                                                                              self.pivot_big_arrow1)
        self.rotated_big_arrow2, self.rect_big_arrow2 = self.__rotate_surface(self.big_arrow, self.big_arrow_angle,
                                                                              self.pivot_big_arrow2)

    @staticmethod
    def __check_for_exit():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # exit the game out of the loop if closed
                sys.exit()

    def __render(self):
        """
        renders needed images based on the flags data
        :return:
        """
        self.__rotate_arrows()
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.bg, [0, 0])
        self.screen.blit(self.rotated_small_arrow1, self.rect_small_arrow1)
        self.screen.blit(self.rotated_small_arrow2, self.rect_small_arrow2)
        self.screen.blit(self.rotated_big_arrow1, self.rect_big_arrow1)
        self.screen.blit(self.rotated_big_arrow2, self.rect_big_arrow2)
        if self.signal_left_flag:
            self.screen.blit(self.signal_left, (0, 0))
        if self.signal_right_flag:
            self.screen.blit(self.signal_right, (0, 0))
        if self.brakes_flag:
            self.screen.blit(self.brakes, (0, 0))
        if self.engine_flag:
            self.screen.blit(self.engine, (0, 0))
        if self.flasher_flag:
            self.screen.blit(self.flasher, (0, 0))
        if self.seat_belt_flag:
            self.screen.blit(self.seat_belt, (0, 0))
        if self.battery_flag:
            self.screen.blit(self.battery, (0, 0))

    def __flash_warning_sign(self):
        """
        flashing a warning sign when needed with an interval of 10
        :return:
        """
        if self.warning_sign_flash < 10:
            self.screen.blit(self.warning_sign, self.warning_rect)
        self.warning_sign_flash += -1
        if self.warning_sign_flash < 0:
            self.warning_sign_flash = 20

    def __check_for_warning(self):
        """
        checking if the driver is driving unsafe
        :return:
        """
        c0 = self.big_arrow_angle > 30  # if speed is more than 170
        c1 = self.acceleration[-1] > 5  # if last recorded acceleration is more than 5 m/(s^2)
        c2 = self.seat_belt_flag  # if the driver seat belt is off
        if c0 or c1 or c2:
            self.__flash_warning_sign()

    def start(self):
        """
        starting the dashboard and choosing the mode
        :return:
        """
        engine = self.__choosing_screen()
        while True:
            engine()
            self.__check_for_exit()
            self.__render()
            self.__check_for_warning()
            pygame.display.flip()


s = DashBoard()
s.start()
