import math
import pygame

#vertices are numbered from 0 to V-1

class graph:

    cords = {}
    
    def __init__(self,window,V,E,limx,limy,direct,weighted,weights):
        self.window = window
        self.V = V
        self.E = E
        self.screenx = limx
        self.screeny = limy
        self.direct = direct
        self.weighted = weighted
        self.weights = weights
        self.rad = 150+(self.V-7)*10 if ((150+(V-7)*10)<min(limx/2,limy/2)-10) else min(limx/2,limy/2)-20
        #print(self.rad)
        midx = self.screenx//2
        midy = self.screeny//2
        angle = 2*math.pi/self.V
    
        for i in range(0,self.V):
            sin,cos = math.sin(i*angle),math.cos(i*angle)
            nodex = (self.screenx/2)+(self.rad*cos)
            nodey = (self.screeny/2)- (self.rad*sin)
            self.cords[i] = (int(nodex),int(nodey))
        

    def display_vert(self,vertexrad = 20,radmakebig = 20, makebigset = [],textsize=15,color = (0,150,0),diff = [],color2=(255,0,0)):
        #drawing the vertices
        for i in range(0,self.V):
            nx,ny = self.cords[i]
            font = pygame.font.Font('freesansbold.ttf', textsize) 
            if i not in diff:
                if i not in makebigset:
                    pygame.draw.circle(self.window,color,(nx,ny),vertexrad)
                    text = font.render(str(i), True, (0,0,0), color)
                else:
                    pygame.draw.circle(self.window,color,(nx,ny),radmakebig)
                    text = font.render(str(i), True, (0,0,0), color)
            else:                
                pygame.draw.circle(self.window,color2,(nx,ny),vertexrad)
                text = font.render(str(i), True, (0,0,0), color2)
            textRect = text.get_rect() 
            textRect.center = self.cords[i]
            self.window.blit(text, textRect)
        return self.cords


    def arrow(self, lcolor, tricolor, start, end, trirad):
        rotation = math.degrees(math.atan2(start[1]-end[1], end[0]-start[0]))+90
        pygame.draw.polygon(self.window, tricolor, ((end[0]+trirad*math.sin(math.radians(rotation)), end[1]+trirad*math.cos(math.radians(rotation))), (end[0]+trirad*math.sin(math.radians(rotation-120)), end[1]+trirad*math.cos(math.radians(rotation-120))), (end[0]+trirad*math.sin(math.radians(rotation+120)), end[1]+trirad*math.cos(math.radians(rotation+120)))))

    def display_edges(self,colorline=(0,0,0),s=[],color2=(0,0,0),thickline = 3):
        #drawing the edges
        if(self.direct==False):
            for i in self.E:
                a,b,c,d = self.cords[i[0]][0],self.cords[i[0]][1],self.cords[i[1]][0],self.cords[i[1]][1]               
                x = c-20 if (a<c) else c+20
                y = (((d-b)/(c-a))*(x-c))+d if (a<c) else (((d-b)/(c-a))*(x-c))+d
                if i not in s:
                    pygame.draw.line(self.window,colorline,self.cords[i[0]],self.cords[i[1]],thickline)
                    self.arrow(colorline,colorline,[a,b],[x,y],5) 
                else:
                    pygame.draw.line(self.window,color2,self.cords[i[0]],self.cords[i[1]],thickline)
                    self.arrow(color2,color2,[a,b],[x,y],5) 
                                  
                
                  
            
    def display_weights(self,textsize = 15):
        if self.weighted:
            j = 0
            for i in self.E:
                l = self.cords[i[0]]
                r = self.cords[i[1]]
                
                if r[0]-l[0]:
                    theta = math.atan((l[1]-r[1])/(r[0]-l[0]))
                else:
                    theta = math.pi/2
                ang = (180/math.pi * theta)
                mid = [(r[0]+l[0])//2,(r[1]+l[1])//2]
                font = pygame.font.Font('freesansbold.ttf', textsize) 
                #font = pygame.font.SysFont('freesansbold.ttf', 30, True, False)
                text = font.render(str(self.weights[j]), True, (0,0,0))
                text = pygame.transform.rotate(text,ang)
                if ang>0:
                    self.window.blit(text,[mid[0]+2,mid[1]+2])
                else:
                    self.window.blit(text,[mid[0],mid[1]+5])
                j+=1

    def display_labels(self,labels):
        for i in range (len(labels)):
            l = self.cords[i]
            font = pygame.font.Font('freesansbold.ttf', 15) 
            text = font.render(str(labels[i]), True, (0,0,0))
            if l[1]>self.screeny/2:
                self.window.blit(text,[l[0],l[1]+20+2])
            else:
                self.window.blit(text,[l[0],l[1]-20-2-20])
