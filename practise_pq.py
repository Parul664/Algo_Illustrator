from Dijkstra import Dijkstraa
from p_queue import p_queue
from graph import graph
from dis_matrix import dis_matrix
import math
import pygame
from make_tree import make_tree

pygame.init()

limx = 1000
limy = 600

window = pygame.display.set_mode((limx,limy))
pygame.display.set_caption('Graph')

window.fill(pygame.Color("white"))
V = 6
edges = [[1,2],[2,3],[1,4],[5,1],[3,4],[1,3]]            
#w = [1,2,3,4,5,2]
#g = Dijkstraa(window,6,edges,limx,limy,0,1,w)
#g.demo_algo_initialize(1)

#pq = p_queue(window,400,limx,limy)
#pq.show_skeleton()
#pq.fill_pq([1,2,4,5,4,5,5,6],[1,2,31,4,5,61,7,7,88,8])


#damn = dis_matrix(window,limx,limy)
#damn.show([2,3,5,4])

mk = make_tree(window,V,edges,limx,limy)
g_dic = {1:[2,3],2:[11],3:[10,6,7,8],6:[9,8]}

mk.make_tree(g_dic,1,60,100,100)


end = 0
while not end:
    for event in pygame.event.get():
        if(event.type==pygame.QUIT):
            end = True
    pygame.display.flip()

pygame.quit()
quit()
