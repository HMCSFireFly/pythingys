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

f = 0
v=5

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
def floor():
    pygame.Rect(0,270,600,500)
    

def redrawGameWindow():
    global walkcount
    win.blit(bg, (f-600,0))
    win.blit(bg, (f,0))
    win.blit(bg, (f+600,0))
    man.draw(win)
    floor()
    

man = player(70,270,64,64)
run = True
while run:
    clock.tick(27)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    keys = pygame.key.get_pressed() ; pygame.key.get_mods()
    
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
        if keys[pygame.K_SPACE]:
            man.isJump = True
            man.left = False
            man.right = False
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
    if man.x <= 50:
        man.x = man.x + man.vel
        f += v
    if f >= 600:
        f = 0
    elif f <= -600:
        f = 0
    if man.y >= 270:
        man.y = 270
    man.y = man.y + 10
    
    print (man.x)    
    print (man.y)
    print (f)
    
  
    
    pygame.display.update()
    #-------------landscape-------------#
    
   
   
   
    redrawGameWindow()
   
pygame.quit()

