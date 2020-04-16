import random as rand
import pygame
from visuals import *
import time

class computer:
    def __init__(self,ip):
        self.trustedConnections = []
        self.ip = ip
        if(rand.randint(0,3) == 0):
            self.OS = "Sun"
        else:
            self.OS = "VAX"
        self.timesInfected = 0
class network:
    def __init__(self):
        self.networkComputers = []
    def exampleNetwork(self):
        while(True):
            try:
                size = input("How large would you like your network x by x just input one number")
                for x in range(int(size)):
                    self.networkComputers.append([])
                    for y in range(int(size)):
                        self.networkComputers[x].append(computer([x,y]))
                break
            except:
                print("please input a valid value")

    def initAllConnections(self):
        #this will go LRTB through the computers and connect the ones next to each other
        for i in range(len(self.networkComputers)):
            for j in range(len(self.networkComputers[0])):
                try:
                    self.networkComputers[i][j].trustedConnections.append[i-1][j-1]
                    self.networkComputers[i][j].trustedConnections.append[i-1][j]
                    self.networkComputers[i][j].trustedConnections.append[i-1][j+1]
                    self.networkComputers[i][j].trustedConnections.append[i][j-1]
                    self.networkComputers[i][j].trustedConnections.append[i][j+1]
                    self.networkComputers[i][j].trustedConnections.append[i+1][j-1]
                    self.networkComputers[i][j].trustedConnections.append[i+1][j]
                    self.networkComputers[i][j].trustedConnections.append[i+1][j+1]
                except:
                    print("something went wrong initiating connections")
    #def initRandomConnections(self):
        #this will create random connections through certain Ip address'

if __name__ == "__main__":
    sample = network()
    sample.exampleNetwork()
    heightWidth = len(sample.networkComputers)*60

    if __debug__ :
        allComputers = sample.networkComputers

        for i in allComputers:
            for j in i:
                print(j.ip)
    #creating the intial state
    pygame.init()
    wormDisplay = pygame.display.set_mode([heightWidth,heightWidth])
    makeBackground(len(sample.networkComputers))
    theBackground = pygame.image.load("defaultBackground.png").convert()
    wormDisplay.blit(theBackground,(0,0))
    pygame.display.flip()
    fps = 5
    clock = pygame.time.Clock()
    # this puts every computer in the network on the display
    for i in range(len(sample.networkComputers)):
        for j in range(len(sample.networkComputers[0])):
            infections = sample.networkComputers[i][j].timesInfected
            ip = sample.networkComputers[i][j].ip
            mode,size,bytes = makeComputerImage(infections,ip)
            toBlit = pygame.image.fromstring(bytes,size,mode)
            wormDisplay.blit(toBlit,(j*60+5,i*60+5))
            pygame.display.flip()
            clock.tick(fps)


    #this will wait until I enter play to run
    while(True):
        shouldIStayOrShouldIGo = input("play?")
        if(shouldIStayOrShouldIGo == "play"):
            break
        else:
            time.sleep(.5)
    ''' what I want to do is make the background, blit the computers into their positions
    also possibly make it so that it is random whether a connection is made between
    every howevermany computers. From there make a 'virus' that uses the different ideas
    from the morris bug'''
