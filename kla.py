import pygame
import sys
def rotate(surface, angle, pivot, offset):
    rotated_image = pygame.transform.rotozoom(surface, -angle,1)  # Rotate the image.
    rotated_offset = offset.__rotate_surface(angle,,,  # Rotate the offset vector.
    # Add the offset vector to the center/pivot point to shift the rect.
    rect = rotated_image.get_rect(center=pivot)
    return rotated_image, rect  # Return the rotated image and shifted rect.


pygame.init()
bg = pygame.image.load("Data/BG.png")
width, height = bg.get_size()
screen = pygame.display.set_mode((width, height))
big_arrow = pygame.image.load("Data/Big_Arrow.png")
clock = pygame.time.Clock()
small_arrow = pygame.image.load("Data/Small_Arrow.png")
signal_right = pygame.image.load("Data/RightArrow.png")
signal_left = pygame.image.load("Data/LeftArrow.png")
brakes = pygame.image.load("Data/Brakes.png")
engine = pygame.image.load("Data/Engine.png")
flasher = pygame.image.load("Data/Flasher.png")
seat_belt = pygame.image.load("Data/SeatBelt.png")
battery = pygame.image.load("Data/Battery.png")
battery_flag = False
acceleration = 0
big_arrow_angle = -126 
small_arrow_angle1 = -7
small_arrow_angle2 = 37
pivot_small_arrow1=[318,398]
pivot_small_arrow2=[431,398]
pivot_big_arrow1=[150,509]
pivot_big_arrow2=[600,508]
offset=pygame.math.Vector2(0,0)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    # mouse = pygame.mouse.get_pos()
    # print(mouse)
    brakes_flag = False
    signal_right_flag = False
    signal_left_flag = False
    engine_flag = False
    flasher_flag = False
    seat_belt_flag = False
    battery_flag = False
    big_arrow_angle -=1
    if big_arrow_angle >-125 and acceleration >0:
        acceleration -=1
    elif big_arrow_angle >-125 and acceleration <0:
        acceleration +=1
    keys = pygame.key.get_pressed()
    if keys[pygame.K_r] and small_arrow_angle2 < 37:
        small_arrow_angle2 +=2
    if small_arrow_angle2 >-36:

        if keys[pygame.K_w] or keys[pygame.K_UP]:
            if acceleration <252:
                acceleration +=2
            if acceleration >0:
                big_arrow_angle +=2
            else:
                big_arrow_angle -=1
            if small_arrow_angle2 >-37:
                small_arrow_angle2 -=0.02
        elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
            if acceleration >-252:
                acceleration -=2
            if acceleration <0:
                big_arrow_angle +=2
            else:
                big_arrow_angle -=1
            if small_arrow_angle2 >-37:
                small_arrow_angle2 -=0.02
    elif not small_arrow_angle2 >-36:
        big_arrow_angle -=1
        if acceleration >0:
            acceleration -=1
        if acceleration<0:
            acceleration +=1
    if keys[pygame.K_SPACE]:
        brakes_flag = True
        big_arrow_angle -=4
        if acceleration >0:
            acceleration -=4
        if acceleration<0:
            acceleration +=4
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        signal_right_flag = True
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        signal_left_flag = True
    if keys[pygame.K_1]:
        engine_flag = True
    if keys[pygame.K_2]:
        flasher_flag = True
    if keys[pygame.K_3]:
        seat_belt_flag = True
    if keys[pygame.K_4]:
        battery_flag = True
    acceleration = min(max(acceleration,-252),252)
    print(f"\r{acceleration}",end='')
    big_arrow_angle = min(max(big_arrow_angle, -126), 126)
    rotated_small_arrow1, rect_small_arrow1 = rotate(small_arrow, small_arrow_angle1, pivot_small_arrow1, offset)
    rotated_small_arrow2, rect_small_arrow2 = rotate(small_arrow, small_arrow_angle2, pivot_small_arrow2, offset)
    rotated_big_arrow1, rect_big_arrow1 = rotate(big_arrow, big_arrow_angle, pivot_big_arrow1, offset)
    rotated_big_arrow2, rect_big_arrow2 = rotate(big_arrow, big_arrow_angle, pivot_big_arrow2, offset)
    screen.blit(bg, [0, 0])
    screen.blit(rotated_small_arrow1, rect_small_arrow1)
    screen.blit(rotated_small_arrow2, rect_small_arrow2)
    screen.blit(rotated_big_arrow1, rect_big_arrow1)
    screen.blit(rotated_big_arrow2, rect_big_arrow2)
    if signal_left_flag:
        screen.blit(signal_left,[3,-18])
    if signal_right_flag:
        screen.blit(signal_right,[-7,-18])
    if brakes_flag:
        screen.blit(brakes,[-4,-18])
    if engine_flag:
        screen.blit(engine,[-8,-18])
    if flasher_flag:
        screen.blit(flasher,[-12,-18])
    if seat_belt_flag:
        screen.blit(seat_belt,[-16,-18])
    if battery_flag:
        screen.blit(battery,[0,-18])
    pygame.display.update()
    clock.tick(30)