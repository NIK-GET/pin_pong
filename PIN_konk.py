from pygame import *

'''Необхадимые классы'''

#игровая сцена
back = (200, 255, 255) #цвет фона
win_width = 600
win_heaight = 500
window = display.set_mode((win_width, win_heaight))
window.fill(back) # fill заменить на blit для картинки


# нам нужны такие картинки:
#img_back = "background.jpg" # фон игры
img_racket = "racket.png" #ракетка
img_ball = "tenis_ball.png" # мяч

#флаги отвечающие за состаяние игры
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

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


# класс главных игроков
class Player(GameSprite):
    # метод для управления спрайтом стрелками клавиатуры
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_width - 80:
            self.rect.y += self.speed

    def update_l(self):
        keys = key.get_pressed()
        if keys[K_W] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_S] and self.rect.y < win_width - 80:
            self.rect.y += self.speed


racket1 = Player(img_racket, 30, 200, 4, 50, 150)  
racket2 = Player(img_racket, 520, 200, 4, 50, 150) 
ball = GameSprite(img_ball, 200, 200, 4, 50, 50)

font.init()
font1 = font.SysFont('Arial', 35)
lose2 = font1.render('1 игрока на расстрел', True, (180, 0, 0))
lose1 = font1.render('2 игрока на расстрел', True, (180, 0, 0))

speed_x = 3
speed_y = 3


while game:
    # событие нажатия на кнопку Закрыть
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.fill(back)
        racket1.update_l()
        racket2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

# если мяч достиг границ экранна то он меняет направление его движения
        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1
            speed_y *= 1
        if ball.rect.y > win_heaight-50 or ball.rect.y < 0:
            speed_y *= -1

# если мяч улетел за ракетки, выводим надпись проигрыша для первого игрока
        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))
            game_over = True

# если мяч улетел за ракетки, выводим надпись проигрыша для второго игрока
        if ball.rect.x > win_width:
            finish = True
            window.blit(lose2, (200, 200))
            game_over = True


        racket1.reset()
        racket2.reset()
        ball.reset()

            
    display.update()
    clock.tick(FPS)


