from tkinter import Frame, Tk, ttk
import tkinter



class GameBoard():
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.resizable(width=0,height=0)
        self.root.geometry('{}x{}'.format(1200, 392))
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
        self.bits = [4, 4, 4, 4, 4, 4 , 0, 4, 4, 4, 4, 4, 4 , 0 ]
        self.game_page()
        self.root.mainloop()

    def initial_state(self):
        i=0
        while i<14:
            self.houses[i].set(self.bits[i])
            i+=1
    def game_page(self):
        self.initial_state()
        tkinter.Label(self.root,textvariable=self.houses[6],bg='red',width=18,height=23).place(x=0,y=0)
        x_pos = 150
        x_pos1 = 150
        p2_pos=200
        p1_pos=0
        tkinter.Button(self.root,textvariable= self.houses[0],bg='blue',command=lambda:self.rule(0), width= 15,height=10,borderwidth=3).place(x=150,y=p2_pos)
        tkinter.Button(self.root,textvariable= self.houses[1],bg='blue',command=lambda:self.rule(1), width=15,height=10,borderwidth=3).place(x=300,y=p2_pos)
        tkinter.Button(self.root,textvariable= self.houses[2],bg='blue',command=lambda:self.rule(2), width=15,height=10,borderwidth=3).place(x=450,y=p2_pos)
        tkinter.Button(self.root,textvariable= self.houses[3],bg='blue',command=lambda:self.rule(3), width=15,height=10,borderwidth=3).place(x=600,y=p2_pos)
        tkinter.Button(self.root,textvariable= self.houses[4],bg='blue',command=lambda:self.rule(4), width=15,height=10,borderwidth=3).place(x=750,y=p2_pos)
        tkinter.Button(self.root,textvariable= self.houses[5],bg='blue',command=lambda:self.rule(5), width=15,height=10,borderwidth=3).place(x=900,y=p2_pos)
        tkinter.Button(self.root,textvariable= self.houses[7] ,bg='red',command=lambda:self.rule(7), width=15,height=10,borderwidth=3).place(x=150,y=p1_pos)
        tkinter.Button(self.root,textvariable= self.houses[8] ,bg='red',command=lambda:self.rule(8), width=15,height=10,borderwidth=3).place(x=300,y=p1_pos)
        tkinter.Button(self.root,textvariable= self.houses[9] ,bg='red',command=lambda:self.rule(9), width=15,height=10,borderwidth=3).place(x=450,y=p1_pos)
        tkinter.Button(self.root,textvariable= self.houses[10],bg='red',command=lambda:self.rule(10), width=15,height=10,borderwidth=3).place(x=600,y=p1_pos)
        tkinter.Button(self.root,textvariable= self.houses[11],bg='red',command=lambda:self.rule(11), width=15,height=10,borderwidth=3).place(x=750,y=p1_pos)
        tkinter.Button(self.root,textvariable= self.houses[12],bg='red',command=lambda:self.rule(12), width=15,height=10,borderwidth=3).place(x=900,y=p1_pos)
   
        tkinter.Label(self.root,textvariable=self.houses[13],bg='blue',width=18,height=23).place(x=1055,y=0)
    
    def update(self):
        i=0
        while i<14:
            self.houses[i].set(self.bits[i])
            i+=1

    def rule(self,house_index):
        num = self.bits[house_index]
        self.bits[house_index] = 0
        while(num > 0):
            house_index = (house_index + 1)%14 
            self.bits[house_index] += 1
            num-=1 
        self.update()
    

GameBoard()
