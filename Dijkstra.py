import time
from graph import graph
import math
import pygame

class Dijkstraa:
    def __init__(self,window,V,E,limx,limy,direct,weighted,weights):
        self.window = window
        self.V = V
        self.E = E
        self.screenx = limx
        self.screeny = limy
        self.direct = direct
        self.weighted = weighted
        self.weights = weights
        #self.bg = bg
        self.g = graph(window,V,E,limx,limy,direct,weighted,weights)
        self.g.display_edges()
        self.cords = self.g.display_vert()        
        self.g.display_weights()
        #self.g.display_labels([1,2,3,5,3,4])
        pygame.display.update()

    def make2SortReturn(self,aa):
        vert = [key for key in aa if not self.visited[key]]
        delta = [aa[key] for key in vert]
        vert_sorted = [x for _,x in sorted(zip(delta,vert))]
        return vert_sorted
       
    def demo_algo_initialize(self,source):
        self.dis = [100000 for i in range(self.V)]        #d
        self.S = []
        self.labell = [100000 for i in range(self.V)] 
        self.visited = [False for i in range(self.V)]   #visited
        self.vertDis = {}
        for i in range(self.V):
            self.vertDis[i] = 1000000
        self.source = source                            #source
        self.dis[source] = 0                            #dis
        self.vertDis[source] = 0
        self.labell[source] = 0
        self.vert_sorted = self.make2SortReturn(self.vertDis)
        self.adjList = {}
        self.children=[]
        self.makebigset = []
        self.reset()
        i = 0
        #initialise the adjList
        for v in range(self.V):
            self.adjList[v] = []
        for edge in self.E:
            self.adjList[edge[0]].append([edge[1],self.weights[i]])
            i+=1

    def put_textt(self,s,x,y,font_size,color):
        font = pygame.font.Font('freesansbold.ttf',font_size)
        text = font.render(s,True,color)
        self.window.blit(text,[x,y])
        textRec = text.get_rect()
        return textRec

    def update(self,timee):
        pygame.display.update()
        time.sleep(timee)
        

    def reset(self,vertex_rad = 20):
        self.window.fill(pygame.Color("white"))
        self.g.display_edges(s = self.children,color2 = (255,0,100))
        self.cords = self.g.display_vert(makebigset = self.makebigset,radmakebig = vertex_rad,diff = self.S)        
        self.g.display_weights()
        self.g.display_labels(self.labell)
        pygame.display.update()
        
    def algo(self,count):
        if not self.vert_sorted:
            stop = 0
            return stop
        if self.vert_sorted:
            stop = 1
            #poping the vertex from the priority queue
            v= self.vert_sorted.pop(0)
            print(self.vert_sorted)
            #print(self.delta)
            s = "Vertex Popped: " +str(v)
            self.S.append(v)
            self.reset()
            self.put_textt(s,self.screenx-300,self.screeny-70,20,(0,0,0))
            self.update(1)       #update for 3 second
            self.dis[v] = self.vertDis[v]
            self.visited[v] = True
            
            s = "Exploring its children..."

            for child,weigh in self.adjList[v]:
                print("child",child,"weight: ",weigh)
                if not self.visited[child]:
                    #find it in the vert list
                    ss = "Vertex: "+str(child)
                    self.children.append([v,child])
                    self.reset()
                    self.makebigset = [child]
                    print("The makebigset set now is:",self.makebigset)
                    self.MakeVertBig()
                    self.makebigset = []
                    self.put_textt(s,self.screenx-300,self.screeny-70,20,(0,0,0))
                    self.put_textt(ss,self.screenx-300,self.screeny-35,20,(0,0,0))
                    self.update(3)
                    
                    if(self.vertDis[child]>self.dis[v]+weigh):
                        self.vertDis[child] = self.dis[v] + weigh
                        self.labell[child] = self.vertDis[child]                        
                        self.reset()
                        print("After removal: vertices: ",self.vert_sorted)
            self.update(1)
            self.children = []
            self.vert_sorted = self.make2SortReturn(self.vertDis)
            return stop


    
    def MakeVertBig(self):
        print("entered")
        for i in range(2):
            for i in range(7):
                self.reset(vertex_rad=20+i)
                time.sleep(1/100)
            for i in range(7):
                self.reset(vertex_rad=27-i)
                time.sleep(1/100)
            time.sleep(1/20)






                        
                            
