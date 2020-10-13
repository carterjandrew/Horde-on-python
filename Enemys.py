#Cardi A's Code
#These import all of the nessisairy classes for the code to run.
from CharacterClasses import *
import time
#This is the enemys class. It contains a list of all of the enemys on the screen.
#It imports self wich acts as a globaliser for variables(so they can be shared inbetween all diferent functions)
#It also imports sn, meaning starting number.
#Along with "count" wich dictates how long a level lasts and "other" wich is the player to make sure that they spawn ouseide of the players safe box
class Enemys:
    #Initialises all variables talked about above
    def __init__(self,sn,count,other):
        self.count = count
        self.enemys = []
        self.level = 1
        self.counter = 0
        counter = 0
        while counter < sn:
            self.enemys.append(Oponent(other))
            counter += 1
    #This funtion uses a while loop to run through each individual NPC(non player character) and move it either towards the player or away from other enemys. 
    def move(self,playerx,playery):
        counter = 0
        while counter < len(self.enemys):
            if self.collide(counter,playerx,playery) == False:
                self.enemys[counter].AI(playerx,playery)
            counter += 1
    #This function uses a while loop to run through all NPCs and draw them on to the screen
    def draw(self,window):
        counter = 0
        while counter < len(self.enemys):
            self.enemys[counter].draw(window)
            counter += 1
    def flashDraw(self,window):
        counter = 0
        while counter < len(self.enemys):
            self.enemys[counter].flashDraw(window)
            counter += 1
    #This funtion will add 5 new enemys to the list. However, first it will check if there are enough enemys to start a new level.
    #When a new level is started all enemys are respawned using a while loop and then the "count" variable is increased by 10
    def addNewEnn(self,window,other):
        if len(self.enemys) < self.count:
            counter = 0
            while counter < 5:
                self.enemys.append(Oponent(other))
                counter += 1
        else:
            time.sleep(1)
            counter = 0
            self.count += 10
            while counter < len(self.enemys):
                self.enemys[counter].respawn(other)
                counter += 1
            counter = 0
            while counter < len(self.enemys):
                self.enemys[counter].draw(window)
                counter += 1
            self.level += 1
            pygame.display.update()
            time.sleep(1)
    #This funtion uses a while loop to check if an enemy is colliding with any other enemys. If so it will return true so the enemy can move away acordingly. 
    def collide(self, num,pX,pY):
        counter = 0
        while counter < len(self.enemys):
            if num != counter:
                if self.enemys[num].collide(self.enemys[counter],pX,pY) == True:
                    return True
            counter += 1
        return False
    #This checks if ANY of the enemys have collided with the player. If so it will respawn that enemy in a new location. 
    def pCollide(self,other):
        counter = 0
        while counter < len(self.enemys):
            if self.enemys[counter].collide(other,800,300) == True:
                time.sleep(1)
                self.enemys[counter].respawn(other)
                return True
            counter += 1
        return False
    #This returns the level that they are on(Not actually used)
    def getLevel(self):
        return self.level
    #This returns the length of the list, or the amount of enemys on the screen. 
    def getEns(self):
        return len(self.enemys)
                
            
    
