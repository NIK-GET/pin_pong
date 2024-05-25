from pygame import *
from random import randint
# z

speed_y = randint(2, 4)

'''Необходимые классы'''

# подгружаем отдельно функции для работы со шрифтом
font.init()
font1 = font.SysFont('Arial', 30)


score1 = 0
score2 = 0
sila11 = 3
sila22 = 3

#фоновая музыка
mixer.init()
mixer.music.load('likovanie-publiki-27488.ogg')
mixer.music.play()
fire_sound = mixer.Sound('schelchok-zapuska-myacha.ogg')



#класс-родитель для спрайтов
class GameSprite(sprite.Sprite):
   def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
       super().__init__()
       self.image = transform.scale(image.load(player_image), (wight, height)) #вместе 55,55 - параметры
       self.speed = player_speed
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y


   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
   def update_r(self):
       keys = key.get_pressed()
       if keys[K_UP] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[K_DOWN] and self.rect.y < win_height - 80:
           self.rect.y += self.speed 
   def update_l(self):
       keys = key.get_pressed()
       if keys[K_w] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[K_s] and self.rect.y < win_height - 80:
           self.rect.y += self.speed

#class text(font):
#    def __init__(self, text_speed):
#        self.speed = text_speed
#
#
#text = (оооооо, 1, (255, 25, 255), 5)

class Sila(GameSprite):
    def sila1(self):
       keys = key.get_pressed()
       if keys[K_q] and self.rect.y < 350:
            speed_x *= -1
            speed_y *= 1
            sila11 = sila11 - 1 
    def sila2(self):
       keys = key.get_pressed()
       if keys[K_p] and self.rect.y > 350:
            speed_x *= -1
            speed_y *= 1 
            sila22 = sila22 - 1 

           

#игровая сцена:


win_width = 700
win_height = 500
display.set_caption(":)")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load('kort.png'), (win_width, win_height))


#флаги, отвечающие за состояние игры
game = True
finish = False
clock = time.Clock()
FPS = 120


#создания мяча и ракетки   
racket1 = Player('racket.png', 30, 200, 4, 100, 150) 
racket2 = Player('racket.png', 520, 200, 4, 100, 150)
ball = GameSprite('tenis_ball.png', 200, 200, 4, 50, 50)


font.init()
font = font.Font(None, 35)
lose1 = font.render('PLAYER 1 LOSE!', True, (180, 0, 0))
lose2 = font.render('PLAYER 2 LOSE!', True, (180, 0, 0))



speed_x = 3
speed_y = 3


while game:
   for e in event.get():
       if e.type == QUIT:
           game = False
  
   if finish != True:


       window.blit(background, (0,0))
       racket1.update_l()
       racket2.update_r()
       ball.rect.x += speed_x
       ball.rect.y += speed_y

       text1 = font1.render("Счет: " + str(score1), 1, (255, 25, 255))
       window.blit(text1, (30, 90))
       text2 = font1.render("Счет: " + str(score2), 1, (255, 25, 255)) 
       window.blit(text2, (565, 90))  

    #   sila111 = font1.render("Сила: " + str(sila22), 1, (255, 25, 255))
    #   window.blit(sila111, (30, 60))
    #   sila222 = font1.render("Сила: " + str(sila11), 1, (255, 25, 255)) 
    #   window.blit(sila222, (580, 60)) 


       if sprite.collide_rect(racket1, ball): 
           speed_x *= -1
           speed_y *= 1
           score1 = score1 + 1
           fire_sound.play()


       if sprite.collide_rect(racket2, ball):
            speed_x *= -1
            speed_y *= 1
            score2 = score2 + 1
            fire_sound.play()


    
      
       #если мяч достигает границ экрана, меняем направление его движения
       if ball.rect.y > win_height-50 or ball.rect.y < 0:
           speed_y *= -1
           fire_sound.play()


       #если мяч улетел дальше ракетки, выводим условие проигрыша для первого игрока
       if ball.rect.x < 0:
           finish = True
           window.blit(lose1, (250, 90))
           game_over = True


       #если мяч улетел дальше ракетки, выводим условие проигрыша для второго игрока
       if ball.rect.x > win_width:
           finish = True
           window.blit(lose2, (250, 90))
           game_over = True
    


       racket1.reset()
       racket2.reset()
       ball.reset()


   display.update()
   clock.tick(FPS)
