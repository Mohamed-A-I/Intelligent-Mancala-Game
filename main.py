from tkinter import Frame, ttk
import tkinter

bits = [4, 4, 4, 4, 4, 4 , 0, 4, 4, 4, 4, 4, 4 , 0 ]
def play(n):
    bits[n] =0
    l1.config(text=bits[n])

root = tkinter.Tk()
root.resizable(width=0,height=0)
root.geometry('{}x{}'.format(1200, 392))

root.title("manacala game")

button_width=15
p1_pos=0
p2_pos=200

tkinter.Label(root,text='score \n {}'.format(bits[6]),bg='red',width=18,height=23).place(x=0,y=0)

l1 =tkinter.Button(root,text=bits[0],bg='blue',width=button_width,height=10,borderwidth=3,command=play(0)).place(x=150,y=p2_pos)
l2 =tkinter.Button(root,text=bits[1],bg='blue',width=button_width,height=10,borderwidth=3,command=play(1)).place(x=300,y=p2_pos)
l3 =tkinter.Button(root,text=bits[2],bg='blue',width=button_width,height=10,borderwidth=3,command=play(2)).place(x=450,y=p2_pos)
l4 =tkinter.Button(root,text=bits[3],bg='blue',width=button_width,height=10,borderwidth=3,command=play(3)).place(x=600,y=p2_pos)
tkinter.Button(root,text=bits[4],bg='blue',width=button_width,height=10,borderwidth=3,command=play(4)).place(x=750,y=p2_pos)
tkinter.Button(root,text=bits[5],bg='blue',width=button_width,height=10,borderwidth=3,command=play(5)).place(x=900,y=p2_pos)
tkinter.Button(root,text=bits[7] ,bg='red',width=button_width,height=10,borderwidth=3,command=play(7)).place(x=150,y=p1_pos)
tkinter.Button(root,text=bits[8] ,bg='red',width=button_width,height=10,borderwidth=3,command=play(8)).place(x=300,y=p1_pos)
tkinter.Button(root,text=bits[9] ,bg='red',width=button_width,height=10,borderwidth=3,command=play(9)).place(x=450,y=p1_pos)
tkinter.Button(root,text=bits[10],bg='red',width=button_width,height=10,borderwidth=3,command=play(10)).place(x=600,y=p1_pos)
tkinter.Button(root,text=bits[11],bg='red',width=button_width,height=10,borderwidth=3,command=play(11)).place(x=750,y=p1_pos)
tkinter.Button(root,text=bits[12],bg='red',width=button_width,height=10,borderwidth=3,command=play(12)).place(x=900,y=p1_pos)

tkinter.Label(root,text='score \n {}'.format(bits[13]),bg='blue',width=18,height=23).place(x=1055,y=0)

# red_player_layout(p2_pos)


root.mainloop()

