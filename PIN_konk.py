from pygame import *

'''Необхадимые классы'''

#игровая сцена
back = (200, 255, 255) #цвет фона
win_width = 600
win_heaight = 500
window = display.set_mode((win_width, win_heaight))
window.fill(back)

#флагиб отвечающие за состаяние игры
game = True
finish = False

#таймер
clock = time.Clock()
FPS = 60

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    display.update()
    clock.tick(FPS)

