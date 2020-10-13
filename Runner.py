#Cardi A's Code
import pygame,sys
from pygame import *
from CharacterClasses import *
from Enemys import *
from random import randint

#Initialisers- Initialises pygame and creates objects from all of my Character Classes
pygame.init()
basicfont = pygame.font.SysFont(None, 48)
screen = pygame.display.set_mode((1920,1080),pygame.FULLSCREEN)
pygame.key.set_repeat(1,1)
PURPLE = (27,14,56)

#This initialises all the player and enemy entities along with sound effects
ORANGE = (239, 74, 37)
guy = Player()
thunder = pygame.mixer.Sound('thunder.wav')
wind = pygame.mixer.music.load('wind.wav')
enemys = Enemys(10,10,guy)
#Draws the initial screen incuding the background and your character.
#However it does not draw the enemy characters because they require for the player to be on the screen to move towards him.
#This also creates two counters:
#Counter dictates how many iterations will go by before the enemy characters will move towards the player
#Counter2 dictates how many iterations will occur before five more enemys will apear
#Counter3 Dictates if the screen should draw normally or draw during a lightining flash
#The pygame.mixer.play function will play the wind sound effect on a loop.
screen.fill(PURPLE)
guy.draw(screen)
pygame.mixer.music.play(-1)
pygame.display.update()
counter = 0
counter2 = 0
counter3 = 0
flash = randint(3000,4000)
#This creates an infinite loop so that the game will run until the number of lives the Character has is 0
while True:
    #This will draw the screen during a lighning flash with a white background.
    if counter3 == flash:
        #This plays the thunder sound effect.
        thunder.play(0)
        #Draws in a white background to cover up the previous drawing
        screen.fill((254,254,254))
        #Every 3 iterations this code will use the player x and y to run through a loop of all the enemys and either move them towards the player or away from other-
        #- characters that they are touching.
        if counter == 3:
            x = guy.getX()
            y = guy.getY()
            enemys.move(x,y)
            counter = 0
        #This will check for a key being pressed down. If the escape key is pressed the game will run an infinite loop and dispay a "Paused" text box on the screen -
        #- esle it will check for wich arrow key is pressed and move the character acording to that
        for event in pygame.event.get():
            if event.type==QUIT or (event.type==KEYUP and event.key==K_ESCAPE):
                count = 0
                while count < 1:
                    guy.draw(screen)
                    enemys.draw(screen)
                    fullPrint = "Paused"
                    text = basicfont.render(fullPrint, True, (255, 255, 255), None)
                    textrect = text.get_rect()
                    textrect.centerx = 1920/2
                    textrect.centery = 1080/2
                    screen.blit(text, textrect)
                    pygame.display.update()
                    for event in pygame.event.get():
                        if (event.type==KEYUP and event.key==K_ESCAPE):
                            count += 1
                
            elif event.type==KEYDOWN:
                
                if event.key==K_UP:
                    guy.moveUp()

                if event.key==K_DOWN:
                    guy.moveDown()

                if event.key==K_LEFT:
                    guy.moveLeft()

                if event.key==K_RIGHT:
                    guy.moveRight()
                if event.key==K_f:
                    screen = pygame.display.set_mode((1920,1080),pygame.FULLSCREEN)
                    
                if event.key==K_n:
                    screen = pygame.display.set_mode((1920,1080),pygame.NOFRAME)
                    
        #Now that all of the moving parts have been updated, the display will draw the blocks into place using the screen entity as a place to draw.
        x = guy.getX()
        y = guy.getY()
        screen.fill((254,254,254))
        guy.flashDraw(screen)
        enemys.flashDraw(screen)
        #Every 10000 iterations of the code the enemys function will add five more characters to the list. If a certain number of enemys is exceeded it will respawn all of-
        #- the enemys ouside of a 100 pixel radius of the player and create a new level. 
        if counter2 == 10000:
            screen.fill(PURPLE)
            guy.draw(screen)
            enemys.addNewEnn(screen,guy)
            counter2 = 0
        #This will check if any of the enemy characters have collided with the player. If so the game will pause for a second, the character will have a life taken away, -
        #- and the enemy will respawn in a location outside of a 100 pixel area of the player. 
        if enemys.pCollide(guy) == True:
            guy.death()
        #This will get the number of lives remaining to the player and then print out a white text box(no background) on the top-left of the screen displaying that information. 
        num = guy.getLives()
        fullPrint = "Lives: {}".format(num)
        text = basicfont.render(fullPrint, True, (0,0,0), None)
        textrect = text.get_rect()
        textrect.centerx = 90
        textrect.centery = 20
        screen.blit(text, textrect)
        fullPrint = "Lives: {}".format(num)
        #This will got the number of enemy characters that are spawned on the screen and then diplay this information in a text box on the top-right of the screen
        num = enemys.getEns()
        fullPrint = "Horde: {}".format(num)
        text = basicfont.render(fullPrint, True, (0,0,0), None)
        textrect = text.get_rect()
        textrect.centerx = 1830
        textrect.centery = 20
        screen.blit(text, textrect)
        pygame.display.update()
        #This will reset the time before another flash happens and pause the screen for 1/30 of a second so that the frame is displayed in the screen.
        flash = randint(1000,4000)
        counter3 = 0
        time.sleep(1/10)




#This is the screen drawn when it is not flashing lightning. 
    else:    
        #Draws in a purple background to cover up the previous drawing
        screen.fill(PURPLE)
        #Every 10 iterations this code will use the player x and y to run through a loop of all the enemys and either move them towards the player or away from other-
        #- characters that they are touching.
        if counter == 3:
            x = guy.getX()
            y = guy.getY()
            enemys.move(x,y)
            counter = 0
        #This will check for a key being pressed down. If the escape key is pressed the game will run an infinite loop and dispay a "Paused" text box on the screen -
        #- esle it will check for wich arrow key is pressed and move the character acording to that
        for event in pygame.event.get():
            if event.type==QUIT or (event.type==KEYUP and event.key==K_ESCAPE):
                count = 0
                while count < 1:
                    guy.draw(screen)
                    enemys.draw(screen)
                    fullPrint = "Paused"
                    text = basicfont.render(fullPrint, True, (255, 255, 255), None)
                    textrect = text.get_rect()
                    textrect.centerx = 1920/2
                    textrect.centery = 1080/2
                    screen.blit(text, textrect)
                    pygame.display.update()
                    for event in pygame.event.get():
                        if (event.type==KEYUP and event.key==K_ESCAPE):
                            count += 1
                
            elif event.type==KEYDOWN:
                
                if event.key==K_UP:
                    guy.moveUp()

                if event.key==K_DOWN:
                    guy.moveDown()

                if event.key==K_LEFT:
                    guy.moveLeft()

                if event.key==K_RIGHT:
                    guy.moveRight()
                if event.key==K_f:
                    screen = pygame.display.set_mode((1920,1080),pygame.FULLSCREEN)
                if event.key==K_n:
                    screen = pygame.display.set_mode((1920,1080),pygame.NOFRAME)
        #Now that all of the moving parts have been updated, the display will draw the blocks into place using the screen entity as a place to draw.
        x = guy.getX()
        y = guy.getY()
        guy.draw(screen)
        enemys.draw(screen)
        #Every 10000 iterations of the code the enemys function will add five more characters to the list. If a certain number of enemys is exceeded it will respawn all of-
        #- the enemys ouside of a 100 pixel radius of the player and create a new level. 
        if counter2 == 10000:
            screen.fill(PURPLE)
            guy.draw(screen)
            enemys.addNewEnn(screen,guy)
            counter2 = 0
        #This will check if any of the enemy characters have collided with the player. If so the game will pause for a second, the character will have a life taken away, -
        #- and the enemy will respawn in a location outside of a 100 pixel area of the player. 
        if enemys.pCollide(guy) == True:
            guy.death()
        #This will get the number of lives remaining to the player and then print out a white text box(no background) on the top-left of the screen displaying that information. 
        num = guy.getLives()
        fullPrint = "Lives: {}".format(num)
        text = basicfont.render(fullPrint, True, (255, 255, 255), None)
        textrect = text.get_rect()
        textrect.centerx = 90
        textrect.centery = 20
        screen.blit(text, textrect)
        fullPrint = "Lives: {}".format(num)
        #This will got the number of enemy characters that are spawned on the screen and then diplay this information in a text box on the top-right of the screen
        num = enemys.getEns()
        fullPrint = "Horde: {}".format(num)
        text = basicfont.render(fullPrint, True, (255, 255, 255), None)
        textrect = text.get_rect()
        textrect.centerx = 1830
        textrect.centery = 20
        screen.blit(text, textrect)
        pygame.display.update()
    #These counters are used to have funtions happen that do not occur evey time the program runs through. 
    counter += 1
    counter2 += 1
    counter3 += 1
