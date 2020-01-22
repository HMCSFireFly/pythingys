import pygame
pygame.init()
win = pygame.display.set_mode((600,500))
pygame.display.set_caption("Test Game")
walkright = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R3.png'), pygame.image.load('R2.png'), pygame.image.load('R6.png')]
walkleft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L3.png'), pygame.image.load('L2.png'), pygame.image.load('L6.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('idle.png')
JL = pygame.image.load('L7.png')
JR = pygame.image.load('R7.png')
clock = pygame.time.Clock()
house = pygame.image.load('house.png')
p = pygame.image.load('platform.png')
f = 0
v=5
a = 0


class player:
    def __init__(self,x,y,height,width):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.walkcount = 0
    #player's draw function#    
    def draw(self,win):
        if self.walkcount + 1 >= 27:
            self.walkcount = 0
        if self.left:
            win.blit(walkleft[self.walkcount//3],(self.x,self.y))
            self.walkcount += 1
        elif self.right:
            win.blit(walkright[self.walkcount//3],(self.x,self.y))
            self.walkcount +=1
        else:
            win.blit(char,(self.x,self.y))
            pygame.display.update()
#mock floor#
def floor():
    pygame.Rect(0,270,600,500)
#redraw#
def redrawGameWindow():
    global walkcount
    win.blit(bg, (f-600,0))
    win.blit(bg, (f,0))
    win.blit(bg, (f+600,0))
    win.blit(house, (f+120,270))
    win.blit(p, (a+230,268))
    man.draw(win)
    floor()
#begin#
man = player(70,270,64,64)
run = True
while run:
    clock.tick(27)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed() 
    if keys[pygame.K_a]:
        man.x -= man.vel
        man.left = True
        man.right = False
    elif keys[pygame.K_d]:
        man.x += man.vel
        man.right = True
        man.left = False     
    else:
        man.right = False
        man.left = False
        man.walkcount = 0
    if keys[pygame.K_LSHIFT]:
        man.vel = 10
        v = 10
    else:
        man.vel = 5
        v = 5
    if not(man.isJump):
        ##Space##
        if keys[pygame.K_SPACE]:
            man.isJump = True
            man.walkcount = 0
    else:
        if man.jumpCount >= -10:
            neg = 1
            if man.jumpCount < 0:
                neg = -1
            man.y -= (man.jumpCount ** 2) * 0.5* neg
            man.jumpCount -= 1      
        else:
            man.isJump = False
            man.jumpCount = 10    
    if man.x >= 460:
        man.x = man.x - man.vel
        f -= v
        a -= v
    if man.x <= 50:
        man.x = man.x + man.vel
        f += v
        a += v
    #-------------landscape-------------#
    #moc plat#
    def platform(xx,yy):
        if man.y >= yy and man.y <= yy+20 and man.x >= a+xx and man.x <= a+xx+100:
            print('This is a platform, it took quite a few hours of trial and error to get this right and make it work like a platform')
            man.y = yy
            man.isJump = False
            man.jumpCount = 10
            if keys[pygame.K_SPACE]:
                man.isJump = True
                
    platform(200,200)
    #-----------------------------------#
    if f >= 600:
        f = 0
    elif f <= -600:
        f = 0
    if man.y >= 270:
        man.y = 270
    man.y = man.y + 10
    print ('x :',man.x)    
    print ('y :',man.y)
    print ('location : ',a)
    print ('Scroll :', f)
    print ('keys :',keys[pygame.K_a],keys[pygame.K_d],keys[pygame.K_SPACE],keys[pygame.K_LSHIFT])
    print (man.isJump)
    print (man.jumpCount)
    pygame.display.update()
    redrawGameWindow()  
pygame.quit()