import pygame as p
import time
import random as r
p.font.init() #initialize font

w,h= 800,600                    #defining width and height
win= p.display.set_mode((w,h))      #creating a window
p.display.set_caption('Dodge attack')
BG= p.transform.scale(p.image.load('space-galaxy.jpg'),(w,h)) ###Load image also use without transform
                                                            #pygame.transform.scale(bg command,() 
                                                            #and scale to your width and height)
player_height =60
player_width = 40
player_vel= 5  #movement of player

star_width = 10
star_height = 20 #projectile size
star_vel = 5 #projectile movement

font = p.font.SysFont('Arial',30) #choose font type and size


def draw(player,time_completed,stars):  #func ton draw anything to our game window
    win.blit(BG, (0,0)) #blit func for drawing , 0,0 coordinate for top left of the screen
    p.draw.rect(win, "green" ,player) #draw the player on the window

    for star in stars:
        p.draw.rect(win, "white", star) #draws projectiles in window 
    time_text = font.render(f"TIME:{round(time_completed)}s", 1, "white") #time to rounded to the second on screen(1 is anti-alias not worry about it)
    win.blit(time_text, (10,10)) #print time on window in 10,10 x and y coordinate on screen
    board= font.render("SCOREBOARD", 1, "white")
    win.blit(board,(600, 10))
    
    p.display.update()  #update every draw

def play():  #main func to run game 
    run = True

    player= p.Rect(200,h-player_height, player_width, player_height) #define player

    clock = p.time.Clock() #clock object regulates speed of character
    start_time = time.time() #current time
    time_completed = 0 

    star_add_increment = 2000 #increment of projectiles per 2000 milli sec
    star_count = 0 #tells us when to add next projectile
    hit =  False #checks for collision

    scores=[]

    stars= [] #stores all projectiles in screen

    while run:  #main game function
        star_count += clock.tick(60)  #spped of our loop 60fps for now, returns time since last clock tick
        time_completed = time.time() - start_time #gives the time passed in the game

        if star_count > star_add_increment : #checks if time completed is greater than star increment time
            for _ in range(5): #generates 5 projectiles at one time
                star_x = r.randint(0, w- star_width) #generates star at random x and y coordinate
                star= p.Rect(star_x, -star_height, star_width, star_height) #make star start at above top of screen and move downwards
                stars.append(star)
            star_add_increment = max(200, star_add_increment-50) #makes the addition of projectiles faster and sets a minimum time of 200 mmillisec
            star_count=0 #resets the varaible

        
        
        
        for event in p.event.get(): #all events in loop
            if event.type == p.QUIT: #check for close key
                run= False
                break
        keys = p.key.get_pressed()  #dictionary of all pressed keys
        if keys[p.K_LEFT] and player.x - player_vel >=0:  #checks if object is in frame(<0 is out)
            player.x -= player_vel #reducing x coordinate for movement
        if keys[p.K_RIGHT]  and player.x  + player_vel + player_width <= w: #x is top left of player so need to account for player width
            player.x += player_vel #increaing x coordinate for movement
                                   #player. can access height,width or x and y coordinatew
            
        for star in stars[:]: #makes a copy of stars list so we don't get errors while modfication of list during run time
             star.y += star_vel #moves downward in y direction
             if star.y > h: #if star hits bottom of screen
                 stars.remove(star)
             elif star.y + star_height >= player.y and star.colliderect(player): #check if star collides with player through side or above
                stars.remove(star)
                hit = True #collision occured
                break
        
        if hit:
            lost_text= font.render(f"Game Over! Your score is : {round(time_completed)}", 1, "yellow") #deine losing text
            win.blit(lost_text, (w/2- lost_text.get_width()/2, h/2-lost_text.get_height()/2)) #print on centerof the screen use .get_ to get height or width of text
            scores.append(round(time_completed))
            
            p.display.update() #display screen update after collision
            p.time.delay(5000)
           
            
            p.display.update() #display screen update after collision
          
        
            play()

        for score in scores:
        
            text= font.render(f"player {round(time_completed)}", 1, "white")
            win.blit(text,(600,40))
        
        
        draw(player,time_completed,stars)

    p.quit()

if __name__ == '__main__':
    play()