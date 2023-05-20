from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self,image1,x,y,speed,width,height):
        super().__init__()

        self.image=transform.scale(image.load(image1), (width,height))
        self.speed=speed
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y

    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class Player(GameSprite):
    def updete_r(self):
        keys=key.get_pressed()
        if keys[K_UP] and self .rect.y > 5:
            self.rect.y -=self.speed
        if keys[K_DOWN] and self .rect.y < win_height - 80:
            self.rect.y +=self.speed
    def updete_l(self):
        keys=key.get_pressed()
        if keys[K_w] and self .rect.y > 5:
            self.rect.y -=self.speed
        if keys[K_s] and self .rect.y < win_height - 80:
            self.rect.y +=self.speed

back = (200, 255, 255)
win_width= 600
win_height = 500
window = display.set_mode((win_width,win_height))


game = True
finish= False
clock = time.Clock()
FPS = 60

racket1 = Player('14.png',30,200,4,50,150)
racket2 = Player('14.png',520,200,4,50,150)
ball= GameSprite('13.png',200,200,4,50,50)
font.init()
font=font.Font(None,35)
lose1=font.render('1 Игрок-ЛОХ', True,(180,0,0))
lose1=font.render('2 Игрок-ЛОХ', True,(180,0,0))

speed_x = 3
speed_y = 3


while game:
    for e in event.get():
        if e.type== QUIT:
            game = False
    

    if finish != True:
        window.fill((200,255,255))
        racket1.updete_l()
        racket2.updete_r()

        ball.rect.x +=speed_x
        ball.rect.y += speed_y

        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1
            speed_y *= 1

        if ball.rect.y > win_height-50 or ball.rect.y <0:
            speed_y*= -1

        if ball.rect.x < 0:
            finish = True
            window.blit(lose1,(200,200))
            game=False

        if ball.rect.x > win_width:
            finish = True
            window.blit(lose2,(200,200))
            game=False
        
        racket1.reset()
        racket2.reset()
        ball.reset()
    display.update()
    clock.tick(FPS)