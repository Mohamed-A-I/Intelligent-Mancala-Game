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
    for i in binAmount:
        print(binAmount.index(i))

    # chosenBin=i
    # binAmount[chosenBin] = 0
    # tkinter.Button(root,text=binAmount[chosenBin],command=clicked, bg='red',width=button_width,height=10,borderwidth=3).place(x=150,y=p2_pos)
    # for i in binAmount[chosenBin+1:6]:
    #      binAmount[i] =  binAmount[i] +1
    #      tkinter.Button(root,text=binAmount[i] ,command=clicked, bg='red',width=button_width,height=10,borderwidth=3).place(x=150,y=p2_pos)



def get_winner(self):
    if binAmount[13] < binAmount[6]:
        print("Player One has won the game!")
    elif binAmount[13] > binAmount[6]:
        print("Player Two has won the game!")
    else:
        print("The game ended in a tie.")


def checkisover():
    sideOne = 0
    sideTwo = 0
    for j in range(6):
        sideOne = int(sideOne) + int(binAmount[j])
        sideTwo = int(sideTwo) + int(binAmount[j+7])
        
    if(int(sideOne) == 0 or int(sideTwo) == 0):
        playing = False
        binAmount[6] = int(binAmount[6]) + int(sideOne)
        binAmount[13] = int(binAmount[13]) + int(sideTwo)
        for k in range(6):
            binAmount[k] = 0
            binAmount[k+7] = 0


x=150
for i in binAmount[0:6]:
    if not binAmount[6]:
        tkinter.Button(root,text=binAmount[i],command=clicked, bg='red',width=button_width,height=10,borderwidth=3).place(x=x,y=p2_pos)
        x=x+150

tkinter.Label(root,text='score \n {}'.format(binAmount[6]),bg='red',width=20,height=23).place(x=1055,y=0)




x=150
for i in binAmount[7:13]:
    if not binAmount[13]:
        tkinter.Button(root,text=binAmount[i],command=clicked,bg='blue',width=button_width,height=10,borderwidth=3).place(x=x,y=p1_pos)
        x=x+150

tkinter.Label(root,text='score \n {}'.format(binAmount[13]),bg='blue',width=18,height=23).place(x=0,y=0)

        
'''
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
'''






root.mainloop()