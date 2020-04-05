from tkinter import *
import tkinter as tk
from graph import graph
from Dijkstra import Dijkstraa
import time
import math
import pygame
from tkinter.ttk import *
import tkinter.font as tkfont


class switch_Frames:
    def __init__(self):
        self._frame = None     #initially there is no frame
        self.root = Tk()                       #stores the current frame
        self.root.title("Algo Illustrator")
        s = Style()
        s.configure('My.TFrame', background='black')

        #initialise it with the startFrame Frame
        self.switch_frame(Beginning_Frame)
        self.root.geometry('500x400')
        self.root.resizable(True,True)
        

    def switch_frame(self,frame_class):
        new_frame = frame_class(self)
        #new_frame is an object of the frame_class class
        if self._frame is not None:
            self._frame.destroy()
            #destroy the object that was previously created
        self._frame = new_frame.frame
        self._frame.pack(fill='both',expand=True)


class Beginning_Frame:
    def __init__(self,master):
        self.frame = Frame(master.root,style='My.TFrame')      

        #Button 1
        myFont = tkfont.Font(family='Helvetica', size=15, weight='bold')        
        label = tk.Label(self.frame,font=myFont, text = "Display Graph",fg="white",bg = "black")
        label.place(x=0,y=10)
        button = tk.Button(self.frame,width = 20,text="Click here!",command =lambda: master.switch_frame(DisplayGraph) )        
        button.place(x=200,y=10)        

        #button 2
        label2 = tk.Label(self.frame,font=myFont, text = "Illustrate Algorithm",fg="white",bg = "black")
        label2.place(x=0,y=50)        
        button2 = Button(self.frame,width = 20,text="Click here!",command =lambda: master.switch_frame(AlgoDemonstrate) )        
        button2.place(x=200,y=50)
                

class DisplayGraph:
    def __init__(self,master):
        self.V = 1000
        self.E = []
        self.weights = []
        self.weighted = False
        self.frame = Frame(master.root,style='My.TFrame')
        myFont = tkfont.Font(family='Helvetica', size=15, weight='bold')
        label = tk.Label(self.frame,font=myFont,text = "Please enter the specifications of the graph!",bg = "black",fg="white")
        label.place(x=0,y = 0)
        button = Button(self.frame,text="Return",width = 10,command =lambda: master.switch_frame(Beginning_Frame))
        button.place(x=10,y = 240)
        button_go = Button(self.frame,text="Go!!",width = 10,command =self.show_graph)
        button_go.place(x=100,y = 240)
        self.myFont2 = tkfont.Font(family='Helvetica', size=12, weight='bold')

        label_weighted = tk.Label(self.frame,font=self.myFont2,text = "Weighted ",bg = "black",fg="white")
        button_weighted = Button(self.frame,text="Yes",width = 10,command =self.take_weights)
        label_weighted.place(x=0,y = 110)
        button_weighted.place(x=160,y = 110)

        #Entery Widgets
        
        label1 = tk.Label(self.frame,font=self.myFont2,text = "Number of Vertices ",bg = "black",fg="white")
        label2 = tk.Label(self.frame,font=self.myFont2,text = "Enter the edges ",bg = "black",fg="white")
        self.e1 = tk.Entry(self.frame,width=12)
        self.e2 = tk.Entry(self.frame,width=5)
        self.e3 = tk.Entry(self.frame,width = 5)
        button1 = tk.Button(self.frame,width = 10,text = "Enter",command =self.recordVertices )
        button1.place(x = 310,y=70)
        button2 = tk.Button(self.frame,width = 10,text="Enter",command =self.recordEdges)
        button2.place(x=310,y=160)
        label1.place(x=0,y=70)
        self.e1.place(x=160,y=70)
        label2.place(x=0,y=160)        
        self.e2.place(x=160,y=160)
        self.e3.place(x = 200,y=160)
        self.label3 = None      #initially

    def recordVertices(self):
        self.V = int(self.e1.get(),10)
        print("The number of Vertices are: ",self.V)
        str2 = "\nPut the first Vertex in FirstBox\n and second Vertex of Edge in 2nd Box"
        string = "Egdes should consist of Vertices \n only from 0 to "+ str(self.V)+str2
        l1 = tk.Label(self.frame,font=self.myFont2,text = string,bg = "black",fg="white")
        l1.place(x=20,y=300)

    def recordEdges(self):        
        if self.label3 is not None:
            self.label3.destroy()
        a,b = int(self.e2.get(),10),int(self.e3.get(),10) 
        print(a,b)
        if a>=self.V or b>=self.V:
            print("checked its invalid!!!")
            self.label3 =tk.Label(self.frame,font=self.myFont2,text = "Invalid",bg = "black",fg="red")
            self.label3.place(x =160 ,y=190)
            self.e2.delete(0, tk.END)
            self.e3.delete(0, tk.END)
            self.e4.delete(0, tk.END)
            return
        if(self.weighted):
            c = int(self.e4.get(),10)
            self.weights.append(c)
            self.e4.delete(0, tk.END)
        self.E.append([a,b])
        print("Edge is ",self.E)
        print("weights are",self.weights)
        self.e2.delete(0, tk.END)
        self.e3.delete(0, tk.END)
        

    def show_graph(self):

        pygame.init()
        limx = 1000
        limy = 600
        window = pygame.display.set_mode((limx,limy))
        pygame.display.set_caption('Graph')     
        window.fill(pygame.Color("white"))
        self.g = graph(window,self.V,self.E,limx,limy,0,self.weighted,self.weights)       
        self.g.display_edges()
        self.cords = self.g.display_vert() 
        pygame.display.update()
        if(self.weighted==True):
            self.g.display_weights()
        end = 0
        while not end:
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    end=True
            pygame.display.flip()
        pygame.quit()


    
    def take_weights(self):
        self.weighted = True
        self.e4 = tk.Entry(self.frame,width=5)
        self.e4.place(x=240,y=160)
        string = "Enter in the weights\n third column"
        l1 = tk.Label(self.frame,font=self.myFont2,text = string,bg = "black",fg="white")
        l1.place(x=250,y=105)
        
        
        
class AlgoDemonstrate:
    def __init__(self,master):
        self.frame = Frame(master.root,style='My.TFrame')
        myFont = tkfont.Font(family='Helvetica', size=15, weight='bold')

        label = tk.Label(self.frame,font=myFont,text = "Select the algorithm to demostrate!",bg = "black",fg="white")
        button = Button(self.frame,text="Return",width = 15,command =lambda: master.switch_frame(Beginning_Frame))
        label.place(x=0,y=0)
        button.place(x=10,y=150)
        
        self.myFont2 = tkfont.Font(family='Helvetica', size=12, weight='bold')
        label1 = tk.Label(self.frame,font=self.myFont2,text = "Dijkstra's ",bg = "black",fg="white")
        label1.place(x=0,y=70)
        button1 = tk.Button(self.frame,width = 10,text = "Click!!",command= lambda: master.switch_frame(Dijkstra))
        button1.place(x = 210,y=70)

class Dijkstra(DisplayGraph):
    def __init__(self,master):
        self.V = 1000
        self.E = []
        self.weights = []
        self.weighted = 0
        self.source = 0                 #default source is 0
        self.frame = Frame(master.root,style='My.TFrame')
        myFont = tkfont.Font(family='Helvetica', size=15, weight='bold')
        label = tk.Label(self.frame,font=myFont,text = "Please enter the specifications of the graph for Performing Dijkstra!",bg = "black",fg="white")
        label.place(x=0,y = 0)
        button = Button(self.frame,text="Return",width = 10,command =lambda: master.switch_frame(AlgoDemonstrate))
        button.place(x=10,y = 250)
        button_go = Button(self.frame,text="Go!!",width = 10,command =self.Perform)
        button_go.place(x=100,y = 250)

        #Entery Widgets
        self.myFont2 = tkfont.Font(family='Helvetica', size=12, weight='bold')
        label1 = tk.Label(self.frame,font=self.myFont2,text = "Number of Vertices ",bg = "black",fg="white")
        label2 = tk.Label(self.frame,font=self.myFont2,text = "Enter the edges ",bg = "black",fg="white")
        self.e1 = tk.Entry(self.frame,width=12)
        self.e2 = tk.Entry(self.frame,width=5)
        self.e3 = tk.Entry(self.frame,width = 5)
        label_weighted = tk.Label(self.frame,font=self.myFont2,text = "Weighted ",bg = "black",fg="white")
        button_weighted = Button(self.frame,text="Yes",width = 10,command =self.take_weights)
        label_weighted.place(x=0,y = 110)
        button_weighted.place(x=160,y = 110)

        label_source = tk.Label(self.frame,font=self.myFont2,text = "Souce Vertex ",bg = "black",fg="white")
        button_source = Button(self.frame,text="Enter",width = 10,command =self.take_source)
        label_source.place(x=0,y = 210)
        button_source.place(x=310,y=210)
        self.entry_source = tk.Entry(self.frame,width = 5)
        self.entry_source.place(x=160,y = 210)
        
        button1 = tk.Button(self.frame,width = 10,text = "Enter",command =self.recordVertices )
        button1.place(x = 310,y=70)
        button2 = tk.Button(self.frame,width = 10,text="Enter",command =self.recordEdges)
        button2.place(x=310,y=160)
        label1.place(x=0,y=70)
        self.e1.place(x=160,y=70)
        label2.place(x=0,y=160)        
        self.e2.place(x=160,y=160)
        self.e3.place(x = 200,y=160)
        self.label3 = None      #initially    

    def take_source(self):
        self.source = int(self.entry_source.get(),10)
        print("The source is",self.source)
    
    def Perform(self):
        pygame.init()
        limx = 1000
        limy = 600
        window = pygame.display.set_mode((limx,limy))
        pygame.display.set_caption('Graph')     
        window.fill(pygame.Color("white"))

        if(self.weighted==False):
            for i in range(self.V):
                self.weights.append(1)
        
        g = Dijkstraa(window,self.V,self.E,limx,limy,0,self.weighted,self.weights)
        g.demo_algo_initialize(self.source)
        
        end = 0
        cont = 1
        while not end:
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    end=True
            cont = g.algo(cont)
            if(cont==0):
                end = 1
            pygame.display.flip()
        pygame.quit()

          
switch = switch_Frames()
switch.root.mainloop()
