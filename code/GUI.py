from tkinter import Frame, Tk, ttk
import tkinter
from tkinter.constants import FALSE, TRUE
from tkinter.messagebox import showinfo
from calcState import *
import time
class Mancala():
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.resizable(width=0,height=0)
        self.root.geometry('{}x{}'.format(1200, 392))
        self.root.title("mancala game")
       
        
        self.house1 = tkinter.StringVar()
        self.house2 = tkinter.StringVar() 
        self.house3 = tkinter.StringVar()
        self.house4 = tkinter.StringVar()
        self.house5 = tkinter.StringVar()
        self.house6 = tkinter.StringVar()
        self.house7 = tkinter.StringVar()
        self.house8 = tkinter.StringVar() 
        self.house9 = tkinter.StringVar()
        self.house10 = tkinter.StringVar()
        self.house11 = tkinter.StringVar()
        self.house12 = tkinter.StringVar()
        self.house13 = tkinter.StringVar()
        self.house14 = tkinter.StringVar()
        self.number =5
        self.houses =[
            self.house1,
            self.house2,
            self.house3,
            self.house4,
            self.house5,
            self.house6,
            self.house7 ,
            self.house8 ,
            self.house9 , 
            self.house10, 
            self.house11, 
            self.house12, 
            self.house13, 
            self.house14 
        ]
        # manacala info
       
        self.bits = [4, 4, 4, 4, 4, 4 , 0, 4, 4, 4, 4, 4, 4 , 0 ]
        self.player = 0 
        self.play_type = 0 #play without steeling
        self.computer = 0
        
        self.AI = AI((self.bits))
        self.home()

        self.root.mainloop()


        
###############################################################################   
#                                  Pages
###############################################################################   
    def game_page(self):
        self.initial_state()
        self.menu()
        tkinter.Label(self.root,textvariable=self.houses[13],bg='red',width=18,height=23).place(x=0,y=0)
        x_pos = 150
        x_pos1 = 150
        p2_pos=200
        p1_pos=0
        tkinter.Button(self.root,textvariable= self.houses[0],bg='blue',
        command=lambda:self.play_select(0), 
        width= 15,height=10,borderwidth=3).place(x=150,y=p2_pos)
        tkinter.Button(self.root,textvariable= self.houses[1],bg='blue',command=lambda:self.play_select(1), width=15,height=10,borderwidth=3).place(x=300,y=p2_pos)
        tkinter.Button(self.root,textvariable= self.houses[2],bg='blue',command=lambda:self.play_select(2), width=15,height=10,borderwidth=3).place(x=450,y=p2_pos)
        tkinter.Button(self.root,textvariable= self.houses[3],bg='blue',command=lambda:self.play_select(3), width=15,height=10,borderwidth=3).place(x=600,y=p2_pos)
        tkinter.Button(self.root,textvariable= self.houses[4],bg='blue',command=lambda:self.play_select(4), width=15,height=10,borderwidth=3).place(x=750,y=p2_pos)
        tkinter.Button(self.root,textvariable= self.houses[5],bg='blue',command=lambda:self.play_select(5), width=15,height=10,borderwidth=3).place(x=900,y=p2_pos)
        tkinter.Button(self.root,textvariable= self.houses[12],bg='red',command=lambda:self.play_select(12), width=15,height=10,borderwidth=3).place(x=150,y=p1_pos)
        tkinter.Button(self.root,textvariable= self.houses[11],bg='red',command=lambda:self.play_select(11), width=15,height=10,borderwidth=3).place(x=300,y=p1_pos)
        tkinter.Button(self.root,textvariable= self.houses[10],bg='red',command=lambda:self.play_select(10), width=15,height=10,borderwidth=3).place(x=450,y=p1_pos)
        tkinter.Button(self.root,textvariable= self.houses[9],bg='red',command=lambda:self.play_select(9), width=15,height=10,borderwidth=3).place(x=600,y=p1_pos)
        tkinter.Button(self.root,textvariable= self.houses[8],bg='red',command=lambda:self.play_select(8), width=15,height=10,borderwidth=3).place(x=750,y=p1_pos)
        tkinter.Button(self.root,textvariable= self.houses[7],bg='red',command=lambda:self.play_select(7), width=15,height=10,borderwidth=3).place(x=900,y=p1_pos)
   
        tkinter.Label(self.root,textvariable=self.houses[6],bg='blue',width=18,height=23).place(x=1055,y=0)
    
    def home(self):
       
     
        # steeling or without steeling 
        tkinter.Button(self.root,text="steeling",command=lambda:self.choosegame(0), 
        width= 15,height=5,borderwidth=3).place(x=650,y=0)
        tkinter.Button(self.root,text="without steeling",command=lambda:self.choosegame(1), 
        width= 15,height=5,borderwidth=3).place(x=650,y=100)
        # tkinter.Label(self.root, textvariable=self.steeloption).place(x=700,y=250)
        # let's play
        tkinter.Button(self.root,text="Let's play!",command=lambda:self.changepage(2), 
        width= 15,height=5,borderwidth=3).place(x=550,y=280)
         # AI or multiplayer
       
        tkinter.Button(self.root,text="Multiplayer",command = lambda:self.AI_or_mul(0), 
        width= 15,height=5,borderwidth=3).place(x=450,y=0)
        tkinter.Button(self.root,text="AI", command = lambda:self.AI_or_mul(1),
        width= 15,height=5,borderwidth=3).place(x=450,y=100)


    def menu(self):
        menubar = tkinter.Menu(self.root)
        menubar.add_command(label="Home",command=lambda:self.changepage(1))
        menubar.add_command(label="Exit", command=self.root.quit)

        self.root.config(menu=menubar)


    
###############################################################################   
#                                Pages Logic
###############################################################################  
    def update(self):
        i=0
        while i<14:
            self.houses[i].set(self.bits[i])
            i+=1

    def initial_state(self):

        i=0
        self.player = 0
        self.bits = [4, 4, 4, 4, 4, 4 , 0, 4, 4, 4, 4, 4, 4 , 0 ]
        if(self.computer == 1):
            while(self.player == 0):
                pos = self.AI.mini_max(self.bits,2,True,False)    
                self.play_without_steeling(pos)
                print("blue {}".format(self.bits))
                print(pos)    

            
       
        
        while i<14:
            self.houses[i].set(self.bits[i])
            i+=1

    def changepage(self,pagenum):
        for widget in self.root.winfo_children():
            widget.destroy()
        if pagenum == 1:
            self.home()
        elif pagenum == 2:
            self.game_page()    

    def choosegame(self,type):

        self.play_type = type

###############################################################################   
#                                  Game Logic
###############################################################################
    def play_without_steeling(self,house_index):
        self.isGameEnd()
        num = self.bits[house_index]
        pushed_index = house_index
        if(self.player == 0 and pushed_index<6 and num != 0):
            self.player = 1
            while(num>0):
                house_index = (house_index + 1)%14
                if(house_index == 13): house_index = 0
                elif(num == 1 and house_index==6): self.player = 0
                self.bits[house_index] += 1
                num -= 1

            self.bits[pushed_index] = 0      
        else:
            if(self.player == 1 and pushed_index>6 and num != 0):
                self.player = 0
                while(num>0):
                    house_index = (house_index + 1)%14
                    if(house_index == 6): house_index = 7
                    elif(num == 1 and house_index==13): self.player = 1
                    self.bits[house_index] += 1
                    num -= 1

                self.bits[pushed_index] = 0
        self.update()

    def play_with_steeling(self,house_index):
        self.isGameEnd()
        num = self.bits[house_index]
        pushed_index = house_index
        if(self.player == 0 and pushed_index<6 and num != 0):
            self.player = 1
            while(num>0):
                house_index = (house_index + 1)%14
                if(house_index == 13): house_index = 0
                elif(num == 1 and house_index==6): self.player = 0
                elif(num==1 and self.bits[house_index] == 0):
                    self.bits[6] += 1 + self.bits[12-house_index]
                    self.bits[12-house_index] = 0
                    self.bits[house_index] = 0
                    num -= 1
                    continue
                self.bits[house_index] += 1
                num -= 1

            self.bits[pushed_index] = 0      
        
        else:
            if(self.player == 1 and pushed_index>6 and num != 0):
                self.player = 0
                while(num>0):
                    house_index = (house_index + 1)%14
                    if(house_index == 6): house_index = 7
                    elif(num == 1 and house_index==13): self.player = 1
                    elif(num==1 and self.bits[house_index] == 0):
                        self.bits[13] += 1 + self.bits[12-house_index]
                        self.bits[12-house_index] = 0
                        self.bits[house_index] = 0
                        num -= 1
                        continue
                    self.bits[house_index] += 1
                    num -= 1

                self.bits[pushed_index] = 0
        self.update()

    def multiplayer(self,house_index):
        if(self.play_type == 1): self.play_without_steeling(house_index)
        else: self.play_with_steeling(house_index)
   
        
    def winner(self):
       
        if int(self.bits[13]) < int(self.bits[6]):
            
            showinfo("winner", "blue player win")
            print("Player One has won the game!")
        elif int(self.bits[13]) > int(self.bits[6]):
          
            showinfo("winner", "red player win")
            print("Player Two has won the game!")
        else:
            showinfo("winner", "no win")
            print("The game ended in a tie.")

        
        self.initial_state()

    def isGameEnd(self):
        if(sum(self.bits[0:6]) == 0 or sum(self.bits[7:13]) == 0):
            self.bits[13] += sum(self.bits[7:13])
            self.bits[6] += sum(self.bits[0:6])
            self.update()
            self.winner()
           



    def AI_player(self,house_index):
        if(self.play_type == 1):
            self.play_without_steeling(house_index)
        else:
            self.play_with_steeling(house_index)
        print("red {}".format(self.bits))
        while(self.player == 0):
            print(" entre ai")
            if(self.play_type == 1):
                pos = self.AI.mini_max_alpha_beta(self.bits, 2, -999, 999, True,False)
                self.play_without_steeling(pos)
            else:
                pos = self.AI.mini_max_alpha_beta(self.bits, 2, -999, 999, True,True)  
                self.play_with_steeling(pos)  
            print("pos{}".format(pos))
            
            print("blue {}".format(self.bits))

          

    def play_select(self,house_index):
      
        print("player {}".format(self.player))
        if(self.computer == 1):
            # print("cimputer {}".format(self.computer))
        
            self.AI_player(house_index)
        else:
            self.multiplayer(house_index)
    def AI_or_mul(self,computer):
       
        self.computer = computer

