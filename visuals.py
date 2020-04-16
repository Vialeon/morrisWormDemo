from PIL import Image, ImageFont,ImageDraw
#import pygame

def makeComputerImage(timesInfected,ip):
    fnt = ImageFont.truetype('arial.ttf',24)
    if(timesInfected<16):
        img = Image.new('RGB',(50,50),color = 'black')
        d = ImageDraw.Draw(img)
        d.text((15,20),str(timesInfected),fqnt = fnt,fill = (0,255,0))
        d.text((15,0),str(ip),fqnt = fnt,fill = (0,255,0))
        return img.mode,img.size,img.tobytes(),0
    else:
        img = Image.new('RGB',(50,50),color = 'red')
        d = ImageDraw.Draw(img)
        d.text((0,20),"Game Over",fqnt = fnt,fill = (0,255,0))
        return img.mode,img.size,img.tobytes(),1


    # to use this to make a pygame image use pygame.image.fromstring(data,size,mode)


def makeBackground(sizeOfArray):
    img = Image.new('RGB',(sizeOfArray*60,sizeOfArray*60),color = 'white')
    img.save("defaultBackground.png")
