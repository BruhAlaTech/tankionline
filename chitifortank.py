import pygame
import random
w = int(input())
h = int(input())
size = 40
#listX = []
#listY = []

def fielding(h, w, size):
    for i in range(h):
        for j in range(w):
            pygame.draw.rect(sc, (255, 255, 255), (20 + j*size, 20 + i*size, size, size), 2)

def draw_obj(x, y, c):
    global size
    #def rerandomX():
       # for i in listX:
        #    if x == listX[i]:
          #          x = random.randrange(1, h, 1)
             #       rerandomX()
    #def rerandomY():
       # for i in listY:
         #   if y == listY[i]:
          #          y = random.randrange(1, h, 1)
            #        rerandomY()
    if c != e:

            pygame.draw.circle(sc, (0, 255, 0), (20 + x * size - size // 2, 20 + y * size - size // 2), size // 2)
            c = c + 1

            x = random.randrange(1, h, 1)
            y = random.randrange(1, w, 1)

            if e != c:
               # listX = listX + x
               # listY = listY + y
                draw_obj(x,y,c)




pygame.init()

sc = pygame.display.set_mode((20 + w*size + 20 + 200, 20 + h*size + 20))

fielding(h, w, size)
e = 0.4 * h * w
c = 0
x = random.randrange(1, h, 1)
y = random.randrange(1, w, 1)
draw_obj(x, y, c)

pygame.display.update()

while 1:
    pygame.time.delay(1000)
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
