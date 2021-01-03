import pygame
import sys
from PIL import Image

# image = Image.open("Webp.net-resizeimage (15).png")
# mode = image.mode
# size = image.size
# data = image.tobytes()
#
# py_image = pygame.image.fromstring(data, size, mode)
image = pygame.image.load("~\ps\BG.png")
w, h = image.get_size()
image2 = pygame.image.load("~\ps\Big_Arrow.png")
# image4 = pygame.image.load("11sdasd.png")
# image6 = pygame.image.load("11sdasd2.png")
# image8 = pygame.image.load("11sdasd2.png")
sc = pygame.display.set_mode((w, h))
mouse = pygame.mouse.get_pos()
i = 0
checkw = False
checks = False
image3 = pygame.transform.rotate(image2, i)
# image5 = pygame.transform.rotate(image4, i)
# image7 = pygame.transform.rotate(image6, i)
# image9 = pygame.transform.rotate(image8, i)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                checkw = True
            if event.key == pygame.K_s:
                checks = True
        if event.type == pygame.KEYUP:
            checkw = False
            checks = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # image = image.rotate(10)
            print(mouse)
    if checkw:
        i -= 2
    else:
        checkw = False
    if checks:
        i += 2
    else:
        checks = False
    image3 = pygame.transform.rotate(image2, i)
    mouse = pygame.mouse.get_pos()
    # image5 = pygame.transform.rotate(image4, i)
    # image7 = pygame.transform.rotate(image6, i)
    # image9 = pygame.transform.rotate(image8, i)
    rect = image3.get_rect()
    rect.center = 598, 503
    # rect2 = image5.get_rect()
    # rect2.center = 145, 502
    # rect3 = image7.get_rect()
    # rect3.center = 319, 404
    # rect4 = image9.get_rect()
    # rect4.center = 430, 404
    sc.fill((245, 245, 245))
    sc.blit(image, (0, 0))
    sc.blit(image3, rect)
    # sc.blit(image5,rect2)
    # sc.blit(image7, rect3)
    # sc.blit(image9,rect4)
    pygame.display.flip()
