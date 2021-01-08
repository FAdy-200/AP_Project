import pygame
import sys

class DashBoardUserInput:
    def __init__(self):
        pygame.init()
        self.bg = pygame.image.load("Data/BG.png")
        self.width, self.height = self.bg.get_size()
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.big_arrow = pygame.image.load("Data/Big_Arrow.png")
        self.small_arrow = pygame.image.load("Data/Small_Arrow.png")
        self.signal_right = pygame.image.load("Data/RightArrow.png")
        self.signal_left = pygame.image.load("Data/LeftArrow.png")
        self.brakes = pygame.image.load("Data/Brakes.png")
        self.engine = pygame.image.load("Data/Engine.png")
        self.flasher = pygame.image.load("Data/Flasher.png")
        self.seat_belt = pygame.image.load("Data/SeatBelt.png")
        self.battery = pygame.image.load("Data/Battery.png")
        self.clock = pygame.time.Clock()
        self.acceleration = 0
        self.big_arrow_angle = -126 
        self.small_arrow_angle1 = -7
        self.small_arrow_angle2 = 37
        self.pivot_small_arrow1=[318,398]
        self.pivot_small_arrow2=[431,398]
        self.pivot_big_arrow1=[150,509]
        self.pivot_big_arrow2=[600,508]
        self.offset=pygame.math.Vector2(0,0)       

    def __check_for_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def __set_flags(self):
        """
        Change all the required flags to be used in the render function
        :param event:
        :return:
        """
        self.brakes_flag = False
        self.signal_right_flag = False
        self.signal_left_flag = False
        self.engine_flag = False
        self.flasher_flag = False
        self.seat_belt_flag = False
        self.battery_flag = False
        self.big_arrow_angle -=1
        if self.big_arrow_angle >-125 and self.acceleration >0:
            self.acceleration -=1   
        elif self.big_arrow_angle >-125 and self.acceleration <0:
            self.acceleration +=1
        self.keys = pygame.key.get_pressed()  
        if self.small_arrow_angle2 >-36:
            if self.keys[pygame.K_w] or self.keys[pygame.K_UP]:
                if self.acceleration <252:
                    self.acceleration +=2
                if self.acceleration >0:
                    self.big_arrow_angle +=2
                else:
                    self.big_arrow_angle -=1
                if self.small_arrow_angle2 >-37:
                    self.small_arrow_angle2 -=0.2
            elif self.keys[pygame.K_s] or self.keys[pygame.K_DOWN]:
                if self.acceleration >-252:
                    self.acceleration -=2
                if self.acceleration <0:
                    self.big_arrow_angle +=2
                else:
                    self.big_arrow_angle -=1
                if self.small_arrow_angle2 >-37:
                    self.small_arrow_angle2 -=0.2
        elif not self.small_arrow_angle2 >-36:
            self.big_arrow_angle -=1
            if self.acceleration >0:
                self.acceleration -=1
            if self.acceleration<0:
                self.acceleration +=1
        if self.keys[pygame.K_SPACE]:
            self.brakes_flag = True
            self.big_arrow_angle -=4
            if self.acceleration >0:
                self.acceleration -=4
            if self.acceleration<0:
                self.acceleration +=4
        if self.keys[pygame.K_d] or self.keys[pygame.K_RIGHT]:
            self.signal_right_flag = True
        if self.keys[pygame.K_a] or self.keys[pygame.K_LEFT]:
            self.signal_left_flag = True
        if self.keys[pygame.K_1]:
            self.engine_flag = True
        if self.keys[pygame.K_2]:
            self.flasher_flag = True
        if self.keys[pygame.K_3]:
            self.seat_belt_flag = True
        if self.keys[pygame.K_4]:
            self.battery_flag = True
        if self.keys[pygame.K_5]:
            self.small_arrow_angle2 =37
        self.acceleration = min(max(self.acceleration,-252),252)
        print(f"\r{self.acceleration}",end='')
        self.big_arrow_angle = min(max(self.big_arrow_angle, -126), 126)
        self.rotated_small_arrow1, self.rect_small_arrow1 = rotate(self.small_arrow, self.small_arrow_angle1, self.pivot_small_arrow1, self.offset)
        self.rotated_small_arrow2, self.rect_small_arrow2 = rotate(self.small_arrow, self.small_arrow_angle2, self.pivot_small_arrow2, self.offset)
        self.rotated_big_arrow1, self.rect_big_arrow1 = rotate(self.big_arrow, self.big_arrow_angle, self.pivot_big_arrow1, self.offset)
        self.rotated_big_arrow2, self.rect_big_arrow2 = rotate(self.big_arrow, self.big_arrow_angle, self.pivot_big_arrow2, self.offset)

    def __render(self):
        """
        renders needed images based on the input
        :return:
        """
        self.screen.blit(self.bg, [0, 0])
        self.screen.blit(self.rotated_small_arrow1, self.rect_small_arrow1) 
        self.screen.blit(self.rotated_small_arrow2, self.rect_small_arrow2) 
        self.screen.blit(self.rotated_big_arrow1, self.rect_big_arrow1) 
        self.screen.blit(self.rotated_big_arrow2, self.rect_big_arrow2)
        if self.signal_left_flag:
            self.screen.blit(self.signal_left,[3,-18])
        if self.signal_right_flag:
            self.screen.blit(self.signal_right,[-7,-18])
        if self.brakes_flag:
            self.screen.blit(self.brakes,[-4,-18])
        if self.engine_flag:
            self.screen.blit(self.engine,[-8,-18])
        if self.flasher_flag:
            self.screen.blit(self.flasher,[-12,-18])
        if self.seat_belt_flag:
            self.screen.blit(self.seat_belt,[-16,-18])   
        if self.battery_flag:
            self.screen.blit(self.battery,[0,-18])

    def __check_for_warning(self):
        """
        MY JOB LEAVE IT ALONE
        :return:
        """
        pass

    def start(self):
        while True:
            self.__check_for_events()
            self.__set_flags()
            self.__render()
            # self.__check_for_warning()
            pygame.display.update()
            self.clock.tick(120)

def rotate(surface, angle, pivot, offset):
    rotated_image = pygame.transform.rotozoom(surface, -angle,1)  # Rotate the image.
    rotated_offset = offset.rotate(angle)  # Rotate the offset vector.
    # Add the offset vector to the center/pivot point to shift the rect.
    rect = rotated_image.get_rect(center=pivot)
    return rotated_image, rect  # Return the rotated image and shifted rect.

test = DashBoardUserInput()
test.start()