from tkinter import Frame, ttk
import tkinter
root = tkinter.Tk()
root.resizable(width=0,height=0)
root.geometry('{}x{}'.format(1200, 392))

root.title("manacala game")

button_width=15
p1_pos=0
p2_pos=200
binAmount = [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0]
playing = True

playerOne = True

messageCode = 0

giveawayPile = -1

lastRecipient = -1
chosenBin = -1
def clicked():
    if chosenBin >= 0:
        giveawayPile = binAmount[chosenBin]
        binAmount[chosenBin] = 0
        if int(giveawayPile) <= 0:
            messageCode = -1  # empty bin was chosen
    i = 0
    for element in binAmount:
        binAmount[i] = binAmount[i]
        if binAmount[i] < 10:
            binAmount[i] = binAmount[i]
        else:
            binAmount[i] = binAmount[i]
        i = i + 1
    print(i)


def get_winner(self):
    if binAmount[13] < binAmount[6]:
        print("Player One has won the game!")
    elif binAmount[13] > binAmount[6]:
        print("Player Two has won the game!")
    else:
        print("The game ended in a tie.")



tkinter.Button(root,text=binAmount[0],command=clicked, bg='red',width=button_width,height=10,borderwidth=3).place(x=150,y=p2_pos)
tkinter.Button(root,text=binAmount[1],command=clicked,bg='red',width=button_width,height=10,borderwidth=3).place(x=300,y=p2_pos)
tkinter.Button(root,text=binAmount[2],command=clicked,bg='red',width=button_width,height=10,borderwidth=3).place(x=450,y=p2_pos)
tkinter.Button(root,text=binAmount[3],command=clicked,bg='red',width=button_width,height=10,borderwidth=3).place(x=600,y=p2_pos)
tkinter.Button(root,text=binAmount[4],command=clicked,bg='red',width=button_width,height=10,borderwidth=3).place(x=750,y=p2_pos)
tkinter.Button(root,text=binAmount[5],command=clicked,bg='red',width=button_width,height=10,borderwidth=3).place(x=900,y=p2_pos)
tkinter.Label(root,text='score \n {}'.format(binAmount[6]),bg='red',width=20,height=23).place(x=1055,y=0)


tkinter.Button(root,text=binAmount[7],command=clicked,bg='blue',width=button_width,height=10,borderwidth=3).place(x=150,y=p1_pos)
tkinter.Button(root,text=binAmount[8] ,command=clicked,bg='blue',width=button_width,height=10,borderwidth=3).place(x=300,y=p1_pos)
tkinter.Button(root,text=binAmount[9] ,command=clicked,bg='blue',width=button_width,height=10,borderwidth=3).place(x=450,y=p1_pos)
tkinter.Button(root,text=binAmount[10],command=clicked,bg='blue',width=button_width,height=10,borderwidth=3).place(x=600,y=p1_pos)
tkinter.Button(root,text=binAmount[11],command=clicked,bg='blue',width=button_width,height=10,borderwidth=3).place(x=750,y=p1_pos)
tkinter.Button(root,text=binAmount[12],command=clicked,bg='blue',width=button_width,height=10,borderwidth=3).place(x=900,y=p1_pos)
tkinter.Label(root,text='score \n {}'.format(binAmount[13]),bg='blue',width=18,height=23).place(x=0,y=0)



root.mainloop()