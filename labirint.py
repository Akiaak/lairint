from pygame import *
class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,size_x,size_y):
        sprite.Sprite.__init__(self)
        self.image=transform.scale(image.load(player_image),(size_x,size_y))
        self.rect = self.image.get_rect()
        self.rect.x=player_x
        self.rect.y=player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class Player(GameSprite):
        def __init__(self,player_image,player_x,player_y,size_x,size_y,player_x_speed,player_y_speed):
            GameSprite.__init__(self,player_image,player_x,player_y,size_x,size_y)
            self.x_speed=player_x_speed
            self.y_speed=player_y_speed
        def udate(self):
            if packman.rect.x<=win_width-80 and packman.x_speed>0 or packman.rect.x>=0 and packman.x_speed<0:
                self.rect.x +=self.x_speed
            platforms_toched = sprite.spritecollide(self,barriers,False)
            if self.x_speed>0:
                for p in platforms_toched:
                    self.rect.right = min(self.rect.right,p.rect.left)
            elif self.x_speed<0:
                for p in platforms_toched:
                    self.rect.left = max(self.rect.left, p.rect.right)
            if packman.rect.y<=win_height-80 and packman.y_speed>0 or packman.rect.y>=0 and packman.y_speed<0:
                self.rect.y += self.y_speed
            platforms_toched = sprite.spritecollide(self,barriers,False)
            if self.y_speed>0:
                for p in platforms_toched:
                    self.rect.bottom = min(self.rect.bottom,p.rect.top)
            elif self.y_speed <0:
                for p in platforms_toched:
                    self.rect.top = max(self.rect.top, p.rect.bottom)
win_width=700
win_height=500
display.set_caption("Лабиринт")
window = display.set_mode((win_width,win_height))
back = (119,210,223)

barriers = sprite.Group()

w1 = GameSprite('w.jpg', win_width/2 - win_width/3,win_height/2,300,50)
w2 = GameSprite('w.jpg',370,100,50,400)

barriers.add(w1)
barriers.add(w2)

packman=Player('he.png', 5 ,  win_height-80,80,80,0,0)
monster = GameSprite('p.png',win_width-80,180,80,80)
final_sprite = GameSprite('d.png',win_width-85,win_height-100,80,80)

finish=False
run=True
while run:
    time.delay(50)

    for e in event.get():
        if e.type ==QUIT:
            run = False
        elif e.type==KEYDOWN:
            if e.key ==K_LEFT:
                packman.x_speed=-10
            elif e.key==K_RIGHT:
                packman.x_speed=10
            elif e.key==K_UP:
                packman.y_speed=-10
            elif e.key==K_DOWN:
                packman.y_speed=10
        elif e.type ==KEYUP:
            if e.key ==K_LEFT:
                packman.x_speed=0
            elif e.key==K_RIGHT:
                packman.x_speed=0
            elif e.key==K_UP:
                packman.y_speed=0
            elif e.key==K_DOWN:
                packman.y_speed=0
    if not finish:
        window.fill(back)
        barriers.draw(window)

        monster.reset()
        final_sprite.reset()
        packman.reset()
        packman.udate()
        if sprite.collide_rect(packman,monster):
            finish = True
            img = image.load('fn.png')
            d = img.get_width() // img.get_height()
            window.fill((255,255,255))
            window.blit(transform.scale(img,(win_height*d,win_height)),(90,0))
        if sprite.collide_rect(packman,final_sprite):
            finish=True
            img = image.load('fd.jpg')
            window.fill((255,255,255))
            window.blit(transform.scale(img,(win_width,win_height)), (0,0))

    display.update()