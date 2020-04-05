from Dijkstra import Dijkstraa
from graph import graph 
import math
import pygame
pygame.init()

limx = 1000
limy = 600

window = pygame.display.set_mode((limx,limy))
pygame.display.set_caption('Graph')

#bg = pygame.image.load('C:/Users/Parul/Pictures/white.jpg')
#bg = pygame.transform.scale(bg,(limx,limy))
#window.blit(bg,(0,0))
window.fill(pygame.Color("white"))
#labels = [1,2,3,4,7,8]
edges = [[1,2],[2,3],[1,4],[5,1],[3,4],[5,1]]            
w = [1,2,3,4,5,6]
g = Dijkstraa(window,6,edges,limx,limy,0,1,w)
g.demo_algo_initialize(1)

cont = 1
end = 0
while not end:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            end=True
    cont = g.algo(cont)
    if(cont==0):
        end = 1
    pygame.display.flip()
    
pygame.quit()
quit()
