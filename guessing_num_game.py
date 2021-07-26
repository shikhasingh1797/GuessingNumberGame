import tkinter
from random import randint
from tkinter import messagebox
from tkinter.constants import BOTTOM

 
low=0
high=9
rand=randint(low,high)
print(rand)




def check(guess):
    
    if guess<rand:
        tkinter.Label(tk,text=f"{guess} number is too low",font="normal 20 bold").pack()
        #label.config(text=guess)
    elif guess>rand:
        tkinter.Label(tk,text=f"{guess} number is too high",font="normal 20 bold").pack()
    else:
        tkinter.messagebox.showinfo("You win!",f"{guess} is correct")

def restart(guess):
    entry["state"]="disabled"
    button["state"]="disabled"
    check(guess)
    
tk=tkinter.Tk()
tk.geometry(('800x800') )
tk.title("Singh Guessing number game")
Button=tkinter.Button(tk,text=f"GUESSING NUMBER GAME",font=("Arial Bold",40),bd=12,bg="Tomato")
Button.pack()


label=tkinter.Label(tk,text="",width=150,font=("Arial Bold",30))
label.pack()


entry=tkinter.Entry(tk,fg="red",bg="violet",font=("Arial Bold",35),relief="solid")
entry.pack()


button=tkinter.Button(tk, text="Guess",bg="orange",fg="blue",font=("Arial Bold",45),command=lambda:check(int(entry.get())))
button.pack()

#br=tkinter.Button(tk, text="Restart",bg="pink",fg="blue",font=("Arial Bold",45),bd=8,command=lambda:restart(int(entry.get())))
#br.pack(side='bottom')


tk.mainloop()