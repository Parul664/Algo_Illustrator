import math
import pygame

class p_queue:

    def __init__(self,window, lenn, limx,limy):
        self.window = window
        self.lenn = lenn
        self.limx = limx
        self.limy = limy
        #font is set to be 20... change it here if you want
        self.font = pygame.font.Font('freesansbold.ttf', 20)
        self.font2 = pygame.font.Font('freesansbold.ttf', 12) 
        self.el_in_queue = []
        #first make the external frame
        #            80
        #a----------b--
        #\   |lenn / lenn/cos(50)
        # \  |    /
        #  c-----d
        #     60 |100

        self.tilt = math.tan(math.pi/60)
        self.d = [limx - (lenn*math.tan(math.pi/60))-80,limy-150]
        self.c = [limx - (lenn*math.tan(math.pi/60))-140,limy-150]
        self.b = [limx-80,limy-lenn-150]
        self.a = [limx - (2*lenn*math.tan(math.pi/60))-140,limy-lenn-150]
        
        
    def line(self,a,b):
        pygame.draw.line(self.window,(0,0,0),a,b,3)

    def show_skeleton(self):
        self.line(self.b,self.d)
        self.line(self.c,self.d)
        self.line(self.a,self.c)

    def fill_pq(self,elements,delta,diss = 40):
        self.el_in_queue = []
        #elements.sort(reverse = True)
        for element in elements:
            self.el_in_queue.append(element)
        
        damn = []
        for el in elements:
            sett = delta[el]
            damn.append(sett)
        zipped_pairs = zip(damn, elements)
        elements = [x for _, x in sorted(zipped_pairs)]
        elements.reverse()

        dis = self.lenn/len(elements) if (self.lenn<(diss*len(elements))) else diss
        p0 = (self.c[0]-(dis*self.tilt),self.c[1]-dis)
        p1 = (self.d[0]+(dis*self.tilt),self.d[1]-dis)
        p0_bef,p1_bef = self.c,self.d

        #if all the elements are not able to fit inside the priority queue
        for el in elements:
            its_dis = str(delta[el]) if delta[el]!=100000 else "inf"
            
            pygame.draw.polygon(self.window,(150,255,150),[p0,p1,p1_bef,p0_bef])
            pygame.draw.line(self.window,(0,0,0),[p0[0],p0[1]],[p1[0],p1[1]],3)
            #write the element in priority queue
            text = self.font.render(str(el),True,(0,0,0))
            text_cords = [(p0[0]+p1[0])/2 - 5, (p0[1]+p0_bef[1])/2-9]
            self.window.blit(text,text_cords)

            pygame.draw.circle(self.window,(0,200,200),(int(text_cords[0]+5+90+self.tilt),int(text_cords[1]+9)),15)
            text2 = self.font2.render(its_dis,True,(0,0,0))
            textRect = text2.get_rect() 
            textRect.center = [int(text_cords[0]+5+90+self.tilt),int(text_cords[1]+9)]
            self.window.blit(text2, textRect)
            
            p0_bef, p1_bef = p0,p1
            p0 = (p0_bef[0] - (dis*self.tilt), p0_bef[1] - dis)
            p1 = (p1_bef[0] + (dis*self.tilt), p1_bef[1] - dis)            
        self.show_skeleton()
        #pygame.display.update()
        


        #make transition of vertices after they have been sorted
        #def remove_element(self,sorted_elements):
            
        
        
        
        

    
    
        
