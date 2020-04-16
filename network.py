import random as rand
import pygame
from visuals import *

class computer:
    def __init__(self,ip):
        self.trustedConnections = []
        self.ip = ip
        if(rand.randint(0,3) == 0):
            self.OS = "Sun"
        else:
            self.OS = "VAX"
        timesInfected = 0
class network:
    def __init__(self):
        self.networkComputers = []
    def exampleNetwork(self):
        while(True):
            #try:
            size = input("How large would you like your network x by x just input one number")
            for x in range(int(size)):
                self.networkComputers.append([])
                for y in range(int(size)):
                    self.networkComputers[x].append(computer([x,y]))
            break
            #except:
            #    print("please input a valid value")
if __name__ == "__main__":
    sample = network()
    sample.exampleNetwork()
    if __debug__ :
        allComputers = sample.networkComputers
        for i in allComputers:
            for j in i:
                print(j.ip)
    ''' what I want to do is make the background, blit the computers into their positions
    also possibly make it so that it is random whether a connection is made between
    every howevermany computers. From there make a 'virus' that uses the different ideas
    from the morris bug'''
