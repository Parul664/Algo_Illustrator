import time
import pygame
import math


class make_tree:

    

    def __init__(self,window, V,E, limx, limy,textsize = 15):
        self.V = V
        self.E = E
        self.screenx = limx
        self.screeny = limy
        self.window = window
        self.font = pygame.font.Font('freesansbold.ttf', textsize)
        self.level = {}


    def make_circle(self,text,nx,ny,color =(0,255,0),rad = 10):
        pygame.draw.circle(self.window,color,(int(nx),int(ny)),rad)
        text = self.font.render(text, True, (0,0,0), color)
        textRect = text.get_rect() 
        textRect.center = [nx,ny]
        self.window.blit(text, textRect)
        #Call it as:
        #mk.make_circle(20,str(10),(0,255,0),50,50)


    def drawline(self,a,b):
        pygame.draw.line(self.window,(0,0,0),a,b,2)

        
    #g is the graph
    def make_tree(self,g_dic,s,sep_between_layers,startx,starty,ll =0):
        if s not in g_dic or len(g_dic[s])==0:
            return

        
        #self.make_circle(text = str(s), nx = startx,ny = starty)
        number = len(g_dic[s]) 
        if number%2==0:
            #distance between vertices is 20
            cx = 0            
            if ll not in self.level:
                cx = startx - (((number+2)/2)*30) +15
                
            else:
                cx = self.level[ll]+5
            
            for child in g_dic[s]:                      
                cx = cx + 30
                cy = starty + sep_between_layers
                print(child,cx,cy) 
                self.drawline((startx,starty),(cx,cy))
                self.make_tree(g_dic,child,sep_between_layers,cx,cy,ll = ll+1)
       
                self.make_circle(text = str(s), nx = startx,ny = starty)
             
                self.make_circle(text = str(child), nx = cx,ny = cy)
                self.level[ll] = cx
                  

        #if odd 
        else:
            cx = 0            
            if ll not in self.level:
                cx = startx - (((number+1)/2)*30)
            else:
                cx = self.level[ll]+5
                
            for child in g_dic[s]:                
                cx = cx + 30
                cy = starty + sep_between_layers
                self.drawline((startx,starty),(cx,cy))
                self.make_tree(g_dic,child,sep_between_layers,cx,cy,ll = ll+1)
               
                self.make_circle(text = str(s), nx = startx,ny = starty)
                
                self.make_circle(text = str(child), nx = cx,ny = cy)
                self.level[ll] = cx
                print(child,cx,cy)  

                
                

                
            
            

        
        
        

    
        
