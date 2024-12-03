import pygame as p
import os #differnt system different separators
p.font.init()
p.mixer.init()

W,H = 1000,600
Win = p.display.set_mode((W,H))
p.display.set_caption('Battle Attack')
ship_w= 90
ship_h = 90
vel= 5
bullet_vel = 7
max_bullet = 3

font = p.font.SysFont('Arial',40) 
font2 = p.font.SysFont('comicsans',90)

red_hit= p.USEREVENT + 1
blue_hit = p.USEREVENT + 2

bullet_sound = p.mixer.Sound(os.path.join('Components','bulletsound.mp3'))
collide = p.mixer.Sound(os.path.join('Components','crash.mp3'))
fatality = p.mixer.Sound(os.path.join('Components','fatality.mp3'))


BORDER =p.Rect(W//2-5,0,10,H)

BG= p.transform.scale(p.image.load('space-galaxy.jpg'),(W,H))

ship1_img= p.image.load(os.path.join('Components','redship.png'))
ship1= p.transform.rotate(p.transform.scale(ship1_img,(ship_w,ship_h)),270)
ship2_img= p.image.load(os.path.join('Components','blueship11.png'))
ship2= p.transform.rotate(p.transform.scale(ship2_img,(ship_w,ship_h)),90)

def draw(red,blue, red_bullet, blue_bullet,red_health, blue_health):
    Win.blit(BG,(0,0))
    p.draw.rect(Win,'black',BORDER)
    red_health_text = font.render("HEALTH:" + str(red_health),1,"white")
    blue_health_text = font.render("HEALTH:" + str(blue_health),1,"white")
    Win.blit(red_health_text,(10,10))
    Win.blit(blue_health_text,(820,10))
    Win.blit(ship1,(red.x,red.y))
    Win.blit(ship2,(blue.x,blue.y)) 
    for bullet in red_bullet:
        p.draw.rect(Win,'red',bullet)
    for bullet in blue_bullet:
        p.draw.rect(Win,'blue',bullet)

    p.display.update()

def blue_move(keys_pressed,blue):
     if keys_pressed[p.K_RIGHT] and blue.x + blue.width + vel < W:
           blue.x += vel
     if keys_pressed[p.K_LEFT] and blue.x - vel  > BORDER.x:
           blue.x -= vel
     if keys_pressed[p.K_UP] and blue.y - vel > 0:
           blue.y -= vel
     if keys_pressed[p.K_DOWN] and blue.y + blue.height-5 + vel < H:
          blue.y += vel
     
def red_move(keys_pressed,red):
      if keys_pressed[p.K_a] and red.x - vel > 0:
           red.x -= vel
      if keys_pressed[p.K_d] and red.x + red.width + vel < BORDER.x:
           red.x += vel
      if keys_pressed[p.K_w] and red.y - vel > 0:
           red.y -= vel
      if keys_pressed[p.K_s] and red.y + red.height +vel < H:
           red.y += vel


def handle_bullets(red_bullet, blue_bullet, red, blue):
      for bullet in red_bullet:
           bullet.x += bullet_vel
           if blue.colliderect(bullet):
               p.event.post(p.event.Event(blue_hit))
               red_bullet.remove(bullet)

           elif bullet.x > W:
               red_bullet.remove(bullet)
            

      for bullet in blue_bullet:
           bullet.x -= bullet_vel
           if red.colliderect(bullet):
                p.event.post(p.event.Event(red_hit))
                blue_bullet.remove(bullet)
           elif bullet.x < 0:
                blue_bullet.remove(bullet)

def winner(text):
     win_text = font2.render(text,1,'white')         
     Win.blit(win_text,( W//2 - win_text.get_width()//2, H//2 - win_text.get_height()//2))

            
     p.display.update()
     p.time.delay(3000)




def play():
    red= p.Rect(100,300,ship_w,ship_h)
    blue= p.Rect(700,300,ship_w,ship_h)
    red_bullet =[]
    blue_bullet =[]
    clock=p.time.Clock()

    red_health = 10
    blue_health =10
    run = True
    while run:
         clock.tick(60)
         for event in p.event.get():
            if event.type== p.QUIT:
                run= False
                p.quit()

            if event.type == p.KEYDOWN:
                  if event.key == p.K_LCTRL and len(red_bullet) < max_bullet:
                       bullet = p.Rect(red.x + red.width, red.y + red.height//2 - 5 , 20,10)
                       red_bullet.append(bullet)
                       bullet_sound.play()
                      
                  if event.key == p.K_RCTRL and len(blue_bullet) < max_bullet:
                       bullet = p.Rect(blue.x, blue.y + blue.height//2 -5 , 20,10)
                       blue_bullet.append(bullet)
                       bullet_sound.play()


                  if event.key == p.K_SPACE:
                       play()

            if event.type == red_hit:
                  red_health -= 1
                  collide.play()
                  

            if event.type == blue_hit:
                  blue_health -= 1
                  collide.play()

         winner_text= ""
         if red_health <=0 :
           winner_text = "FATALITY! Blue Wins"   
           fatality.play()  
         if blue_health <=0 :
            winner_text = "FATALITY! Red Wins"  
            fatality.play()  
    
         if winner_text != "":
            winner(winner_text)
            play()
     
          
         
     


         keys_pressed= p.key.get_pressed()
         blue_move(keys_pressed,blue)
         red_move(keys_pressed,red)
         handle_bullets(red_bullet, blue_bullet, red, blue,)
         draw(red,blue,red_bullet,blue_bullet,red_health, blue_health)


   



         
      
    
    

if __name__ == "__main__":
        play()

