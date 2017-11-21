from tkinter import *
import tkinter.messagebox


def checked(i) :
      global player
      button = list[i]

      if button["text"] != "     " :
            return
      button["text"] = player 
      button["bg"] = "yellow"

      if player == "X" :
            wincheck[i] = "X"
            check()
            player = "O"
            button["bg"] = "yellow"
      else :
            wincheck[i] = "O"
            check()
            player = "X"
            button["bg"] = "lightgreen"

window = Tk()
player = "X"
list= []
wincheck = [""]*9

for i in range(9) :
      b = Button(window, text="     ", command=lambda k=i: checked(k))
      b.grid(row=i//3, column=i%3)
      list.append(b)
      
def check() : 
      if  wincheck[0]==wincheck[3]==wincheck[6]=="X" or wincheck[1]==wincheck[4]==wincheck[7]=="X" or wincheck[2]==wincheck[5]==wincheck[8]=="X" :
            tkinter.messagebox.showinfo("win!","X have won!")
            quit()
      elif wincheck[0]==wincheck[1]==wincheck[2] == "X" or wincheck[3]==wincheck[4]==wincheck[5] == "X" or wincheck[6]==wincheck[7]==wincheck[8] == "X" :
            tkinter.messagebox.showinfo("win!","X have won!")
            quit()
      elif wincheck[0]==wincheck[4]==wincheck[8] == "X" or wincheck[2]==wincheck[4]==wincheck[6] == "X" :
            tkinter.messagebox.showinfo("win!","X have won!")
            quit()
      elif  wincheck[0]==wincheck[3]==wincheck[6] == "O" or wincheck[1]==wincheck[4]==wincheck[7] == "O" or wincheck[2]==wincheck[5]==wincheck[8] == "O" :
            tkinter.messagebox.showinfo("win!","O have won!")
            quit()
      elif wincheck[0]==wincheck[1]==wincheck[2] == "O" or wincheck[3]==wincheck[4]==wincheck[5] == "O" or wincheck[6]==wincheck[7]==wincheck[8] == "O" :
            tkinter.messagebox.showinfo("win!","O have won!")
            quit()
      elif wincheck[0]==wincheck[4]==wincheck[8] == "O" or wincheck[2]==wincheck[4]==wincheck[6] == "O" :
            tkinter.messagebox.showinfo("win!","O have won!")
            quit() 
            
window.mainloop()



