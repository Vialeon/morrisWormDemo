import random as rand
import pygame
from visuals import *
import time
'''
Things I could add atm. Passwords for each computer and a giant thing that tries all of them
add a pseudo smtp connection with the debug mode thinger(people could've turned off debug)
try the fingerd bug if smtp does not 'work' ie buffer overflow (note fingerd was just backwards compatible and actually fixed in 1979)
rexec and passwords: cornell did not encrypt usernames and they wre readily available. After getting the username just use rexec
rsh and trust: local host only knows network address for trusted connections<-- this can be spoofed

'''
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
                size = input("How large would you like your network x by x just input one number: ")
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
    def infectComputer(self,x):
        print(x)
        self.networkComputers[x][x].timesInfected +=1

def runTheSimulation(sample,heightWidth,wormDisplay):
    totalKilled = 0
    print("starting worm")
    sample.infectComputer(int(heightWidth/120))
    for x in range(100):
        for i in range(len(sample.networkComputers)):
            for j in range(len(sample.networkComputers[0])):
                if(sample.networkComputers[i][j].timesInfected!=0 and sample.networkComputers[i][j].timesInfected<16):
                    for k in range(-1,2):
                        for y in range(-1,2):
                            if(k!=0 or y!=0):
                                if(rand.randint(0,6) == 3):
                                    sample.networkComputers[(i+k)%(len(sample.networkComputers))][(j+y)%(len(sample.networkComputers))].timesInfected+=1

                infections = sample.networkComputers[i][j].timesInfected
                ip = sample.networkComputers[i][j].ip
                mode,size,bytes,dead= makeComputerImage(infections,ip)
                if(infections == 16):
                    totalKilled+=dead
                    sample.networkComputers[i][j].timesInfected+=1

                toBlit = pygame.image.fromstring(bytes,size,mode)
                wormDisplay.blit(toBlit,(j*60+5,i*60+5))
                pygame.display.flip()
                if(totalKilled>(50)):
                    return x
        clock.tick(2)


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
            mode,size,bytes,holder = makeComputerImage(infections,ip)
            toBlit = pygame.image.fromstring(bytes,size,mode)
            wormDisplay.blit(toBlit,(j*60+5,i*60+5))
            pygame.display.flip()


    #this will wait until I enter play to run
    while(True):
        shouldIStayOrShouldIGo = input("play?")
        if(shouldIStayOrShouldIGo == "play"):
            break
        else:
            time.sleep(.5)
    totalKilled = 0
    print("starting worm")
    print("iterations over network: ",runTheSimulation(sample,heightWidth,wormDisplay))
    time.sleep(10)
    if False:
        sample.infectComputer(int(heightWidth/120))
        for x in range(100):
            for i in range(len(sample.networkComputers)):
                for j in range(len(sample.networkComputers[0])):
                    if(sample.networkComputers[i][j].timesInfected!=0 and sample.networkComputers[i][j].timesInfected<16):
                        for x in range(-1,2):
                            for y in range(-1,2):
                                if(x!=0 or y!=0):
                                    if(rand.randint(0,6) == 3):
                                        sample.networkComputers[(i+x)%(len(sample.networkComputers))][(j+y)%(len(sample.networkComputers))].timesInfected+=1

                    infections = sample.networkComputers[i][j].timesInfected
                    ip = sample.networkComputers[i][j].ip
                    mode,size,bytes,dead= makeComputerImage(infections,ip)
                    totalKilled+=dead
                    toBlit = pygame.image.fromstring(bytes,size,mode)
                    wormDisplay.blit(toBlit,(j*60+5,i*60+5))
                    pygame.display.flip()
                    if(totalKilled>(len(sample.networkComputers)*len(sample.networkComputers))):
                        print(x," iterations over network")
                        x = 100
                        i = len(sample.networkComputers)
                        break
            clock.tick(10)




    # to start it could be more like it's just that if the guy next to you is infected you have a 1/7 chance of being infected
    #for i in range(len(sample.networkComputers)):
        #for j in range(len(sample.networkComputers[0])):


    #try smtp if debug enabled then run command to open and run bug if succeeded the init should send a byte to some server/flip a switch
    #if that doesn't work try fingerd if the machine is VAX this succeeds if it not then it fails
    #if that doesn't work try rexec with the bunch of usernames you got from the the /etc/passwd file that has uncencryped usernames and the common passwords you've got
    #if that doesn't work try rsh.. search for trusted connections and connect to said hosts if from rhosts just pass the right user name along and replicate
    #what I want to do is make the background, blit the computers into their positions
    #also possibly make it so that it is random whether a connection is made between
    #every howevermany computers. From there make a 'virus' that uses the different ideas
    #from the morris bug
