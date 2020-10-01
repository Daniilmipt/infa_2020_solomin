import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((800, 530))

rect(screen, (254, 214, 163), (0, 0, 800, 530))
rect(screen, (254, 214, 197), (0, 110, 800, 125))
rect(screen, (158, 127, 154), (0, 380, 800, 530))
circle(screen, (252, 239, 27), (400, 110), 40)

polygon(screen, (252, 153, 45), [(165, 108), (196, 119), (205, 140), (307, 204), (360, 195), (387, 209), (165, 230)])

polygon(screen, (252, 153, 45), [(387, 209), (429, 165), (463, 182), (480, 161), (480, 200)])

mountain_1 = []
for i in range(480, 550, 1):
    mountain_1.append((i, (-25 / 2000) * (i - 480) ** 2 + 161))
for i in range(550, 600, 1):
    mountain_1.append((i, 0.029 * (i - 580) ** 2 + 74))
mountain_1.append((600, 189))
mountain_1.append((480, 200))

polygon(screen, (252, 153, 45), mountain_1)

mountain_2 = []
for i in range(0, 165, 1):
    mountain_2.append((i, (-109 / 21904) * (i - 17) ** 2 + 217))
mountain_2.append((165, 230))
mountain_2.append((0, 245))

polygon(screen, (252, 153, 45), mountain_2)

polygon(screen, (252, 153, 45), [(600, 85), (634, 134), (666, 127), (718, 155), (750, 140), (800, 170), (600, 189)])

polygon(screen, (173, 65, 49),
        [(800, 190), (800, 340), (655, 344), (655, 284), (688, 240), (720, 263), (740, 235), (770, 240)])
polygon(screen, (173, 65, 49),
        [(459, 284), (459, 350), (140, 360), (140, 340), (175, 282), (231, 311), (260, 240), (325, 255), (385, 300)])

mountain_3 = []
for i in range(25, 155, 1):
    mountain_3.append((i, (18 / 841) * (i - 73) ** 2 + 214))
mountain_3.append((140, 360))
mountain_3.append((25, 360))
polygon(screen, (173, 65, 49), mountain_3)

mountain_4 = []
for i in range(450, 565, 1):
    mountain_4.append((i, (1 / 125) * (i - 550) ** 2 + 220))
mountain_4.append((565, 360))
mountain_4.append((450, 360))
polygon(screen, (173, 65, 49), mountain_4)

polygon(screen, (178, 125, 135), [(0, 358), (800, 340), (800, 530), (0, 530)])

mountain_5 = []
for i in range(565, 655, 1):
    mountain_5.append((i, (-59 / 7921) * (i - 655) ** 2 + 285))
mountain_5.append((655, 360))
mountain_5.append((565, 360))
polygon(screen, (173, 65, 49), mountain_5)

polygon(screen, (178, 125, 135), [(0, 358), (800, 340), (800, 530), (0, 530)])


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
