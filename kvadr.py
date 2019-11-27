import pygame
w=int(input())
h=int(input())
size=40
def fielding (h,w,s):
    for i in range (h):
        for j in range(w):
            pygame.draw.rect(sc,(255,255,255),(20+j*size,20+i*size,size,size),2)
def draw_obj(x,y,t):
    global size
    if t == 1:
        pygame.draw.circle(sc,(0,255,0),(20+x*size-size//2,20+y*size-size//2),size//2)
pygame.init()
 
sc = pygame.display.set_mode((20+w*size+20+200,20+h*size+20))
 
# здесь будут рисоваться фигуры
fielding(h,w,size)
draw_obj(5,2,1)
#pygame.draw.circle(sc,(0,255,0),(25,25),20)

pygame.display.update()
 
while 1:
    pygame.time.delay(1000)
    for i in pygame.event.get():
        if i.type == pygame.QUIT: exit()
