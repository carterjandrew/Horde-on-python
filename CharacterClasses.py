#Cardi A's Code:
#This is all of the nessisairy imports to run my code incuding: pygame as my game engine, randint to get a spawning and respawning location, and sys as the method to quit the game once finished. 
import pygame, sys
from pygame import *
from random import randint
import math

#This is the player class, it incudes all of the funtions(Algorithms that change different variables assigned to the player), variables, and skins(aka an orange box)
class Player:
    #This is the initialisation and it creates the player and all of its different varables. These incude: Number of lives, the color of the box, and the x and y coordinates 
    def __init__(self):
        self.x = randint(0,1000)
        self.y = randint(0,1000)
        self.color = (239,74,37)
        self.darkMode = False
        self.lives = 10
        #This function uses the pygame engine to draw your player at its x and y variable coordiantes on to imported screen: window
        #It will also draw 3 light boxes surrouning the player using the players x and y coordinates
    def draw(self,window):
        pygame.draw.rect(window, (30,12,30), (self.x-190,self.y-190,400,400))
        pygame.draw.rect(window, (59,24,10), (self.x-90,self.y-90,200,200))
        pygame.draw.rect(window, (117,47,19), (self.x-40,self.y-40,100,100))
        pygame.draw.rect(window, self.color, (self.x,self.y,20,20))
    #This draws the player during a flash withougt all of the light boxes around it.
    def flashDraw(self,window):
        pygame.draw.rect(window, self.color, (self.x,self.y,20,20))
        #This will change the players self.y so that the player is one pixel further up
    def moveUp(self):
        if self.y > 0:
            self.y -= 1
            #This will change the player self.y so that the player os one pixel further down
    def moveDown(self):
        if self.y < 1060:
            self.y += 1
            #This will change the players self.x so that the player is one pixel the the right
    def moveRight(self):
        if self.x < 1900:
            self.x += 1
            #This will change the players self.x so that the player is one pixel the the left
    def moveLeft(self):
        if self.x > 0:
            self.x -= 1
            #This will return the players x from the top-left corner (so that the enemys can move towards and see if they have collided with the character)
    def getX(self):
        return self.x
            #This will return the players y from the top-left corner (so that the enemys can move towards and see if they have collided with the character)
    def getY(self):
        return self.y
            #This returns a list of the coordinates of the players rectangle in the following format: [top-left x position, top-left y position, length, width]
    def getRec(self):
        return [self.x, self.y, 20, 20]
            #This returns a far larger box of wich enemys must spawn outside (So they won't respawn right on top of you)
    def getSafeBox(self):
        return [self.x - 50, self.y - 50, 100, 100]
            #This funtion dictates what happens to the player if he is hit by an enemy
    def death(self):
        self.lives -= 1
        if self.lives == 0:
            sys.exit()
            pygame.quit()
            #Retuns the number of lives that the player has remaining (to print out on screen)
    def getLives(self):
        return self.lives
    #This is the oponent(or enemy) class, it incudes all of the funtions(Algorithms that change different variables assigned to the player), variables, and skins(aka a dark purple box)
    #This class is unique because it is not directly accessed by the runner. Instead, it is put into a larger list of oponents in the "Enemys" class
class Oponent:
    #This is the initialisation and it creates the player and all of its different varables. These incude: The color and the X and Y coordinates if the NPC
    #Most of the code is to choose the location of the enemy so it is outside the safezone box of the player
    def __init__(self,other):
        otherRec = other.getSafeBox()
        if otherRec[0] <= 0:
            otherRec[0] = otherRec[0] + 50
        if otherRec[1] <= 0:
            otherRec[1] = otherRec[1] + 50
        if otherRec[0] + otherRec[2] >= 1920:
            otherRec[0] = otherRec[0] - 50
        if otherRec[1] + otherRec[3] >= 1080:
            otherRec[1] = otherRec[1] - 50
        chooser = randint(0,1)
        if chooser == 1:
            self.x = randint(otherRec[0] + otherRec[2] , 1920)
        else:
            self.x = randint(0 , otherRec[0])

        chooser = randint(0,1)
        if chooser == 1:
            self.y = randint(otherRec[1] + otherRec[3] , 1080)
        else:
            self.y = randint(0 , otherRec[1])
        self.color = (27,14,56)
    #This function uses the pygame engine to draw the enemy at its x and y variable coordiantes on to imported screen: window
    def draw(self,window):
        pygame.draw.rect(window, self.color, (self.x,self.y,20,20))
    def flashDraw(self,window):
        pygame.draw.rect(window, (10,10,200), (self.x,self.y,20,20))
    #This function contains an algorithm that will find the farthest direction from the player and move that way. It can move: Up, Down, Left, Right, and diagonal in all directions
    #This is used to have the enemys chase the player
    def AI(self,playerX,playerY):
        if abs(playerY - self.y) > abs(playerX - self.x):
            if self.y > playerY:
                self.y -= 1
            else:
                self.y += 1
        elif abs(playerY - self.y) == abs(playerX - self.x):
            if self.y > playerY:
                self.y -= 1
            else:
                self.y += 1
            if self.x > playerX:
                self.x -= 1
            else:
                self.x += 1
        else:
            if self.x > playerX:
                self.x -= 1
            else:
                self.x += 1
    #This function contains an algorithm that will find the farthest direction from the player and move away from that direction. It can move: Up, Down, Left, Right, and diagonal in all directions
    #This is used to keep the enemys ouside of each other
    def OPAI(self,playerX,playerY):
        if abs(playerY - self.y) < abs(playerX - self.x):
            if self.y < playerY:
                self.y -= 1
            else:
                self.y += 1
        elif abs(playerY - self.y) == abs(playerX - self.x):
            if self.y < playerY:
                self.y -= 1
            else:
                self.y += 1
            if self.x < playerX:
                self.x -= 1
            else:
                self.x += 1
        else:
            if self.x < playerX:
                self.x -= 1
            else:
                self.x += 1
    #This will predict wich way the enemy will move and return a list with the value it will move in this order: [up, down, left, right]
    def getMove(self,playerX,playerY):
        if abs(playerY - self.y) > abs(playerX - self.x):
            if self.y > playerY:
                return [1,0,0,0]
            else:
                return [0,1,0,0]
        else:
            if self.x > playerX:
                return [0,0,1,0]
            else:
                return [0,0,0,1]
    #This retunrns a value that will tell the enemeys class wether to move towards the player or away from another enemy. 
    def ChooseAI(self):
        return self.AI
    #Returns the x coordinate of the top-left corner of the enemy
    def getX(self):
        return self.x
    #Returns the y coordinate of the top-left corner of the enemy
    def getY(self):
        return self.y
    #This returns a list of the coordinates of the enemys rectangle in the following format: [top-left x position, top-left y position, length, width]
    def getRec(self):
        return [self.x, self.y, 20, 20]
    #This funtion is used to check is the enemy has collided with any other object(other) and will return true if it has and false if it hasn't
    def collide(self, other,pX,pY):
            myRec = self.getRec()
            direc = self.getMove(pX,pY)
            otherRec = other.getRec()
            if direc[0] == 1:
                myRec[1] -= 1
            elif direc[1] == 1:
                myRec[1] += 1
            elif direc[2] == 1:
                myRec[0] -= 1
            elif direc[3] == 1:
                myRec[0] += 1
            oRight  = otherRec[0] + otherRec[2]
            oBottom  = otherRec[1] + otherRec[3]
            right = myRec[0] + myRec[2]
            bottom = myRec[1] + myRec[3]
            if (otherRec[0] <= right) and (oRight >= self.x) and (otherRec[1] <= bottom) and (oBottom >= self.y):
                self.OPAI(otherRec[0],otherRec[1])
                return True
            else:
                return False
    #This function will respawn the enemy in a random location outside of the players safebox.
    def respawn(self,other):
        otherRec = other.getSafeBox()
        if otherRec[0] <= 0:
            otherRec[0] = otherRec[0] + 50
        if otherRec[1] <= 0:
            otherRec[1] = otherRec[1] + 50
        if otherRec[0] + otherRec[2] >= 1920:
            otherRec[0] = otherRec[0] - 50
        if otherRec[1] + otherRec[3] >= 1080:
            otherRec[1] = otherRec[1] - 50
        chooser = randint(0,1)
        if chooser == 1:
            self.x = randint(otherRec[0] + otherRec[2] , 1920)
        else:
            self.x = randint(0 , otherRec[0])

        chooser = randint(0,1)
        if chooser == 1:
            self.y = randint(otherRec[1] + otherRec[3] , 1080)
        else:
            self.y = randint(0 , otherRec[1])
