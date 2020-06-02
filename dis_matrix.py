import math
import pygame
from p_queue import p_queue

class dis_matrix:

    def __init__(self,window,limx,limy):
        self.window = window
        self.limx = limx
        self.limy = limy
        self.font = pygame.font.Font('freesansbold.ttf', 15)
        self.l = 60
        self.d = 30

    def line(self,a,b):
        pygame.draw.line(self.window,(0,0,0),a,b,2)

    def show_skeleton(self,x,y,a,b,c,d,el):
        self.line(a,b)
        self.line(b,d)
        self.line(c,d)
        self.line(a,c)
        text = self.font.render(str(el), True, (0,0,0))
        self.window.blit(text,[x+int(self.l/2)-3,y+int(self.d/2)-6])
    
    def show(self,diction):
        #takes as input a dictionary..lol had to do it because I used that in Dijkstra
        n = len(diction)
        
        #starting positions
        x,xx,y,yy = 50,50,14,14+self.d   

    
        for el in diction:
            a = "inf" if (diction[el]==1000000) else diction[el]
            self.show_skeleton(x,y,[x,y],[x+self.l,y],[x,y+self.d],[x+self.l,y+self.d],el)
            self.show_skeleton(xx,yy,[xx,yy],[xx+self.l,yy],[xx,yy+self.d],[xx+self.l,yy+self.d],a)
            x += self.l
            xx += self.l
            
            
        
            
            
            
        
