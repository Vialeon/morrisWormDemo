from PIL import Image
#import pygame

def makeComputerImage(timesInfected):
    fnt = ImageFont.truetype('arial.ttf',24)
    img = Image.new('RGB',(50,50),color = 'black')
    d = ImageDraw.Draw(img)
    d.text((25,5),num,fqnt = fnt,fill = (255,255,255)
    # to use this to make a pygame image use pygame.image.fromstring(data,size,mode)
    return img.mode,img.size,img.tobytes()

def makeBackground(sizeOfArray):
    img = Image.new('RGB',(sizeOfArray*60,sizeOfArray*60),color = 'white')
    img.save("defaultBackground.png")
