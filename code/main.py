from tkinter import Frame, ttk
import tkinter
root = tkinter.Tk()
root.resizable(width=0,height=0)
root.geometry('{}x{}'.format(1200, 392))

root.title("manacala game")

button_width=15
p1_pos=0
p2_pos=200
rec = []
for i in range(14):
    if(i == 6 or i==13):
        rec.insert(i,0)
        continue
    rec.insert(i,4)
tkinter.Label(root,text='score \n {}'.format(rec[13]),bg='blue',width=18,height=23).place(x=0,y=0)

tkinter.Button(root,text=rec[0],bg='red',width=button_width,height=10,borderwidth=3).place(x=150,y=p2_pos)
tkinter.Button(root,text=rec[1],bg='red',width=button_width,height=10,borderwidth=3).place(x=300,y=p2_pos)
tkinter.Button(root,text=rec[2],bg='red',width=button_width,height=10,borderwidth=3).place(x=450,y=p2_pos)
tkinter.Button(root,text=rec[3],bg='red',width=button_width,height=10,borderwidth=3).place(x=600,y=p2_pos)
tkinter.Button(root,text=rec[4],bg='red',width=button_width,height=10,borderwidth=3).place(x=750,y=p2_pos)
tkinter.Button(root,text=rec[5],bg='red',width=button_width,height=10,borderwidth=3).place(x=900,y=p2_pos)

tkinter.Button(root,text=rec[7] ,bg='blue',width=button_width,height=10,borderwidth=3).place(x=150,y=p1_pos)
tkinter.Button(root,text=rec[8] ,bg='blue',width=button_width,height=10,borderwidth=3).place(x=300,y=p1_pos)
tkinter.Button(root,text=rec[9] ,bg='blue',width=button_width,height=10,borderwidth=3).place(x=450,y=p1_pos)
tkinter.Button(root,text=rec[10],bg='blue',width=button_width,height=10,borderwidth=3).place(x=600,y=p1_pos)
tkinter.Button(root,text=rec[11],bg='blue',width=button_width,height=10,borderwidth=3).place(x=750,y=p1_pos)
tkinter.Button(root,text=rec[12],bg='blue',width=button_width,height=10,borderwidth=3).place(x=900,y=p1_pos)

# red_player_layout(p2_pos)
tkinter.Label(root,text='score \n {}'.format(rec[6]),bg='red',width=20,height=23).place(x=1055,y=0)


root.mainloop()