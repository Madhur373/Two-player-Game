import pygame as p
import time
import random as r
p.font.init()

w,h= 800,600                    
win= p.display.set_mode((w,h))      
p.display.set_caption('Battle Attack')

BG= p.transform.scale(p.image.load('space-galaxy.jpg'),(w,h))

player_height =60
player_width = 40
player_vel= 5


star_vel = 5

bullet_width = 5
bullet_height = 10
bullet_vel = 5



font = p.font.SysFont('Arial',30)



def draw(player):  
    win.blit(BG, (0,0)) 
    p.draw.rect(win, "green" ,player)
    stars=[]
    for _ in range(3):
        star_x = r.randint(0, w-20)
        star_y = 0
        star= p.draw.circle(win, 'yellow',(star_x,star_y),20)
        stars.append(star)

        for star in stars[:]:
             star_y = star_y + star_vel 
             print(star_y)
        
    

       
   
    p.display.update() 



def play(): 
    run = True

    player= p.Rect(200,h-player_height, player_width, player_height)
    
     

    clock = p.time.Clock()
    star_add_increment = 2000 
    star_count = 0 
    hit =  False 
    bullet=[]

    
    
    
    while run:
       clock.tick(60)
       for event in p.event.get(): 
            if event.type == p.QUIT: 
                run= False
                break

       keys = p.key.get_pressed()  
       if keys[p.K_LEFT] and player.x - player_vel >=0:  
            player.x -= player_vel 
       if keys[p.K_RIGHT]  and player.x  + player_vel + player_width <= w: 
            player.x += player_vel

       
        # for star in stars[:]:
        #      star_y = star_y + star_vel 
        #      print(star_y)
        #      if star_y > h: 
        #          stars.remove(star)
        #      elif star.y + 20>= player.y and star.colliderect(player): 
        #         hit = True 
        #         break
        
        # if hit:
            
        #     p.display.update() 
        #     p.time.delay(2000)
        #     play()
        
        
        
       draw(player)
    p.quit()

if __name__ == '__main__':
    play()